from django.conf.urls import include, url
from hospedajes import views

urlpatterns = [

    url(r'^admin/list/types/$', views.list_type, name='list_type'),
    url(r'^admin/edit/types/(?P<type_id>\d+)/$', views.edit_type, name='edit_type'),
    url(r'^admin/delete/types/(?P<type_id>\d+)/$', views.delete_type, name='delete_type'),
]