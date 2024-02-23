from django.contrib import admin

from recordComparision.models import DefaultPointsSystemForAnswersModel

# Register your models here.
@admin.register(DefaultPointsSystemForAnswersModel)
class DefaultPointsSystemForAnswersModelAdmin(admin.ModelAdmin):
    list_display = ('female_question','male_question','female_answer','male_answer','total_points', 'is_match')  # Specify fields to display in the admin list view
    list_filter = ('is_active',)  # Add filters for the admin list view