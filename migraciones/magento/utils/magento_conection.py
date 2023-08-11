import mysql.connector
from magento.models import MagentoProducts


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
        "Multiplicar",
        "Blanco y negro",
    ]
    magento_products = MagentoProducts.objects.all()[:10]
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
