from django.shortcuts import render, get_object_or_404, redirect
from .models import Album
def home(request):
    return render(request, 'home.html')

def albums(request):
    albums = Album.objects.all()
    return render(request, 'albums.html', {'albums': albums})

def album_detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    if request.method == 'POST':
        album.comments = request.POST['comments']
        album.save()
        return redirect('album_detail', album_id=album_id)
    return render(request, 'album_detail.html', {'album': album})
