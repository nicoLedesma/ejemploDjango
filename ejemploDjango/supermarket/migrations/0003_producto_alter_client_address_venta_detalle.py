# Generated by Django 4.2.3 on 2023-08-25 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supermarket', '0002_client_address_client_created_at_client_cuit_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.AlterField(
            model_name='client',
            name='address',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_ammount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('date', models.DateField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supermarket.client')),
            ],
        ),
        migrations.CreateModel(
            name='Detalle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supermarket.producto')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalle', to='supermarket.venta')),
            ],
        ),
    ]
