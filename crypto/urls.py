from django.conf.urls import patterns, include, url
from django.contrib import admin
from crypto_app.views import HomeView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'crypto.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomeView.as_view(), name='home'),
)
