# Generated by Django 2.2.1 on 2019-06-19 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sucursal', '0005_evalua_id_evaluando'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='cedula',
            field=models.IntegerField(default=1, verbose_name='Cedula de Identidad'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='evalua',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]