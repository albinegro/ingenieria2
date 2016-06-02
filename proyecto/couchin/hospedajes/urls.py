from django.conf.urls import include, url
from hospedajes import views

urlpatterns = [
    url(r'^view/detail/1/$', views.view_detail, name='view_detail'),
    url(r'^list/couchin/$', views.list_couchin, name='list_couchin'),
    url(r'^admin/list/types/$', views.list_type, name='list_type'),
    url(r'^admin/add/types/$', views.add_type, name='add_type'),
    url(r'^admin/edit/types/(?P<type_id>\d+)/$', views.edit_type, name='edit_type'),
    url(r'^admin/delete/types/(?P<type_id>\d+)/$', views.delete_type, name='delete_type'),
]