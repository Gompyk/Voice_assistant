import logging
from config.settings import GENERAL_SETTINGS
import os
from datetime import datetime


class Logger:
    def __init__(self):
        # Создание директории для логов
        log_dir = GENERAL_SETTINGS['log_directory']
        os.makedirs(log_dir, exist_ok=True)

        # Имя файла лога с текущей датой
        log_file = os.path.join(
            log_dir,
            f"assistant_{datetime.now().strftime('%Y%m%d')}.log"
        )

        # Настройка логгера
        logging.basicConfig(
            filename=log_file,
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s: %(message)s'
        )
        self.logger = logging.getLogger()

    def log(self, message):
        """Запись информационного сообщения"""
        print(message)  # Вывод в консоль
        self.logger.info(message)

    def error(self, message):
        """Запись сообщения об ошибке"""
        print(f"ОШИБКА: {message}")
        self.logger.error(message)