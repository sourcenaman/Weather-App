# Generated by Django 3.1.4 on 2021-01-09 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Weather',
            new_name='City',
        ),
    ]