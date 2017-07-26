from datetime import datetime

from django.db import models

from org.models import CourseOrg


class Course(models.Model):
    degree_type = (
        ("cj", "初级"),
        ("zj", "中级"),
        ("gj", "高级")
    )
    org = models.ForeignKey(CourseOrg, verbose_name='所属的课程机构')
    name = models.CharField(max_length=50, verbose_name="课程名称")
    desc = models.CharField(max_length=300, verbose_name="课程描述", null=True, blank=True)
    detail = models.TextField(verbose_name="课程详情", null=True, blank=True)
    degree = models.CharField(choices=degree_type, max_length=2)
    learn_times = models.IntegerField(default=0, verbose_name="学习时长(分钟数)", null=True, blank=True)
    students = models.IntegerField(default=0, verbose_name="学习人数", null=True, blank=True)
    fav_nums = models.IntegerField(default=0, verbose_name="收藏人数", null=True, blank=True)
    image = models.ImageField(upload_to="course/%Y/%m", verbose_name="封面图片", max_length=100, null=True, blank=True)
    click_nums = models.IntegerField(default=0, verbose_name="点击数", null=True, blank=True)
    # 表的添加时间
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间", null=True, blank=True)

    class Meta:
        verbose_name = "课程"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 章节表
class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name="课程")
    name = models.CharField(max_length=100, verbose_name="章节名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "章节"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 视频播放的信息
class Video(models.Model):
    # 是章节表有关联
    lesson = models.ForeignKey(Lesson, verbose_name="章节")
    name = models.CharField(max_length=100, verbose_name="视频名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "视频"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseResource(models.Model):
    # 和 课程有关联
    course = models.ForeignKey(Course, verbose_name="课程")
    name = models.CharField(max_length=100, verbose_name="名称")
    # 下载的是文件 就需要 文本的类型 就会 在后台形成上传的样式
    download = models.FileField(upload_to="course/resource/%Y/%m", verbose_name="资源文件", max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "课程资源"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
