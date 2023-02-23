# Generated by Django 4.1.5 on 2023-02-22 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namehotel', models.CharField(max_length=50)),
                ('room_normal_price', models.FloatField(max_length=50)),
                ('room_vip_price', models.FloatField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telephone', models.CharField(max_length=12)),
                ('namehotel', models.CharField(max_length=50)),
                ('roomhotel', models.CharField(max_length=15)),
                ('pirec_room', models.FloatField(max_length=50)),
                ('date_checkin', models.DateTimeField(auto_now_add=True)),
                ('date_checkout', models.DateTimeField()),
            ],
        ),
    ]
