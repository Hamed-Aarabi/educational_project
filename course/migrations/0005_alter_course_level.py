# Generated by Django 4.2 on 2023-05-10 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_alter_course_created_at_alter_course_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='level',
            field=models.CharField(max_length=255, verbose_name='سطح دوره'),
        ),
    ]