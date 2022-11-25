# Generated by Django 4.1.3 on 2022-11-18 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_cliente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lanches1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produto', models.CharField(max_length=50, verbose_name='Produto')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='valor')),
            ],
        ),
    ]
