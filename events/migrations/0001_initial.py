# Generated by Django 2.0.5 on 2019-06-06 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('venue', models.TextField()),
                ('date', models.DateField()),
                ('time', models.CharField(max_length=10)),
                ('details', models.TextField()),
                ('cover_pic', models.ImageField(upload_to='static/uploads/events/cover')),
                ('icon', models.ImageField(upload_to='static/uploads/events/icon')),
                ('email', models.EmailField(max_length=254)),
                ('flag', models.BooleanField(default=False)),
            ],
        ),
    ]
