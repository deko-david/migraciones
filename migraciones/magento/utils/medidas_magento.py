import re
from magento.models import MagentoProducts

TAG_RE = re.compile(r"<[^>]+>")

RE_SUB_PATTERNS = [
    ("X", "x"),
    ("-", "x"),
    ("diámetro y", ""),
    ("diámetro", ""),
    ("profunidad", ""),
    ("alto:", ""),
    ("Altura:", ""),
    ("ALTO (cm)=", ""),
    ("ancho:", ""),
    ("ANCHO (cm)=", ""),
    ("profundo:", ""),
    ("PROFUNDO (cm)=", ""),
    ("Profundidad:", ""),
    ("fondo:", ""),
    ("FONDO (cm)=", ""),
    ("¶-", ""),
    ("Ancho:", ""),
    ("Alto:", ""),
    ("Profundo:", ""),
    ("Largo", ""),
    ("Alto", ""),
    ("Ancho", ""),
    ("Alto =", ""),
    ("Alto=", ""),
    ("Ancho =", ""),
    ("Ancho=", ""),
    ("largo =", ""),
    ("largo=", ""),
    ("/", ""),
    ("-", ""),
    ("Al:", ""),
    ("An:", ""),
    ("L:", ""),
    ("W:", ""),
]


def list_that_can_be_used(list_measure: list):
    """
    This function is used to get the measures that can be used
    """
    for item in list_measure:
        list_item: list = list(item)

        sort_list = list_item.copy()
        sort_list.sort()
        greater = sort_list[-1]
        can_be_used = True
        for i in range(len(sort_list) - 1):
            value = sort_list[i]

            if float(greater) == 0:
                can_be_used = False
                break
            else:
                percent = (float(value) * 100) / float(greater)
                if percent < 0.1:
                    can_be_used = False
                    break
        if not can_be_used:
            list_measure.remove(item)
    return list_measure


def get_measures_3_dimensions(string):
    """
    This function is used to get the measures of 3 dimensions
    """
    measures = []
    regex = (
        r"(\d+)(?:\s?\bcm|m\b)?\s?x\s?(\d+)(?:\s?\bcm|m\b)?\s?x\s?(\d+)(?:\s?\bcm|m\b)?"
    )
    measures = re.findall(regex, string, re.MULTILINE)
    # for matchNum, match in enumerate(matches, start=1):
    #     measures.append(match.groups())
    text_meassures = []
    measure = list_that_can_be_used(measures)

    for measure in measures:
        if (
            float(measure[0]) < 1000
            and float(measure[1]) < 1000
            and float(measure[2]) < 1000
            and not measure[0].startswith("0")
            and not measure[1].startswith("0")
            and not measure[2].startswith("0")
        ):
            text_meassures.append(f"{measure[0]} x {measure[1]} x {measure[2]}")
    text_meassures.sort()
    return set(text_meassures)


def get_measures_2_dimensions(string):
    """
    This function is used to get the measures of 2 dimensions
    """
    measures = []
    regex = r"(\d+\.\d+|\d+)([ \t\n\r\f\v])?(?:\s?\bcm|m\b)?\s?[ \t\n\r\f\v|x]\s?(\d+\.\d+|\d+)([ \t\n\r\f\v])?(?:\s?\bcm|m\b)?\s?"
    matches = re.findall(regex, string, re.MULTILINE)
    measures = []
    for match in matches:
        temp_match = []
        for m in match:
            print("--", m, "--", sep="\n")
            if m != "" and m != " " and m != "  ":
                temp_match.append(m)
        measures.append(temp_match)
    text_meassures = []
    measure = list_that_can_be_used(measures)
    for measure in measures:
        if len(measure) == 2:
            if (
                float(measure[0]) < 1000
                and float(measure[1]) < 1000
                and not measure[0].startswith("0")
                and not measure[1].startswith("0")
            ):
                text_meassures.append(f"{measure[0]} x {measure[1]}")
    text_meassures.sort()
    return set(text_meassures)


def get_float_measures_3_dimensions(string):
    """
    This function is used to get the measures of 3 dimensions
    """
    measures = []
    regex = r"(\d+\.\d+|\d+)(?:\s?\bcm|m\b)?\s?[ \t\n\r\f\v|x]\s?(\d+\.\d+|\d+)(?:\s?\bcm|m\b)?\s?[ \t\n\r\f\v|x]\s?(\d+\.\d+|\d+)(?:\s?\bcm|m\b)?"
    measures = re.findall(regex, string, re.MULTILINE)
    # for matchNum, match in enumerate(matches, start=1):
    #     measures.append(match.groups())
    text_meassures = []
    measure = list_that_can_be_used(measures)
    for measure in measures:
        if len(measure) == 3:
            if (
                float(measure[0]) < 1000
                and float(measure[1]) < 1000
                and float(measure[2]) < 1000
                and not measure[0].startswith("0")
                and not measure[1].startswith("0")
                and not measure[2].startswith("0")
            ):
                text_meassures.append(f"{measure[0]} x {measure[1]} x {measure[2]}")
    text_meassures.sort()
    return set(text_meassures)


def get_float_measures_2_dimensions(string):
    """
    This function is used to get the measures of 2 dimensions
    """
    measures = []
    regex = r"(\d+)(?:\s?\bcm|m\b)?\s?x\s?(\d+)(?:\s?\bcm|m\b)?"
    measures = re.findall(regex, string, re.MULTILINE)
    # for matchNum, match in enumerate(matches, start=1):
    #     measures.append(match.groups())
    text_meassures = []
    measure = list_that_can_be_used(measures)
    for measure in measures:
        if (
            float(measure[0]) < 1000
            and float(measure[1]) < 1000
            and not measure[0].startswith("0")
            and not measure[1].startswith("0")
        ):
            text_meassures.append(f"{measure[0]} x {measure[1]}")
    text_meassures.sort()
    return set(text_meassures)


