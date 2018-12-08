from django.db import models
from .cinema import Cinema

class Hall(models.Model):
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    rows = models.SmallIntegerField(default=5)
    seats = models.SmallIntegerField(default=50)

    class Meta:
        verbose_name = "halll"
        verbose_name_plural = "halls"

    def __str__(self):
        return "{}".format(self.name)
