# Generated by Django 2.1.2 on 2018-10-25 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock_prices', '0003_auto_20181023_1753'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stockprices',
            name='comp_id',
        ),
        migrations.DeleteModel(
            name='StockPrices',
        ),
    ]