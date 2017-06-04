from django.conf.urls import patterns, url
from music_pool import views

urlpatterns = patterns('',
    url(r'^songs$', views.all_song, name='all_song')
)