"""test1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)), 
    url(r'^$','testing.views.content'), #content page has been set as the homepage
    url(r'^content/','testing.views.content', name = 'content'),
    #url(r'^navbar/','testing.views.navbar', name = 'navbar'), 
    url(r'^detail/(?P<art_id>[0-9]+)/','testing.views.detail', name = 'detail'), #article id has been passed as an argument in the url. 
    #url(r'^whereto/','testing.views.whereto', name = 'whereto'),
]
'''navbar and whereto pages are been restricted from external access 
if they are not listed in the url patterns, this is a major advantage in python with respect to other frameworks.'''

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)