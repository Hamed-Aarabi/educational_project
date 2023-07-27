# Generated by Django 4.2.1 on 2023-06-26 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common_views', '0001_initial'),
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseComment',
            fields=[
                ('commentbaseclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='common_views.commentbaseclass')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_of_courses', to='course.course', verbose_name='دوره')),
            ],
            bases=('common_views.commentbaseclass',),
        ),
    ]