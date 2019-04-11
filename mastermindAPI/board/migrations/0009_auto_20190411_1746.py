# Generated by Django 2.1.7 on 2019-04-11 17:46

import board.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0008_movement_player'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movement',
            options={'ordering': ('created',)},
        ),
        migrations.AlterField(
            model_name='game',
            name='code',
            field=models.CharField(choices=[('R', 'RED'), ('G', 'GREEN'), ('B', 'BLUE'), ('O', 'ORANGE'), ('P', 'PURPLE'), ('Y', 'YELLOW')], default=board.models.create_code, max_length=64),
        ),
        migrations.AlterField(
            model_name='movement',
            name='code',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]
