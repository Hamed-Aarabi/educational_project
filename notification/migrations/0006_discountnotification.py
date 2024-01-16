# Generated by Django 4.2.1 on 2023-08-28 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0007_course_discount_price'),
        ('notification', '0005_delete_discountnotification'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiscountNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('discount', models.BooleanField(default=False)),
                ('title', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course_discount_notification', to='course.course')),
            ],
        ),
    ]