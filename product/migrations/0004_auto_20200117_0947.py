# Generated by Django 2.1.5 on 2020-01-17 09:47

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0003_auto_20200117_0901'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Producta',
            new_name='Product',
        ),
    ]
