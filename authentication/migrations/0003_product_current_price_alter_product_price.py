# Generated by Django 4.0.5 on 2022-06-23 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_product_combo_offer'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='current_price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(),
        ),
    ]
