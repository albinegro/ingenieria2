from django.conf.urls import include, url
from hospedajes import views

urlpatterns = [
    url(r'^view/detail/(?P<hospe_id>\d+)/$', views.view_detail, name='view_detail'),
    url(r'^list/couchin/$', views.list_couchin, name='list_couchin'),
    url(r'^my/list/couchin/(?P<user_id>\d+)/$', views.my_hospedajes, name='my_hospedajes'),
    url(r'^my/create/couchin/$', views.create_hospedaje, name='create_hospedaje'),
    url(r'^booking/info/(?P<hospe_id>\d+)/$', views.info_booking, name='info_booking'),
    url(r'^my/list/photo/(?P<hospe_id>\d+)/$', views.list_photo, name='list_photo'),
    url(r'^my/edit/couchin/(?P<hospe_id>\d+)/$', views.edit_hospedaje, name='edit_hospedaje'),
    url(r'^my/delete/couchin/(?P<hospe_id>\d+)/$', views.delete_hospedaje, name='delete_hospedaje'),
    url(r'^admin/list/types/$', views.list_type, name='list_type'),
    url(r'^admin/add/types/$', views.add_type, name='add_type'),
    url(r'^admin/edit/types/(?P<type_id>\d+)/$', views.edit_type, name='edit_type'),
    url(r'^admin/delete/types/(?P<type_id>\d+)/$', views.delete_type, name='delete_type'),
    url(r'^my/make/favorito/(?P<user_id>\d+)/(?P<hospe_id>\d+)/$', views.make_favorito, name='make_favorito'),
    url(r'^my/favoritos/(?P<user_id>\d+)/$', views.my_favoritos, name='my_favoritos'),
    url(r'^my/responder/(?P<pregun_id>\d+)/$', views.responder, name='responder'),
    url(r'^all/responder/(?P<user_id>\d+)/$', views.all_responder, name='all_responder'),
    url(r'^have/preguntas/$', views.have_preguntas, name='have_preguntas'),
    url(r'^all/pregunta/(?P<user_id>\d+)/$', views.all_pregunta, name='all_pregunta'),
    url(r'^have/respuestas/$', views.have_respuestas, name='have_respuestas'),
]