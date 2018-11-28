from django.db import models

# Create your models here.
class Cinema(models.Model):
    city = models.ForeignKey('CountriesAndCities.City')
    name = models.CharField(max_length=255)
    rating = models.PositiveIntegerField(default=0, editable=False)
    votes = models.PositiveIntegerField(default=0, editable=False)
    website = models.URLField(blank=True, null=True)
    lat = models.CharField(max_length=255, blank=True, null=True)
    lon = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return "{}".format(self.name)


class Hall(models.Model):
    cinema = models.ForeignKey(Cinema)
    name = models.CharField(max_length=255)
    seats = models.SmallIntegerField(default=0)

    def __str__(self):
        return "{}".format(self.name)
