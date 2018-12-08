from django.db import models
from .session import Session

class Ticket(models.Model):
    session = models.ForeignKey(Session, on_delete=models.SET_NULL, null=True)
    row = models.SmallIntegerField()
    col = models.SmallIntegerField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} {} Hall: {}".format(self.session.film.name, self.session.hall.cinema.name, self.session.hall.name)

    class Meta:
        verbose_name = "ticket"
        verbose_name_plural = "tickets"
