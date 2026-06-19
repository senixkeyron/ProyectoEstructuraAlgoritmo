def cargar_texto(nombre_archivo):
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        return archivo.readlines()


def limpiar_palabra(palabra):
    signos = ".,;:!?()[]{}\"'¿¡\n\t"
    return palabra.strip(signos).lower()