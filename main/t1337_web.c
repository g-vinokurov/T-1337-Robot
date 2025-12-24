
#include <esp_system.h>
#include <esp_event.h>
#include <esp_wifi.h>
#include <esp_log.h>
#include <nvs_flash.h>
#include <driver/uart.h>
#include <esp_http_server.h>
#include <string.h>
#include "driver/gpio.h"
#include "esp_timer.h"
#include "freertos/FreeRTOS.h"

#define SOFT_UART_TX_GPIO 2  // GPIO2
#define BIT_DELAY_US  3333 // (1000000 / 300) 

#define TAG "T1337_WEB"

#define UART_BAUD_RATE     300

#define WIFI_SSID          "T1337_WEB"
#define WIFI_PASS          "t1337_tank"
#define MAX_STA_CONN       4

typedef enum {
    CMD_LFORWARD  = '0',
    CMD_RFORWARD  = '1',
    CMD_LBACKWARD = '2',
    CMD_RBACKWARD = '3',
    CMD_LRELEASE  = '4',
    CMD_RRELEASE  = '5',
    CMD_TRIGHT    = '6',
    CMD_TLEFT     = '7',
    CMD_TSTOP     = '8'
} cmd_t;


// Функция точной микросекундной задержки
static void delay_us(uint64_t us) {
    uint64_t start = esp_timer_get_time(); // Используем uint64_t!
    uint64_t elapsed = 0;
    while (elapsed < us) {
        elapsed = esp_timer_get_time() - start;
        // Небольшая оптимизация: отдаём управление, если осталось ждать много
        if ((us - elapsed) > 1000) { // Если осталось больше 1 мс
            vTaskDelay(1 / portTICK_PERIOD_MS); // Освобождаем CPU на 1 тик (~10 мс)
        }
    }
}

// Отправка одного байта через программный UART
static void uart_soft_send_byte(char c) {
    portENTER_CRITICAL();
    
    // 1. Старт-бит (логический 0)
    gpio_set_level(SOFT_UART_TX_GPIO, 0);
    delay_us(BIT_DELAY_US);

    // Отправляем 8 бит данных МЛАДШИЙ БИТ ПЕРВЫЙ (LSB-first)
    for (int i = 0; i < 8; i++) { // Цикл от 0 до 7, а не от 7 до 0!
        gpio_set_level(SOFT_UART_TX_GPIO, (c >> i) & 1);
        delay_us(BIT_DELAY_US);
    }

    // 3. Стоп-бит (логическая 1)
    gpio_set_level(SOFT_UART_TX_GPIO, 1);
    delay_us(BIT_DELAY_US);
    
    portEXIT_CRITICAL();
}

static void init_uart_soft(void) {
    ESP_LOGI(TAG, "Initializing Software UART TX on GPIO%d...", SOFT_UART_TX_GPIO);

    // Настройка GPIO как выхода
    gpio_set_direction(SOFT_UART_TX_GPIO, GPIO_MODE_OUTPUT);
    gpio_set_level(SOFT_UART_TX_GPIO, 1); // Устанавливаем высокий уровень (стоп-бит)
    ESP_LOGI(TAG, "GPIO%d set as OUTPUT, level HIGH", SOFT_UART_TX_GPIO);

    // ОТПРАВЛЯЕМ тестовый байт ПРАВИЛЬНОЙ функцией
    ESP_LOGI(TAG, "Sending test byte 'X' via correct function...");
    uart_soft_send_byte('X'); // Теперь используется исправленная функция
    ESP_LOGI(TAG, "Software UART initialized.");
}

// Обновлённая функция отправки команды (заменяет старую)
void send_uart_command(char cmd) {
    uart_soft_send_byte(cmd);
    ESP_LOGI(TAG, "Command sent via SOFT UART: %c", cmd);
}

static void send_error_response(httpd_req_t *req, int error_code, const char *message) {
    char response[256];
    int msg_len = strlen(message);
    
    switch(error_code) {
        case 400:
            snprintf(response, sizeof(response), 
                     "HTTP/1.1 400 Bad Request\r\n"
                     "Content-Type: text/plain\r\n"
                     "Content-Length: %d\r\n\r\n%s", 
                     msg_len, message);
            break;
        case 404:
            snprintf(response, sizeof(response),
                     "HTTP/1.1 404 Not Found\r\n"
                     "Content-Type: text/plain\r\n"
                     "Content-Length: %d\r\n\r\n%s",
                     msg_len, message);
            break;
        case 500:
        default:
            snprintf(response, sizeof(response),
                     "HTTP/1.1 500 Internal Server Error\r\n"
                     "Content-Type: text/plain\r\n"
                     "Content-Length: %d\r\n\r\n%s",
                     msg_len, message);
            break;
    }
    
    httpd_resp_send(req, response, strlen(response));
}

// --- /api/cmd ---
static esp_err_t command_post_handler(httpd_req_t *req) {
    char buffer[128];
    int ret;
    
    // Read plain text body
    ret = httpd_req_recv(req, buffer, sizeof(buffer)-1);
    if (ret <= 0) {
        send_error_response(req, 400, "Empty request");
        return ESP_FAIL;
    }
    buffer[ret] = '\0';
    
    // Remove any trailing whitespace or newlines
    for (int i = ret-1; i >= 0; i--) {
        if (buffer[i] == '\r' || buffer[i] == '\n' || buffer[i] == ' ') {
            buffer[i] = '\0';
        } else {
            break;
        }
    }
    
    // Check if we received a valid command
    char command = '\0';
    
    // Check for single character commands
    if (strlen(buffer) == 1) {
        command = buffer[0];
    }
    
    // Validate command
    if (command == '\0') {
        send_error_response(req, 400, "Invalid command");
        return ESP_FAIL;
    }
    
    // Send command
    send_uart_command(command);
    
    // Send response
    const char *response = "OK: Command '%c' was sent\n";
    char resp_buffer[64];
    snprintf(resp_buffer, sizeof(resp_buffer), response, command);
    httpd_resp_set_type(req, "text/plain");
    httpd_resp_send(req, resp_buffer, strlen(resp_buffer));
    
    return ESP_OK;
}

