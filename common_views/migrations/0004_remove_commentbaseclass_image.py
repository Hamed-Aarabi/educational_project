# Generated by Django 4.2.1 on 2023-07-27 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common_views', '0003_alter_commentbaseclass_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentbaseclass',
            name='image',
        ),
    ]
