#include "esp_wifi.h"
#include "esp_log.h"
#include "esp_netif.h"
#include "esp_http_server.h"
#include "esp_camera.h"
#include "nvs_flash.h"

static const char *TAG = "ESP32_CAM";

#define CAMERA_MODEL_AI_THINKER_OV3660
#define PWDN_GPIO_NUM    -1 // Не используется на большинстве плат
#define RESET_GPIO_NUM   -1 // Не используется
#define XCLK_GPIO_NUM     0 // ВАЖНО! Для OV3660 почти всегда GPIO0
#define SIOD_GPIO_NUM    26 // I2C SDA (уже с подтяжкой R10)
#define SIOC_GPIO_NUM    27 // I2C SCL (уже с подтяжкой R11)

#define Y9_GPIO_NUM       5
#define Y8_GPIO_NUM      18
#define Y7_GPIO_NUM      19
#define Y6_GPIO_NUM      21
#define Y5_GPIO_NUM      36
#define Y4_GPIO_NUM      39
#define Y3_GPIO_NUM      34
#define Y2_GPIO_NUM      35
#define VSYNC_GPIO_NUM   25
#define HREF_GPIO_NUM    23
#define PCLK_GPIO_NUM    22

// === КОНФИГУРАЦИЯ СЕТИ ===
#define WIFI_SSID      "T1337_WEB"
#define WIFI_PASS      "t1337_tank"
#define STATIC_IP      "192.168.4.10"
#define GATEWAY_IP     "192.168.4.1"
#define NETMASK        "255.255.255.0"

// === 1. ИНИЦИАЛИЗАЦИЯ NVS (ДОЛЖНА БЫТЬ ПЕРВОЙ!) ===
static void initialize_nvs(void) {
    ESP_LOGI(TAG, "Initializing NVS...");
    
    esp_err_t ret = nvs_flash_init();
    if (ret == ESP_ERR_NVS_NO_FREE_PAGES || ret == ESP_ERR_NVS_NEW_VERSION_FOUND) {
        // Если NVS раздел поврежден, стираем и пробуем снова
        ESP_LOGE(TAG, "NVS partition needs to be erased (error: 0x%x)", ret);
        ESP_ERROR_CHECK(nvs_flash_erase());
        ret = nvs_flash_init();
    }
    ESP_ERROR_CHECK(ret);
    ESP_LOGI(TAG, "NVS initialized successfully");
}

// === 2. ИНИЦИАЛИЗАЦИЯ WI-FI ===
static void wifi_init_sta_static(void) {
    ESP_LOGI(TAG, "Initializing Wi-Fi...");
    
    // 1. Инициализация сетевого стека
    ESP_ERROR_CHECK(esp_netif_init());
    
    // 2. Создание цикла событий
    ESP_ERROR_CHECK(esp_event_loop_create_default());
    
    // 3. Создание STA интерфейса
    esp_netif_t *sta_netif = esp_netif_create_default_wifi_sta();
    if (!sta_netif) {
        ESP_LOGE(TAG, "Failed to create default STA netif");
        return;
    }
    
    // 4. Инициализация Wi-Fi
    wifi_init_config_t cfg = WIFI_INIT_CONFIG_DEFAULT();
    ESP_ERROR_CHECK(esp_wifi_init(&cfg));
    
    // 5. Настройка Wi-Fi
    wifi_config_t wifi_config = {
        .sta = {
            .ssid = WIFI_SSID,
            .password = WIFI_PASS,
            .threshold.authmode = WIFI_AUTH_WPA2_PSK,
        },
    };
    
    ESP_ERROR_CHECK(esp_wifi_set_mode(WIFI_MODE_STA));
    ESP_ERROR_CHECK(esp_wifi_set_config(WIFI_IF_STA, &wifi_config));
    ESP_ERROR_CHECK(esp_wifi_start());
    
    // 6. Настройка статического IP (если нужно)
    esp_netif_ip_info_t ip_info;
    memset(&ip_info, 0, sizeof(ip_info));
    esp_netif_str_to_ip4(STATIC_IP, &ip_info.ip);
    esp_netif_str_to_ip4(GATEWAY_IP, &ip_info.gw);
    esp_netif_str_to_ip4(NETMASK, &ip_info.netmask);
    
    ESP_ERROR_CHECK(esp_netif_dhcpc_stop(sta_netif));
    ESP_ERROR_CHECK(esp_netif_set_ip_info(sta_netif, &ip_info));
    
    ESP_LOGI(TAG, "Wi-Fi STA initialized. Connecting to AP: %s", WIFI_SSID);
    ESP_ERROR_CHECK(esp_wifi_connect());
}

