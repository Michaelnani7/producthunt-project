# Generated by Django 2.1.5 on 2020-01-17 09:01

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0002_make'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Make',
            new_name='Producta',
        ),
        migrations.RemoveField(
            model_name='product',
            name='hunter',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]