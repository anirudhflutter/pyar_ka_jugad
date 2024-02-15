import django
from django.db import models


# Create your models here.
class CitiesModel(models.Model):
    """Model for cities data"""

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False)
    created_at = models.DateTimeField(default=django.utils.timezone.now, blank=True)
    updated_at = models.DateTimeField(default=django.utils.timezone.now, blank=True)
    state_id = models.IntegerField(blank=True, default=0)
    objects = models.Manager()


class StatesModel(models.Model):
    """Model for states data"""
    id = models.AutoField(primary_key=True)
    state_code = models.CharField(max_length=5, blank=False)
    country_id = models.IntegerField(blank=True, default=0)
    state_name = models.CharField(max_length=100, blank=False)
    created_at = models.DateTimeField(default=django.utils.timezone.now, blank=True)
    updated_at = models.DateTimeField(default=django.utils.timezone.now, blank=True)
    objects = models.Manager()


class CountriesModel(models.Model):
    """Model for countries data"""
    id = models.AutoField(primary_key=True)
    country_code = models.CharField(max_length=5, blank=False)
    country_name = models.CharField(max_length=100, blank=False)
    created_at = models.DateTimeField(default=django.utils.timezone.now, blank=True)
    updated_at = models.DateTimeField(default=django.utils.timezone.now, blank=True)
    objects = models.Manager()


class CountriesDialCodeModel(models.Model):
    """Model for countries dial code data"""
    id = models.AutoField(primary_key=True)
    country_dial_code = models.CharField(max_length=10, blank=False)
    country_code = models.CharField(max_length=5, blank=False)
    country_name = models.CharField(max_length=100, blank=False)
    created_at = models.DateTimeField(default=django.utils.timezone.now, blank=True)
    updated_at = models.DateTimeField(default=django.utils.timezone.now, blank=True)
    objects = models.Manager()
