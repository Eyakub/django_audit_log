from django.db import models
from django.contrib.auth.models import User
from easyaudit.models import RequestEvent


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class RequestEventExtra(models.Model):
    request_event = models.OneToOneField(RequestEvent, on_delete=models.CASCADE, related_name='extra')
    country = models.CharField(max_length=64, blank=True, null=True)
    user_agent = models.TextField(blank=True, null=True)
