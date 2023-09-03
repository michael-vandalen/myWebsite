from django.db import models

class Album(models.Model):
    """
    Represents an album in the music database.

    Attributes:
        title (str): The title of the album.
        artist (str): The artist or band that released the album.
        release_date (date): The release date of the album.
        cover_image (ImageField): The cover image of the album.
        comments (str, optional): Additional comments or notes about the album (optional).

    Methods:
        __str__(): Returns a string representation of the album (its title).
    """
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=100)
    release_date = models.DateField()
    cover_image = models.ImageField(upload_to='album_covers/')
    comments = models.TextField(blank=True)

    def __str__(self):
        return self.title

class BandMember(models.Model):
    """
    Represents a band member or artist in the music database.

    Attributes:
        name (str): The name of the band member.
        role (str): The role or position of the band member (e.g., guitarist, vocalist).
        bio (str): A biography or description of the band member.

    Methods:
        __str__(): Returns a string representation of the band member (their name).
    """
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    bio = models.TextField()

    def __str__(self):
        return self.name
    
class Song(models.Model):
    """
    Represents a song in the music database.

    Attributes:
        title (str): The title of the song.
        album (Album): The album to which the song belongs (foreign key relationship).
        duration (duration): The duration of the song.

    Methods:
        __str__(): Returns a string representation of the song (its title).
    """
    title = models.CharField(max_length=200)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    duration = models.DurationField()

    def __str__(self):
        return self.title
