from django.db import models  # noqa F401
from datetime import datetime


class Pokemon(models.Model):
    title = models.CharField('Название', max_length=200)
    title_en = models.CharField('Название на английском', max_length=200, blank=True)
    title_jp = models.CharField('Название на японском', max_length=200, blank=True)
    image = models.ImageField('Картинка', null=True, blank=True)
    description = models.TextField('Описание', blank=True)
    previous_evolution = models.ForeignKey('self',
                                           verbose_name='Из кого эволюционировал',
                                           on_delete=models.SET_NULL,
                                           null=True, blank=True,
                                           related_name='next_evolution')

    def __str__(self):
        return f'{self.title}'


class PokemonEntity(models.Model):
    lat = models.FloatField('', null=True, blank=True)
    lon = models.FloatField('', null=True, blank=True)
    pokemon = models.ForeignKey(Pokemon, related_name='pokemon_entities',
                                on_delete=models.CASCADE)
    appeared_at = models.DateTimeField('Время появления')
    disappeared_at = models.DateTimeField('Время исчезновения')
    level = models.IntegerField('Уровень', null=True, blank=True)
    health = models.IntegerField('Здоровье', null=True, blank=True)
    attack = models.IntegerField('Атака', null=True, blank=True)
    defense = models.IntegerField('Защита', null=True, blank=True)
    stamina = models.IntegerField('Выносливость', null=True, blank=True)
