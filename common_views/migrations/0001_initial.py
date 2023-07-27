# Generated by Django 4.2.1 on 2023-06-25 18:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentBaseClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=255, null=True, verbose_name='کاربر')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='ایمیل')),
                ('image', models.ImageField(null=True, upload_to='comments')),
                ('text', models.TextField(verbose_name='دیدگاه')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('dislikes', models.ManyToManyField(editable=False, related_name='comment_dislike', to=settings.AUTH_USER_MODEL, verbose_name='تعداد دیس لایک')),
                ('heart', models.ManyToManyField(editable=False, related_name='comment_heart', to=settings.AUTH_USER_MODEL, verbose_name='تعداد علاقه ها')),
                ('likes', models.ManyToManyField(editable=False, related_name='comment_likes', to=settings.AUTH_USER_MODEL, verbose_name='تعداد لایک')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_parent', to='common_views.commentbaseclass', verbose_name='پاسخ به')),
            ],
            options={
                'verbose_name': 'کامنت',
                'verbose_name_plural': 'کامنت ها',
                'ordering': ('-created_at',),
            },
        ),
    ]
