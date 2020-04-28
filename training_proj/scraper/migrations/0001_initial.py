# Generated by Django 3.0.4 on 2020-03-31 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScrapedData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airline_name', models.CharField(max_length=100)),
                ('biz_model', models.CharField(max_length=100)),
                ('network', models.CharField(max_length=100)),
                ('group', models.CharField(max_length=100)),
                ('hub', models.CharField(max_length=100)),
                ('territory', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=1000)),
                ('iata_code', models.CharField(max_length=50)),
                ('icao_code', models.CharField(max_length=50)),
                ('about', models.CharField(max_length=1000)),
                ('ranking', models.CharField(max_length=50)),
                ('prevrank', models.CharField(max_length=50)),
                ('ratingval', models.CharField(max_length=50)),
            ],
        ),
    ]
