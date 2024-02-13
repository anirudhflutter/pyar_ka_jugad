from django.db import models
from django.utils import timezone

from question.models import QuestionForFemaleModel, QuestionForMaleModel

class QuestionOptionsForFemalesModel(models.Model):
    title = models.CharField(max_length=255)
    question = models.ForeignKey(QuestionForFemaleModel, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

class QuestionOptionsForMalesModel(models.Model):
    title = models.CharField(max_length=255)
    question = models.ForeignKey(QuestionForMaleModel, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
