# Generated by Django 3.2.9 on 2022-02-03 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20220203_1614'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fundraiser',
            name='session',
        ),
        migrations.AddField(
            model_name='fundraiser',
            name='start_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]