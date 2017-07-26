from django.contrib import admin
from .models import UserProfile, EmailVerifyRecord


# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'is_active', 'email']


@admin.register(EmailVerifyRecord)
class EmailVerifyRecordAdmin(admin.ModelAdmin):
    list_display = ['id', 'send_type', 'code', 'email']
