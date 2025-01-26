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
        },
        "show_desktop": {
            "phrases": [
                "свернуть все",
                "свернуть"
            ],
            "description": "Минимизировать все окна"
        },
        "minimize_window": {
            "phrases": [
                "свернуть окно"
            ],
            "description": "Свернуть текущее окно"
        },
        "open_task_manager": {
            "phrases": [
                "открыть диспетчер задач",
                "диспетчер"
            ],
            "description": "Открыть диспетчер задач Windows"
        },
        "open_explorer": {
            "phrases": [
                "открыть проводник"
            ],
            "description": "Открыть проводник Windows"
        },
        "open_settings": {
            "phrases": [
                "открыть настройки"
            ],
            "description": "Открыть настройки системы"
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

    # Команды браузера
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
        "go_to_site": {
            "phrases": [
                "перейти на"
            ],
            "description": "Открыть указанный сайт"
        },
        "refresh_page": {
            "phrases": [
                "обновить страницу"
            ],
            "description": "Обновить текущую вкладку"
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

    # Утилиты
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
