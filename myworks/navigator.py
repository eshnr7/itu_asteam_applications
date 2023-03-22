#!/usr/bin/env python3

#Date       :21.03.23
#@author    :eshnr7(www.github.com/eshnr7)


"""
EN:

    This code is written to publish to '/force_control' topic.
    Please make sure you have 'ros_clients' in dependencies of your ROS Package before running it.
    Be sure the file you will copy this code from is executable.

"""

import rospy
from ros_clients.msg import GeneralizedForce
import os

def force_controller():

    pub = rospy.Publisher('/force_control', GeneralizedForce, queue_size=10)
    rospy.init_node('navigator', anonymous=True)
    
    rate = rospy.Rate(10)
    
    force_messages = GeneralizedForce() 

    while not rospy.is_shutdown():
        
        print('_'*25,"\n")
        print("X: {}, N: {}, Y: {}".format(force_messages.x, force_messages.n, force_messages.y))
        print('_'*25)

        print("\nPress enter after each data entry.")
        print("Press ctrl+c and then enter to stop the program.")
        typing = input("\n\nW: +x\tS: -x\nA: -n\tD: +n\nR: +y\tQ: -y\n\n")
            
        if typing == 'w':
                
            if force_messages.x <= 100 and force_messages.x >= -125:
                force_messages.x += 25

        elif typing == "s":
                
            if force_messages.x <= 125 and force_messages.x >= -100:
                force_messages.x -= 25     
            
        elif typing == "d":
                
            if force_messages.n <= 100 and force_messages.n >= -125:
                force_messages.n += 25             

        elif typing == 'a':

            if force_messages.n <= 125 and force_messages.n >= -100:
                force_messages.n -= 25 
        
        elif typing == 'q':

            if force_messages.y <= 125 and force_messages.y >= -100:
                force_messages.y -= 25        

        elif typing == 'r':

            if force_messages.y <= 125 and force_messages.y >= -100:
                force_messages.y += 25   


        pub.publish(force_messages)
        os.system('clear') # Clear terminal screen after each input
        rate.sleep()

if __name__ == '__main__':
    try:
        force_controller()
    except rospy.signal_shutdown('-'):
        pass
