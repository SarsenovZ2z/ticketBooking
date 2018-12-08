from django.db import models
from .film import Film
from .hall import Hall

class Session(models.Model):
    film = models.ForeignKey(Film, on_delete=models.SET_NULL, null=True)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    price = models.CharField(max_length=255, default='1000 KZT')
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()

    def __str__(self):
        return "{} {} {} {}".format(self.film.name, self.hall.cinema.name, self.hall.name, self.start_at)

    class Meta:
        verbose_name = "session"
        verbose_name_plural = "sessions"
