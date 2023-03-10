# Generated by Django 4.1.5 on 2023-01-28 23:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alabanza', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='schedules', to='alabanza.musician')),
                ('musicians', models.ManyToManyField(to='alabanza.musician')),
                ('tracks', models.ManyToManyField(to='alabanza.song')),
            ],
            options={
                'verbose_name': 'Programacion',
                'verbose_name_plural': 'Programaciones',
            },
        ),
    ]
