# Generated by Django 3.2.7 on 2021-12-02 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leo', '0002_auto_20211202_1252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsletter',
            name='caption',
        ),
    ]
