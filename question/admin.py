from django.contrib import admin

from question.models import QuestionForFemaleModel, QuestionForMaleModel

# Register your models here.
@admin.register(QuestionForFemaleModel)
class QuestionForFemaleModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')  # Specify fields to display in the admin list view
    list_filter = ('is_active',)  # Add filters for the admin list view

@admin.register(QuestionForMaleModel)
class QuestionForMaleModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')  # Specify fields to display in the admin list view
    list_filter = ('is_active',)  # Add filters for the admin list view