# Generated by Django 3.2.9 on 2022-03-22 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_auto_20220320_2017'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='url',
            field=models.CharField(default=0, max_length=200, unique=True, verbose_name="URL (auto generated. Don't touch)"),
            preserve_default=False,
        ),
    ]
