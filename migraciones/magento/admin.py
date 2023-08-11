from django.contrib import admin
from magento.models import MagentoProducts


# Register your models here.
class MagentoProductsAdmin(admin.ModelAdmin):
    list_display = ("entity_id",)
    readonly_fields = ("entity_id",)


admin.site.register(MagentoProducts, MagentoProductsAdmin)
