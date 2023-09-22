from django.db import models

class Rooms(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Rooms'
    
    def __str__(self):
        return self.name
