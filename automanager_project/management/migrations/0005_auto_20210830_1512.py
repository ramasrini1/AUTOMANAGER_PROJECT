# Generated by Django 3.2.6 on 2021-08-30 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_customer_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='lic',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='vin',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
