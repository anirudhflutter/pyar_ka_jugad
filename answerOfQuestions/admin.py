from django.contrib import admin

# Register your models here.
from django.contrib import admin

from answerOfQuestions.models import AnswersOfFemalesModel, AnswersOfMalesModel

# Register your models here.
class AnswersOfFemalesModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')  # Specify fields to display in the admin list view
    list_filter = ('is_active',)  # Add filters for the admin list view

class AnswersOfMalesModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')  # Specify fields to display in the admin list view
    list_filter = ('is_active',)  # Add filters for the admin list view
    
admin.site.register(AnswersOfFemalesModel)
admin.site.register(AnswersOfMalesModel)

