# Generated by Django 5.0.6 on 2024-05-28 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('listed_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('min_profitable_price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
