# Полный справочник голосовых команд

COMMANDS = {
    # Системные команды
    "system": {
        "lock": {
            "phrases": [
                "заблокировать",
                "блокировка",
                "lock screen"
            ],
            "description": "Блокировка экрана"
        },
        "unlock": {
            "phrases": [
                "разблокировать",
                "открыть",
                "unlock"
            ],
            "description": "Разблокировка экрана"
        },
        "shutdown": {
            "phrases": [
                "выключить",
                "выключение",
                "shutdown"
            ],
            "description": "Выключение компьютера"
        },
        "restart": {
            "phrases": [
                "перезагрузить",
                "перезагрузка",
                "restart"
            ],
            "description": "Перезагрузка компьютера"
        }
    },

    # Медиа-команды
    "media": {
        "volume_up": {
            "phrases": [
                "громче",
                "увеличить звук",
                "volume up"
            ],
            "description": "Увеличение громкости"
        },
        "volume_down": {
            "phrases": [
                "тише",
                "уменьшить звук",
                "volume down"
            ],
            "description": "Уменьшение громкости"
        },
        "mute": {
            "phrases": [
                "отключить звук",
                "включить звук",
            ],
            "description": "Включение/выключение звука"
        },
        "play_pause": {
            "phrases": [
                "стоп",
                "пауза",
            ],
            "description": "Пауза/воспроизведение"
        },
        "next_track": {
            "phrases": [
                "следующий трек",
                "следующий",
                "next"
            ],
            "description": "Следующий трек"
        },
        "prev_track": {
            "phrases": [
                "прошлый трек",
                "прошлый",
                "previous"
            ],
            "description": "Предыдущий трек"
        },
    },

    "browser":  {
        "new_tab": {
            "phrases": [
                "новая вкладка",
                "новая"
            ],
            "description": "Новая вкладка"
        },
        "close_tab": {
            "phrases": [
                "закрыть вкладку",
                "закрыть"
            ],
            "description": "Закрыть вкладку"
        },
        "reopen_tab": {
            "phrases": [
                "восстановить вкладку",
                "восстановить"
            ],
            "description": "Восстановить вкладку"
        },
        "open_browser": {
            "phrases": [
                "браузер",
                "browser"
            ],
            "description": "Открыть браузер"
        },
         "open_youtube": {
            "phrases": [
                "ютуб",
                "youtube"
            ],
            "description": "Открыть youtube"
        },
         "open_github": {
            "phrases": [
                "гитхаб",
                "github",
                "git",
            ],
            "description": "Открыть github"
        },
    },

    "utils":  {
        "screenshot":  {
            "phrases": [
                "скриншот",
                "скрин"
            ],
            "description": "Сделать скриншот"
        },
        "open_notepad":  {
            "phrases": [
                "блокнот",
                "notepad"
            ],
            "description": "Открытие блокнота"
        },
        "open_calculator":  {
            "phrases": [
                "калькулятор",
            ],
            "description": "Открытие калькулятора"
        },
        "open_cmd":  {
            "phrases": [
                "командная строка",
                "строка"
            ],
            "description": "Открытие командной строки"
        },

    }
}


# Функция для быстрого поиска команды
def find_command(user_phrase):
    for category in COMMANDS.values():
        for command, details in category.items():
            if user_phrase.lower() in [phrase.lower() for phrase in details['phrases']]:
                return command, category
    return None, None