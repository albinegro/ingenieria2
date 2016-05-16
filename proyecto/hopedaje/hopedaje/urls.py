from django.conf.urls import include, url
from django.contrib import admin
 
urlpatterns = [
    # Examples:
    # url(r'^$', 'hopedaje.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('home.urls', namespace='home')),
    url(r'hospedajes/^$', include('hospedajes.urls', namespace='hospedajes')),
    url(r'reservas/^$', include('reservas.urls', namespace='reservas')),
    url(r'customers/^$', include('customers.urls', namespace='customers')),
        
]
