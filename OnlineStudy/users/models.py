from django.db import models
from django.contrib.auth.models import User, AbstractUser

from datetime import datetime


# Create your models here.
class UserProfile(AbstractUser):
    """用户扩展表"""
    gender_type = (
        ('0', '女'),
        ('1', '男')
    )
    nick_name = models.CharField(max_length=50, verbose_name='昵称')
    birthday = models.DateField(verbose_name='生日', null=True, blank=True)
    gender = models.CharField(choices=gender_type, default='0', max_length=3, verbose_name='性别')
    address = models.CharField(max_length=50, verbose_name='地址')
    head_image = models.ImageField(upload_to='upload/%Y%M', verbose_name='头像')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        ordering = ('-id',)

    def __str__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    """验证信息"""
    code_type = (
        ('0', '注册码'),
        ('1', '忘记密码')
    )
    code = models.CharField(max_length=20, verbose_name="邮箱验证码")
    email = models.EmailField(max_length=50, verbose_name="邮箱")
    send_type = models.CharField(verbose_name='验证码类型', choices=code_type, max_length=10)
    send_time = models.DateTimeField(default=datetime.now, verbose_name='发送时间')

    # 发送时间  用于验证这个验证码是否过期 需要到包 datetime  当前的默认时间
    # 去掉括号 就是在这个类实例化的时候 才会去执行这个函数 不去掉 括号的时候
    # 数据库迁移的时候 就会执行这个函数  这样时间就不准确了

    class Meta:
        verbose_name = "邮箱验证码"
        verbose_name_plural = verbose_name
        ordering = ('-id',)

    def __str__(self):
        return self.send_type + '--' + self.email


class Banner(models.Model):
    """轮播图"""
    title = models.CharField(max_length=100, verbose_name="标题")
    image = models.ImageField(upload_to="banner/%Y/%m", verbose_name="轮播图", max_length=100)
    url = models.URLField(max_length=200, verbose_name="访问地址")
    index = models.IntegerField(default=100, verbose_name="顺序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "轮播图"
        verbose_name_plural = verbose_name
        ordering = ('-id',)

    def __str__(self):
        return self.title
