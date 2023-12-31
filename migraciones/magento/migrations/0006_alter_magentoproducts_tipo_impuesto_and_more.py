# Generated by Django 4.2.4 on 2023-08-11 02:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("magento", "0005_alter_magentoproducts_meta_descripcion"),
    ]

    operations = [
        migrations.AlterField(
            model_name="magentoproducts",
            name="Tipo_impuesto",
            field=models.CharField(help_text="Impuesto", max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name="magentoproducts",
            name="cantidad",
            field=models.BigIntegerField(help_text="cantidad", null=True),
        ),
        migrations.AlterField(
            model_name="magentoproducts",
            name="category_list",
            field=models.CharField(
                help_text="category_list", max_length=255, null=True
            ),
        ),
        migrations.AlterField(
            model_name="magentoproducts",
            name="description",
            field=models.TextField(help_text="description", null=True),
        ),
        migrations.AlterField(
            model_name="magentoproducts",
            name="esta_en_stock",
            field=models.CharField(
                help_text="esta_en_stock", max_length=250, null=True
            ),
        ),
        migrations.AlterField(
            model_name="magentoproducts",
            name="estado",
            field=models.CharField(help_text="estado", max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name="magentoproducts",
            name="imagen",
            field=models.CharField(help_text="imagen", max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="magentoproducts",
            name="imagen2",
            field=models.CharField(help_text="imagen2", max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="magentoproducts",
            name="meta_titulo",
            field=models.TextField(help_text="meta_titulo", null=True),
        ),
        migrations.AlterField(
            model_name="magentoproducts",
            name="nombre",
            field=models.CharField(help_text="nombre", max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name="magentoproducts",
            name="p_especial_desde",
            field=models.DateTimeField(help_text="p_especial_desde", null=True),
        ),
        migrations.AlterField(
            model_name="magentoproducts",
            name="p_especial_hasta",
            field=models.DateTimeField(help_text="p_especial_hasta", null=True),
        ),
        migrations.AlterField(
            model_name="magentoproducts",
            name="peso",
            field=models.FloatField(help_text="peso", max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name="magentoproducts",
            name="precio",
            field=models.BigIntegerField(help_text="precio", null=True),
        ),
        migrations.AlterField(
            model_name="magentoproducts",
            name="precio_especial",
            field=models.BigIntegerField(help_text="precio_especial", null=True),
        ),
        migrations.AlterField(
            model_name="magentoproducts",
            name="short_description",
            field=models.TextField(help_text="short_description", null=True),
        ),
        migrations.AlterField(
            model_name="magentoproducts",
            name="url",
            field=models.CharField(help_text="url", max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name="magentoproducts",
            name="visibilidad",
            field=models.CharField(help_text="visibilidad", max_length=250, null=True),
        ),
    ]
