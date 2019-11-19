from django.db import models
from ckeditor.fields import RichTextField

class Residency(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=50)
    info = RichTextField()
    active = models.BooleanField(default=True)
    artists = models.ManyToManyField('artists.Artist')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name