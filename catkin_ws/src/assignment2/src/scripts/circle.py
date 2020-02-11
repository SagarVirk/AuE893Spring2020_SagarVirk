#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
PI = 3.1415926535897

def circle():
    # Starts a new node
    rospy.init_node('robot_cleaner', anonymous=True)
    publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

    #Receiveing the user's input
    print("Let's move your robot")
    speed = 3
    distance =13
    radius = (distance-0.8)/(2*PI)
   # isForward = input("Foward?: ")#True or False

    #Checking if the movement is forward or backwards
    #if(isForward):
     #   vel_msg.linear.x = abs(speed)
    #else:
    vel_msg.linear.x = speed
    #Since we are moving just in x-axis
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = speed/radius

     # Setting the current time for distance calculus
    t0 = rospy.Time.now().to_sec()
    current_distance = 0

    #Loop to move the turtle in an specified distance
    while(current_distance < distance):
        #Publish the velocity
        publisher.publish(vel_msg)
        #Takes actual time to velocity calculus
        t1=rospy.Time.now().to_sec()
        #Calculates distancePoseStamped
        current_distance= speed*(t1-t0)
    #After the loop, stops the robot
    vel_msg.linear.x = 0
    vel_msg.angular.z = 0
    #Force the robot to stop
    publisher.publish(vel_msg)

if __name__ == '__main__':
    try:
        #Testing our function
        circle()
    except rospy.ROSInterruptException: pass
