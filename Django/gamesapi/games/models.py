from unicodedata import name
from django.db import models

# Create your models here.
class Game(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200, blank=True, default='')
    release_date = models.CharField(max_length=200, blank=True, default='')
    played = models.BooleanField(default=False)
    
    class Meta:
        ordering = ('name',)