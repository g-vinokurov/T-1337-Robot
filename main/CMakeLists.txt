idf_component_register(
    SRCS "t1337_web.c"
    INCLUDE_DIRS "."
    REQUIRES esp8266 driver nvs_flash esp_http_server
)
