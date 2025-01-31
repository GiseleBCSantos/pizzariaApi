# Generated by Django 5.1.5 on 2025-01-31 00:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='data_pedido',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 31, 0, 9, 11, 216609)),
        ),
        migrations.AddField(
            model_name='pedido',
            name='status',
            field=models.CharField(choices=[('aberto', 'Aberto'), ('finalizado', 'Finalizado'), ('cancelado', 'Cancelado')], default='aberto', max_length=10),
        ),
        migrations.AddField(
            model_name='pedido',
            name='valor_total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='precoBase',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='tamanho',
            name='modificador',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]
