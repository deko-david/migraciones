# Generated by Django 4.2.4 on 2023-08-11 02:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("magento", "0004_alter_magentoproducts_cantidad_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="magentoproducts",
            name="meta_descripcion",
            field=models.TextField(help_text="meta_descripcion", null=True),
        ),
    ]
