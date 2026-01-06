#include <esp_system.h>
#include <esp_event.h>
#include <esp_wifi.h>
#include <esp_log.h>
#include <nvs_flash.h>
#include <driver/uart.h>
#include <esp_http_server.h>
#include <string.h>
#include "driver/gpio.h"
#include "freertos/FreeRTOS.h"

#define TAG "T1337_WEB"

// Конфигурация аппаратного UART
#define UART_NUM           UART_NUM_2      // Используем UART2
#define UART_TX_PIN        GPIO_NUM_17     // TX для ESP32-S3
#define UART_RX_PIN        GPIO_NUM_16     // RX для ESP32-S3
#define UART_BAUD_RATE     115200          // Высокая скорость (было 300)

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

// Инициализация аппаратного UART
static void init_hardware_uart(void) {
    ESP_LOGI(TAG, "Initializing Hardware UART%d at %d baud...", UART_NUM, UART_BAUD_RATE);

    // Конфигурация параметров UART
    uart_config_t uart_config = {
        .baud_rate = UART_BAUD_RATE,
        .data_bits = UART_DATA_8_BITS,
        .parity = UART_PARITY_DISABLE,
        .stop_bits = UART_STOP_BITS_1,
        .flow_ctrl = UART_HW_FLOWCTRL_DISABLE,
        .source_clk = UART_SCLK_DEFAULT,
    };

    // Установка конфигурации UART
    ESP_ERROR_CHECK(uart_param_config(UART_NUM, &uart_config));

    // Установка пинов UART
    ESP_ERROR_CHECK(uart_set_pin(UART_NUM, UART_TX_PIN, UART_RX_PIN, UART_PIN_NO_CHANGE, UART_PIN_NO_CHANGE));

    // Установка буферов приема/передачи
    ESP_ERROR_CHECK(uart_driver_install(UART_NUM, 1024, 0, 0, NULL, 0));

    // Отправка тестового байта (ровно как в оригинале)
    const char test_byte = 'X';
    uart_write_bytes(UART_NUM, &test_byte, 1);
    ESP_LOGI(TAG, "Test byte '%c' sent via HARDWARE UART", test_byte);
    ESP_LOGI(TAG, "UART pins: TX=%d, RX=%d", UART_TX_PIN, UART_RX_PIN);
}

// Отправка команды через аппаратный UART (ТОЧНО как в оригинале)
void send_uart_command(char cmd) {
    // Отправляем ровно один байт, как в оригинальной программе
    int bytes_written = uart_write_bytes(UART_NUM, &cmd, 1);
    
    if (bytes_written == 1) {
        ESP_LOGI(TAG, "Command sent via HARDWARE UART: %c (at %d baud)", cmd, UART_BAUD_RATE);
    } else {
        ESP_LOGE(TAG, "Failed to send command via UART. Written: %d", bytes_written);
    }
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

// --- /api/cmd --- (без изменений)
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
    
    // Send command (логика не изменилась!)
    send_uart_command(command);
    
    // Send response
    const char *response = "OK: Command '%c' was sent\n";
    char resp_buffer[64];
    snprintf(resp_buffer, sizeof(resp_buffer), response, command);
    httpd_resp_set_type(req, "text/plain");
    httpd_resp_send(req, resp_buffer, strlen(resp_buffer));
    
    return ESP_OK;
}

// Start web server with API endpoints (без изменений)
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
    // 1. Инициализация сетевого стека
    ESP_ERROR_CHECK(esp_netif_init());
    
    // 2. Создание цикла событий
    ESP_ERROR_CHECK(esp_event_loop_create_default());
    
    // 3. Создание сетевого интерфейса для AP
    esp_netif_create_default_wifi_ap();

    // 4. Инициализация WiFi драйвера
    wifi_init_config_t cfg = WIFI_INIT_CONFIG_DEFAULT();
    ESP_ERROR_CHECK(esp_wifi_init(&cfg));

    // 5. Установка режима AP
    ESP_ERROR_CHECK(esp_wifi_set_mode(WIFI_MODE_AP));

    // 6. Конфигурация точки доступа
    wifi_config_t wifi_config = {
        .ap = {
            .ssid = WIFI_SSID,
            .password = WIFI_PASS,
            .ssid_len = strlen(WIFI_SSID),
            .channel = 6,
            .authmode = WIFI_AUTH_WPA_WPA2_PSK,
            .max_connection = MAX_STA_CONN,
            .beacon_interval = 100,
            .pmf_cfg = {
                .required = false,
            },
        },
    };

    // 7. Установка конфигурации
    ESP_ERROR_CHECK(esp_wifi_set_config(WIFI_IF_AP, &wifi_config));

    // 8. Запуск WiFi
    ESP_ERROR_CHECK(esp_wifi_start());

    // 9. Получение и вывод IP-адреса AP
    esp_netif_ip_info_t ip_info;
    esp_netif_t* netif = esp_netif_get_handle_from_ifkey("WIFI_AP_DEF");
    if (netif) {
        esp_netif_get_ip_info(netif, &ip_info);
        ESP_LOGI(TAG, "WiFi AP started. SSID:%s, IP:" IPSTR, wifi_config.ap.ssid, IP2STR(&ip_info.ip));
    } else {
        ESP_LOGI(TAG, "WiFi AP started. SSID:%s", wifi_config.ap.ssid);
    }
}

void app_main(void) {
    ESP_LOGI(TAG, "====== ESP32-S3 T1337 WEB STARTED ======");
    
    // Инициализация NVS
    esp_err_t ret = nvs_flash_init();
    if (ret == ESP_ERR_NVS_NO_FREE_PAGES || ret == ESP_ERR_NVS_NEW_VERSION_FOUND) {
        ESP_ERROR_CHECK(nvs_flash_erase());
        ret = nvs_flash_init();
    }
    ESP_ERROR_CHECK(ret);
    ESP_LOGI(TAG, "NVS initialized successfully");
    
    // Инициализация аппаратного UART
    init_hardware_uart();
    
    // Инициализация WiFi и веб-сервера
    wifi_init_softap();
    start_api_server();
    
    ESP_LOGI(TAG, "=== SYSTEM READY ===");
    ESP_LOGI(TAG, "Connect to WiFi: %s, Password: %s", WIFI_SSID, WIFI_PASS);
    ESP_LOGI(TAG, "Send POST commands to: http://192.168.4.1/api/cmd");
    ESP_LOGI(TAG, "UART speed: %d baud (was 300 baud with software UART)", UART_BAUD_RATE);
    
    // Основной цикл
    while(1) {
        vTaskDelay(1000 / portTICK_PERIOD_MS);
    }
}

