from django.contrib import admin

# Register your models here.
from django.contrib import admin

from questionOption.models import QuestionOptionsForFemalesModel, QuestionOptionsForMalesModel

# Register your models here.
class QuestionOptionsForFemalesModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'question')  # Specify fields to display in the admin list view
    list_filter = ('is_active',)  # Add filters for the admin list view

class QuestionOptionsForMalesModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'question')  # Specify fields to display in the admin list view
    list_filter = ('is_active',)  # Add filters for the admin list view

admin.site.register(QuestionOptionsForFemalesModel)
admin.site.register(QuestionOptionsForMalesModel)