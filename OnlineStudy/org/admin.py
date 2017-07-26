from django.contrib import admin
from .models import CityDict, CourseOrg, Teacher


# Register your models here.
@admin.register(CityDict)
class CityDictAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'desc']


@admin.register(CourseOrg)
class CourseOrgAdmin(admin.ModelAdmin):
    list_display = ['name', 'desc', 'city', 'category', 'click_nums']


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'org', 'click_nums']






    # org = models.ForeignKey(CourseOrg, verbose_name="所属机构")
    # name = models.CharField(max_length=50, verbose_name="教师名称")
    # work_years = models.IntegerField(default=0, verbose_name="工作年限")
    # work_company = models.CharField(max_length=50, verbose_name="就职公司")
    # work_position = models.CharField(max_length=50, verbose_name="公司职位")
    # points = models.CharField(max_length=50, verbose_name="教学特点")
    # click_nums = models.IntegerField(default=0, verbose_name="点击数")
    # fav_nums = models.IntegerField(default=0, verbose_name="收藏数")
    # add_time = models.DateTimeField(default=datetime.now)




    #
    # name = models.CharField(max_length=50, verbose_name='机构名称')
    # desc = models.TextField(verbose_name='机构描述')
    # category = models.CharField(verbose_name='机构类别', default='pxjg', max_length=20,
    #                             choices=category_type)
    # click_nums = models.IntegerField(default=0, verbose_name='点击数')
    # fav_nums = models.IntegerField(default=0, verbose_name='收藏数')
    # logo_image = models.ImageField(upload_to='org/%Y/%m', verbose_name='logo')
    # address = models.CharField(max_length=150, verbose_name='机构地址')
    # city = models.ForeignKey(CityDict, verbose_name='所在城市')
    # students = models.IntegerField(default=0, verbose_name='学习人数')
    # course_nums = models.IntegerField(default=0, verbose_name='课程数')
    # add_time = models.DateTimeField(default=datetime.now)
