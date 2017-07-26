from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.generic import View
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login, authenticate, logout

from .forms import RegisterForm, LoginForm
from utils.send_email import send_email
from .models import EmailVerifyRecord, UserProfile


# Create your views here.

class RegisterView(View):
    """register"""

    def get(self, request):
        """get提交"""
        if request.is_ajax():
            # ajax 验证邮箱是否存在
            email = request.GET.get('email')
            user_email = UserProfile.objects.filter(email=email).first()
            if user_email:
                data = {'code': '0', 'err': '邮箱已经存在...'}
            else:
                data = {'code': '1', 'err': 'null'}
            return JsonResponse(data)
        register_form = RegisterForm()
        content = {'register_form': register_form}
        return render(request, 'users/register.html', content)

    def post(self, request):
        """post提交"""
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            email = request.POST.get('email')
            return self.register_verify(email, register_form, request)
        else:
            content = {'register_form': register_form}
            return render(request, 'users/register.html', content)

    def register_verify(self, email, register_form, request):
        """注册信息验证"""
        if UserProfile.objects.filter(email=email).first():
            content = {'err': '要注册的邮箱已经存在...', 'register_form': register_form}
            return render(request, 'users/register.html', content)
        password = make_password(request.POST.get('password'))
        UserProfile.objects.create(email=email, password=password, is_active=False, username=email)
        try:
            if send_email(email, "register"):
                return render(request, 'users/send_success.html')
            else:
                content = {'err': '邮件发送失败,请检查邮箱是否正确...', 'register_form': register_form}
                return render(request, 'users/register.html', content)
        except Exception as err:
            # TODO 这里的错误应该写入日志
            content = {'err': '邮件发送失败,请检查邮箱是否正确...', 'register_form': register_form}
            return render(request, 'users/register.html', content)


class LoginView(View):
    """login"""

    def get(self, request):
        content = {}
        return render(request, 'users/login.html', content)

    def post(self, request):
        login_form = LoginForm(request.POST)
        print(login_form)
        if login_form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return redirect('/users/index')
                else:
                    err = "账户还没有激活,请先激活账户"
            else:
                err = "用户名或者密码错误.."
            content = {'err': err, 'login_form': login_form}
        else:
            content = {'login_form': login_form}
        return render(request, 'users/login.html', content)


class LoginOutView(View):
    """退出"""

    def get(self, request):
        logout(request)
        return redirect('/users/login')


class IndexView(View):
    """首页展示"""

    # TODO 首页的内容需要从数据库查询后展示在页面的
    def get(self, request):
        print(request.user)
        return render(request, 'users/index.html')


class RegisterActiveView(View):
    """邮件激活验证"""

    def get(self, request):
        register_code = request.GET.get('register')
        register_email = EmailVerifyRecord.objects.filter(code=register_code).first().email
        if register_email:
            UserProfile.objects.filter(email=register_email).update(is_active=True)
            return render(request, 'users/login.html')
        else:
            # TODO 是否要考虑验证码过期问题
            err = "验证码过期,请重新进行注册,激活..."
            return render(request, 'users/active_faile.html')
