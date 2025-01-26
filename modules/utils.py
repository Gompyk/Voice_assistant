import pyautogui
import os
import subprocess

class Utilities:
    @staticmethod
    def screenshot(filename="screenshot.png"):
        """Создание скриншота"""
        try:
            screenshot = pyautogui.screenshot()
            screenshot_path = os.path.join(os.getcwd(), filename)
            screenshot.save(screenshot_path)
            return f"Скриншот сохранен: {screenshot_path}"
        except Exception as e:
            return f"Ошибка создания скриншота: {e}"

    @staticmethod
    def open_calculator():
        """Открытие калькулятора"""
        try:
            subprocess.Popen('calc.exe')
            return "Калькулятор открыт"
        except Exception as e:
            return f"Ошибка открытия калькулятора: {e}"

    @staticmethod
    def open_notepad():
        """Открытие блокнота"""
        try:
            subprocess.Popen('notepad.exe')
            return "Блокнот открыт"
        except Exception as e:
            return f"Ошибка открытия блокнота: {e}"

    @staticmethod
    def open_cmd():
        """Открытие командной строки"""
        try:
            subprocess.Popen('cmd.exe')
            return "Командная строка открыта"
        except Exception as e:
            return f"Ошибка открытия командной строки: {e}"

    @staticmethod
    def open_explorer():
        """Открыть проводник"""
        try:
            subprocess.run('explorer', shell=True)
            return "Открыт проводник"
        except Exception as e:
            return f"Ошибка открытия проводника: {e}"

    @staticmethod
    def open_settings():
        """Открыть настройки системы"""
        try:
            subprocess.run('start ms-settings:', shell=True)
            return "Открыты настройки системы"
        except Exception as e:
            return f"Ошибка открытия настроек: {e}"


    