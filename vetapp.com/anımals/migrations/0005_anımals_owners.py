# Generated by Django 4.0.2 on 2022-02-23 18:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('anımals', '0004_anımals_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='anımals',
            name='owners',
            field=models.ManyToManyField(blank=True, related_name='Animal_added', to=settings.AUTH_USER_MODEL),
        ),
    ]
