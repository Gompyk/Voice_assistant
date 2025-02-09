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

    @staticmethod
    def open_youtube(url="https://youtube.com"):
        """Открытие страницы"""
        try:
            webbrowser.open(url)
            return f"Открыт браузер со страницей {url}"
        except Exception as e:
            return f"Ошибка открытия браузера: {e}"

    @staticmethod
    def open_github(url="https://github.com"):
        """Открытие страницы"""
        try:
            webbrowser.open(url)
            return f"Открыт браузер со страницей {url}"
        except Exception as e:
            return f"Ошибка открытия браузера: {e}"

    @staticmethod
    def go_to_site(url):
        """Переход на указанный сайт"""
        try:
            webbrowser.open(url)
            return f"Перейдено на сайт {url}"
        except Exception as e:
            return f"Ошибка перехода на сайт: {e}"

    @staticmethod
    def refresh_page():
        """Обновление текущей страницы"""
        try:
            keyboard.press_and_release('f5')
            return "Страница обновлена"
        except Exception as e:
            return f"Ошибка обновления страницы: {e}"
