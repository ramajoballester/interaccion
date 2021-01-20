#!/usr/bin/env python

import rospy
from interaccion.msg import pos_usuario

def talker():
    pub = rospy.Publisher('pos_usuario_topic', pos_usuario, queue_size=1) #Se crea e inicia el publicador, indicando el topic, tipo de mensaje, y tamano de cola
    rospy.init_node('posicion_usuario_nodo', anonymous=True) # Se crea e inicia el nodo respectivo
    rate = rospy.Rate(10) # Se configura la frequencia de ejecucion del bucle, en este caso ajustada a 10 Hz
    pos = pos_usuario() # Se crea una variable de tipo inf_personal_usuario, la cual se utilizara para publicar el mensaje


    while not rospy.is_shutdown(): # Bucle de ejecucion
        pos.x = int(raw_input("Introduce la coordenada X de la posicion: ")) # Se solicita al usuario por terminal la informacion, su entrada se convierte en entero y se guarda en la variable
        rospy.loginfo("Coordenada X: " + str(pos.x)) # Se muestra por pantalla lo introducido
        pos.y = int(raw_input("Introduce la coordenada Y de la posicion: ")) # Se solicita al usuario por terminal la informacion, su entrada se convierte en entero y se guarda en la variable
        rospy.loginfo("Coordenada Y: " + str(pos.y)) # Se muestra por pantalla lo introducido
        pos.z = int(raw_input("Introduce la coordenada Z de la posicion: ")) # Se solicita al usuario por terminal la informacion, su entrada se convierte en entero y se guarda en la variable
        rospy.loginfo("Coordenada Z: " + str(pos.z)) # Se muestra por pantalla lo introducido

        pub.publish(pos) # Se publica el mensaje
        
        rate.sleep()

if __name__ == '__main__':
    try:
        talker() # Se ejecuta la funcion que contiene el programa principal
    except rospy.ROSInterruptException:
        pass
