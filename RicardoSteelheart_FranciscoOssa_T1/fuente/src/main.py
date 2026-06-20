import time  # Importa el módulo time para medir tiempos

class TablaHash:  # Define la clase TablaHash
    def __init__(self, tamano=1000):  # Constructor de la tabla hash
        self.tamano = tamano  # Guarda el tamaño de la tabla
        self.tabla = []  # Crea la lista principal de la tabla
        for _ in range(tamano):  # Repite según el tamaño indicado
            self.tabla.append([])  # Agrega una cubeta vacía

    def funcion_hash(self, palabra):  # Calcula el índice hash de una palabra
        suma = 0  # Inicializa la suma
        for letra in palabra:  # Recorre cada letra
            suma += ord(letra)  # Suma el código ASCII de la letra
        return suma % self.tamano  # Retorna un índice válido

    def insertar(self, palabra, linea):  # Inserta una palabra y línea
        indice = self.funcion_hash(palabra)  # Calcula el índice
        cubeta = self.tabla[indice]  # Obtiene la cubeta
        for elemento in cubeta:  # Recorre la cubeta
            if elemento[0] == palabra:  # Si la palabra ya existe
                if linea not in elemento[1]:  # Si la línea no está registrada
                    elemento[1].append(linea)  # Agrega la línea
                return  # Termina la función
        cubeta.append([palabra, [linea]])  # Agrega una nueva palabra

    def buscar(self, palabra):  # Busca una palabra en la tabla
        indice = self.funcion_hash(palabra)  # Calcula el índice
        cubeta = self.tabla[indice]  # Obtiene la cubeta
        for elemento in cubeta:  # Recorre la cubeta
            if elemento[0] == palabra:  # Si encuentra la palabra
                return elemento[1]  # Retorna las líneas
        return []  # Retorna vacío si no encuentra nada

def cargar_texto(nombre_archivo):  # Carga un archivo de texto
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:  # Abre el archivo
        return archivo.readlines()  # Retorna sus líneas

def limpiar_palabra(palabra):  # Limpia una palabra
    signos = ".,;:!?()[]{}\"'¿¡\n\t"  # Signos a eliminar
    return palabra.strip(signos).lower()  # Quita signos y pasa a minúscula

def busqueda_fuerza_bruta(lineas, patron):  # Busca recorriendo todas las líneas
    ocurrencias = []  # Lista de líneas encontradas
    patron = patron.lower()  # Convierte el patrón a minúscula
    for i in range(len(lineas)):  # Recorre las líneas
        linea = lineas[i].lower()  # Convierte la línea a minúscula
        if patron in linea:  # Verifica si el patrón está en la línea
            ocurrencias.append(i + 1)  # Guarda el número de línea
    return ocurrencias  # Retorna las ocurrencias

def crear_indice_diccionario(lineas):  # Crea índice usando diccionario
    indice = {}  # Crea diccionario vacío
    for i in range(len(lineas)):  # Recorre las líneas
        palabras = lineas[i].split()  # Divide la línea en palabras
        for palabra in palabras:  # Recorre cada palabra
            palabra = limpiar_palabra(palabra)  # Limpia la palabra

            if palabra != "":  # Verifica que no esté vacía
                if palabra not in indice:  # Si no existe en el índice
                    indice[palabra] = []  # Crea lista para esa palabra
                if (i + 1) not in indice[palabra]:  # Evita repetir línea
                    indice[palabra].append(i + 1)  # Agrega número de línea
    return indice  # Retorna el índice

def crear_indice_hash(lineas):  # Crea índice usando tabla hash propia
    tabla = TablaHash()  # Crea una tabla hash
    for i in range(len(lineas)):  # Recorre las líneas
        palabras = lineas[i].split()  # Divide la línea en palabras

        for palabra in palabras:  # Recorre cada palabra
            palabra = limpiar_palabra(palabra)  # Limpia la palabra

            if palabra != "":  # Verifica que no esté vacía
                tabla.insertar(palabra, i + 1)  # Inserta palabra y línea
    return tabla  # Retorna la tabla hash

def buscar_diccionario(indice, patron):  # Busca usando diccionario
    patron = limpiar_palabra(patron)  # Limpia el patrón
    return indice.get(patron, [])  # Retorna líneas o lista vacía

def buscar_hash(tabla, patron):  # Busca usando tabla hash
    patron = limpiar_palabra(patron)  # Limpia el patrón
    return tabla.buscar(patron)  # Retorna resultado de la búsqueda

