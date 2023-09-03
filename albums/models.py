from django.db import models

class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=100)
    release_date = models.DateField()
    cover_image = models.ImageField(upload_to='album_covers/')
    comments = models.TextField(blank=True)

    def __str__(self):
        return self.title

class BandMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    bio = models.TextField()

    def __str__(self):
        return self.name
    
class Song(models.Model):
    title = models.CharField(max_length=200)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    duration = models.DurationField()

    def __str__(self):
        return self.title
