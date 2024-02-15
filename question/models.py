from django.db import models
from django.utils import timezone

class QuestionForFemaleModel(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, default='', blank=False)
    is_active = models.BooleanField(default=True, null=True)
    is_deleted = models.BooleanField(default=True, null=True)
    created_at = models.DateTimeField(default=timezone.now, null=True)
    updated_at = models.DateTimeField(default=timezone.now, null=True)

class QuestionForMaleModel(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, default='', blank=False)
    is_active = models.BooleanField(default=True, null=True)
    is_deleted = models.BooleanField(default=True, null=True)
    created_at = models.DateTimeField(default=timezone.now, null=True)
    updated_at = models.DateTimeField(default=timezone.now, null=True)