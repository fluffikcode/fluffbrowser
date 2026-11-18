"""Every user-facing string, in one place.

The interface ships in Russian (that is how FluffBrowser was designed).
Change the values below to translate the app — no other file needs touching.
"""

APP_NAME = "FluffBrowser"

# Welcome screen
TAGLINE = "Интеллектуальный веб-ассистент"
DESCRIPTION = "Напишите задачу в свободной форме, и агент выполнит её в браузере."
COMMANDS_LABEL = "Команды:"
CMD_CLEAR = "clear"
CMD_CLEAR_HINT = "(очистить экран)"
CMD_EXIT = "exit"
CMD_EXIT_HINT = "(выход)"
WELCOME_TITLE = "✦  F L U F F   S Y S T E M  ✦"
SUBTITLE_TEMPLATE = "v{version} • Agentic Browser"

# Status lines
BUSY_TASK = "◈ Выполнение задачи в браузере..."
BUSY_BROWSER = "Инициализация Chromium..."
BUSY_CLOSE = "Закрытие браузера..."
READY = "  ✦ Сессия браузера активна"
CLOSED = "  ◈ Браузер закрыт."

# Result / error panels
RESULT_TITLE = "✦ FluffBrowser"
RESULT_FALLBACK = "*Задача завершена (текстовый результат отсутствует).*"
ERROR_TITLE = "◈ Ошибка выполнения"

# Prompt
PROMPT_TITLE = "✦ Вы"
PROMPT_ARROW = "▸"

# Session control
GOODBYE = "Сессия завершена. До скорой встречи."
INTERRUPT = "  ◈ Принудительная остановка..."
EXIT_COMMANDS = ("exit", "выход", "quit", "q")
CLEAR_COMMANDS = ("clear", "очистить", "cls")

# Configuration warnings
CONFIG_TITLE = "◈ Проверьте настройки"
CONFIG_HINT = (
    "Откройте startbrowser.py и заполните BASE_URL, API_KEY и MODEL — "
    "или создайте .env на основе .env.example."
)
WARNING_PLACEHOLDER_KEY = "API-ключ пока не указан (стоит заглушка your-api-key)."
WARNING_INVALID_URL = "BASE_URL должен начинаться с http:// или https://"
