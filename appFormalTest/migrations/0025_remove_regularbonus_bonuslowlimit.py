# Generated by Django 2.2.3 on 2019-09-21 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appFormalTest', '0024_commission_commlimit_multisevicepercnet_regularbonus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='regularbonus',
            name='bonusLowLimit',
        ),
    ]
