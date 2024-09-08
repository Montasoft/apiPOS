# Generated by Django 5.0.7 on 2024-09-08 22:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0003_estadopedido_pedido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='cantidad_recibida',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='cantidad_solicitada',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='fecha_esperado',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='fecha_recibido',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='fecha_solicitud',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='proveedor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='compras.proveedor'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='valor_esperado',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='valor_recibido',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]