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

    