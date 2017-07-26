from django.conf.urls import url
from django.views.generic import TemplateView

from users import views

urlpatterns = [
    url(r'^index/$', views.IndexView.as_view(), name='index'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^login_out/$', views.LoginOutView.as_view(), name='login_out'),
    url(r'^register/$', views.RegisterView.as_view(), name='register'),
    url(r'^register_active/$', views.RegisterActiveView.as_view(), name='register_active'),
    url(r'^send_success/$', TemplateView.as_view(template_name='users/send_success.html')),
]
