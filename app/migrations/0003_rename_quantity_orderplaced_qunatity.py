# Generated by Django 4.0 on 2022-01-02 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210911_0009'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderplaced',
            old_name='quantity',
            new_name='qunatity',
        ),
    ]
