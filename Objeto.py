class Objeto():
    # Constructor
    def __init__(self, nomb, direc):
        self.__nombre = nomb
        self.__direccion = direc
        self.__forma = ''
        self.__color = ''

    # Setters
    def setNombre(self, nomb):
        self.__nombre = nomb

    def setDireccion(self, direc):
        self.__nombre = direc

    def setForma(self, form):
        self.__forma = form

    def setColor(self, col):
        self.__color = col

    # Getters
    def getNombre(self):
        return self.__nombre

    def getDireccion(self):
        return self.__direccion

    def getForma(self):
        return self.__forma

    def getColor(self):
        return self.__color


# prueba
"""
objetito = Objeto('Libro', './libro')
objetito.setForma('Regular')
objetito.setColor('Rojo')
print(objetito.getNombre())
print(objetito.getDireccion())
print(objetito.getForma())
print(objetito.getColor())
print('----------------------')
lista = [Objeto('balon mundial','nuevo/balon'), Objeto('perrito','perro.jpg')]
print(lista[0].getNombre())
print(lista[1].getNombre())
"""
