# Generated by Django 4.1.7 on 2023-03-21 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SalesInvoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=12)),
                ('address', models.TextField()),
                ('amount', models.IntegerField()),
                ('discount_amount', models.IntegerField()),
                ('tax_percent', models.CharField(max_length=4)),
                ('invoice_items', models.JSONField()),
            ],
        ),
    ]
