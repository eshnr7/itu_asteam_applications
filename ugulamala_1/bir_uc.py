#!/usr/bin/env python3
#Date: 22.01.23
#@author: Enes Sahiner (eshnr7)
#source code [0]: www.github.com/aniskoubaa/ros_essentials_cpp/blob/master/src/topic02_motion/turtlesim/turtlesim_cleaner.py
#source code [1]: www.wiki.ros.org/turtlesim/Tutorials/Go%20to%20Goal

#TR:
#Turtlesim’in pozisyonunu kontrol eden bir node yazınız.

#EN:
#Write a node that controls position of Turtlesim.

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
import time

def goal_position(x_goal, y_goal):
    global x
    global y
    global orientation

    velocity_message = Twist() #to set new speeds. 
    #If it is 'Pose()' instead of 'Twist()', you cannot change anything

    while (True):
        K_linear = 0.5 
        euclidean_distance = abs(math.sqrt(((x_goal-x) ** 2) + ((y_goal-y) ** 2))) #distance calculation

        linear_speed = euclidean_distance * K_linear #more distance more linear speed

        K_angular = 4.0
        goal_angle = math.atan2(y_goal-y, x_goal-x)
        angular_speed = (goal_angle-orientation)*K_angular

        velocity_message.linear.x = linear_speed # new linear speed
        velocity_message.angular.z = angular_speed #new angular speed

        velocity_publisher.publish(velocity_message) #new angular and linear speed are published

        if euclidean_distance <0.02: #tolerance
            print("You have reached the position!")
            break

def callback(pose_message:Pose):
    global x
    global y
    global orientation
    
    x= pose_message.x
    y= pose_message.y
    orientation = pose_message.theta


if __name__ == '__main__':
    try:
        
        rospy.init_node('turtlesim_control_position', anonymous=True)

        #declare velocity publisher
        cmd_vel_topic='/turtle1/cmd_vel'
        velocity_publisher = rospy.Publisher(cmd_vel_topic, Twist, queue_size=10)

        pose_subscriber = rospy.Subscriber("/turtle1/pose", Pose, callback) 

        time.sleep(2)

        goal_position(10.0, 1.0) #control position
       
    except rospy.ROSInterruptException:
        pass