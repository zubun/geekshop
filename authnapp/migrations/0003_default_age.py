# Generated by Django 4.0.1 on 2022-01-31 18:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [("authnapp", "0002_user_model_extend")]

    operations = [
        migrations.AlterField(
            model_name="shopuser",
            name="activation_key_expires",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 2, 2, 18, 10, 46, 114412, tzinfo=utc), verbose_name="актуальность ключа"
            ),
        )
    ]
