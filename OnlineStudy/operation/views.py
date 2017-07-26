from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View

from .forms import UserAskForm


# Create your views here.

class UserAskView(View):
    """用户咨询"""

    def post(self, request):
        """这个需要使用modelform 来解决"""
        if request.is_ajax():
            print(request.POST)
            user_ask_form = UserAskForm(request.POST)
            if user_ask_form.is_valid():
                print(user_ask_form.cleaned_data)
                user_ask_form.save()
                content = {'code': '1', 'err': 'null'}
            else:
                content = {'code': '0', 'err': '验证失败'}
            return JsonResponse(content)
