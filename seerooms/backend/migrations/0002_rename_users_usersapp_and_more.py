# Generated by Django 4.1.3 on 2022-11-05 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='Usersapp',
        ),
        migrations.RenameField(
            model_name='usersapp',
            old_name='id_user',
            new_name='id_user_app',
        ),
    ]
