# Generated by Django 3.1.7 on 2021-09-09 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LithiumBattery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('kind', models.CharField(max_length=20)),
                ('battery_capacity', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('rated_input_voltage', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('rated_input_current', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('charger_voltage', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('charger_current', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('purchase_period', models.DateField(auto_now_add=True)),
                ('charging_start_time', models.DateTimeField(auto_now_add=True)),
                ('loss', models.DecimalField(decimal_places=2, default=1.2, max_digits=20)),
                ('min_voltage', models.DecimalField(decimal_places=2, default=3.7, max_digits=20)),
                ('max_voltage', models.DecimalField(decimal_places=2, default=4.2, max_digits=20)),
            ],
        ),
    ]
