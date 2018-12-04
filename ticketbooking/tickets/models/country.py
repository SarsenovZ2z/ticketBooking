from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)

    class Meta:
        verbose_name = "country"
        verbose_name_plural = "countries"

    def __str__(self):
        return "({}){}".format(self.code, self.name)
