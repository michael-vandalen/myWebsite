from django.shortcuts import render, get_object_or_404, redirect
from .models import Album
def home(request):
    """
    Renders the home page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered home page.
    """
    return render(request, 'home.html')

def albums(request):
    """
    Renders a list of albums.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered albums page with a list of albums.
    """
    albums = Album.objects.all()
    return render(request, 'albums.html', {'albums': albums})

def album_detail(request, album_id):
    """
    Renders the detail page for a specific album and handles comments.

    Args:
        request (HttpRequest): The HTTP request object.
        album_id (int): The ID of the album to display.

    Returns:
        HttpResponse: The rendered album detail page.
    """
    album = get_object_or_404(Album, pk=album_id)
    if request.method == 'POST':
        album.comments = request.POST['comments']
        album.save()
        return redirect('album_detail', album_id=album_id)
    return render(request, 'album_detail.html', {'album': album})
