from django.db import models

class Prophet(models.Model):
    name = models.CharField(max_length=100)
    birth_year = models.CharField(max_length=100)
    death_year = models.CharField(max_length=100)
    books = models.TextField(help_text="Comma-separated list of books attributed to the prophet")

    class Meta:
        verbose_name = "Prophet"
        verbose_name_plural = "Prophets"

    def __str__(self):
        return self.name