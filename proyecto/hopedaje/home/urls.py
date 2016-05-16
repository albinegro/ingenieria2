from django.conf.urls import include, url
from home import views

urlpatterns = [

    url(r'^$', views.home, name='home'),
    url(r'^close_popup/$', views.close_popup, name='close_popup'),
]