# Generated by Django 4.2.6 on 2023-10-30 17:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('backend', '0010_rumors_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavoriteCoin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coin_id', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=100)),
                ('symbol', models.CharField(max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
