import mysql.connector
import re
from magento.models import MagentoProducts

COLOR_LIST = [
    "Aguamarina",
    "Amaretto",
    "Amarillo",
    "Amarillo brillante",
    "Amarillo brillante",
    "Amarillo canario",
    "Amarillo canario intenso",
    "Amarillo canario oscuro",
    "Amarillo canario vibrante",
    "Amarillo curry",
    "Amarillo lima",
    "Amarillo lima oscuro",
    "Amarillo limón",
    "Amarillo limón",
    "Amarillo limón brillante",
    "Amarillo limón pálido",
    "Amarillo limón vibrante",
    "Amarillo maíz",
    "Amarillo maíz vibrante",
    "Amarillo mostaza",
    "Amarillo mostaza claro",
    "Amarillo mostaza claro",
    "Amarillo mostaza intenso",
    "Amarillo mostaza oscuro",
    "Amarillo mostaza suave",
    "Amarillo ocre",
    "Amarillo oro",
    "Amarillo oro cálido",
    "Amarillo oro claro",
    "Amarillo oro vibrante",
    "Amarillo pálido",
    "Amarillo pálido",
    "Amarillo pastel",
    "Amarillo pastel cálido",
    "Amarillo pastel suave",
    "Ámbar",
    "Ámbar oscuro",
    "Azul",
    "Azul acero",
    "Azul acero claro",
    "Azul celeste",
    "Azul celeste claro",
    "Azul celeste claro",
    "Azul celeste oscuro",
    "Azul celeste vibrante",
    "Azul cielo",
    "Azul cielo claro",
    "Azul claro",
    "Azul cobalto",
    "Azul cobalto brillante",
    "Azul cobalto claro",
    "Azul cobalto claro",
    "Azul cobalto intenso",
    "Azul cobalto oscuro",
    "Azul eléctrico",
    "Azul eléctrico claro",
    "Azul eléctrico oscuro",
    "Azul grisaceo",
    "Azul hielo",
    "Azul hielo claro",
    "Azul marino",
    "Azul marino claro",
    "Azul marino claro",
    "Azul marino intenso",
    "Azul marino oscuro",
    "Azul marino profundo",
    "Azul marino profundo claro",
    "Azul marino profundo claro",
    "Azul marino profundo vibrante",
    "Azul marino suave",
    "Azul marino suave",
    "Azul medianoche",
    "Azul medianoche claro",
    "Azul petróleo",
    "Azul petróleo claro",
    "Azul petróleo oscuro",
    "Azul piscina",
    "Azul piscina claro",
    "Azul real",
    "Azul real claro",
    "Azul turquesa",
    "Azul turquesa brillante",
    "Azul turquesa claro",
    "Azul turquesa oscuro",
    "Azul ultramar",
    "Azul ultramar oscuro",
    "Azul zafiro",
    "Azul zafiro claro",
    "Azul zafiro claro",
    "Azul zafiro intenso",
    "Azul zafiro profundo",
    "Beige",
    "Beige cálido",
    "Beige claro",
    "Blanco",
    "Blanco marquez",
    "Borgoña",
    " Café ",
    " Café Arcilla ",
    "Café moca",
    "Caramelo",
    "Canela",
    "Caqui",
    "Celeste",
    "Chocolate Mate",
    "Chocolate",
    "Cian",
    "Coral",
    "Coral brillante",
    "Coral claro",
    "Coral oscuro",
    "Coral suave",
    "Crema",
    "Dorado",
    "Frambuesa",
    "Frambuesa oscuro",
    "Frambuesa vibrante",
    "Gris",
    "Gris acero",
    "Gris acero claro",
    "Gris azulado",
    "Gris carbón",
    "Gris claro",
    "Gris claro",
    "Gris humo",
    "Gris marengo",
    "Gris oscuro",
    "Gris perla",
    "Gris perla cálido",
    "Gris pizarra",
    "Gris topo",
    "Gris topo claro",
    "Gris topo oscuro",
    "Índigo",
    "Lavanda",
    "Lavanda claro",
    "Lavanda claro",
    "Lavanda oscuro",
    "Lima",
    "Magenta",
    "Malva",
    "Marfil",
    "Marfil oscuro",
    "Marrón",
    "Marrón avellana",
    "Marrón avellana cálido",
    "Marrón cacao",
    "Marrón café",
    "Marrón café oscuro",
    "Marrón caramelo",
    "Marrón chocolate",
    "Marrón chocolate cálido",
    "Marrón chocolate oscuro",
    "Marrón claro",
    "Marrón claro",
    "Marrón claro",
    "Marrón nogal",
    "Marrón nogal cálido",
    "Marrón oscuro",
    "Marrón terracota",
    "Marrón tostado",
    "Melocotón",
    "Moca",
    "Morado",
    "Mostaza",
    "Multicolor",
    "Naranja",
    "Naranja quemado",
    "Naranja suave",
    "Negro",
    "Oliva",
    "Plateado",
    "Púrpura",
    "Rojo",
    "Rojo bermellón",
    "Rojo bermellón cálido",
    "Rojo bermellón claro",
    "Rojo bermellón oscuro",
    "Rojo bermellón oscuro",
    "Rojo cardenal",
    "Rojo cardenal claro",
    "Rojo carmesí",
    "Rojo carmesí brillante",
    "Rojo carmesí cálido",
    "Rojo carmesí oscuro",
    "Rojo carmesí profundo",
    "Rojo carmín",
    "Rojo cereza",
    "Rojo cereza intenso",
    "Rojo cereza oscuro",
    "Rojo cereza vibrante",
    "Rojo coral",
    "Rojo coral claro",
    "Rojo coral vibrante",
    "Rojo escarlata",
    "Rojo escarlata oscuro",
    "Rojo fuego",
    "Rojo granate",
    "Rojo granate oscuro",
    "Rojo ladrillo",
    "Rojo ladrillo oscuro",
    "Rojo oscuro",
    "Rojo oscuro",
    "Rojo oscuro",
    "Rojo óxido",
    "Rojo rubí",
    "Rojo rubí claro",
    "Rojo rubí intenso",
    "Rojo rubí oscuro",
    "Rojo rubí vibrante",
    "Rojo sangre",
    "Rojo tomate",
    "Rojo tomate oscuro",
    "Rojo vino",
    "Rojo vino cálido",
    "Rojo vino oscuro",
    "Rojo vino tinto",
    "Rosa",
    "Rosa antiguo",
    "Rosa antiguo claro",
    "Rosa antiguo suave",
    "Rosa bebé",
    "Rosa bebé",
    "Rosa chicle",
    "Rosa chicle claro",
    "Rosa chicle oscuro",
    "Rosa claro",
    "Rosa coral",
    "Rosa coral oscuro",
    "Rosa empolvado",
    "Rosa empolvado cálido",
    "Rosa fucsia",
    "Rosa fuerte",
    "Rosa fuerte oscuro",
    "Rosa intenso",
    "Rosa intenso",
    "Rosa intenso",
    "Rosa neón",
    "Rosa neón",
    "Rosa neón suave",
    "Rosa pálido",
    "Rosa pálido",
    "Rosa pálido",
    "Rosa pálido",
    "Rosa pálido cálido",
    "Rosa pastel",
    "Rosa pastel",
    "Rosa pastel cálido",
    "Rosa salmón",
    "Rosa salmón cálido",
    "Rosa salmón claro",
    "Rosa salmón intenso",
    "Rosa salmón vibrante",
    "Rosa suave",
    "Rosa suave cálido",
    "Rosa vibrante",
    "Rosado suave",
    "Salvia",
    "Terracota",
    "Turquesa",
    "Turquesa claro",
    "Verde",
    "Verde abeto",
    "Verde abeto claro",
    "Verde abeto fresco",
    "Verde abeto oscuro",
    "Verde bosque",
    "Verde bosque oscuro",
    "Verde bosque oscuro",
    "Verde esmeralda",
    "Verde esmeralda cálida",
    "Verde esmeralda claro",
    "Verde esmeralda fresco",
    "Verde esmeralda oscuro",
    "Verde hierba",
    "Verde hoja",
    "Verde hoja fresco",
    "Verde jade",
    "Verde lima",
    "Verde lima brillante",
    "Verde lima intenso",
    "Verde lima oscuro",
    "Verde limón",
    "Verde limón claro",
    "Verde manzana",
    "Verde manzana brillante",
    "Verde manzana cálido",
    "Verde mar",
    "Verde mar claro",
    "Verde mar oscuro",
    "Verde menta",
    "Verde menta claro",
    "Verde menta fresca",
    "Verde menta suave",
    "Verde musgo",
    "Verde musgo fresco",
    "Verde oliva cálido",
    "Verde oliva claro",
    "Verde oliva claro",
    "Verde oliva oscuro",
    "Verde oliva oscuro",
    "Verde oliva oscuro",
    "Verde olivo",
    "Verde pino",
    "Verde pino fresco",
    "Verde pistacho",
    "Verde pistacho claro",
    "Verde pistacho oscuro",
    "Verde salvia",
    "Verde salvia claro",
    "Violeta",
    "Wengue",
    "Duna",
]


