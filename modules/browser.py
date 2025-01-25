
import pyautogui
import keyboard
import webbrowser

class BrowserCommands:
    @staticmethod
    def new_tab():
        """Открытие новой вкладки"""
        try:
            keyboard.press_and_release('ctrl+t')
            return "Новая вкладка открыта"
        except Exception as e:
            return f"Ошибка открытия вкладки: {e}"

    @staticmethod
    def close_tab():
        """Закрытие текущей вкладки"""
        try:
            keyboard.press_and_release('ctrl+w')
            return "Вкладка закрыта"
        except Exception as e:
            return f"Ошибка закрытия вкладки: {e}"

    @staticmethod
    def reopen_tab():
        """Восстановление закрытой вкладки"""
        try:
            keyboard.press_and_release('ctrl+shift+t')
            return "Вкладка восстановлена"
        except Exception as e:
            return f"Ошибка восстановления вкладки: {e}"

    @staticmethod
    def open_browser(url="https://google.com"):
        """Открытие браузера"""
        try:
            webbrowser.open(url)
            return f"Открыт браузер со страницей {url}"
        except Exception as e:
            return f"Ошибка открытия браузера: {e}"