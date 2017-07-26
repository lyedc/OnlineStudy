from django.conf.urls import url

from org import views

urlpatterns = [
    url(r'^org_list/(?P<category>\d+)-(?P<city_id>\d+)/$', views.OrgListView.as_view(), name='org_list'),
    url(r'^org_study/$', views.OrgStudyView.as_view(), name='org_study'),
    url(r'^org_detail/(?P<nid>\d+)/$', views.OrgDetailView.as_view(), name='org_detail'),
]