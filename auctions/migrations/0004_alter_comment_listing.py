# Generated by Django 4.1.3 on 2022-12-13 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='listing',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='listingComment', to='auctions.listing'),
        ),
    ]
