# Generated by Django 4.1.2 on 2022-11-29 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ausentismos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ausentismo',
            name='totalAFP',
            field=models.CharField(blank=True, default='', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='ausentismo',
            name='totalArl',
            field=models.CharField(blank=True, default='', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='ausentismo',
            name='totalEPS',
            field=models.CharField(blank=True, default='', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='ausentismo',
            name='totalEmpresa',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='ausentismo',
            name='totalIncapacidad',
            field=models.CharField(blank=True, default='', max_length=30, null=True),
        ),
    ]