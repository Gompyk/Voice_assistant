import tkinter as tk
from core.assistant import VoiceAssistant
import speech_recognition as sr

class VoiceAssistantGUI:
    def __init__(self, master):
        self.master = master
        master.title("Голосовой Ассистент")
        master.geometry("300x600")  # Установка более компактной формы
        master.resizable(False, False)  # Запрет изменения размеров окна
        master.configure(bg="#2E8B57")  # Установка темного фона

        # Темная строка заголовка
        self.header = tk.Frame(master, bg="#2E8B57")
        self.header.pack(fill=tk.X)

        # Элемент для отображения громкости
        self.volume_indicator = tk.Canvas(master, width=200, height=200, bg='white', highlightthickness=0)
        self.volume_indicator.pack(pady=20)

        # Создание круга
        self.volume_circle = self.volume_indicator.create_oval(25, 25, 175, 175, fill='#3CB371', outline='')  # Цвет круга

        # Добавление значка микрофона
        self.microphone_icon = self.volume_indicator.create_text(100, 100, text="🎤", font=("Arial", 40), fill="white")

        # Поле для вывода распознанного текста
        self.output_label = tk.Label(master, text="", bg="#2E8B57", font=("Arial", 14), borderwidth=2, relief="groove")
        self.output_label.pack(pady=10)

        self.assistant = VoiceAssistant()  # Создание экземпляра ассистента
        self.recognizer = sr.Recognizer()  # Инициализация распознавателя

        # Запуск распознавания речи
        self.start_recognition()

    def start_recognition(self):
        with sr.Microphone() as source:
            while True:
                audio = self.recognizer.listen(source)
                try:
                    text = self.recognizer.recognize_google(audio, language='ru-RU')
                    self.output_label.config(text=text)  # Отображение распознанного текста
                    self.process_command(text)  # Обработка команды
                except sr.UnknownValueError:
                    pass

    def process_command(self, command):
        response = self.assistant.process_command(command)  # Вызов метода обработки команды
        self.output_label.config(text=f"Ответ: {response}")  # Отображение ответа на экране

if __name__ == "__main__":
    root = tk.Tk()
    gui = VoiceAssistantGUI(root)
    root.mainloop()
