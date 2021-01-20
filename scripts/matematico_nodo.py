#!/usr/bin/env python

from interaccion.srv import multiplicador,multiplicadorResponse
import rospy

def multiplica(req): #
    print("Devolviendo [%s * 2 = %s]"%(req.entrada, req.entrada * 2)) # Cuando
    # el servicio es llamado, se duplica el entero introducido
    return multiplicadorResponse(req.entrada * 2)

def multiplicador_server():
    rospy.init_node('matematico_nodo') # Se crea e inicia el nodo respectivo
    s = rospy.Service('multiplicador', multiplicador, multiplica) # Se crea e
    # inicia el servicio multiplicador, el cual utiliza el servicio
    # creado 'muliplicador', el callback llamado 'multiplica'
    print("Preparado para recibir numeros.")

    rospy.spin()

if __name__ == '__main__':
    try:
        multiplicador_server() # Se ejecuta la funcion que contiene el
        # programa principal
    except rospy.ROSInterruptException:
        pass
