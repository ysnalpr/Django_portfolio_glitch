# Generated by Django 3.2.6 on 2021-08-31 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0011_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='body',
            new_name='message',
        ),
    ]