// Start web server with API endpoints
static httpd_handle_t start_api_server(void) {
    httpd_config_t config = HTTPD_DEFAULT_CONFIG();
    config.server_port = 80;
    config.max_uri_handlers = 10;
    
    httpd_handle_t server = NULL;
    
    if (httpd_start(&server, &config) == ESP_OK) {
        // Register API endpoints
        httpd_uri_t command_post_uri = {
            .uri = "/api/cmd",
            .method = HTTP_POST,
            .handler = command_post_handler,
            .user_ctx = NULL
        };
        
        httpd_register_uri_handler(server, &command_post_uri);
        
        ESP_LOGI(TAG, "API server started on port %d", config.server_port);
    }
    
    return server;
}

static void wifi_init_softap(void) {
    // 1. Инициализация сетевого стека (ОБЯЗАТЕЛЬНО ПЕРВОЙ)
    tcpip_adapter_init();

    // 2. Создание цикла событий
    ESP_ERROR_CHECK(esp_event_loop_create_default());

    // 3. Инициализация WiFi драйвера
    wifi_init_config_t cfg = WIFI_INIT_CONFIG_DEFAULT();
    ESP_ERROR_CHECK(esp_wifi_init(&cfg));

    // 4. ЯВНОЕ указание режима AP перед настройкой
    ESP_ERROR_CHECK(esp_wifi_set_mode(WIFI_MODE_AP));

    // 5. Подготовка конфигурации с ВСЕМИ полями
    wifi_config_t wifi_config = {
        .ap = {
            .ssid = WIFI_SSID, // Имя сети
            .password = WIFI_PASS, // Пароль
            .ssid_len = strlen(WIFI_SSID), // ВАЖНО: длина SSID
            .channel = 6, // Канал WiFi (1-13)
            .authmode = WIFI_AUTH_WPA_WPA2_PSK, // Тип аутентификации
            .max_connection = 4, // Макс. число клиентов
            .beacon_interval = 100 // Интервал beacon
        }
    };

    // 6. Указываем хранить настройки в RAM (чтобы обойти NVS)
    // ESP_ERROR_CHECK(esp_wifi_set_storage(WIFI_STORAGE_RAM));
    ESP_ERROR_CHECK(esp_wifi_set_storage(WIFI_STORAGE_FLASH));

    // 7. Установка конфигурации
    esp_err_t set_config_result = esp_wifi_set_config(WIFI_IF_AP, &wifi_config);
    if (set_config_result != ESP_OK) {
        ESP_LOGE(TAG, "Failed to set WiFi config: %s", esp_err_to_name(set_config_result));
        return; // или esp_restart();
    }

    // 8. Запуск WiFi
    ESP_ERROR_CHECK(esp_wifi_start());

    // 9. Получение и вывод IP-адреса AP
    tcpip_adapter_ip_info_t ip_info;
    tcpip_adapter_get_ip_info(TCPIP_ADAPTER_IF_AP, &ip_info);
    ESP_LOGI(TAG, "WiFi AP started. SSID:%s, IP:" IPSTR, wifi_config.ap.ssid, IP2STR(&ip_info.ip));
}

void app_main(void) {
    ESP_LOGI(TAG, "====== APP MAIN STARTED ======");
    
    // 1. Настроим GPIO1 как выход (повторим, на всякий случай)
    gpio_set_direction(SOFT_UART_TX_GPIO, GPIO_MODE_OUTPUT);
    
    // 2. Поморгаем 10 раз с интервалом 500 мс
    for (int i = 0; i < 10; i++) {
        gpio_set_level(SOFT_UART_TX_GPIO, 1); // ВКЛ (светодиод горит)
        ESP_LOGI(TAG, "LED ON");
        vTaskDelay(500 / portTICK_PERIOD_MS);
        
        gpio_set_level(SOFT_UART_TX_GPIO, 0); // ВЫКЛ (светодиод не горит)
        ESP_LOGI(TAG, "LED OFF");
        vTaskDelay(500 / portTICK_PERIOD_MS);
    }
    
    ESP_LOGI(TAG, "====== LED TEST END. Starting main app... ======");
    
    // Инициализация NVS
    esp_err_t ret = nvs_flash_init();
    if (ret == ESP_ERR_NVS_NO_FREE_PAGES || ret == ESP_ERR_NVS_NEW_VERSION_FOUND) {
        // Если раздел поврежден или структура обновилась, стираем его
        ESP_ERROR_CHECK(nvs_flash_erase());
        ret = nvs_flash_init();
    }
    ESP_ERROR_CHECK(ret); // Проверяем успешность инициализации
    ESP_LOGI(TAG, "NVS initialized successfully");
    
    init_uart_soft();
    wifi_init_softap();
    start_api_server();
    
    ESP_LOGI(TAG, "=== SYSTEM READY ===");
    
    while(1) { vTaskDelay(1000 / portTICK_PERIOD_MS); }
}

