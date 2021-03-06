# Generated by Django 4.0 on 2022-01-11 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_product_product_stock'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderplaced',
            options={'get_latest_by': ('ordered_date',), 'ordering': ('ordered_date',)},
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sold_quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.product')),
            ],
        ),
    ]
