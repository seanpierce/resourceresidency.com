# Generated by Django 2.1.4 on 2019-11-19 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('residencies', '0001_initial'),
        ('artists', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='residencies',
            field=models.ManyToManyField(to='residencies.Residency'),
        ),
    ]
