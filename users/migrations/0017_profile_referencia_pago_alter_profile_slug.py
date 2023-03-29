# Generated by Django 4.1.7 on 2023-03-28 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_profile_pagado_alter_profile_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='referencia_pago',
            field=models.IntegerField(default=27158, unique=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='slug',
            field=models.SlugField(default=5939292140, null=True, unique=True),
        ),
    ]
