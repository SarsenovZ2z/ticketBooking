from django.db import models
from .country import Country

class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "city"
        verbose_name_plural = "cities"

    def __str__(self):
        return "{}".format(self.name)
