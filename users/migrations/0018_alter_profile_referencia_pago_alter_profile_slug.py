# Generated by Django 4.1.7 on 2023-03-28 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_profile_referencia_pago_alter_profile_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='referencia_pago',
            field=models.IntegerField(default=66999, unique=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='slug',
            field=models.SlugField(default=2162094787, null=True, unique=True),
        ),
    ]