// === 3. ИНИЦИАЛИЗАЦИЯ КАМЕРЫ ===
static esp_err_t camera_init(void) {
    ESP_LOGI(TAG, "=== INITIALIZING OV3660 on ESP32S ===");
    
    // ВКЛЮЧАЕМ ПИТАНИЕ КАМЕРЫ
    ESP_LOGI(TAG, "Powering camera via GPIO33...");
    gpio_reset_pin(33);
    gpio_set_direction(33, GPIO_MODE_OUTPUT);
    gpio_set_level(33, 1);
    vTaskDelay(200 / portTICK_PERIOD_MS); // Даем питанию стабилизироваться

    // КОНФИГУРАЦИЯ ИМЕННО ДЛЯ OV3660
    camera_config_t config;
    config.ledc_channel = LEDC_CHANNEL_0;
    config.ledc_timer = LEDC_TIMER_0;
    config.pin_d0 = Y2_GPIO_NUM;
    config.pin_d1 = Y3_GPIO_NUM;
    config.pin_d2 = Y4_GPIO_NUM;
    config.pin_d3 = Y5_GPIO_NUM;
    config.pin_d4 = Y6_GPIO_NUM;
    config.pin_d5 = Y7_GPIO_NUM;
    config.pin_d6 = Y8_GPIO_NUM;
    config.pin_d7 = Y9_GPIO_NUM;
    config.pin_xclk = XCLK_GPIO_NUM;      // GPIO0 для OV3660
    config.pin_pclk = PCLK_GPIO_NUM;
    config.pin_vsync = VSYNC_GPIO_NUM;
    config.pin_href = HREF_GPIO_NUM;
    config.pin_sscb_sda = SIOD_GPIO_NUM;  // I2C SDA (GPIO26)
    config.pin_sscb_scl = SIOC_GPIO_NUM;  // I2C SCL (GPIO27)
    config.pin_pwdn = PWDN_GPIO_NUM;
    config.pin_reset = RESET_GPIO_NUM;
    config.xclk_freq_hz = 12000000;       // 12 МГц - рабочая частота OV3660
    config.pixel_format = PIXFORMAT_JPEG;
    config.frame_size = FRAMESIZE_SVGA;   // Начните с SVGA (800x600), можно FRAMESIZE_VGA (640x480)
    config.jpeg_quality = 10;             // Качество JPEG (1-63, меньше = лучше)
    config.fb_count = 2;                  // Два фреймбуфера для стабильности
    config.grab_mode = CAMERA_GRAB_WHEN_EMPTY;

    ESP_LOGI(TAG, "Attempting to init camera with OV3660 config...");
    esp_err_t err = esp_camera_init(&config);
    
    if (err != ESP_OK) {
        ESP_LOGE(TAG, "Camera init failed with error 0x%x", err);
        ESP_LOGI(TAG, "Trying alternative XCLK pin GPIO4...");
        config.pin_xclk = 4; // Пробуем альтернативный пин для XCLK
        err = esp_camera_init(&config);
        
        if (err != ESP_OK) {
            ESP_LOGE(TAG, "Camera init failed completely. Please check:");
            ESP_LOGI(TAG, "1. OV3660 is 3.3V, not 5V!");
            ESP_LOGI(TAG, "2. Flat cable is firmly seated (try reseating)");
            ESP_LOGI(TAG, "3. Power supply can provide >500mA");
            return err;
        }
    }

    // Если дошли сюда - камера инициализирована!
    sensor_t *s = esp_camera_sensor_get();
    if (s != NULL) {
        ESP_LOGI(TAG, "=== CAMERA DETECTED ===");
        ESP_LOGI(TAG, "Sensor PID: 0x%04X, VER: 0x%04X", s->id.PID, s->id.VER);
        
        if (s->id.PID == OV3660_PID) {
            ESP_LOGI(TAG, "Model: OV3660 (3MP) confirmed!");
        } else {
            ESP_LOGI(TAG, "Unknown model, PID: 0x%04X", s->id.PID);
        }
    }
    
    ESP_LOGI(TAG, "Camera initialization SUCCESSFUL!");
    return ESP_OK;
}

