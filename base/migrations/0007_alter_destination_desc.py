# Generated by Django 3.2.9 on 2022-03-22 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_destination_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='desc',
            field=models.TextField(null=True, verbose_name='Content'),
        ),
    ]
