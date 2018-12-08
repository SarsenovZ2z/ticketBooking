from django.db import models

class Film(models.Model):
    name = models.CharField(max_length=255)
    premiere = models.DateField()
    description = models.TextField(blank=True, null=True)
    main_poster = models.ImageField(upload_to='films')
    votes = models.BigIntegerField(default=0, editable=False)
    votes_number = models.BigIntegerField(default=0, editable=False)

    def __str__(self):
        return "{}({})".format(self.name, self.premiere)

    class Meta:
        verbose_name = "film"
        verbose_name_plural = "films"
        
