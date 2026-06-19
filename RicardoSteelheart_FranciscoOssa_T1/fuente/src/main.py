import time
from utilidades import cargar_texto
from busqueda import (
    busqueda_fuerza_bruta,
    crear_indice_diccionario,
    crear_indice_hash,
    buscar_diccionario,
    buscar_hash
)


def medir_tiempo_busqueda(funcion, repeticiones):
    inicio = time.time()

    for _ in range(repeticiones):
        funcion()

    fin = time.time()

    tiempo_total = fin - inicio
    tiempo_promedio = tiempo_total / repeticiones

    return tiempo_total, tiempo_promedio


def ejecutar_consultas_archivo(nombre_archivo, lineas, indice_diccionario, indice_hash):
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        consultas = archivo.readlines()

    for consulta in consultas:
        patron = consulta.strip()

        if patron != "":
            print("\nPatrón:", patron)
            print("Fuerza bruta:", busqueda_fuerza_bruta(lineas, patron))
            print("Diccionario Python:", buscar_diccionario(indice_diccionario, patron))
            print("Tabla Hash propia:", buscar_hash(indice_hash, patron))


def menu():
    lineas = []
    indice_diccionario = None
    indice_hash = None

    while True:
        print("\n===== MENÚ PRINCIPAL =====")
        print("1. Cargar archivo de texto")
        print("2. Buscar por fuerza bruta")
        print("3. Crear índice con diccionario de Python")
        print("4. Crear índice con tabla hash propia")
        print("5. Buscar usando diccionario de Python")
        print("6. Buscar usando tabla hash propia")
        print("7. Ejecutar consultas desde archivo")
        print("8. Medir tiempos")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese nombre del archivo: ")

            try:
                lineas = cargar_texto(nombre)
                indice_diccionario = None
                indice_hash = None

                print("Archivo cargado correctamente.")
                print("Cantidad de líneas:", len(lineas))

            except FileNotFoundError:
                print("Error: el archivo no existe.")

        elif opcion == "2":
            if not lineas:
                print("Primero debe cargar un archivo.")
            else:
                patron = input("Ingrese patrón a buscar: ")
                resultado = busqueda_fuerza_bruta(lineas, patron)
                print("Líneas encontradas:", resultado)

        elif opcion == "3":
            if not lineas:
                print("Primero debe cargar un archivo.")
            else:
                inicio = time.time()
                indice_diccionario = crear_indice_diccionario(lineas)
                fin = time.time()

                print("Índice con diccionario creado.")
                print("Tiempo de creación:", fin - inicio, "segundos")

        elif opcion == "4":
            if not lineas:
                print("Primero debe cargar un archivo.")
            else:
                inicio = time.time()
                indice_hash = crear_indice_hash(lineas)
                fin = time.time()

                print("Índice con tabla hash propia creado.")
                print("Tiempo de creación:", fin - inicio, "segundos")

        elif opcion == "5":
            if indice_diccionario is None:
                print("Primero debe crear el índice con diccionario.")
            else:
                patron = input("Ingrese patrón a buscar: ")
                resultado = buscar_diccionario(indice_diccionario, patron)
                print("Líneas encontradas:", resultado)

        elif opcion == "6":
            if indice_hash is None:
                print("Primero debe crear el índice hash.")
            else:
                patron = input("Ingrese patrón a buscar: ")
                resultado = buscar_hash(indice_hash, patron)
                print("Líneas encontradas:", resultado)

        elif opcion == "7":
            if not lineas:
                print("Primero debe cargar un archivo.")
            else:
                if indice_diccionario is None:
                    indice_diccionario = crear_indice_diccionario(lineas)

                if indice_hash is None:
                    indice_hash = crear_indice_hash(lineas)

                archivo_consultas = input("Ingrese archivo de consultas: ")

                try:
                    ejecutar_consultas_archivo(
                        archivo_consultas,
                        lineas,
                        indice_diccionario,
                        indice_hash
                    )
                except FileNotFoundError:
                    print("Error: el archivo de consultas no existe.")

        elif opcion == "8":
            if not lineas:
                print("Primero debe cargar un archivo.")
            else:
                patron = input("Ingrese patrón para medir: ")
                repeticiones = int(input("Ingrese cantidad de repeticiones: "))

                if indice_diccionario is None:
                    indice_diccionario = crear_indice_diccionario(lineas)

                if indice_hash is None:
                    indice_hash = crear_indice_hash(lineas)

                total_fb, promedio_fb = medir_tiempo_busqueda(
                    lambda: busqueda_fuerza_bruta(lineas, patron),
                    repeticiones
                )

                total_dic, promedio_dic = medir_tiempo_busqueda(
                    lambda: buscar_diccionario(indice_diccionario, patron),
                    repeticiones
                )

                total_hash, promedio_hash = medir_tiempo_busqueda(
                    lambda: buscar_hash(indice_hash, patron),
                    repeticiones
                )

                print("\n===== RESULTADOS =====")
                print("Método                 Tiempo total        Tiempo promedio")
                print("Fuerza bruta           ", total_fb, "     ", promedio_fb)
                print("Diccionario Python     ", total_dic, "     ", promedio_dic)
                print("Tabla Hash propia      ", total_hash, "     ", promedio_hash)

        elif opcion == "0":
            print("Programa finalizado.")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu()