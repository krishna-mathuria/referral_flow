# Generated by Django 3.2.6 on 2021-08-31 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0007_auto_20210831_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referrals',
            name='referred_to',
            field=models.CharField(max_length=30),
        ),
    ]
