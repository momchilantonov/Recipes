# Generated by Django 3.2.4 on 2021-06-23 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='time',
            field=models.PositiveIntegerField(),
        ),
    ]