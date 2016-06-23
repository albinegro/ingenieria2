from django.conf.urls import include, url
from customers import views
from django.contrib.auth.views import login, logout, password_reset, password_reset_done,\
                                      password_reset_confirm, password_reset_complete,\
                                      password_change, password_change_done


urlpatterns = [
    # Examples:
    # url(r'^$', 'electro.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^login/$', login,{'template_name':'login/login.html'}, name='login'),
    url(r'^logout/$', logout, {'next_page': '/'}, name="logout"),
    url(r'^password_change/$', views.password_change,
        {
            'template_name': 'password/change.html',
            'post_change_redirect': 'customers:password_change_done'
        },
        name="password_change"),
    #user reset
    url(r'^password_change_done/$', password_change_done,
        {
            'template_name': 'password/change_done.html',
        },
        name="password_change_done"),
    url(r'^password_reset/$', views.reset_password,
        name="password_reset"),
    url(r'^password_reset/done/$', password_reset_done,
        {'template_name': 'password/done.html'},
        name="password_reset_done"),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        password_reset_confirm, {
            'template_name': 'password/reset_confirm.html',
            'post_reset_redirect': 'customers:password_reset_complete'
        },  name="password_reset_confirm"),
    url(r'^reset/done/$', password_reset_complete,
        {'template_name': 'password/reset_complete.html'},
        name='password_reset_complete'),
    url(r'^select/$', views.select_account, name='select'),
    url(r'^change/acept/(?P<user_id>\d+)/$', views.acept_change, name='acept_change'),
    url(r'^create/client/$', views.create_user_client, name='create_user_client'),
    url(r'^update/premium/(?P<user_id>\d+)/$', views.update_premium, name='update_premium'),
    url(r'^update/user/(?P<user_id>\d+)/$', views.update_user, name='update_user'),
    url(r'^info/account/(?P<user_id>\d+)/$', views.info_account, name='info_account'),
    url(r'^info/user/(?P<user_id>\d+)/$', views.info_user, name='info_user'),
    url(r'^admin/conf/$', views.admin_conf, name='admin_conf'),

]