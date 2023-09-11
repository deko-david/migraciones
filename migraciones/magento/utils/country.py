import re
from magento.models import MagentoProducts

COUNTRY_LIST = [
    "Colombia",
    "China",
    "Brasil",
    "Bélgica",
    "Belgica",
    "Turquía",
    "Estados Unidos",
    "Inglaterra",
    "Perú",
    "Pakistán",
    "Mexico",
    "México",
    "Austria",
    "Madagascar",
    "Italia",
    "India",
    "España",
    "Reino Unido",
    "Holanda",
    "Alemania",
    "Portugal",
    "Chile",
]


def list_country():
    return COUNTRY_LIST


def find_country(text) -> list:
    l = "|".join(COUNTRY_LIST)
    regex = r"" + l
    matches = re.findall(regex, text, flags=re.IGNORECASE)
    return matches


def cargar_country():
    products = MagentoProducts.objects.all()
    print(products)
    counter = 1
    for product in products:
        print(counter)
        counter = counter + 1
        # descripcion larga
        product_description = product.description
        # lista_pais = []
        if product_description is not None:
            lista_pais = find_country(product_description)
            lista_capitalizada = capitalizar_textos(lista_pais)
            lista_pais = convertir_lista_en_set(lista_capitalizada)
        # descripcion corta
        product_short_description = product.short_description
        if product_short_description is not None:
            lista_pais_short = find_country(product_short_description)
            lista_capitalizada_short = capitalizar_textos(lista_pais_short)
            lista_pais_short = convertir_lista_en_set(lista_capitalizada_short)
        lista_definitiva = lista_pais | lista_pais_short
        print(lista_definitiva)
        set_definitivo = set(lista_definitiva)
        product.pais = list(set_definitivo)
        product.save()


def convertir_lista_en_set(lista: list):
    return set(lista)


def capitalizar_textos(lista: list) -> list:
    lista_capitalizada = []
    for item in lista:
        lista_capitalizada.append(item.capitalize())
    return lista_capitalizada
