from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'lifegraph.views.index'),

    url(r'^admin/', include(admin.site.urls)),

    # included urls
    url(r'^report/', include('report.urls')),
)
