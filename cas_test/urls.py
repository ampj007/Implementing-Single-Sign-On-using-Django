from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import myapp.views
import myapp2.views
import myapp3.views


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', myapp.views.home, name='home'),
    url(r'^account/login/$', myapp.views.login, name='login'),
    url(r'^account/loggedin/$', myapp.views.loggedin, name='loggedin'),
    url(r'^account/logout/$', myapp.views.logout, name='logout'),
    url(r'^account/auth/$', myapp.views.auth_view, name='auth'),
    url(r'^app2/login/$', myapp2.views.login, name='login1'),
    url(r'^app2/loggedin/$', myapp2.views.loggedin, name='loggedin1'),
    url(r'^app2/logout/$', myapp2.views.logout, name='logout1'),
    url(r'^app2/auth/$', myapp2.views.auth_view, name='auth1'),
    url(r'^app3/login/$', myapp3.views.login, name='login2'),
    url(r'^app3/loggedin/$', myapp3.views.loggedin, name='loggedin2'),
    url(r'^app3/logout/$', myapp3.views.logout, name='logout2'),
    url(r'^app3/auth/$', myapp3.views.auth_view, name='auth2'),
]
