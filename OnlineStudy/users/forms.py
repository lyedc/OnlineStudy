from django import forms
from captcha.fields import CaptchaField

class RegisterForm(forms.Form):
    """注册表单验证"""
    email = forms.EmailField(required=True)
    password = forms.CharField(min_length=5,max_length=10,required=True)
    captcha = CaptchaField(error_messages={'invalid':'验证码不正确...'})


class LoginForm(forms.Form):
    """登录表单验证"""
    username= forms.CharField(required=True)
    password = forms.CharField(required=True)
