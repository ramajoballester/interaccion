#!/usr/bin/env python

import csv
import rospy
import rospkg
from datetime import datetime
from interaccion.msg import *
from interaccion.srv import *
from std_msgs.msg import String, Bool, Empty


class mostrarHandle:
    def __init__(self, path):
        self.path = path # Ruta de los datos
        rospy.init_node('mostrardata_nodo') # Se crea e incia el nodo respectivo
        rospy.Service('mostrardatos', mostrardatos, self.mostrarCallback) # Se crea
        # e inicia el servicio, indicando su numbre, el tipo de servicio que recibe y su callback

    def mostrarCallback(self, e): # Callback del servicio

        rospy.loginfo('Mostrando por pantalla los usuarios guardados')

        file = self.path + '/data/data.csv' # Ruta
        # del archivo
        with open(file, 'rb') as f: # Se abre el archivo en modo lectura
            reader = csv.reader(f)
            lista = list(reader) # Se transforma su constenido en lista

        for line in lista:  # Se muestra por pantalla linea por linea
            print line

        return mostrardatosResponse()


if __name__ == "__main__":
    try:
        rosp = rospkg.RosPack()
        path = rosp.get_path('interaccion') # Ruta del directorio para guardar
        # los datos
        mostrarHandle(path) # Se ejecuta la funcion que contiene el programa principal

        rospy.spin()
    except rospy.ROSInterruptException:
        pass