def medir_tiempo_busqueda(funcion, repeticiones):  # Mide tiempo de una búsqueda
    inicio = time.time()  # Guarda tiempo inicial
    for _ in range(repeticiones):  # Repite la búsqueda
        funcion()  # Ejecuta la función recibida

    fin = time.time()  # Guarda tiempo final
    tiempo_total = fin - inicio  # Calcula tiempo total
    tiempo_promedio = tiempo_total / repeticiones  # Calcula promedio
    return tiempo_total, tiempo_promedio  # Retorna ambos tiempos

def ejecutar_consultas_archivo(nombre_archivo, lineas, indice_diccionario, indice_hash):  # Ejecuta búsquedas desde archivo
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:  # Abre archivo de consultas
        consultas = archivo.readlines()  # Lee todas las consultas
    for consulta in consultas:  # Recorre cada consulta
        patron = consulta.strip()  # Quita espacios y saltos
        if patron != "":  # Verifica que no esté vacía
            print("\nPatrón:", patron)  # Muestra el patrón
            print("Fuerza bruta:", busqueda_fuerza_bruta(lineas, patron))  # Busca por fuerza bruta
            print("Diccionario Python:", buscar_diccionario(indice_diccionario, patron))  # Busca en diccionario
            print("Tabla Hash propia:", buscar_hash(indice_hash, patron))  # Busca en tabla hash


