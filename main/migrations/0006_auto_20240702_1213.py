# Generated by Django 3.2.25 on 2024-07-02 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20240701_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='requirement',
            field=models.CharField(max_length=3000),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='responsibility',
            field=models.CharField(max_length=3000),
        ),
    ]
