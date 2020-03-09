import sys
import os
from tensorflow.python.keras.preprocessing.image import ImageDataGenerator
from tensorflow.python.keras import optimizers
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dropout, Flatten, Dense, Activation
from tensorflow.python.keras.layers import  Convolution2D, MaxPooling2D
from tensorflow.python.keras import backend as k


# Elimina seciones de keras activas
k.clear_session()

# Directorio de imagenes para entrenar y validar
data_entrenamiento = './data/entrenamiento'
data_validacion = './data/validacion'

# Inicio Parametros
# Nro de veces a iterar los datos durante el entrenamiento
epocas = 20

# Tamaño en el que se procesara las imagenes
altura, longitud = 100, 100

# Nro de imagenes a procesar en cada uno de los pasos
batch_size = 30

# Nro de veces que se procesa la informacion en cada epoca
pasos = 1000

# Al final de la epoca se corre 200 pasos con el set de datos de validacion
pasos_validacion = 200

# Nro de filtros en cada convolcion (profundidad)
filtrosConv1 = 32
filtrosConv2 = 64

# Tamaño filtro a usar en convulcion altura, longitud
tamano_filtro1 = (3, 3)
tamano_filtro2 = (2 , 2)

# Tamaño de filtro a usar en max pooling
tamano_pool = (2, 2)

# Existe dos clases Irregular y Regular
clases = 2

# Learning Grade
lr = 0.0005
# Fin parametros

# Pre procesamiento de imagenes

entrenamiento_datagen = ImageDataGenerator(
    rescale=1. / 255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True)

validacion_datagen=ImageDataGenerator(rescale=1. / 255)

# Ingresa a la ruta data_entrenamiento abre todas las carpetas y las procesa
imagen_entrenamiento = entrenamiento_datagen.flow_from_directory(
    data_entrenamiento,
    target_size=(altura, longitud),
    batch_size=batch_size,
    class_mode='categorical')

imagen_validacion = validacion_datagen.flow_from_directory(
    data_validacion,
    target_size=(altura, longitud),
    batch_size=batch_size,
    class_mode='categorical')

# imagen_entrenamiento y imagen_validacion ya tienen las imagenes para entrenar la red neuronal
# Crear la red convolucional cnn

# La red neuronal es sequencial
cnn = Sequential()

# Primera capa convolucional
cnn.add(Convolution2D(filtrosConv1, tamano_filtro1, padding='same', input_shape=(altura, longitud, 3), activation='relu'))

# Añadimos una capa pooling
cnn.add(MaxPooling2D(pool_size=tamano_pool))

# Capa convolucional
cnn.add(Convolution2D(filtrosConv2, tamano_filtro2, padding='same', activation='relu'))
# Añadimos una capa pooling
cnn.add(MaxPooling2D(pool_size=tamano_pool))

# Iniciar clasificacion
#La imagen se vuelve plana 1 dimension que contiene la informacion de la red neuronal
cnn.add(Flatten())

# Capa que almacena todas las neuronas en total 256
cnn.add(Dense(256, activation='relu'))

# A la capa le apaga el 50% de neuronas para aprender caminos alternos
cnn.add(Dropout(0.5))

# Ultima capa solo tiene 2 neuronas e indica en porcentajes la clasificacion correcta
cnn.add(Dense(clases, activation='softmax'))

# Mide que tan bien va aprendiendo, va a optimizarse con Adam y la metrica es el porcentaje de que tan bien aprende la red neuronal
cnn.compile(loss='categorical_crossentropy', optimizers=optimizers.Adam(lr=lr), metrics=['accuracy'])

# Corre mil pasos en cada una de las epocas cuando termina corre 200 pasos de validacion y luego pasa a la otra epoca
cnn.fit_generator(imagen_entrenamiento, steps_per_epoch=pasos, epochs=epocas, validation_data=imagen_validacion, validation_steps=pasos_validacion)

# Generar modelo
# Busca la carpeta modelo si no existe la crea
dir = './modelo/'
if not os.path.exists(dir):
    os.mkdir(dir)

# Almacenar el modelo y pesos de las capas
cnn.save('./modelo/modelo.h5')
cnn.save_weights('./modelo/pesos.h5')

