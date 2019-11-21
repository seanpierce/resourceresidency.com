from django.db import models

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

from django.db import models


class Image(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.image.name
