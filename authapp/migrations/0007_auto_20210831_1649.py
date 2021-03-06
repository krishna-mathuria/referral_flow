# Generated by Django 3.2.6 on 2021-08-31 11:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0006_referrals'),
    ]

    operations = [
        migrations.AddField(
            model_name='referrals',
            name='referee_inc',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='referrals',
            name='referred_to_inc',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='user',
            name='share',
            field=models.IntegerField(default=10, validators=[django.core.validators.MaxValueValidator(20), django.core.validators.MinValueValidator(0)]),
        ),
    ]
