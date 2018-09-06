# Generated by Django 2.0.5 on 2018-09-06 08:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Discussion', '0004_notification'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='receiver',
        ),
        migrations.AddField(
            model_name='notification',
            name='receiver',
            field=models.ManyToManyField(related_name='receive_notifies', to=settings.AUTH_USER_MODEL, verbose_name='接收者'),
        ),
    ]
