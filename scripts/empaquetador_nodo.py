#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from interaccion.msg import *


class Person:
    def __init__(self):
        # ???
        self.info = inf_personal_usuario()
        self.emocion = ''
        self.posicion = pos_usuario()
        self.usuario_msg = usuario()
        self.reset()

    def callback_pos(self, data):
        self.posicion = data
        print(self.posicion)
        self.posicion_ok = True

    def callback_emocion(self, data):
        self.emocion = data
        print(self.emocion)
        self.emocion_ok = True

    def callback_info(self, data):
        self.info = data
        print(self.info)
        self.info_ok = True

    def reset(self):
        self.info_ok = False
        self.emocion_ok = False
        self.posicion_ok = False


def talker(person):
    pub = rospy.Publisher('user_topic', usuario, queue_size=1)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        if person.info_ok and person.emocion_ok and person.posicion_ok:
            person.usuario_msg.infPersonal = person.info
            person.usuario_msg.emocion = person.emocion.data
            person.usuario_msg.posicion = person.posicion
            pub.publish(person.usuario_msg)
            print(person.usuario_msg)
            person.reset()
        rate.sleep()


def listener(person):
    rospy.Subscriber('pos_usuario_topic', pos_usuario, person.callback_pos)
    rospy.Subscriber('emocion_topic', String, person.callback_emocion)
    rospy.Subscriber('inf_pers_topic', inf_personal_usuario, person.callback_info)



if __name__ == '__main__':
    try:
        rospy.init_node('empaquetador_nodo', anonymous=False)
        person = Person()
        listener(person)
        talker(person)
    except rospy.ROSInterruptException:
        pass
