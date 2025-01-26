import os
import subprocess
import pyautogui
import keyboard
# from voice_assistant.config.credentials import get_system_password


class SystemCommands:
    @staticmethod
    def lock_screen():
        """Блокировка экрана"""
        try:
            subprocess.run('rundll32.exe user32.dll,LockWorkStation', shell=True)
            return "Экран заблокирован"
        except Exception as e:
            return f"Ошибка блокировки: {e}"

    @staticmethod
    def unlock_screen():
        """Разблокировка экрана"""
        try:
            # Эмуляция нажатия Enter
            pyautogui.press('enter')

            # Опциональный ввод пароля
            password = get_system_password()
            keyboard.write(password)
            keyboard.press('enter')

            return "Выполнена попытка разблокировки"
        except Exception as e:
            return f"Ошибка разблокировки: {e}"

    @staticmethod
    def shutdown():
        """Выключение компьютера"""
        try:
            os.system('shutdown /s /t 1')
            return "ПК будет выключен"
        except Exception as e:
            return f"Ошибка выключения: {e}"

    @staticmethod
    def restart():
        """Перезагрузка компьютера"""
        try:
            os.system('shutdown /r /t 1')
            return "ПК будет перезагружен"
        except Exception as e:
            return f"Ошибка перезагрузки: {e}"

    @staticmethod
    def sleep():
        """Спящий режим"""
        try:
            os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')
            return "ПК переходит в спящий режим"
        except Exception as e:
            return f"Ошибка перехода в спящий режим: {e}"

    @staticmethod
    def hibernate():
        """Гибернация"""
        try:
            os.system('rundll32.exe powrprof.dll,SetSuspendState 1,1,0')
            return "ПК переходит в режим гибернации"
        except Exception as e:
            return f"Ошибка гибернации: {e}"

    @staticmethod
    def minimize_window():
        """Свернуть текущее окно"""
        try:
            pyautogui.hotkey('win', 'd')  # Свернуть все окна
            return "Текущее окно свернуто"
        except Exception as e:
            return f"Ошибка сворачивания окна: {e}"

    @staticmethod
    def show_desktop():
        """Перейти на рабочий стол"""
        try:
            pyautogui.hotkey('win', 'd')  # Свернуть все окна
            return "Перешли на рабочий стол"
        except Exception as e:
            return f"Ошибка перехода на рабочий стол: {e}"

