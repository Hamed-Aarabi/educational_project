# Generated by Django 4.2.1 on 2023-08-12 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_alter_myuser_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='is_student',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='myuser',
            name='is_teacher',
            field=models.BooleanField(default=False),
        ),
    ]
