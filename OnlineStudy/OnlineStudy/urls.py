"""OnlineStudy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve  #用于处理静态文件
from django.conf import settings
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^users/', include('users.urls', namespace='users')),
    url(r'^org/', include('org.urls', namespace='org')),
    url(r'^course/', include('course.urls', namespace='course')),
    url(r'^operation/', include('operation.urls', namespace='operation')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),  # 处理上传文件的访问路径
]
