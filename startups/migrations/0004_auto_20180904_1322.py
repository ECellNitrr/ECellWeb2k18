# Generated by Django 2.0.5 on 2018-09-04 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('startups', '0003_startupregister'),
    ]

    operations = [
        migrations.RenameField(
            model_name='startupregister',
            old_name='preference1',
            new_name='startup',
        ),
        migrations.RemoveField(
            model_name='startupregister',
            name='preference2',
        ),
    ]