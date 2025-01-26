<h1>Голосовой Ассистент</h1>
<h2>🤖 Описание проекта</h2>
Голосовой ассистент с поддержкой различных команд управления системой, медиа и браузером.

<h2>📦 Требования: </h2>

Python 3.7+<br>
Windows (основная поддержка) <br>
Микрофон<br>
Стабильное интернет-соединение<br>

<h2>🔧 Установка зависимостей:</h2>
pip install SpeechRecognition<br>
pip install pyaudio<br>
pip install keyboard<br>
pip install pyautogui<br>

<h2>🚀 Запуск приложения:</h2>

python -m voice_assistant.main

<h2>📋 Список команд: </h2>

<b>Системные команды:</b><br>
- "заблокировать" / "блокировка" - Блокировка экрана<br>
- "разблокировать" / "открыть" - Разблокировка экрана (в процессе доработки)<br>
- "выключить" / "выключение" - Выключение компьютера<br>
- "перезагрузить" / "перезагрузка" - Перезагрузка компьютера<br>
- "свернуть все" - Минимизировать все окна<br>
- "свернуть окно" - Свернуть текущее окно<br>
- "открыть проводник" - Открыть проводник Windows<br>
- "открыть настройки" - Открыть настройки системы<br>

<b>Медиа-управление:</b>
- "громче" / "увеличить звук" - Увеличение громкости<br>
- "тише" / "уменьшить звук" - Уменьшение громкости<br>
- "отключить звук" - Включение/выключение звука<br>
- "стоп" / "пауза" - Пауза/воспроизведение<br>
- "следующий трек" / "next" / "следующий" - Следующий трек<br>
- "прошлый трек" / "прошлый" / "previous" - Предыдущий трек<br>

<b>Управление браузером:</b>
- "новая вкладка" - Открыть новую вкладку<br>
- "закрыть вкладку" - Закрыть текущую вкладку<br>
- "восстановить вкладку" - Восстановить закрытую вкладку<br>
- "браузер" - Открыть браузер<br>
- "перейти на [название сайта]" - Открыть указанный сайт<br>
- "обновить страницу" - Обновить текущую вкладку<br>
- "ютуб" / "youtube" - Открыть youtube <br>
- "гитхаб" / "github" - Открыть github <br>

<b>Утилиты:</b>
- "скриншот" - Создать скриншот  <br>
- "блокнот" - Открыть блокнот  <br>
- "калькулятор" - Отрыть калькулятор <br>
- "командная строка" / "строка" - Открыть командную строку

<h2>🛠 Настройка</h2>
<b>Изменение / добавление команд</b>
- В modules/file.py прописываете метод с новым функционалом (при добавлении) <br>
- Редактируйте файл config/commands.py для добавления или изменения голосовых команд. <br>
- Далее по образцу редактируете файл core/command_processor.py <br>

<h2>Безопасность</h2>
Храните пароли и sensitive-данные в config/credentials.py<br>

<h2>⚠️ Известные проблемы</h2>
- Требуется стабильное интернет-соединение  <br>
- Работает корректно только в Windows  <br>
- Необходим микрофон  <br>

<h2>🔧 Troubleshooting</h2>
- Убедитесь, что микрофон включен  <br>
- Проверьте громкость микрофона  <br>
- Говорите четко и внятно  <br>
- Запускайте от имени администратора  <br>

<h2>📝 Логирование</h2>
Логи сохраняются в директории logs/ с разбивкой по датам.  <br>

<h2>🤝 Вклад в проект (please)</h2>
- Форкните репозиторий  <br>
- Создайте свою ветку (git checkout -b feature/AmazingFeature)  <br>
- Закоммитьте изменения (git commit -m 'Add some AmazingFeature')  <br>
- Запушьте в ветку (git push origin feature/AmazingFeature)  <br>
- Откройте Pull Request  <br>

<h2><b>💡 Советы по использованию:</b></h2>
- Говорите естественно и четко  <br>
- Проверьте настройки микрофона перед использованием  <br>
- Экспериментируйте с командами  <br>

<h2>🚀 Планы развития</h2>
- Добавление голосового помощника с ИИ  <br>
- Поддержка большего количества команд  <br>
- Кроссплатформенность  <br>

<h2><b>лицензия</b></h2>
Тестовый проект!
