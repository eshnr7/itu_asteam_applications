#!/usr/bin/env python3
import rospy
from turtlesim.msg import Pose
import time

def velocity_msg(velocity_publisher, velocity_goal):
    global current_vel

    loop_rate = rospy.Rate(100)
    velocity_message = Pose()

    while (True):
        K_velocity = 0.5

        error = abs(velocity_goal-current_vel)
        linear_velocity = error*K_velocity
        
        velocity_message.linear_velocity = linear_velocity
        velocity_publisher.publish(velocity_message)

        if error < 0.01:
            break


def pose_callback(pose_message: Pose):
    global current_vel

    current_vel = pose_message.linear_velocity
    


if __name__ == "__main__":
    try:
        rospy.init_node("turtlesim_velocity", anonymous= True)

        cmd_vel_topic = "/turtle1/pose"
        velocity_publisher = rospy.Publisher(cmd_vel_topic, Pose, queue_size=10)

        position_topic = "/turtle1/pose"
        pose_subscriber = rospy.Subscriber(position_topic, Pose, pose_callback)
        time.sleep(2)


        velocity_msg(velocity_publisher, 1)

    except rospy.ROSInterruptException:
        pass