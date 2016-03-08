from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cas_test.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'myapp.views.home', name='home'),
    url(r'^account/login/$', 'myapp.views.login'),
    url(r'^account/loggedin/$', 'myapp.views.loggedin'),
    url(r'^account/invalid/$', 'myapp.views.invalid_login'),
    url(r'^account/logout/$', 'myapp.views.logout'),
    url(r'^account/auth/$', 'myapp.views.auth_view'),
    url(r'^app2/login/$', 'myapp2.views.login'),
    url(r'^app2/loggedin/$', 'myapp2.views.loggedin'),
    url(r'^app2/invalid/$', 'myapp2.views.invalid_login'),
    url(r'^app2/logout/$', 'myapp2.views.logout'),
    url(r'^app2/auth/$', 'myapp2.views.auth_view'),
    url(r'', include('mama_cas.urls')),
)
