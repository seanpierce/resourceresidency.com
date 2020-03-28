# Generated by Django 2.2.4 on 2020-03-28 19:27

import ckeditor.fields
import content.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_auto_20200328_1728'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('event_date', models.DateTimeField()),
                ('name', models.CharField(max_length=50)),
                ('info', ckeditor.fields.RichTextField()),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='files', verbose_name='Image')),
                ('event', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='content.Event')),
            ],
        ),
        migrations.DeleteModel(
            name='File',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
