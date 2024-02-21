from django.contrib import admin

from user.models import UserModel

# Register your models here.
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'is_active', 'date_joined')  # Specify fields to display in the admin list view
    search_fields = ('username', 'email', 'first_name', 'last_name')  # Add fields for search functionality
    list_filter = ('is_active',)  # Add filters for the admin list view

admin.site.register(UserModel)