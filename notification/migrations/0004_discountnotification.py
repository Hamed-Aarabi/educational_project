# Generated by Django 4.2.1 on 2023-08-28 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiscountNotification',
            fields=[
                ('notification_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='notification.notification')),
                ('discount', models.BooleanField(default=False)),
            ],
            bases=('notification.notification',),
        ),
    ]
