# Generated by Django 2.2 on 2019-04-10 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("board", "0005_game_player"),
    ]

    operations = [
        migrations.CreateModel(
            name="Movement",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("code", models.CharField(blank=True, max_length=4)),
                ("created", models.DateTimeField(auto_now=True)),
                ("result", models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
