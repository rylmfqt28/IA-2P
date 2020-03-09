from Objeto import *

ambiente = []
ambiente.append(Objeto('Audifono', './habitacion/audifono.png'))
ambiente.append(Objeto('Balon', './habitacion/balon.jpg'))
ambiente.append(Objeto('Billetera', './habitacion/billetera.jpg'))
ambiente.append(Objeto('Cascabel', './habitacion/cascabel.png'))
ambiente.append(Objeto('Cuaderno', './habitacion/cuaderno.jpg'))
ambiente.append(Objeto('Escuadra', './habitacion/escuadra.png'))
ambiente.append(Objeto('Gorra', './habitacion/gorra.jpg'))
ambiente.append(Objeto('Libro Banco', './habitacion/libro_banco.jpg'))
ambiente.append(Objeto('Parlante', './habitacion/parlante.jpg'))
ambiente.append(Objeto('Peluche Stich', './habitacion/peluche.jpg'))
ambiente.append(Objeto('Pera', './habitacion/pera.png'))
ambiente.append(Objeto('Regla', './habitacion/regla.png'))
ambiente.append(Objeto('Tenis', './habitacion/tenis.png'))
ambiente.append(Objeto('Vaso', './habitacion/vaso.jpg'))
ambiente.append(Objeto('Cartas-UNO', './habitacion/uno_cartas.jpg'))
ambiente.append(Objeto('Linterna', './habitacion/linterna.png'))
ambiente.append(Objeto('Peluche Elmo', './habitacion/elmo.jpg'))

class Ambiente():
    # Muestra los objetos encontrados en un ambiente
    def mostrar(self):
        print('****SE ENCONTRARON LOS SIGUIENTES OBJETOS EN EL AMBIENTE****')
        for amb in ambiente:
            print(amb.getNombre())
        print('************************************************************')

    # Retorna la lista de objetos
    def darLista(self):
        return ambiente
