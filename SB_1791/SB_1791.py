#!/usr/bin/env python

import rospy
from geometry_msgs.msg  import Twist
from turtlesim.msg import Pose

#initializing the node "node_turtle_revolve"
rospy.init_node('node_turtle_revolve', anonymous=True)

pose = Pose()
rate = rospy.Rate(50)

#callback function of subscriber node
def callback(data):
    global pose
    pose = data
    
#our node is publishing to topic "/turtle/cmd/cmd_vel" topic of type Twist
velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

#also our node has subscribed to topic "/turtle/pose" of type Pose
pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose, callback)

def MakeACircularRound():
        
    radius = 2
    frequency = 0.1
                
    goal_pose = Pose()
    vel_msg = Twist()
    #time will help to check whether one revolution has completed or not
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
            
    #when one round has completed the angular speed is made 0 to stop the turtle   
    vel_msg.linear.x = 0
    vel_msg.angular.z =0
    velocity_publisher.publish(vel_msg)
    rospy.loginfo("Goal reached")

if __name__ == '__main__':
    try:
        MakeACircularRound()
    except rospy.ROSInterruptException:
        pass



      
