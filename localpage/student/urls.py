from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.studentIndex, name='list'),
    url(r'^(?P<pk>[0-9]+)/$', views.studentDetail, name='detail'),
]
