# Generated by Django 4.1.7 on 2023-03-27 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coolapp', '0003_invitationcatalog'),
    ]

    operations = [
        migrations.AddField(
            model_name='invitationcatalog',
            name='category',
            field=models.CharField(default='Fiesta', max_length=20),
        ),
    ]