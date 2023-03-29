# Generated by Django 4.1.7 on 2023-03-28 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_alter_profile_catalogo_invitacion_alter_profile_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='catalogo_invitacion',
        ),
        migrations.AlterField(
            model_name='profile',
            name='slug',
            field=models.SlugField(default=8448214075, null=True, unique=True),
        ),
    ]