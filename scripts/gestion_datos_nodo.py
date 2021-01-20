#!/usr/bin/env python

import csv
import rospy
import rospkg
from datetime import datetime
from interaccion.msg import *
from interaccion.srv import *
from std_msgs.msg import String, Bool, Empty


class GestionHandle:
    def __init__(self, path):
        self.data_path = path
        rospy.init_node('data_nodo') # Se crea e inicia el nodo respectivo
        rospy.Subscriber('data_topic', usuario, self.dataCallback) # Se crea
        # e inicia el suscriptor, indicando el topic, tipo de mensaje, y su
        # callback

        rospy.loginfo('Preparado para recibir datos')

    def dataCallback(self, data): # Callback del suscriptor
        rospy.loginfo('Informacion recibida, gestionando los datos')

        file = self.data_path + '/data/data.csv' # Ruta del archivo

        with open(file, mode='a') as data_file: # Se abre el archivo de datos
            data_writer = csv.writer(data_file, delimiter=',', quotechar='"',
                                        quoting=csv.QUOTE_MINIMAL)

            now = datetime.now() # Se obtiene la fecha y hora actual para
            # almacenarla
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S") # Se formatea
            # Se escribe una nueva fila en el archivo incluyendo, fecha y hora
            # seguida de los datos recibidos
            data_writer.writerow([dt_string, data.infPersonal.nombre,
                                    data.infPersonal.edad,
                                    data.infPersonal.idiomas[:],
                                    data.emocion,data.posicion.x,
                                    data.posicion.y,data.posicion.z])


        rospy.loginfo('Informacion correctamente guardada')


        rospy.wait_for_service('mostrardatos')
        try:
            mostrar_srv = rospy.ServiceProxy('mostrardatos', mostrardatos)
            print(' ')
            mostrar_srv() # Se realiza un call al servicio para mostrar los
            # datos una vez se ha actualizado la tabla


        except rospy.ServiceException, e:
            print "Service call failed: %s" %e



if __name__ == "__main__":
    try:
        rosp = rospkg.RosPack()
        path = rosp.get_path('interaccion')
        handle = GestionHandle(path) # Se ejecuta la
        # funcion que contiene el programa principal

        rospy.spin()
    except rospy.ROSInterruptException:
        pass
