from django.db import models  # noqa F401
from datetime import datetime


class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f'{self.title}'


class PokemonEntity(models.Model):
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    appeared_at = models.DateTimeField(default=datetime.now())
    disappeared_at = models.DateTimeField(default=datetime.now())
    level = models.IntegerField(null=True, blank=True)
    health = models.IntegerField(null=True, blank=True)
    attack = models.IntegerField(null=True, blank=True)
    defense = models.IntegerField(null=True, blank=True)
    stamina = models.IntegerField(null=True, blank=True)
