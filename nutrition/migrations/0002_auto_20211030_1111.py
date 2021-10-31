# Generated by Django 3.2 on 2021-10-30 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutrition', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='carbohydrate',
        ),
        migrations.AddField(
            model_name='product',
            name='fat',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='protein',
            field=models.IntegerField(default=0),
        ),
    ]
