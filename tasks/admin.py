from django.contrib import admin

from tasks.models import Task


class TaskAdmin(admin.ModelAdmin):

    class Meta:
        model = Task

    list_display = ('id', 'title', 'description', 'deadline', 'telegram_user_id', 'status')


admin.site.register(Task, TaskAdmin)
