#!/usr/bin/env python


import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('emocion_topic', String, queue_size=1) #Se crea e inicia el publicador, indicando el topic, tipo de mensaje, y tamano de cola
    rospy.init_node('emocion_usuario_nodo', anonymous=True) # Se crea e incia el nodo respectivo
    rate = rospy.Rate(10) # Se configura la frequencia de ejecucion del bucle, en este caso ajustada a 10 Hz
    emocion = String() # Se crea una variable de String, la cual se utilizara para publicar el mensaje


    while not rospy.is_shutdown(): # Bucle de ejecucion
        emocion = raw_input("Introduce la emocion expresada por el usuario: ") # Se solicita al usuario por terminal la informacion, su entrada se guarda en la variable
        rospy.loginfo("Emocion del usuario: " + emocion) # Se muestra por pantalla lo introducido
        pub.publish(emocion) # Se publica el mensaje


        rate.sleep()

if __name__ == '__main__':
    try:
        talker() # Se ejecuta la funcion que contiene el programa principal
    except rospy.ROSInterruptException:
        pass
