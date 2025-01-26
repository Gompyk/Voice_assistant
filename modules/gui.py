import tkinter as tk
from ..core.assistant import VoiceAssistant  # Обновленный импорт

class VoiceAssistantGUI:
    def __init__(self, master):
        self.master = master
        master.title("Голосовой Ассистент")

        self.label = tk.Label(master, text="Добро пожаловать в голосовой ассистент!")
        self.label.pack()

        self.command_entry = tk.Entry(master)
        self.command_entry.pack()

        self.submit_button = tk.Button(master, text="Отправить", command=self.process_command)
        self.submit_button.pack()

        self.response_label = tk.Label(master, text="")
        self.response_label.pack()

        self.assistant = VoiceAssistant()  # Создание экземпляра ассистента

    def process_command(self):
        command = self.command_entry.get()
        response = self.assistant.process_command(command)  # Вызов метода обработки команды
        self.response_label.config(text=f"Ответ: {response}")  # Отображение ответа на экране

if __name__ == "__main__":
    root = tk.Tk()
    gui = VoiceAssistantGUI(root)
    root.mainloop()
