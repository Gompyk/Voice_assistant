import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt
from core.assistant import VoiceAssistant

class VoiceAssistantGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Голосовой Ассистент")
        self.setFixedSize(300, 600)  # Установка фиксированных размеров окна

        self.assistant = VoiceAssistant()  # Создание экземпляра ассистента

        # Основной виджет
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Вертикальный макет
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # Кнопка для отправки команды
        self.microphone_button = QPushButton("🎤")
        self.microphone_button.setFixedSize(80, 80)  # Установка размера кнопки
        self.microphone_button.setStyleSheet("border-radius: 40px; background-color: #2E8B57;")  # Кнопка с закругленными краями
        self.microphone_button.clicked.connect(self.toggle_assistant)  # Подключение функции
        self.layout.addWidget(self.microphone_button, alignment=Qt.AlignmentFlag.AlignHCenter)  # Центрирование кнопки

        # Поле для вывода распознанного текста
        self.output_label = QLabel("")
        self.output_label.setStyleSheet("border: 1px solid #3CB371; background-color: #2E8B57; padding: 5px;")  # Очерченное поле
        self.layout.addWidget(self.output_label)

    def toggle_assistant(self):
        # Логика для включения/выключения ассистента
        if self.assistant.is_running:
            self.assistant.stop()
            self.microphone_button.setStyleSheet("border-radius: 40px; background-color: #FF6347;")  # Цвет для выключенного состояния
        else:
            self.assistant.start()
            self.microphone_button.setStyleSheet("border-radius: 40px; background-color: #2E8B57;")  # Цвет для включенного состояния

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VoiceAssistantGUI()
    window.show()
    sys.exit(app.exec())
