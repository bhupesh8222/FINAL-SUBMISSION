#!/usr/bin/env python

import rospy
from geometry_msgs.msg  import Twist
from turtlesim.msg import Pose

#our node
rospy.init_node('node_turtle_revolve', anonymous=True)

pose = Pose()
rate = rospy.Rate(50)

def callback(data):
    global pose
    pose = data
    
#publishing over topic and subscribing to pose.
velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose, callback)

def MakeACircularRound():
        
    radius = 2
    frequency = 0.1
                
    goal_pose = Pose()
    vel_msg = Twist()
    rate.sleep()
    StartTime = float(rospy.Time.now().to_sec())
    distance = 0
        
            
    while (2*3.1416*radius) >= distance and not rospy.is_shutdown():
        
        vel_msg.linear.x = 2*3.1416*frequency*radius
       
        vel_msg.angular.z = 2*3.1416*frequency
        
        FinishTime=float(rospy.Time.now().to_sec())
        
        #distance in circular path = time * speed
        distance = vel_msg.linear.x * (FinishTime-StartTime)

        #publishing our message                        
        velocity_publisher.publish(vel_msg)
        rospy.loginfo("Moving in a circle")
        rate.sleep()
            
        
    vel_msg.linear.x = 0
    vel_msg.angular.z =0
    velocity_publisher.publish(vel_msg)
    rospy.loginfo("Goal reached")

MakeACircularRound()
      
