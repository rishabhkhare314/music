from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import Http404

from music.models import Album, Song

def index(request):
  all_album=Album.objects.all()
  return render(request, 'home.html', {'data':all_album})

def detail(request, album_id):
  try:
    album=Album.objects.get(pk=album_id)
    songs = Song.objects.filter(album=album_id)
   # print(album)
  #  print(songs)
    #return render(request, 'details.html', {'data':album})
  except Album.DoesNotExist:
    raise Http404("Album Does Not Found")
  return render(request, 'details.html', {'data':album, 'songs':songs})
   #return HttpResponse(html)

   
def favorite(request, album_id):
  print(request.POST['song'])
  album=Album.objects.get(id=album_id)
  try:
    # selected_song = album.song_set.get(pk=request.POST['song'])
    album.is_favorie = request.POST['song']
    #return render(request, 'details.html', {'data':album})
  except (KeyError,Song.DoesNotExist):
    print("error")
  # return render(request, 'details.html', {'data':album, 'error_message':"You didn't select a valid song"})
  #return HttpResponse(html)
  return redirect('/music/'+str(album_id))