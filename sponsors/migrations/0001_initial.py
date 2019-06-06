# Generated by Django 2.0.5 on 2019-06-06 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('details', models.TextField()),
                ('pic', models.ImageField(upload_to='static/uploads/sponsors')),
                ('contact', models.TextField(blank=True, max_length=13, null=True)),
                ('website', models.URLField(blank=True)),
                ('spons_type', models.CharField(choices=[('AS', 'Associate Sponsors'), ('PLTS', 'Platinum Sponsors'), ('GS', 'Gold Sponsors'), ('TS', 'Title Sponsors'), ('PRTS', 'Partner Sponsors')], default='AS', max_length=4)),
                ('flag', models.BooleanField(default=False)),
                ('year', models.IntegerField(default=2018)),
            ],
        ),
    ]
