import speech_recognition as sr
from voice_assistant.config.settings import GENERAL_SETTINGS


class SpeechRecognition:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.language = GENERAL_SETTINGS['language']

    def listen(self, timeout=None):
        """Захват аудио с микрофона"""
        timeout = timeout or GENERAL_SETTINGS['recognition_timeout']

        with self.microphone as source:
            # Адаптация к окружающему шуму
            self.recognizer.adjust_for_ambient_noise(
                source,
                duration=GENERAL_SETTINGS.get('noise_adjustment_time', 1)
            )

            print("Слушаю...")
            audio = self.recognizer.listen(source, timeout=timeout)
            return audio

    def recognize(self, audio):
        """Распознавание речи"""
        try:
            command = self.recognizer.recognize_google(
                audio,
                language=self.language
            )
            return command.lower()
        except sr.UnknownValueError:
            print("Речь не распознана")
            return None
        except sr.RequestError as e:
            print(f"Ошибка сервиса: {e}")
            return None