def create():
    dbmagento = mysql.connector.connect(
        host="34.133.180.160",
        database="dekosas",
        user="root",
        password="3y]t%=Ny^y[vxLJb",
    )
    print(dbmagento)
    cursor = dbmagento.cursor()
    cursor.execute("SELECT * FROM V_TODOS_PRODUCTOS_ATRIBUTOS")
    for row in cursor:
        entity_id = row[0]
        print(entity_id)
        tipo = row[1]
        sku = row[2]
        fecha_creacion = row[3]
        Tipo_impuesto = row[4]
        nombre = row[5]
        url = row[6]
        estado = row[7]
        precio = row[8]
        precio_especial = row[9]
        p_especial_desde = row[10]
        p_especial_hasta = row[11]
        visibilidad = row[12]
        cantidad = row[13]
        esta_en_stock = row[14]
        peso = row[15]
        short_description = row[16]
        description = row[17]
        meta_titulo = row[18]
        meta_descripcion = row[19]
        imagen = row[20]
        imagen2 = row[21]
        category_list = row[22]
        print(entity_id, category_list)
        MagentoProducts.objects.create(
            entity_id=entity_id,
            tipo=tipo,
            sku=sku,
            fecha_creacion=fecha_creacion,
            Tipo_impuesto=Tipo_impuesto,
            nombre=nombre,
            url=url,
            estado=estado,
            precio=precio,
            precio_especial=precio_especial,
            p_especial_desde=p_especial_desde,
            p_especial_hasta=p_especial_hasta,
            visibilidad=visibilidad,
            cantidad=cantidad,
            esta_en_stock=esta_en_stock,
            peso=peso,
            short_description=short_description,
            description=description,
            meta_titulo=meta_titulo,
            meta_descripcion=meta_descripcion,
            imagen=imagen,
            imagen2=imagen2,
            category_list=category_list,
        )


