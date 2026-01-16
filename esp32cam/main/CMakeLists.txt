idf_component_register(
    SRCS "esp32cam.c"
    INCLUDE_DIRS "."
    REQUIRES esp_http_server esp_wifi esp32-camera nvs_flash
)

