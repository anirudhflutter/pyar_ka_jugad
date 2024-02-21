from django.contrib import admin

from recordComparision.models import DefaultPointsSystemForAnswersModel

# Register your models here.
class DefaultPointsSystemForAnswersModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_match')  # Specify fields to display in the admin list view
    list_filter = ('is_active',)  # Add filters for the admin list view

admin.site.register(DefaultPointsSystemForAnswersModel)