# Generated by Django 4.0.6 on 2022-08-06 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motor', '0004_motor_email_motor_merk_motor_telp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='motor',
            name='nama',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
