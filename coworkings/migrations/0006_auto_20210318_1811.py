# Generated by Django 3.1.7 on 2021-03-18 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coworkings', '0005_auto_20210313_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='numberoffice',
            name='number_office',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='datetime_from',
            field=models.DateTimeField(unique=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='datetime_to',
            field=models.DateTimeField(unique=True),
        ),
    ]
