# Generated by Django 4.2 on 2023-05-12 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_remove_episode_video_url_episode_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='video',
            field=models.FileField(null=True, upload_to='episodes/courses/<django.db.models.fields.related.ForeignKey>', verbose_name='ویدئو'),
        ),
    ]
