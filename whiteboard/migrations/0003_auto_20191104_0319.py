# Generated by Django 2.2.6 on 2019-11-04 03:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("whiteboard", "0002_auto_20191103_2336"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lift",
            name="name",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="whiteboard.Movement",
                to_field="name",
            ),
        ),
        migrations.AlterField(
            model_name="movement",
            name="name",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
