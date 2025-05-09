from django.contrib import admin
from .models import Task
from easyaudit.models import RequestEvent
from core.models import RequestEventExtra


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'completed', 'created_by', 'created_at', 'updated_at')
    list_filter = ('completed', 'created_by')
    search_fields = ('title', 'description')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(RequestEventExtra)
class RequestEventExtraAdmin(admin.ModelAdmin):
    list_display = ('request_event', 'country', 'user_agent')