# Generated by Django 4.1.2 on 2022-11-01 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('total', models.IntegerField()),
                ('cliente', models.CharField(max_length=100)),
            ],
        ),
    ]