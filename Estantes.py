
# estante separado por colores
regAzul = []
regRojo = []
regVerde = []
irrAzul = []
irrRojo = []
irrVerde = []

class Estantes():
    
    # Colocar objetos a estante de objetos Regulares
    def ordReg(self, nomb, color):
        if color == 'Azul':
            regAzul.append(nomb)
        if color == 'Rojo':
            regRojo.append(nomb)
        if color == 'Verde':
            regVerde.append(nomb)

    # Colocar objetos a estante de objetos Irregulares
    def ordIrr(self, nomb, color):
        if color == 'Azul':
            irrAzul.append(nomb)
        if color == 'Rojo':
            irrRojo.append(nomb)
        if color == 'Verde':
            irrVerde.append(nomb)

    # Mostrar estante de objetos regulares
    def mostrarReg(self):
        print('**********ESTANTE DE OBJETOS REGULARES***********')
        print('Piso 3: Objetos Azules')
        for obj1 in regAzul:
            print(obj1, end=' ,')
        print('')
        print('Piso 2: Objetos Rojos')
        for obj2 in regRojo:
            print(obj2, end=' ,')
        print('')
        print('Piso 1: Objetos Verdes')
        for obj3 in regVerde:
            print(obj3, end=' ,')
        print('')
        print('*************************************************')

    # Mostrar estante de objetos irregulares
    def mostrarIrr(self):
        print('**********ESTANTE DE OBJETOS IRREGULARES***********')
        print('Piso 3: Objetos Azules')
        for obj4 in irrAzul:
            print(obj4, end=' ,')
        print('')
        print('Piso 2: Objetos Rojos')
        for obj5 in irrRojo:
            print(obj5, end=' ,')
        print('')
        print('Piso 1: Objetos Verdes')
        for obj6 in irrVerde:
            print(obj6, end=' ,')
        print('')
        print('**************************************************')

#prueba
"""
prueba = Estantes()
prueba.ordReg('Balon', 'Azul')
prueba.ordReg('Regla', 'Rojo')
prueba.ordReg('Libro', 'Verde')
prueba.ordReg('Pelota', 'Verde')
prueba.ordIrr('Pera', 'Verde')
prueba.ordIrr('Peluche', 'Azul')
prueba.ordIrr('Tenis', 'Azul')
prueba.mostrarReg()
prueba.mostrarIrr()
"""
