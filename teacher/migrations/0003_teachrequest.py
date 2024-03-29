# Generated by Django 4.2.1 on 2023-08-15 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_teachrule'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeachRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('field', models.CharField(max_length=250)),
                ('description', models.TextField()),
            ],
        ),
    ]
