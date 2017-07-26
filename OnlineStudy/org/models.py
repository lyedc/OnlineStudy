from django.db import models
from datetime import datetime


# # Create your models here.
class CityDict(models.Model):
    """城市列表"""
    name = models.CharField(max_length=20, verbose_name=u'城市名')
    desc = models.CharField(max_length=200, verbose_name=u'描述')
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u'城市'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseOrg(models.Model):
    """授课机构表"""
    category_type = (
        ('1', '培训机构'),
        ('2', '个人'),
        ('3', '高校')
    )
    name = models.CharField(max_length=50, verbose_name='机构名称')
    desc = models.TextField(verbose_name='机构描述', null=True, blank=True)
    category = models.CharField(verbose_name='机构类别', default='0', max_length=50,
                                choices=category_type)
    click_nums = models.IntegerField(default=0, verbose_name='点击数', null=True, blank=True)
    fav_nums = models.IntegerField(default=0, verbose_name='收藏数', null=True, blank=True)
    image = models.ImageField(upload_to='org/%Y/%m', verbose_name='logo', null=True, blank=True)
    address = models.CharField(max_length=150, verbose_name='机构地址', null=True, blank=True)
    city = models.ForeignKey(CityDict, verbose_name='所在城市', null=True, blank=True)
    students = models.IntegerField(default=0, verbose_name='学习人数', null=True, blank=True)
    course_nums = models.IntegerField(default=0, verbose_name='课程数', null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u'课程机构'
        verbose_name_plural = verbose_name
        ordering = ('-id',)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    """讲师表"""
    org = models.ForeignKey(CourseOrg, verbose_name="所属机构")
    name = models.CharField(max_length=50, verbose_name="教师名称")
    work_years = models.IntegerField(default=0, verbose_name="工作年限", null=True, blank=True)
    work_company = models.CharField(max_length=50, verbose_name="就职公司", null=True, blank=True)
    work_position = models.CharField(max_length=50, verbose_name="公司职位", null=True, blank=True)
    points = models.CharField(max_length=50, verbose_name="教学特点", null=True, blank=True)
    click_nums = models.IntegerField(default=0, verbose_name="点击数", null=True, blank=True)
    fav_nums = models.IntegerField(default=0, verbose_name="收藏数", null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = "教师"
        verbose_name_plural = verbose_name
        ordering = ('-id',)

    def __str__(self):
        return self.name
