#!/usr/bin/env python
# encoding: utf-8
import rospy
from std_msgs.msg import String, Bool
from interaccion.msg import *
from interaccion.srv import *
from espeak import espeak


class DialogoHandle:
    def __init__(self):
        self.first_loop = True
        rospy.init_node('dialogo_nodo')
        self.start_pub = rospy.Publisher('start_topic', String, queue_size=1)
        self.reset_pub = rospy.Publisher('reset_topic', String, queue_size=1)
        self.data_pub  = rospy.Publisher('data_topic', usuario, queue_size=1)
        rospy.Subscriber('user_topic', usuario, self.callback)
        rospy.Subscriber('still_alive', Bool, self.timer_callback)

    def callback(self, data):

        self.data_pub.publish(data)

        print(' ')
        print('Información personal')
        espeak.synth('Información personal')
        print(' - Nombre: ' + str(data.infPersonal.nombre))
        espeak.synth('Nombre: ' + str(data.infPersonal.nombre))
        print(' - Edad: ' + str(data.infPersonal.edad))
        espeak.synth('Edad: ' + str(data.infPersonal.edad))
        if data.infPersonal.idiomas:
            for i in range(len(data.infPersonal.idiomas)):
                print(' - Idioma ' + str(i+1) + ': ' + str(data.infPersonal.idiomas[i]))
                espeak.synth('Idioma ' + str(i+1) + ': ' + str(data.infPersonal.idiomas[i]))
                
        else:
            print(' Idiomas: ninguno')
            espeak.synth('Idiomas: ninguno')

        print('Emoción: ' + str(data.emocion))
        espeak.synth('Emoción: ' + str(data.emocion))
        print('Posición')
        espeak.synth('Posición')
        print(' - x: ' + str(data.posicion.x))
        espeak.synth('x: ' + str(data.posicion.x))
        print(' - y: ' + str(data.posicion.y))
        espeak.synth('y: ' + str(data.posicion.y))
        print(' - z: ' + str(data.posicion.z))
        espeak.synth('z: ' + str(data.posicion.z))


        rospy.wait_for_service('multiplicador')
        try:
            mult_srv = rospy.ServiceProxy('multiplicador', multiplicador)
            resp = mult_srv(data.infPersonal.edad)
            print(' ')
            print('Respuesta del servidor. Edad: ' + str(resp))
        except rospy.ServiceException, e:
            print "Service call failed: %s"%e

        if self.first_loop:
            self.start_pub.publish('start_topic')
            self.first_loop = False
        else:
            self.reset_pub.publish('reset_topic')


    def timer_callback(self, data):
        if data.data == True:
            rospy.loginfo('Clock node is still alive')




if __name__ == "__main__":
    try:
        handle = DialogoHandle()
        espeak.set_voice("es") # Configuración del idioma del sintetizador
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
