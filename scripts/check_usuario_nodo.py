#!/usr/bin/env python

import csv
import rospy
import rospkg
import roslaunch
from interaccion.msg import *
from std_msgs.msg import String, Bool, Empty


class SecurityCheck:
    def __init__(self, path):
        self.path = path # Ruta de los datos
        self.running = False
        self.update_node = False
        self.launch = roslaunch.scriptapi.ROSLaunch()
        self.launch.start()
        self.robot_node = roslaunch.core.Node('robotics', 'auctioneer.py',
                            name = 'auctioneer', launch_prefix = 'xterm -e')
        rospy.init_node('check_usuario') # Se crea e inicia el nodo
        rospy.Subscriber('user_topic', usuario, self.checkCallback) # Se crea
        # e inicia el suscriptor, indicando el topic, tipo de mensaje, y su
        # callback

    def checkCallback(self, usuario): # Callback del servicio
        rospy.loginfo('Comprobando la identidad del usuario')

        file = self.path + '/data/data.csv' # Ruta
        # del archivo
        with open(file, 'rb') as f: # Se abre el archivo en modo lectura
            reader = csv.reader(f)
            lista = list(reader) # Se transforma su constenido en lista

        for line in lista:  # Se muestra por pantalla linea por linea
            if line[0] != 'Fecha y hora':
                check = (usuario.infPersonal.nombre == line[1] and
                        usuario.infPersonal.edad == int(line[2]) and
                        usuario.emocion == line[4] and
                        usuario.posicion.x == int(line[5]) and
                        usuario.posicion.y == int(line[6]) and
                        usuario.posicion.z == int(line[7]))

                if check:
                    print('Usuario certificado')
                    print(' ')

                    if not self.running:
                        print('Inicio de sistema multi-robot')
                        self.update_node = True
                    else:
                        print('Parada de sistema multi-robot')
                        self.update_node = True




if __name__ == "__main__":
    try:
        rosp = rospkg.RosPack()
        path = rosp.get_path('interaccion') # Ruta del directorio para guardar
        # los datos
        sec_check = SecurityCheck(path)
        rate = rospy.Rate(10.0)
        while not rospy.is_shutdown():
            if sec_check.update_node:
                if not sec_check.running:
                    process = sec_check.launch.launch(sec_check.robot_node)
                    sec_check.running = True
                else:
                    process.stop()
                    sec_check.running = False
                sec_check.update_node = False
            rate.sleep()

    except rospy.ROSInterruptException:
        pass
