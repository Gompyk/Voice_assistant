import threading
import time
from voice_assistant.core.recognition import SpeechRecognition
from voice_assistant.core.command_processor import CommandProcessor
from voice_assistant.core.logger import Logger
from voice_assistant.config.settings import GENERAL_SETTINGS


class VoiceAssistant:
    def __init__(self):
        self.recognition = SpeechRecognition()  
        self.command_processor = CommandProcessor()
        self.logger = Logger()
        self.is_active = True

    def start(self):
        """Запуск основного потока ассистента"""
        self.logger.log("Ассистент запущен")
        main_thread = threading.Thread(target=self.listen_loop)
        main_thread.start()

    def listen_loop(self):
        """Основной цикл прослушивания"""
        while self.is_active:
            try:
                # Получаем аудио
                audio = self.recognition.listen()

                # Распознаем речь
                command = self.recognition.recognize(audio)

                if command:
                    # Логируем распознанную команду
                    self.logger.log(f"Распознано: {command}")

                    # Обработка команды
                    result = self.command_processor.process(command)

                    # Логирование результата
                    if result:
                        self.logger.log(f"Результат: {result}")

            except Exception as e:
                self.logger.error(f"Ошибка в основном цикле: {e}")
                time.sleep(1)  # Небольшая пауза при ошибке


    def stop(self):
        """Остановка ассистента"""
        self.is_active = False
        self.logger.log("Ассистент остановлен")


    def add_command(self, command_type, handler):
        """Метод для динамического добавления команд"""
        self.command_processor.add_command(command_type, handler)