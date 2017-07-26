from django.contrib import admin
from .models import UserAsk


# Register your models here.
@admin.register(UserAsk)
class UserAskAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'mobile', 'course_name']
