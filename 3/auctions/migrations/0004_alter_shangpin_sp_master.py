# Generated by Django 4.0.3 on 2022-04-21 14:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_remove_shangpin_sp_pinglun_alter_shangpin_sp_master'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shangpin',
            name='sp_master',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
