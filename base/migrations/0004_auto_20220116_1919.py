# Generated by Django 3.2.9 on 2022-01-16 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_destination'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='createdTime',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='destination',
            name='updatedTime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
