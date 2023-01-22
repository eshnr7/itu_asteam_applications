#!/usr/bin/env python3
#Date: 19.01.23
#@author: Enes Sahiner (eshnr7)

#TR:
#Turtlesim’in hareket halindeki doğrusal hızını 
#ve baktığı yönü (derece cinsinden) içeren bir
#mesaj tipi oluşturun ve bunu bir topic üzerinden yayınlayın.

#EN:
#Create a message type containing Turtlesim speed in motion 
#and the orientation (in degrees)
#and publish it on a topic.

import rospy
from turtlesim.msg import Pose
import math
#imported a message class created under workspace before
from asteam_uygulamalar.msg import speed_and_or

#defined orientation and speed variable at global as a float
orientation = float() 
speed = float()

   
def callback(message: Pose):
    global orientation 
    global speed
    orientation = message.theta*(180/math.pi) #radian to degree
    speed = message.linear_velocity


def publisher():
    rospy.Subscriber("/turtle1/pose", Pose, callback)
    pub = rospy.Publisher("/orientation", speed_and_or, queue_size= 10)
    rospy.init_node("orientation", anonymous= True)
    rate = rospy.Rate(10)
    
    while not rospy.is_shutdown():
        speed_and_oriantation = speed_and_or()
        speed_and_oriantation.id = 1
        speed_and_oriantation.name = "Turtlesim's speed and orientation"
        speed_and_oriantation.speed = speed
        speed_and_oriantation.orientation = orientation
        rospy.loginfo("Now, you see the speed and orientation of the turtlesim!")
        rospy.loginfo(speed_and_oriantation)
        pub.publish(speed_and_oriantation)
        rate.sleep()

if __name__ == "__main__":
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass