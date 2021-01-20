#!/usr/bin/env python

import rospy
from interaccion.msg import inf_personal_usuario

def talker():
    pub = rospy.Publisher('inf_pers_topic', inf_personal_usuario, queue_size=1) # Se crea e inicia el publicador, indicando el topic, tipo de mensaje, y tamano de cola
    rospy.init_node('informacion_personal_nodo', anonymous=True) # Se crea e incia el nodo respectivo
    rate = rospy.Rate(10) # Se configura la frequencia de ejecucion del bucle, en este caso ajustada a 10 Hz
    info_pers = inf_personal_usuario() # Se crea una variable de tipo inf_personal_usuario, la cual se utilizara para publicar el mensaje


    while not rospy.is_shutdown(): # Bucle de ejecucion
        info_pers.nombre = raw_input("Introduce el nombre del usuario: ") # Se solicita al usuario por terminal la informacion, su entrada se guarda en la variable
        rospy.loginfo("Nombre del usuario: " + info_pers.nombre) # Se muestra por pantalla lo introducido
        info_pers.edad = int(raw_input("Introduce la edad del usuario: ")) # Se solicita al usuario por terminal la informacion, su entrada se convierte en entero y se guarda en la variable
        rospy.loginfo("Edad del usuario: " + str(info_pers.edad)) # Se muestra por pantalla lo introducido
        info_pers.idiomas.append(raw_input("Introduce uno de los idiomas que habla el usuario: ")) # Se solicita al usuario por terminal la informacion, su entrada se suma a la lista de la variable
        rospy.loginfo("idiomas del usuario: " + info_pers.idiomas[0]) # Se muestra por pantalla lo introducido, en este caso el primer elemento de la lista

        acabado = False # Se inicializa un booleano condicional del proximo bucle

        while acabado == False: # Inicio del bucle de adquisicion de idiomas
            id_posible = raw_input("Introduce otro de los idiomas. Si has terminado solo pulsa intro: ") # Se solicita al usuario por terminal un nuevo idioma o, si se diese el caso, la entrada vacia si hubiese terminado
            if id_posible == "": # Se compueba si se ha introducido la linea de caracteres vacia
                acabado = True # Se termina el bucle
            else:
                info_pers.idiomas.append(id_posible) # En caso de haber un nuevo idioma, se anade a la lista
                rospy.loginfo("idiomas del usuario: " + str(info_pers.idiomas[:])) # Se muestran por pantalla los idiomas introducidos


        pub.publish(info_pers) # Se publica el mensaje
        
        info_pers.idiomas = [] # Eliminar idiomas previos

        rate.sleep()

if __name__ == '__main__':
    try:
        talker() # Se ejecuta la funcion que contiene el programa principal
    except rospy.ROSInterruptException:
        pass
