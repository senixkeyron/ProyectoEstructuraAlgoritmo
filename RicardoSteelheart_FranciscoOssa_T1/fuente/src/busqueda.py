from tabla_hash import TablaHash
from utilidades import limpiar_palabra


def busqueda_fuerza_bruta(lineas, patron):
    ocurrencias = []
    patron = patron.lower()

    for i in range(len(lineas)):
        linea = lineas[i].lower()

        if patron in linea:
            ocurrencias.append(i + 1)

    return ocurrencias


def crear_indice_diccionario(lineas):
    indice = {}

    for i in range(len(lineas)):
        palabras = lineas[i].split()

        for palabra in palabras:
            palabra = limpiar_palabra(palabra)

            if palabra != "":
                if palabra not in indice:
                    indice[palabra] = []

                if (i + 1) not in indice[palabra]:
                    indice[palabra].append(i + 1)

    return indice


def crear_indice_hash(lineas):
    tabla = TablaHash()

    for i in range(len(lineas)):
        palabras = lineas[i].split()

        for palabra in palabras:
            palabra = limpiar_palabra(palabra)

            if palabra != "":
                tabla.insertar(palabra, i + 1)

    return tabla


def buscar_diccionario(indice, patron):
    patron = limpiar_palabra(patron)
    return indice.get(patron, [])


def buscar_hash(tabla, patron):
    patron = limpiar_palabra(patron)
    return tabla.buscar(patron)