def menu():  # Función principal del menú
    lineas = []  # Guarda las líneas del archivo
    indice_diccionario = None  # Índice diccionario inicial
    indice_hash = None  # Índice hash inicial
    while True:  # Ciclo infinito del menú
        print("\n===== MENU PRINCIPAL =====")  # Imprime título
        print("1. Cargar archivo de texto")  # Opción 1
        print("2. Buscar por fuerza bruta")  # Opción 2
        print("3. Crear índice con diccionario de Python")  # Opción 3
        print("4. Crear índice con tabla hash propia")  # Opción 4
        print("5. Buscar usando diccionario de Python")  # Opción 5
        print("6. Buscar usando tabla hash propia")  # Opción 6
        print("7. Ejecutar consultas desde archivo")  # Opción 7
        print("8. Medir tiempos")  # Opción 8
        print("0. Salir")  # Opción salir
        opcion = input("Seleccione una opción: ")  # Lee opción del usuario
        
        if opcion == "1":  # Si el usuario elige cargar archivo
            nombre = input("Ingrese nombre del archivo: ")  # Pide nombre

            try:  # Intenta cargar el archivo
                lineas = cargar_texto(nombre)  # Carga las líneas
                indice_diccionario = None  # Reinicia diccionario
                indice_hash = None  # Reinicia hash

                print("Archivo cargado correctamente.")  # Mensaje de éxito
                print("Cantidad de líneas:", len(lineas))  # Muestra cantidad

            except FileNotFoundError:  # Si no existe el archivo
                print("Error: el archivo no existe.")  # Mensaje de error

        elif opcion == "2":  # Si elige búsqueda fuerza bruta
            if not lineas:  # Si no hay archivo cargado
                print("Primero debe cargar un archivo.")  # Mensaje de aviso
            else:  # Si hay archivo
                patron = input("Ingrese patrón a buscar: ")  # Pide patrón
                resultado = busqueda_fuerza_bruta(lineas, patron)  # Busca patrón
                print("Líneas encontradas:", resultado)  # Muestra resultado

        elif opcion == "3":  # Si elige crear índice diccionario
            if not lineas:  # Si no hay archivo
                print("Primero debe cargar un archivo.")  # Mensaje de aviso
            else:  # Si hay archivo
                inicio = time.time()  # Tiempo inicial
                indice_diccionario = crear_indice_diccionario(lineas)  # Crea índice
                fin = time.time()  # Tiempo final

                print("Índice con diccionario creado.")  # Mensaje de éxito
                print("Tiempo de creación:", fin - inicio, "segundos")  # Muestra tiempo

        elif opcion == "4":  # Si elige crear índice hash
            if not lineas:  # Si no hay archivo
                print("Primero debe cargar un archivo.")  # Mensaje de aviso
            else:  # Si hay archivo
                inicio = time.time()  # Tiempo inicial
                indice_hash = crear_indice_hash(lineas)  # Crea índice hash
                fin = time.time()  # Tiempo final

                print("Índice con tabla hash propia creado.")  # Mensaje de éxito
                print("Tiempo de creación:", fin - inicio, "segundos")  # Muestra tiempo

        elif opcion == "5":  # Si elige buscar en diccionario
            if indice_diccionario is None:  # Si no existe índice
                print("Primero debe crear el índice con diccionario.")  # Mensaje de aviso
            else:  # Si existe índice
                patron = input("Ingrese patrón a buscar: ")  # Pide patrón
                resultado = buscar_diccionario(indice_diccionario, patron)  # Busca patrón
                print("Líneas encontradas:", resultado)  # Muestra resultado

        elif opcion == "6":  # Si elige buscar en hash
            if indice_hash is None:  # Si no existe índice hash
                print("Primero debe crear el índice hash.")  # Mensaje de aviso
            else:  # Si existe índice hash
                patron = input("Ingrese patrón a buscar: ")  # Pide patrón
                resultado = buscar_hash(indice_hash, patron)  # Busca patrón
                print("Líneas encontradas:", resultado)  # Muestra resultado

        elif opcion == "7":  # Si elige ejecutar consultas desde archivo
            if not lineas:  # Si no hay archivo cargado
                print("Primero debe cargar un archivo.")  # Mensaje de aviso
            else:  # Si hay archivo
                if indice_diccionario is None:  # Si no existe diccionario
                    indice_diccionario = crear_indice_diccionario(lineas)  # Lo crea

                if indice_hash is None:  # Si no existe tabla hash
                    indice_hash = crear_indice_hash(lineas)  # La crea

                archivo_consultas = input("Ingrese archivo de consultas: ")  # Pide archivo

                try:  # Intenta ejecutar consultas
                    ejecutar_consultas_archivo(  # Llama función de consultas
                        archivo_consultas,  # Archivo con patrones
                        lineas,  # Líneas del texto
                        indice_diccionario,  # Índice diccionario
                        indice_hash  # Índice hash
                    )
                except FileNotFoundError:  # Si el archivo no existe
                    print("Error: el archivo de consultas no existe.")  # Mensaje de error

        elif opcion == "8":  # Si elige medir tiempos
            if not lineas:  # Si no hay archivo
                print("Primero debe cargar un archivo.")  # Mensaje de aviso
            else:  # Si hay archivo
                patron = input("Ingrese patrón para medir: ")  # Pide patrón
                repeticiones = int(input("Ingrese cantidad de repeticiones: "))  # Pide repeticiones

                if repeticiones <= 0:  # Valida repeticiones
                    print("La cantidad de repeticiones debe ser mayor que 0.")  # Mensaje de error
                else:  # Si el número es válido
                    if indice_diccionario is None:  # Si no existe índice diccionario
                        indice_diccionario = crear_indice_diccionario(lineas)  # Lo crea

                    if indice_hash is None:  # Si no existe índice hash
                        indice_hash = crear_indice_hash(lineas)  # Lo crea

                    total_fb, promedio_fb = medir_tiempo_busqueda(  # Mide fuerza bruta
                        lambda: busqueda_fuerza_bruta(lineas, patron),  # Función anónima
                        repeticiones  # Cantidad de repeticiones
                    )

                    total_dic, promedio_dic = medir_tiempo_busqueda(  # Mide diccionario
                        lambda: buscar_diccionario(indice_diccionario, patron),  # Función anónima
                        repeticiones  # Cantidad de repeticiones
                    )

                    total_hash, promedio_hash = medir_tiempo_busqueda(  # Mide hash
                        lambda: buscar_hash(indice_hash, patron),  # Función anónima
                        repeticiones  # Cantidad de repeticiones
                    )

                    print("\n===== RESULTADOS =====")  # Título resultados
                    print("Método                 Tiempo total        Tiempo promedio")  # Encabezado
                    print("Fuerza bruta           ", total_fb, "     ", promedio_fb)  # Resultado fuerza bruta
                    print("Diccionario Python     ", total_dic, "     ", promedio_dic)  # Resultado diccionario
                    print("Tabla Hash propia      ", total_hash, "     ", promedio_hash)  # Resultado hash

        elif opcion == "0":  # Si elige salir
            print("Programa finalizado.")  # Mensaje final
            break  # Sale del ciclo

        else:  # Si ingresa opción incorrecta
            print("Opcinn invalida.")  # Mensaje de opción inválida

menu()  # Ejecuta el programa