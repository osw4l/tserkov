from django.contrib import admin

from .forms import MusicianForm
from .models import Song, Instrument, Musician, Schedule, ScheduleMusicianInstrument


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'worship', 'link']


@admin.register(Instrument)
class InstrumentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Musician)
class MusicianAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'first_name', 'last_name']
    form = MusicianForm
    filter_horizontal = ('instruments',)


class ScheduleMusicianInstrumentStackedInline(admin.TabularInline):
    model = ScheduleMusicianInstrument
    extra = 0


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'time', 'director']
    inlines = (ScheduleMusicianInstrumentStackedInline,)
    filter_horizontal = ('tracks',)
