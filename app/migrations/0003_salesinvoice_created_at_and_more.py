# Generated by Django 4.1.7 on 2023-03-21 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_backupfiles'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesinvoice',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='backupfiles',
            name='back_up_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
