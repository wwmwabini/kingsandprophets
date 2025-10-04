from tabnanny import verbose
from django.db import models

class King(models.Model):
    name = models.CharField(max_length=100)
    reign_start = models.IntegerField()
    reign_end = models.IntegerField(null=True, blank=True)
    years_reigned = models.CharField(max_length=100)
    is_good = models.BooleanField(default=False)

    class Meta:
        verbose_name = "King"
        verbose_name_plural = "Kings"


    def __str__(self):
        return self.name