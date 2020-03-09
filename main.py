from Ambiente import *
from Objeto import *
from Clasificar import *
from Estantes import *

# Clasificacion
clasif = Clasificar()

# Estantes
estante = Estantes()

# Mostrar objetos del ambiente
ambi = Ambiente()
ambi.mostrar()

# Almacenar objetos encontrados
listaOb = []
listaOb = ambi.darLista()

# Clasificar Objetos
print('**********ORDENANDO OBJETOS ENCONTRADOS**********')
for i in range(len(listaOb)):
    listaOb[i].setColor(clasif.color(listaOb[i].getDireccion()))
    listaOb[i].setForma(clasif.forma(listaOb[i].getDireccion()))
    
    if listaOb[i].getForma() == 'Regular':
        estante.ordReg(listaOb[i].getNombre(), listaOb[i].getColor())

    if listaOb[i].getForma() == 'Irregular':
        estante.ordIrr(listaOb[i].getNombre(), listaOb[i].getColor())

print('**********OBJETOS ORDENADOS**********')
estante.mostrarReg()
estante.mostrarIrr()
