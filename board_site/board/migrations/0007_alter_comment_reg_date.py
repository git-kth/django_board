# Generated by Django 4.0.3 on 2022-05-08 13:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0006_comment_board_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='reg_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 8, 13, 16, 53, 823212, tzinfo=utc)),
        ),
    ]