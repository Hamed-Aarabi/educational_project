# Generated by Django 4.2.1 on 2023-08-20 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactus', '0005_way_contactway'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactway',
            name='ways',
        ),
        migrations.AddField(
            model_name='contactway',
            name='ways',
            field=models.ManyToManyField(related_name='contact_ways', to='contactus.way'),
        ),
    ]