def description_color():
    colors = [
        "rojo",
        "azul",
        "verde",
        "amarillo",
        "Negro",
        "Multicolor",
        "Blanco y negro",
    ]
    magento_products = MagentoProducts.objects.all()
    for products in magento_products:
        description = products.description
        print(description)
        contain = []
        for color in colors:
            if color in description:
                contain.append(color)
                print(contain)
        products.color = contain
        products.save()


# Crea una funcion que as traves de una expresion regular encuentre todas las posibles ocurrencias de colores en español y devuelva una lista con los que encuentre
def find_colors(text) -> list:
    l = "|".join(COLOR_LIST)
    regex = r"" + l
    matches = re.findall(regex, text, flags=re.IGNORECASE)
    return matches


def cargar_colores():
    products = MagentoProducts.objects.filter(color__iexact=[])
    counter = 1
    for product in products:
        print(counter)
        counter = counter + 1
        # descripcion larga
        product_description = product.description
        # lista_colores = []
        if product_description is not None:
            lista_colores = find_colors(product_description)
            lista_capitalizada = capitalizar_textos(lista_colores)
            lista_colores = convertir_lista_en_set(lista_capitalizada)
        # descripcion corta
        product_short_description = product.short_description
        if product_short_description is not None:
            lista_colores_short = find_colors(product_short_description)
            lista_capitalizada_short = capitalizar_textos(lista_colores_short)
            lista_colores_short = convertir_lista_en_set(lista_capitalizada_short)
        lista_definitiva = lista_colores | lista_colores_short
        set_definitivo = set(lista_definitiva)
        product.color = list(set_definitivo)
        product.save()


def convertir_lista_en_set(lista: list):
    return set(lista)


def capitalizar_textos(lista: list) -> list:
    lista_capitalizada = []
    for item in lista:
        lista_capitalizada.append(item.capitalize())
    return lista_capitalizada


TAG_RE = re.compile(r"<[^>]+>")


def remove_tags(text):
    return TAG_RE.sub(" ", text)


def clear_html():
    products = MagentoProducts.objects.all()
    count = 1
    for product in products:
        print(f"Product {count} of {len(products)}")
        count += 1
        medidas = []
        if type(product.description) == str:
            product.description = remove_tags(product.description)
        if type(product.short_description) == str:
            product.short_description = remove_tags(product.short_description)
        product.save()
