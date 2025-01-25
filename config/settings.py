GENERAL_SETTINGS = {
    "app_name": "Voice Assistant",
    "version": "1.0.0",

    # Настройки распознавания
    "language": "ru-RU",
    "recognition_timeout": 3,
    "noise_adjustment_time": 1,

    # Пути и директории
    "log_directory": "./logs/",
    "temp_directory": "./temp/",

    # Параметры безопасности
    "max_recognition_attempts": 3,
    "enable_logging": True
}

# Настройки для разных сервисов
SERVICE_SETTINGS = {
    "speech_recognition": {
        "provider": "google",
        "api_key": None,  # Можно оставить None для бесплатных сервисов
        "alternative_providers": ["sphinx", "wit"]
    },
    "tts_service": {
        "provider": "google",
        "language": "ru"
    }
}