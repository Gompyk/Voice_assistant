from voice_assistant.core.assistant import VoiceAssistant


def main():
    # Создание экземпляра ассистента
    assistant = VoiceAssistant()

    try:
        # Вывод приветственного сообщения
        print("Голосовой ассистент запускается...")

        # Запуск ассистента
        assistant.start()

        # Ожидание завершения работы (можно добавить интерактивное меню)
        input("Нажмите Enter для завершения...")

        # Остановка ассистента
        assistant.stop()

    except Exception as e:
        print(f"Ошибка при работе ассистента: {e}")


if __name__ == "__main__":
    main()