# Generated by Django 3.1 on 2023-01-15 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualdb', '0002_auto_20230115_0449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrapeddata',
            name='scraped_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date_scraped'),
        ),
    ]
