import keyboard
import pyautogui

class MediaCommands:
    @staticmethod
    def volume_up(step=10):
        """Увеличение громкости"""
        try:
            for _ in range(step // 10):
                keyboard.press_and_release('volume up')
            return f"Громкость увеличена на {step}%"
        except Exception as e:
            return f"Ошибка увеличения громкости: {e}"

    @staticmethod
    def volume_down(step=10):
        """Уменьшение громкости"""
        try:
            for _ in range(step // 10):
                keyboard.press_and_release('volume down')
            return f"Громкость уменьшена на {step}%"
        except Exception as e:
            return f"Ошибка уменьшения громкости: {e}"

    @staticmethod
    def mute():
        """Включение/выключение звука"""
        try:
            keyboard.press_and_release('volume mute')
            return "Звук переключен"
        except Exception as e:
            return f"Ошибка переключения звука: {e}"

    @staticmethod
    def play_pause():
        """Пауза/воспроизведение"""
        try:
            keyboard.press_and_release('play/pause media')
            return "Медиа переключено"
        except Exception as e:
            return f"Ошибка управления медиа: {e}"

    @staticmethod
    def next_track():
        """Следующий трек"""
        try:
            keyboard.press_and_release('next track')
            return "Переключено на следующий трек"
        except Exception as e:
            return f"Ошибка переключения трека: {e}"

    @staticmethod
    def prev_track():
        """Предыдущий трек"""
        try:
            keyboard.press_and_release('previous track')
            return "Переключено на предыдущий трек"
        except Exception as e:
            return f"Ошибка переключения трека: {e}"