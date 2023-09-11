from django.db import models


# Create your models here.
class MagentoProducts(models.Model):
    """Model definition for MagentoProducts."""

    # TODO: Define fields here
    entity_id = models.BigIntegerField(
        help_text="entity_id",
    )
    tipo = models.CharField(
        help_text="tipo",
        max_length=250,
    )
    sku = models.CharField(
        help_text="sku",
        max_length=250,
    )
    fecha_creacion = models.DateTimeField(
        help_text="fecha creacion",
    )
    Tipo_impuesto = models.CharField(
        help_text="Impuesto",
        max_length=250,
        null=True,
    )
    nombre = models.CharField(
        help_text="nombre",
        max_length=250,
        null=True,
    )
    url = models.CharField(
        help_text="url",
        max_length=250,
        null=True,
    )
    estado = models.CharField(
        help_text="estado",
        max_length=250,
        null=True,
    )
    precio = models.BigIntegerField(
        help_text="precio",
        null=True,
    )
    precio_especial = models.BigIntegerField(
        help_text="precio_especial",
        null=True,
    )
    p_especial_desde = models.DateTimeField(
        help_text="p_especial_desde",
        null=True,
    )
    p_especial_hasta = models.DateTimeField(
        help_text="p_especial_hasta",
        null=True,
    )
    visibilidad = models.CharField(
        help_text="visibilidad",
        max_length=250,
        null=True,
    )
    cantidad = models.BigIntegerField(
        help_text="cantidad",
        null=True,
    )
    esta_en_stock = models.CharField(
        help_text="esta_en_stock",
        max_length=250,
        null=True,
    )
    peso = models.FloatField(
        help_text="peso",
        max_length=250,
        null=True,
    )
    short_description = models.TextField(
        help_text="short_description",
        null=True,
    )
    description = models.TextField(
        help_text="description",
        null=True,
    )
    meta_titulo = models.TextField(
        help_text="meta_titulo",
        null=True,
    )
    meta_descripcion = models.TextField(
        help_text="meta_descripcion",
        null=True,
    )
    imagen = models.CharField(
        help_text="imagen",
        max_length=255,
        null=True,
    )
    imagen2 = models.CharField(
        help_text="imagen2",
        max_length=255,
        null=True,
    )
    category_list = models.TextField(
        help_text="category_list",
        null=True,
    )
    color = models.JSONField(
        blank=True,
        null=True,
    )
    medidas = models.JSONField(
        blank=True,
        null=True,
    )
    pais = models.JSONField(
        blank=True,
        null=True,
    )
    garantia = models.JSONField(
        blank=True,
        null=True,
    )
    marca = models.JSONField(
        blank=True,
        null=True,
    )

    class Meta:
        """Meta definition for MagentoProducts."""

        verbose_name = "MagentoProducts"
        verbose_name_plural = "MagentoProductss"

    def __str__(self):
        """Unicode representation of MagentoProducts."""
        return str(self.nombre)
