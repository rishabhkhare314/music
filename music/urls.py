
from django.urls import path,re_path
from . import views
app_name='music'
urlpatterns = [
    #/music/album.id
    path('',views.index,name='index'),
    re_path(r'(?P<album_id>[0-9]+)/',views.detail,name='detail'),
     #/music/album.id/favorie
     re_path(r'favorite/(?P<album_id>[0-9]+)',views.favorite,name='favorite'),
]


