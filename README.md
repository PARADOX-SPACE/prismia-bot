# 🌸 Prismia — Discord bot for Paradox SS14

[![Python](https://img.shields.io/badge/python-3.11-blue.svg)](https://python.org)
[![Discord](https://img.shields.io/badge/disnake-blue.svg)](https://discordpy.readthedocs.io/)
[![Docker](https://img.shields.io/badge/docker-ready-blue.svg)](https://docker.com)

Prismia — это многофункциональный Discord-бот для сервера **Paradox Space** (SS14).  
Обеспечивает привязку аккаунтов, логирование, HTTP-сервис для внешних запросов и многое другое.


## ✨ Возможности

- 🔐 **Привязка аккаунтов** — связывание Discord ID с игровыми профилями через одноразовые коды
- 🌐 **HTTP-сервер** — приём POST-запросов для внешней аутентификации
- 📦 **Модульная структура** — команды, события, задачи и модули загружаются автоматически
- 🐳 **Docker-поддержка** — лёгкий запуск в контейнере
- 🔒 **Безопасность** — проверка токенов, защита от спама


## 🚀 Быстрый старт

### 📋 Требования

- Docker и Docker Compose
- Python 3.11+ (для локальной разработки)

### ⚙️ Установка и запуск

1. **Клонируй репозиторий**
   ```bash
   git clone https://github.com/your-repo/prismia-bot.git
   cd prismia-bot
   ```

2. **Создай файл `.env`** (скопируй из `.env.example`)
   ```ini
   DISCORD_TOKEN=your_token_here
   BOT_PREFIX=!
   HTTP_SERVER_TOKEN=my_secret_token
   POSTGRES_DATABASE=ss14_main
   POSTGRES_USER=postgres
   POSTGRES_PASSWORD=password
   POSTGRES_HOST=postgres
   POSTGRES_PORT=5432
   TIMEZONE=Europe/Moscow
   ```

3. **Запусти через Docker Compose**
   ```bash
   docker-compose up -d
   ```

4. **Проверь логи**
   ```bash
   docker-compose logs -f
   ```

## 🐳 Команды Docker

| Команда | Описание |
|---------|----------|
| `docker-compose up -d` | Запустить бота в фоне |
| `docker-compose down` | Остановить и удалить контейнер |
| `docker-compose logs -f` | Просмотр логов |
| `docker-compose up -d --build` | Пересобрать и запустить |


## 🛠️ Локальная разработка (без Docker)

1. **Создай виртуальное окружение**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

2. **Установи зависимости**
   ```bash
   pip install -r requirements.txt
   ```

3. **Запусти бота**
   ```bash
   python main.py
   ```


## 📁 Структура проекта

```
prismia-bot/
├── commands/          # Команды бота
├── events/            # Обработчики событий
├── modules/           # Дополнительные модули
├── tasks/             # Фоновые задачи
├── logs/              # Логи (создаётся автоматически)
├── bot_init.py        # Инициализация бота
├── config.py          # Конфигурация и переменные окружения
├── data.py            # Глобальное хранилище данных
├── http_server.py     # HTTP-сервер для внешних запросов
├── logger.py          # Модуль логирования
├── main.py            # Точка входа
├── Dockerfile         # Инструкция для сборки Docker-образа
├── docker-compose.yml # Конфигурация Docker Compose
└── requirements.txt   # Зависимости Python
```


## 🔐 Безопасность

- Все токены и пароли хранятся в `.env` (не коммитятся в Git)
- HTTP-сервер проверяет токен в каждом запросе
- Поддержка CORS (при необходимости)


## 👑 Автор

**Schrödinger** — [GitHub](https://github.com/Schrodinger71)  
Сделано для Paradox Space
