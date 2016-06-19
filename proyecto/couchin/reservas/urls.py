from django.conf.urls import include, url
from reservas import views

urlpatterns = [

               url(r'^make/booking/(?P<hospe_id>\d+)/(?P<user_id>\d+)/$', views.make_booking, name='make_booking'),
               url(r'^acept/reserva/(?P<hospe_id>\d+)/(?P<rese_id>\d+)/$', views.acept_reserva, name='acept_reserva'),
               url(r'^acept/post/$', views.post_acept, name='post_acept'),
               url(r'^my/booking/(?P<user_id>\d+)/$', views.my_booking, name='my_list_booking'),
               url(r'^my/rental/(?P<user_id>\d+)/$', views.my_rental, name='my_list_rental'),

]