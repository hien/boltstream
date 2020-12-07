# Generated by Django 2.2 on 2019-05-12 18:20

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("boltstream", "0003_streamsession")]

    operations = [
        migrations.AddField(
            model_name="user",
            name="uuid",
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, unique=True, verbose_name="UUID"
            ),
        )
    ]
