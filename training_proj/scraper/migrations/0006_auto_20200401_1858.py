# Generated by Django 3.0.4 on 2020-04-01 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0005_scrapeddata_site_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='scrapeddata',
            name='source_url',
            field=models.CharField(default='www.ibsplc.com', max_length=500),
        ),
        migrations.AlterField(
            model_name='scrapelinks',
            name='image_url',
            field=models.CharField(default='default.jpg', max_length=1000),
        ),
    ]
