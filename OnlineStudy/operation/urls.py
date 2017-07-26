from django.conf.urls import url
from operation import views

urlpatterns = [
    url(r'^user_ask/$', views.UserAskView.as_view(), name='user_ask'),
]
