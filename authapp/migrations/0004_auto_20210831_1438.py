# Generated by Django 3.2.6 on 2021-08-31 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0003_auto_20210831_1330'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='referral_code',
            new_name='referral_code_self',
        ),
        migrations.AlterField(
            model_name='user',
            name='referred_by_code',
            field=models.CharField(max_length=8, null=True, verbose_name='referral code'),
        ),
    ]