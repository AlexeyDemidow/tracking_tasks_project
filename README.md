## Сервис для постановки и отслеживания задач с уведомлениями в Telegram через бота

---
### Функциональность:
1. API на Django REST Framework:
   - POST /tasks/ — создать задачу с полями:
     - title (строка)
     - description (строка)
     - deadline (дата/время)
     - telegram_user_id (целое число)
   - GET /tasks/<id>/ — получить задачу
   - PATCH /tasks/<id>/ — обновить статус задачи (done / undone)
   - GET /tasks/?telegram_user_id=<id> — получить список задач пользователя
2. Фоновая задача (Celery):
Проверяет каждую минуту: есть ли активные задачи с deadline, наступающим в течение 10 минут.
Если есть — отправляет уведомление пользователю через Telegram-бота.
3. [Telegram-бот на aiogram](https://github.com/AlexeyDemidow/tracking_tasks_tg_bot):
   - Команда /start — приветствие
   - Команда /mytasks — возвращает список активных задач из API для telegram_user_id, равного message.from_user.id
   - Команда /done <task_id> — помечает задачу как выполненную
4. Прочее:
   - Redis используется как брокер для Celery
   - Nginx как обратный прокси к Django-приложению
   - Docker

---
### Установка и запуск
- Клонируйте репозиторий
- Установите зависимости `pip install -r requirements.txt`
- Создаем `.env` файл по образцу в `.env.example`
- Выполнить миграции `python manage.py makemigrations` и `python manage.py migrate`
- Для запуска выполните `python manage.py runserver`
- Для запуска в Docker выполните `docker-compose up -d --build`
- [Телеграм бот](https://github.com/AlexeyDemidow/tracking_tasks_tg_bot) выполнен отдельным проектом. Для его запуска клонируйте [репозиторий](https://github.com/AlexeyDemidow/tracking_tasks_tg_bot) и следуйте инструкции 
