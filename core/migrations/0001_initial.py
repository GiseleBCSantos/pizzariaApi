# Generated by Django 5.1.5 on 2025-01-24 17:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cliente",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=50)),
                ("endereco", models.CharField(max_length=50)),
                ("telefone", models.CharField(max_length=50)),
                ("bairro", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Pizza",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("sabor", models.CharField(max_length=50)),
                ("precoBase", models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name="Tamanho",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=50)),
                ("modificador", models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name="Pedido",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "cliente_pedido",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="pedidos",
                        to="core.cliente",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ItensPedido",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantidade", models.IntegerField()),
                (
                    "itensPedido_pedido",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="itens_pedidos",
                        to="core.pedido",
                    ),
                ),
                (
                    "id_pizza",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="pizza_itens_pedidos",
                        to="core.pizza",
                    ),
                ),
                (
                    "id_tamanho",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tamanho_itens_pedidos",
                        to="core.tamanho",
                    ),
                ),
            ],
        ),
    ]
