# Generated by Django 2.2.3 on 2019-07-26 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appFormalTest', '0002_auto_20190725_1621'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stockType', models.CharField(max_length=50)),
                ('stockCode', models.CharField(max_length=50)),
                ('stockName', models.CharField(max_length=50)),
                ('stockPrice', models.IntegerField()),
            ],
        ),
    ]
