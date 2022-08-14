# Generated by Django 4.0.6 on 2022-08-14 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0006_rename_doctor_name_appointment_doctor_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='payment_status',
            field=models.CharField(blank=True, default='pending', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='serial_number',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]