# Generated by Django 4.0.1 on 2022-01-22 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='firstname',
            field=models.CharField(default='noname', max_length=10),
        ),
        migrations.AddField(
            model_name='employees',
            name='lastname',
            field=models.CharField(default='noname', max_length=10),
        ),
    ]