def add_measures(measures: list, text: str) -> list:
    """
    This function is used to add measures to a list
    """
    measures.extend(get_measures_3_dimensions(text))
    measures.extend(get_measures_2_dimensions(text))
    measures.extend(get_float_measures_3_dimensions(text))
    measures.extend(get_float_measures_2_dimensions(text))
    return measures


def multiple_replace(string: str, *pattterns):
    """
    This function is used to replace multiple patterns in a string
    """
    for pattern in pattterns:
        string = string.replace(pattern[0], pattern[1])
    return string


def multiple_re_sub(string: str, replace_with: str = "", pattterns: list = []):
    """
    This function is used to replace multiple patterns in a string
    """
    for pattern in pattterns:
        string = string.replace(pattern[0], pattern[1])
        string = re.sub(pattern[0], pattern[1], string, flags=re.IGNORECASE)
    string = re.sub(r"\s+", " ", string)
    return string


def set_meassurements():
    products = MagentoProducts.objects.all()
    # products = MagentoProducts.objects.filter(medidas__iexact=[])
    # products = MagentoProducts.objects.filter(id=20078)
    count = 1
    for product in products:
        print(f"Product {count} of {len(products)} -->ID: {product.id}")
        count += 1
        the_measures = []
        if product.description is None:
            product.description = ""
        if product.short_description is None:
            product.short_description = ""
        if product.meta_titulo is None:
            product.meta_titulo = ""
        if product.meta_descripcion is None:
            product.meta_descripcion = ""
        if product.imagen is None:
            product.imagen = ""
        if product.imagen2 is None:
            product.imagen2 = ""
        if product.nombre is None:
            product.nombre = ""

        text_no_analize = (
            product.description
            + product.short_description
            + product.meta_titulo
            + product.meta_descripcion
            + product.imagen
            + product.imagen2
            + product.nombre
        )
        # text_no_analize = re.sub(r"\s+", " ", text_no_analize)
        if text_no_analize is not None:
            text_no_analize = multiple_re_sub(
                string=text_no_analize, replace_with="", pattterns=RE_SUB_PATTERNS
            )

        print(text_no_analize)
        if type(text_no_analize) == str:
            the_measures = add_measures(the_measures, text_no_analize)

        set_medidas = set(the_measures)
        lista_medidas_3_dimensiones = []
        lista_medidas_2_dimensiones = []
        for the_measure in set_medidas:
            size = the_measure.split("x")
            if len(size) == 3:
                lista_medidas_3_dimensiones.append(the_measure)
            elif len(size) == 2:
                lista_medidas_2_dimensiones.append(the_measure)
        temp_2_d = lista_medidas_2_dimensiones.copy()
        temp_3_d = lista_medidas_3_dimensiones.copy()
        temp_2_d.sort()
        temp_3_d.sort()
        for the_measure in temp_2_d:
            temp_2_d.sort()
            for medida_3 in temp_3_d:
                temp_3_d.sort()
                if the_measure in medida_3:
                    lista_medidas_2_dimensiones.remove(the_measure)
                    break

        for item in lista_medidas_2_dimensiones:
            exploded_item = item.split("x")
            for item_3 in lista_medidas_3_dimensiones:
                if exploded_item[0] in item_3 and exploded_item[1] in item_3:
                    lista_medidas_2_dimensiones.remove(item)

        lista_medidas_2_dimensiones.extend(lista_medidas_3_dimensiones)
        real = lista_medidas_2_dimensiones.copy()
        real = list(set(real))
        if "1 x 1" in real:
            real.remove("1 x 1")
        if "1 x 1 x 1" in real:
            real.remove("1 x 1 x 1")
        # print("-----------------------")
        for r in real:
            for r2 in real:
                if r == r2:
                    pass
                elif r in r2:
                    if r in real:
                        real.remove(r)

        product.medidas = list(set(real))
        print(real)
        product.save()


def get_unidimensional_measures(string):
    measures = []
    regex = r"(\d+\.\d+|\d+)[ \t\n\r\f\v|x]cm"
    measures = re.findall(regex, string, re.MULTILINE)
    # for matchNum, match in enumerate(matches, start=1):
    #     measures.append(match.groups(0))
    values = []
    for measure in measures:
        for item in measure:
            values.append(item)
    return set(values)


def set_unidimensional_meassurements():
    # products = MagentoProducts.objects.all()
    products = MagentoProducts.objects.filter(medidas__iexact=[])
    # products = MagentoProducts.objects.filter(id=22426)
    count = 1
    for product in products:
        print(f"Product {count} of {len(products)} -->ID: {product.id}")
        count += 1
        the_measures = []
        if product.description is None:
            product.description = ""
        if product.short_description is None:
            product.short_description = ""
        if product.meta_titulo is None:
            product.meta_titulo = ""
        if product.meta_descripcion is None:
            product.meta_descripcion = ""
        if product.imagen is None:
            product.imagen = ""
        if product.imagen2 is None:
            product.imagen2 = ""
        if product.nombre is None:
            product.nombre = ""
        real = []
        text_no_analize = (
            product.description
            + product.short_description
            + product.meta_titulo
            + product.meta_descripcion
            + product.imagen
            + product.imagen2
            + product.nombre
        )
        if text_no_analize is not None:
            real = get_unidimensional_measures(text_no_analize)
        product.medidas = list(real)
        product.save()
