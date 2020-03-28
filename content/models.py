import os

from django.db import models
from django.dispatch import receiver

from ckeditor.fields import RichTextField

class Content(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=50)
    info = RichTextField()
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Content"

    def __str__(self):
        return self.name


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now=True)
    event_date = models.DateField()
    name = models.CharField(max_length=50)
    info = RichTextField()
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name 


class File(models.Model):
    event = models.ForeignKey(Event, default=None, on_delete=models.CASCADE)
    event_file = models.FileField(upload_to='files')