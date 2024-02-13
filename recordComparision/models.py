from django.db import models
from django.utils import timezone

from answerOfQuestions.models import AnswersOfFemalesModel, AnswersOfMalesModel
from user.models import UserModel

class ComparingRecordsAnswerWiseModel(models.Model):
    female_answer = models.ForeignKey(AnswersOfFemalesModel, on_delete=models.CASCADE)
    male_answer = models.ForeignKey(AnswersOfMalesModel, on_delete=models.CASCADE)
    total_points = models.IntegerField(default=0)  # Assuming default value is 0
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

class TotalRecordsComparisonModel(models.Model):
    female_user = models.ForeignKey(UserModel, related_name='female_user', on_delete=models.CASCADE)
    male_user = models.ForeignKey(UserModel, related_name='male_user', on_delete=models.CASCADE)
    total_points = models.IntegerField(default=0)  # Assuming default value is 0
    is_match = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
