from django.urls import path, include
from . import views
from .views import home, albums, album_detail

urlpatterns = [
    path('', views.home, name='home'),
    path('albums/', views.albums, name='albums'),
    path('album/<int:album_id>/', views.album_detail, name='album_detail'),
    path('accounts/', include('django.contrib.auth.urls')),
]
