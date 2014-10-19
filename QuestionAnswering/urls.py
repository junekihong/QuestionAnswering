from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^questions/', include('questions.urls', namespace="questions")),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^static/', include("questions.urls", namespace="questions"))
)

