# Generated by Django 4.2.4 on 2023-08-14 16:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("magento", "0008_alter_magentoproducts_category_list"),
    ]

    operations = [
        migrations.AddField(
            model_name="magentoproducts",
            name="medidas",
            field=models.JSONField(blank=True, null=True),
        ),
    ]
