from voice_assistant.config.commands import COMMANDS, find_command
from voice_assistant.modules.system import SystemCommands
from voice_assistant.modules.media import MediaCommands
from voice_assistant.modules.browser import BrowserCommands
from voice_assistant.modules.utils import Utilities


class CommandProcessor:
    def __init__(self):
        # Маппинг команд к их обработчикам
        self.command_handlers = {
            # Системные команды
            "lock": SystemCommands.lock_screen,
            "unlock": SystemCommands.unlock_screen,
            "shutdown": SystemCommands.shutdown,
            "restart": SystemCommands.restart,

            # Медиа-команды
            "volume_up": MediaCommands.volume_up,
            "volume_down": MediaCommands.volume_down,
            "mute": MediaCommands.mute,
            "play_pause": MediaCommands.play_pause,
            "next_track": MediaCommands.next_track,
            "prev_track": MediaCommands.prev_track,

            # Команды браузера
            "new_tab": BrowserCommands.new_tab,
            "close_tab": BrowserCommands.close_tab,
            "reopen_tab": BrowserCommands.reopen_tab,
            "open_browser": BrowserCommands.open_browser,

            # Утилиты
            "screenshot": Utilities.screenshot,
            "open_notepad": Utilities.open_notepad
        }

    def process(self, command):
        """Обработка голосовой команды"""
        # Поиск команды в справочнике
        cmd_type, category = find_command(command)

        if cmd_type:
            # Выполнение соответствующего обработчика
            handler = self.command_handlers.get(cmd_type)
            if handler:
                return handler()

        return "Команда не распознана"