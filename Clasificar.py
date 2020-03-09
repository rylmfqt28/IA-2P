import numpy as np
from tensorflow.python.keras.preprocessing.image import load_img, img_to_array
from tensorflow.python.keras.models import load_model

# Tamaño a reescalar las imagenes
longitud, altura = 100, 100
# Directorios de los archivos h5
modelo_forma = './modelo/modelo.h5'
pesos_forma = './modelo/pesos.h5'
modelo_color = './modelo_color/modelo_color.h5'
pesos_color = './modelo_color/pesos_color.h5'
#
cnnForma = load_model(modelo_forma)
cnnForma.load_weights(pesos_forma)
cnnColor = load_model(modelo_color)
cnnColor.load_weights(pesos_color)

class Clasificar():
    
    # Predecir Forma
    def forma(self, file):
        res = ''
        x=load_img(file, target_size=(longitud, altura))
        x=img_to_array(x)
        x=np.expand_dims(x, axis=0)
        arreglo=cnnForma.predict(x) ##[[irregular, regular]]
        resultado=arreglo[0]
        respuesta=np.argmax(resultado) ##[[1,0]] o [[0,1]]

        if respuesta == 0:
            res = 'Irregular'
        if respuesta == 1:
            res = 'Regular'

        return res

    # Predecir Color
    def color(self, file):
        res = ''
        x=load_img(file, target_size=(longitud, altura))
        x=img_to_array(x)
        x=np.expand_dims(x, axis=0)
        arreglo=cnnColor.predict(x) ##[[azul, rojo, verde]]
        resultado=arreglo[0]
        respuesta=np.argmax(resultado) ##[[1,0,0]] o [[0,1,0]] o [[0,0,1]]

        if respuesta == 0:
            res = 'Azul'
        if respuesta == 1:
            res = 'Rojo'
        if respuesta == 2:
            res = 'Verde'

        return res


#Prueba
"""
prueba = Clasificar()
print(prueba.forma('./habitacion/elmo.jpg'))
print(prueba.color('./habitacion/elmo.jpg'))
"""
