# Generated by Django 2.2.3 on 2019-08-22 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appFormalTest', '0014_setsale'),
    ]

    operations = [
        migrations.CreateModel(
            name='cusOwnSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ownCusCode', models.CharField(max_length=50)),
                ('ownSetCode', models.CharField(max_length=50)),
                ('ownQua', models.IntegerField()),
            ],
        ),
    ]
