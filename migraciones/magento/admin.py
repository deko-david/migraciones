from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from magento.models import MagentoProducts
from django_json_widget.widgets import JSONEditorWidget
from django.db import models
from import_export import resources


# Register your models here.


class MagentoProductsResource(resources.ModelResource):
    class Meta:
        model = MagentoProducts


class MagentoProductsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_classes = [MagentoProductsResource]
    list_display = ("entity_id", "sku", "nombre", "cantidad", "color")
    formfield_overrides = {
        models.JSONField: {"widget": JSONEditorWidget},
    }
    readonly_fields = ("entity_id", "sku", "nombre", "cantidad")


admin.site.register(MagentoProducts, MagentoProductsAdmin)
