# Generated by Django 4.1.7 on 2023-03-21 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BackupFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='file/')),
                ('back_up_date', models.DateField()),
                ('number_of_rows', models.IntegerField()),
                ('size_of_file', models.IntegerField()),
                ('file_type', models.CharField(max_length=12)),
            ],
        ),
    ]
