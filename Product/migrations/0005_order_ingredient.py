# Generated by Django 2.2.28 on 2023-04-26 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0004_auto_20230426_1624'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='ingredient',
            field=models.ManyToManyField(to='Product.Ingredient'),
        ),
    ]