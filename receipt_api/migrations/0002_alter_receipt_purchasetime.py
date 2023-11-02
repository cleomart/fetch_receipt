# Generated by Django 4.2.6 on 2023-11-02 05:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receipt_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='purchaseTime',
            field=models.TextField(validators=[django.core.validators.RegexValidator('^([0-1]?[0-9]|2[0-3]):[0-5][0-9]:00$', message='Purchase time should have a format HH:MM')]),
        ),
    ]