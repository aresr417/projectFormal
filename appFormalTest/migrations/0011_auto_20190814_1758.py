# Generated by Django 2.2.3 on 2019-08-14 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appFormalTest', '0010_auto_20190814_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='saleCode',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='sale',
            name='saleCusCode',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='sale',
            name='saleEmp',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='sale',
            name='salePoint',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sale',
            name='salePrice',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sale',
            name='saleQua',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sale',
            name='saleRemark',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='sale',
            name='saleShopCode',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='sale',
            name='saleStockCode',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
