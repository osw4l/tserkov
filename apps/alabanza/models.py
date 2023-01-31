from django.db import models
from django.contrib.auth.models import User


class Song(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True
    )
    worship = models.BooleanField(default=False)
    link = models.URLField(unique=True)

    class Meta:
        verbose_name = 'Song'
        verbose_name_plural = 'Songs'

    def __str__(self):
        return self.name


class Instrument(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True
    )

    class Meta:
        verbose_name = 'Instrument'
        verbose_name_plural = 'Instruments'

    def __str__(self):
        return self.name


class Musician(User):
    instruments = models.ManyToManyField(
        Instrument
    )

    class Meta:
        verbose_name = 'Musician'
        verbose_name_plural = 'Musicians'


class Schedule(models.Model):
    date = models.DateField()
    time = models.TimeField()
    director = models.ForeignKey(
        Musician,
        on_delete=models.PROTECT,
        related_name='schedules'
    )
    tracks = models.ManyToManyField(
        Song
    )

    class Meta:
        verbose_name = 'Programacion'
        verbose_name_plural = 'Programaciones'


class ScheduleMusicianInstrument(models.Model):
    schedule = models.ForeignKey(
        Schedule,
        on_delete=models.PROTECT,
        related_name='musicians'
    )
    musician = models.ForeignKey(
        Musician,
        on_delete=models.PROTECT
    )
    instrument = models.ForeignKey(
        Instrument,
        on_delete=models.PROTECT
    )

    class Meta:
        unique_together = ['schedule', 'musician', 'instrument']

