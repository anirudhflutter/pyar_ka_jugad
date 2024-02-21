# pyaarKaJugad/user/models.py

from django.db import models

from location.models import CitiesModel,StatesModel,CountriesModel

class File(models.Model):
    file = models.FileField(blank=False)

class UserModel(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100, default='', null=False)
    last_name = models.CharField(max_length=100, default='', null=False)
    phone_number = models.CharField(max_length=15, null=False)  # Assuming PhoneNumber is a custom validator
    gender = models.CharField(max_length=10, default='', null=False)
    birth_date = models.DateField(default=None, null=False)
    country = models.ForeignKey(CountriesModel, on_delete=models.CASCADE, null=False)
    state = models.ForeignKey(StatesModel, on_delete=models.CASCADE, null=False)
    city = models.ForeignKey(CitiesModel, on_delete=models.CASCADE, null=False)
    images = models.CharField(max_length=200, default='', null=False)
    height = models.CharField(max_length=10, default='', null=False)
    weight = models.CharField(max_length=10, default='', null=False)
    instagram_id = models.CharField(max_length=100, default='', null=True)
    instagram_account_link = models.CharField(max_length=255, default='', null=True)
    is_free_trial_user = models.BooleanField(default=True, null=True)
    is_verified = models.BooleanField(default=False, null=True)
    is_active = models.BooleanField(default=True, null=True)
    is_deleted = models.BooleanField(default=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    designation = models.CharField(max_length=100, default='', null=False)
    occupation = models.CharField(max_length=100, default='', null=False)
