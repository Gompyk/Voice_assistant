# Файл для хранения конфиденциальных данных

CREDENTIALS = {
    # Пароль для разблокировки
    "system_password": None,

    # API ключи
    "speech_recognition_api_key": None,
    "tts_api_key": None,

    # Настройки безопасности
    "allowed_users": [
        "user1",
        "user2"
    ],

    # Соль для хеширования
    "security_salt": "your_unique_salt_here"
}


# Функции для работы с credentials
def get_system_password():
    return CREDENTIALS['system_password']


def check_user_access(username):
    return username in CREDENTIALS['allowed_users']