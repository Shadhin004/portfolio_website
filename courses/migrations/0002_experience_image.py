# Generated by Django 3.0.6 on 2020-05-19 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='image',
            field=models.FileField(blank=True, upload_to='post_image'),
        ),
    ]
