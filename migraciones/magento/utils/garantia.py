import re
from magento.models import MagentoProducts


def find_garantia(texto):
    patron = r"(\d{1,2}|un|Tres|Seis|tres|Un|por|Por|defectos|Defectos|cubre)\s?(defectos|Defectos|de fábrica|de Fábrica|fábrica|Fábrica|Facturación|Año|Año|Años|años|año|Mes|meses|MESES|mes|Meses|siglos|siglo|Días|dias|dia|días|DÍAS|DIAS|semana|Semana)"
    return re.findall(patron, texto)


def cargar_garantia():
    products = MagentoProducts.objects.all()
    counter = 1
    for product in products:
        counter = counter + 1
        print(f"contador = {counter}")
        description = product.description
        texto = product.description + " " + product.short_description
        sku = product.sku
        if description is not None:
            lista_garantia = find_garantia(texto)
            for i in lista_garantia:
                lista_garantia_concat = i[0] + " " + i[1]
                product.garantia = lista_garantia_concat
                product.save()
                print(sku)
                print(product.id)
                print(lista_garantia_concat)


def convertir_lista_en_set(lista: list):
    return set(lista)


def capitalizar_textos(lista: list) -> list:
    lista_capitalizada = []
    for item in lista:
        lista_capitalizada.append(item.capitalize())
    return lista_capitalizada
