# Generated by Django 2.0.4 on 2018-05-19 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speaker',
            name='contact',
            field=models.TextField(blank=True, max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='flag',
            field=models.BooleanField(default=False),
        ),
    ]
