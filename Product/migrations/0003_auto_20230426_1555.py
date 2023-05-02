# Generated by Django 2.2.28 on 2023-04-26 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0002_auto_20230426_1411'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='category',
        ),
        migrations.CreateModel(
            name='ProductsIngredients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient', models.ManyToManyField(to='Product.Ingredient')),
                ('product', models.ManyToManyField(to='Product.Product')),
            ],
        ),
    ]
