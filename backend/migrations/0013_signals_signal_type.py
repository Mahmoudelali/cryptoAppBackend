# Generated by Django 4.2.6 on 2023-10-31 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0012_remove_favoritecoin_coin_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='signals',
            name='signal_type',
            field=models.CharField(default=None, max_length=5, null=True),
        ),
    ]
