# Generated by Django 4.0.3 on 2022-06-05 08:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0012_remove_board_update_date_board_modify_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='reg_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 5, 8, 50, 53, 960104, tzinfo=utc)),
        ),
    ]
