from django.conf.urls import url
from django.contrib import admin

from liquid import views as liquid_views

urlpatterns = [
    url(r'^ffmpeg$', liquid_views.FFMPEG_submit, name='ffmpeg'),
    #url(r'^soundcloud', liquid_views.FFMPEG_submit, name='ffmpeg'),
    url(r'^ffmpeg-submit', liquid_views.FFMPEG_submit, name='ffmpeg_submit'),
    url(r'^soundcloud-submit', liquid_views.soundcloud_submit, name='soundcloud_submit'),
    url(r'^wget-submit', liquid_views.wget_submit, name='wget_submit'),
    url(r'^youtubedl-get-formats', liquid_views.youtube_dl_get_formats, name='youtube_dl_get_formats')

]