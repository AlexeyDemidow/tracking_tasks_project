from django.db import models


class Task(models.Model):
    title = models.CharField('Название', max_length=100)
    description = models.CharField('Описание', max_length=100)
    deadline = models.DateTimeField('Дедлайн',)
    telegram_user_id = models.IntegerField('ID пользователя телеграм')

    done = 'done'
    undone = 'undone'
    status_list = [(done, done), (undone, undone)]
    status = models.CharField('Статус задачи', max_length=10, choices=status_list, default=undone)
