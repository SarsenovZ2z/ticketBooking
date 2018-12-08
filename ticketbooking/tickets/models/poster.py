from django.core.files.storage import FileSystemStorage
from django.db import models
from .film import Film

class Poster(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="posters")
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name = "poster"
        verbose_name_plural = "posters"

    def __str__(self):
        return "{}".format(self.image)
