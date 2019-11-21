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

from django.db import models


class Image(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images')

    @property
    def filename(self):
        return os.path.basename(self.image.name)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.filename


@receiver(models.signals.post_delete, sender=Image)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes image from filesystem
    when corresponding `Image` object is deleted.
    """
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)

@receiver(models.signals.pre_save, sender=Image)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old image from filesystem
    when corresponding `Image` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = Image.objects.get(pk=instance.pk).image
    except Image.DoesNotExist:
        return False

    new_file = instance.image
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)