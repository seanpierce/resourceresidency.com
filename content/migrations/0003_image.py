# Generated by Django 2.2.4 on 2019-11-21 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_auto_20191121_2104'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='public/images')),
            ],
            options={
                'ordering': ['image'],
            },
        ),
    ]
