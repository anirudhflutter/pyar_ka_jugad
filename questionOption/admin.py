from django.contrib import admin

# Register your models here.
from django.contrib import admin

from questionOption.models import QuestionOptionsForFemalesModel, QuestionOptionsForMalesModel

# Register your models here.
@admin.register(QuestionOptionsForFemalesModel)
class QuestionOptionsForFemalesModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'question')  # Specify fields to display in the admin list view
    list_filter = ('question__title',)  # Add filters for the admin list view

@admin.register(QuestionOptionsForMalesModel)
class QuestionOptionsForMalesModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'question')  # Specify fields to display in the admin list view
    list_filter = ('question__title',)  # Add filters for the admin list view