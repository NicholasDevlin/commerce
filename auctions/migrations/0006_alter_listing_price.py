# Generated by Django 4.1.3 on 2022-12-13 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_bid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='price',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bidPrice', to='auctions.bid'),
        ),
    ]
