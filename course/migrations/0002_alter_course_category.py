# Generated by Django 4.2.1 on 2023-08-20 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='category',
            field=models.ManyToManyField(related_name='course_category', to='course.category'),
        ),
    ]
