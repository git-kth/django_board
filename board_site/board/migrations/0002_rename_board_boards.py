# Generated by Django 4.0.3 on 2022-03-26 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Board',
            new_name='Boards',
        ),
    ]