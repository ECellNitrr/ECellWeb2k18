# Generated by Django 2.0.6 on 2018-06-12 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appprofile', '0004_auto_20180612_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]