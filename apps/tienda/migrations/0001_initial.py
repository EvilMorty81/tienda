# Generated by Django 2.0.9 on 2018-12-08 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tienda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_tienda', models.IntegerField()),
                ('nombre_tienda', models.CharField(max_length=50)),
                ('direccion_tienda', models.CharField(max_length=100)),
                ('comuna_tienda', models.CharField(max_length=50)),
                ('ciudad_tienda', models.CharField(max_length=50)),
                ('telefono_tienda', models.IntegerField()),
                ('email_tienda', models.EmailField(max_length=254)),
                ('encargado_tienda', models.CharField(max_length=100)),
            ],
        ),
    ]