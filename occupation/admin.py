from django.contrib import admin
from occupation.models import OccupationModel

# Register your models here.
@admin.register(OccupationModel)
class UserOccupationModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')  # Specify fields to display in the admin list view
