from django.db import models
from django.utils import timezone

from question.models import QuestionForFemaleModel, QuestionForMaleModel
from questionOption.models import QuestionOptionsForFemalesModel, QuestionOptionsForMalesModel
from user.models import UserModel

class AnswersOfMalesModel(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.ForeignKey(QuestionForMaleModel, on_delete=models.CASCADE)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    selected_option = models.ForeignKey(QuestionOptionsForMalesModel, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

class AnswersOfFemalesModel(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.ForeignKey(QuestionForFemaleModel, on_delete=models.CASCADE)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    selected_option = models.ForeignKey(QuestionOptionsForFemalesModel, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
