# Generated by Django 3.2.6 on 2021-08-30 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('memo', models.TextField(blank=True)),
                ('mobile', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=20)),
                ('make', models.CharField(max_length=10)),
                ('model', models.CharField(max_length=10)),
                ('vinNum', models.CharField(max_length=10)),
                ('licNum', models.CharField(max_length=10)),
                ('state', models.CharField(max_length=10)),
            ],
        ),
    ]
