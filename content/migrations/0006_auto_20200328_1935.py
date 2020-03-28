# Generated by Django 2.2.4 on 2020-03-28 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_auto_20200328_1927'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_file', models.FileField(upload_to='files')),
                ('event', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='content.Event')),
            ],
        ),
        migrations.DeleteModel(
            name='Images',
        ),
    ]
