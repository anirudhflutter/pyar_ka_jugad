from django.contrib import admin

from user.models import UserModel

# Register your models here.
@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'first_name', 'last_name', 'is_active', 'created_at', 'is_verified')  # Specify fields to display in the admin list view
    search_fields = ('username', 'email', 'first_name', 'last_name')  # Add fields for search functionality
    list_filter = ('is_active',)  # Add filters for the admin list view
