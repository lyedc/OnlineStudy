from django.contrib import admin
from .models import Course, Lesson, Video


# Register your models here.
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'org', 'degree', 'students', 'click_nums', 'fav_nums']
