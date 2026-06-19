class Nodo:
    def __init__(self, clave, lineas):
        self.clave = clave
        self.lineas = lineas
        self.siguiente = None


class TablaHash:
    def __init__(self, tamano=1009):
        self.tamano = tamano
        self.tabla = [None] * tamano

    def funcion_hash(self, clave):
        valor = 0

        for caracter in clave:
            valor = (valor * 31 + ord(caracter)) % self.tamano

        return valor

    def insertar(self, clave, linea):
        indice = self.funcion_hash(clave)
        actual = self.tabla[indice]

        while actual is not None:
            if actual.clave == clave:
                if linea not in actual.lineas:
                    actual.lineas.append(linea)
                return

            actual = actual.siguiente

        nuevo = Nodo(clave, [linea])
        nuevo.siguiente = self.tabla[indice]
        self.tabla[indice] = nuevo

    def buscar(self, clave):
        indice = self.funcion_hash(clave)
        actual = self.tabla[indice]

        while actual is not None:
            if actual.clave == clave:
                return actual.lineas

            actual = actual.siguiente

        return []