# Generated by Django 4.2.3 on 2023-11-19 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0019_favoritecoin_symbol'),
    ]

    operations = [
        migrations.AddField(
            model_name='favoritecoin',
            name='image',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
