from django.db import models
from .city import City

class Cinema(models.Model):
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255, db_index=True)
    description = models.TextField(blank=True, null=True)
    website = models.URLField(max_length=255, blank=True, null=True)
    votes = models.BigIntegerField(default=0, editable=False)
    votes_number = models.BigIntegerField(default=0, editable=False)
    lat = models.CharField(max_length=255, blank=True, null=True)
    lon = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = "cinema"
        verbose_name_plural = "cinemas"

    def __str__(self):
        return "{} ({})".format(self.name, self.city)
