from django.contrib import admin
from magento.models import MagentoProducts
from django_json_widget.widgets import JSONEditorWidget
from django.db import models


# Register your models here.
class MagentoProductsAdmin(admin.ModelAdmin):
    list_display = ("entity_id", "sku", "nombre", "cantidad", "color")
    formfield_overrides = {
        models.JSONField: {"widget": JSONEditorWidget},
    }
    readonly_fields = ("entity_id", "sku", "nombre", "cantidad", "color")


admin.site.register(MagentoProducts, MagentoProductsAdmin)
