from django.contrib import admin

# Register your models here.
from django.contrib import admin

from answerOfQuestions.models import AnswersOfFemalesModel, AnswersOfMalesModel

# Register your models here.
@admin.register(AnswersOfFemalesModel)
class AnswersOfFemalesModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'selected_option')  # Specify fields to display in the admin list view
    list_filter = ('is_active',)  # Add filters for the admin list view

@admin.register(AnswersOfMalesModel)
class AnswersOfMalesModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'selected_option')  # Specify fields to display in the admin list view
    list_filter = ('is_active',)  # Add filters for the admin list view
    

