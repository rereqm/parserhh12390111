# Generated by Django 3.2.25 on 2024-07-01 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='grafi',
            field=models.CharField(default=2, max_length=40),
            preserve_default=False,
        ),
    ]