// === 4. ОБРАБОТЧИК HTTP-ЗАПРОСА ДЛЯ ВИДЕОПОТОКА (MJPEG) ===
static esp_err_t stream_handler(httpd_req_t *req) {
    camera_fb_t *fb = NULL;
    esp_err_t res = ESP_OK;
    char part_buf[64];

    // Устанавливаем заголовки для MJPEG-потока
    res = httpd_resp_set_type(req, "multipart/x-mixed-replace;boundary=frame");
    if (res != ESP_OK) {
        return res;
    }
    
    httpd_resp_set_hdr(req, "Access-Control-Allow-Origin", "*");
    httpd_resp_set_hdr(req, "Cache-Control", "no-cache");

    ESP_LOGI(TAG, "Starting MJPEG stream to client");

    while (true) {
        fb = esp_camera_fb_get(); // Получаем новый кадр с камеры
        if (!fb) {
            ESP_LOGE(TAG, "Camera capture failed");
            res = ESP_FAIL;
            break;
        }

        // Формируем часть MJPEG-потока
        int blen = snprintf(part_buf, 64,
                            "\r\n--frame\r\n"
                            "Content-Type: image/jpeg\r\n"
                            "Content-Length: %u\r\n\r\n",
                            fb->len);
        if (httpd_resp_send_chunk(req, part_buf, blen) != ESP_OK) {
            break;
        }
        
        if (httpd_resp_send_chunk(req, (const char *)fb->buf, fb->len) != ESP_OK) {
            break;
        }

        esp_camera_fb_return(fb); // Возвращаем буфер кадра
        fb = NULL;
    }

    if (fb) {
        esp_camera_fb_return(fb);
    }
    
    ESP_LOGI(TAG, "MJPEG stream stopped");
    return res;
}

// === 5. НАСТРОЙКА И ЗАПУСК HTTP-СЕРВЕРА ===
static httpd_handle_t start_webserver(void) {
    httpd_config_t config = HTTPD_DEFAULT_CONFIG();
    config.server_port = 80;
    config.max_uri_handlers = 8;

    httpd_handle_t server = NULL;
    if (httpd_start(&server, &config) == ESP_OK) {
        // Регистрируем обработчик для видеопотока
        httpd_uri_t stream_uri = {
            .uri = "/mjpeg/1",
            .method = HTTP_GET,
            .handler = stream_handler,
            .user_ctx = NULL
        };
        httpd_register_uri_handler(server, &stream_uri);
        ESP_LOGI(TAG, "HTTP server started on port %d", config.server_port);
    }
    return server;
}

// === 6. ГЛАВНАЯ ФУНКЦИЯ ===
void app_main(void) {
    ESP_LOGI(TAG, "=== ESP32-CAM Client + Streamer Starting ===");
    
    // 1. СНАЧАЛА ИНИЦИАЛИЗИРУЕМ NVS
    initialize_nvs();
    
    // 2. Инициализируем Wi-Fi
    ESP_LOGI(TAG, "Step 1: Initializing Wi-Fi...");
    wifi_init_sta_static();
    
    // 3. Ждем подключения к Wi-Fi
    ESP_LOGI(TAG, "Step 2: Waiting for Wi-Fi connection...");
    for (int i = 0; i < 20; i++) {
        wifi_ap_record_t ap_info;
        if (esp_wifi_sta_get_ap_info(&ap_info) == ESP_OK) {
            ESP_LOGI(TAG, "Connected to AP: %s, RSSI: %d", 
                    WIFI_SSID, ap_info.rssi);
            break;
        }
        vTaskDelay(500 / portTICK_PERIOD_MS);
    }
    // НЕ включаем питание здесь - это делает camera_init()
    // ESP_LOGI(TAG, "Step 3: Enabling camera power...");
    
    // 4. Камера
    ESP_LOGI(TAG, "Step 4: Initializing camera...");
    esp_err_t cam_err = camera_init();
    if (cam_err != ESP_OK) {
        ESP_LOGW(TAG, "Camera failed, but continuing...");
    }
    
    // 5. Запускаем HTTP-сервер (даже если камера не работает)
    ESP_LOGI(TAG, "Step 5: Starting HTTP server...");
    httpd_handle_t server = start_webserver();
    if (server == NULL) {
        ESP_LOGE(TAG, "Failed to start HTTP server");
    } else {
        ESP_LOGI(TAG, "System ready! Stream: http://%s/mjpeg/1", STATIC_IP);
        ESP_LOGI(TAG, "Note: If camera failed, stream will show black/error");
    }
}
