#!/usr/bin/env python3

#Date: 22.01.23
#@author: Enes Sahiner (eshnr7)
#source code: www.github.com/aniskoubaa/ros_essentials_cpp/blob/master/src/topic02_motion/turtlesim/turtlesim_cleaner.py

#TR:
#Turtlesim’in doğrusal hızını kontrol eden bir node yazınız.

#EN:
#Write a node that controls the linear speed of Turtlesim.


import rospy
import time
from geometry_msgs.msg import Twist


def control_speed(speed):

        velocity_message = Twist()
        velocity_message.linear.x = speed


        loop_rate = rospy.Rate(10)    
        cmd_vel_topic='/turtle1/cmd_vel'
        velocity_publisher = rospy.Publisher(cmd_vel_topic, Twist, queue_size=10)

        while True :
                rospy.loginfo("Turtlesim moves forwards")
                velocity_publisher.publish(velocity_message)

                loop_rate.sleep()
                

if __name__ == '__main__':
    try:
        
        rospy.init_node('turtlesim_motion_pose', anonymous=True)

        cmd_vel_topic='/turtle1/cmd_vel'
        velocity_publisher = rospy.Publisher(cmd_vel_topic, Twist, queue_size=10)
        
        position_topic = "/turtle1/pose" 
        time.sleep(2)

        control_speed(1.0) #control speed
       
    except rospy.ROSInterruptException:
        rospy.loginfo("node terminated.")