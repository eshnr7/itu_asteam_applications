#!/usr/bin/env python3

# Date       :8.4.23
# Author     :eshnr7(www.github.com/eshnr7)

#Note: The coefficients KP, Ki, Kd are not suitable for the x and y directions!!!
# one day i will work on them

import rospy
from geometry_msgs.msg import TwistStamped
from ros_clients.msg import GeneralizedForce

x = 0
y = 0
n = 0

integral_x = 0
integral_y = 0
integral_n = 0

last_error_x = 0
last_error_y = 0
last_error_n = 0

dt= 0.1

def callback(data:TwistStamped):
   
    global x, y, n
    x = data.twist.linear.x
    y = data.twist.linear.y
    n = data.twist.angular.z

def pid_control(error, last_error, integral, Kp, Ki, Kd):
  
    proportional = Kp * error
    integral += error*dt
    derivative = Kd * (error - last_error)/dt
    output = proportional + Ki * integral + derivative
    last_error = error
    return output, last_error, integral

def velocity_goal(xi, yj, nb):
  
    global x, y, n
    global integral_x, integral_y, integral_n
    global last_error_x, last_error_y, last_error_n

    Kp = 100
    Ki = 50
    Kd = 50

    force_msg = GeneralizedForce()

    while not rospy.is_shutdown():

        error_x = xi - x
        error_y = yj - y
        error_n = nb - n
        
        force_i, last_error_x, integral_x = pid_control(error_x, last_error_x, integral_x, Kp, Ki, Kd)
        force_j, last_error_y, integral_y = pid_control(error_y, last_error_y, integral_y, Kp, Ki, Kd)
        force_b, last_error_n, integral_n = pid_control(error_n, last_error_n, integral_n, Kp, Ki, Kd)

        force_msg.x = force_i
        force_msg.y = force_j
        force_msg.n = force_b

        pub.publish(force_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        rospy.init_node('speed_control', anonymous=True)
        pub = rospy.Publisher("/force_control", GeneralizedForce, queue_size=10)
        sub = rospy.Subscriber("/nav/twist", TwistStamped, callback)
        rate = rospy.Rate(10)
        velocity_goal(0.0, 0.0, 0.01)

    except rospy.ROSInterruptException:
        pass
