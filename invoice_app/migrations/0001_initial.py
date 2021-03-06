# Generated by Django 2.2.5 on 2021-01-10 07:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item_entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=100)),
                ('item_catagory', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Item_sold',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurent', models.CharField(max_length=50)),
                ('item_price', models.IntegerField()),
                ('sell_date', models.DateField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoice_app.Item_entry')),
            ],
        ),
    ]
