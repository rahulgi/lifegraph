from django.conf.urls import patterns, url

from report import views

urlpatterns = patterns('',
    url(r'^$', views.new_report),
)
