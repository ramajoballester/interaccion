#!/usr/bin/env python

import rospy
from std_msgs.msg import String, Bool
from datetime import datetime

class Reloj:
    def __init__(self):
        self.show_time = False
        self.pub = rospy.Publisher('still_alive', Bool, queue_size=1)
        self.timer = []
        rospy.Subscriber('start_topic', String, self.start_callback)
        rospy.Subscriber('reset_topic', String, self.callback)

    def callback(self, data):
        self.time_ref = rospy.get_time()
        if data.data == 'reset_topic':
            rospy.loginfo('Reset topic')
        if self.timer:
            self.timer.shutdown()
            self.timer = rospy.Timer(rospy.Duration(60), self.timer_callback)
        else:
            self.timer = rospy.Timer(rospy.Duration(60), self.timer_callback)

    def start_callback(self, data):
        self.show_time = True
        self.time_ref = rospy.get_time()
        rospy.loginfo('Start topic')
        self.callback(data)

    def timer_callback(self, data):
        self.pub.publish(True)
        rospy.loginfo('Still alive')



if __name__ == '__main__':
    try:
        rospy.init_node('reloj_nodo', anonymous=False)
        reloj = Reloj()
        rate = rospy.Rate(3.0)
        while not rospy.is_shutdown():
            if reloj.show_time:
                print(' ')
                print('Local Time: ' + str(datetime.now()))
                print('UTC Time: ' + str(datetime.utcnow()))
                print('Elapsed time from start/reset: ' +
                        str(rospy.get_time() - reloj.time_ref))
            rate.sleep()

    except rospy.ROSInterruptException:
        pass
