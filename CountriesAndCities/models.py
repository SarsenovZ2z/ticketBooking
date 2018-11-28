from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length = 255)
    short_name = models.CharField(max_length = 255)
    code = models.CharField(max_length = 10)

    def __str__(self):
        return "{}".format(self.name)

class City(models.Model):
    country = models.ForeignKey('Country')
    name = models.CharField(max_length = 255)
    short_name = models.CharField(max_length = 255)

    def __str__(self):
        return "{}".format(self.name)
