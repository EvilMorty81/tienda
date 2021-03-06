# Generated by Django 2.0.9 on 2018-12-08 00:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('numero_venta', models.IntegerField(primary_key=True, serialize=False)),
                ('fecha_venta', models.DateTimeField(default=django.utils.timezone.now)),
                ('cantidad_venta', models.IntegerField()),
                ('subtotal_venta', models.IntegerField()),
                ('total_venta', models.IntegerField()),
                ('comentario_venta', models.TextField(blank=True)),
            ],
        ),
    ]
