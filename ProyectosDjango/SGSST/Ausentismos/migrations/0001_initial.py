# Generated by Django 4.1.2 on 2022-11-18 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ausentismo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=80)),
                ('apellidos', models.CharField(max_length=80)),
                ('tipoId', models.CharField(max_length=10)),
                ('identificacion', models.CharField(max_length=20)),
                ('cargo', models.CharField(max_length=20)),
                ('tipoIncapacidad', models.CharField(max_length=100)),
                ('salario', models.CharField(max_length=80)),
                ('eps', models.CharField(max_length=100)),
                ('salarioDia', models.CharField(max_length=10)),
                ('fechaInicial', models.DateField()),
                ('fechaFinal', models.DateField()),
                ('totalDias', models.IntegerField()),
                ('clasificacion', models.CharField(max_length=10)),
            ],
        ),
    ]
