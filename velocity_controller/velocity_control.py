#!/usr/bin/env python3

# Date       :26.03.23
# Author     :eshnr7(www.github.com/eshnr7)


import rospy
from geometry_msgs.msg import TwistStamped
from ros_clients.msg import GeneralizedForce
import time

x = 0
y = 0
n = 0

def velocity_goal(xi, yj, nb):
    global x, y, n

    force_msg = GeneralizedForce()
    while not rospy.is_shutdown():
        error_x = xi - x
        error_y = yj - y
        error_n = nb - n
        proportional = 5
        force_i = proportional * error_x
        force_j = proportional * error_y
        force_b = proportional * error_n

        force_msg.x = force_i
        force_msg.y = force_j
        force_msg.n = force_b

        pub.publish(force_msg)
        rate.sleep()

def callback(data:TwistStamped):
    global x, y, n
    x = data.twist.linear.x
    y = data.twist.linear.y
    n = data.twist.angular.z

if __name__ == '__main__':
    try:
        rospy.init_node('speed_control', anonymous=True)
        pub = rospy.Publisher("/force_control", GeneralizedForce, queue_size=10)
        sub = rospy.Subscriber("/nav/twist", TwistStamped, callback)
        rate = rospy.Rate(10)
        velocity_goal(0.0, 0.0, 0.0)

    except rospy.ROSInterruptException:
        pass
