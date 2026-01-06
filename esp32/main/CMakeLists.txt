idf_component_register(
    SRCS "esp32.c"
    INCLUDE_DIRS "."
    REQUIRES esp_http_server esp_wifi nvs_flash esp_driver_uart esp_driver_gpio
)
