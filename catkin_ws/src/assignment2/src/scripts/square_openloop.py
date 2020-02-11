#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
PI = 3.1415926535897

def square_openloop():
    # Starts a new node
    rospy.init_node('robot_cleaner', anonymous=True)
    publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

    #Receiveing the user's input
    print("Let's move your robot")
    speed = 0.2
    side_len = 2
    angular_s = 0.2

    count = 1
    while (count < 5):

        vel_msg.linear.x = speed
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 0

             # Setting the current time for distance calculus
        t0 = rospy.Time.now().to_sec()
        current_distance = 0

        #Loop to move the turtle in an specified distance
        while(current_distance < side_len):
            publisher.publish(vel_msg)
            t1=rospy.Time.now().to_sec()
            current_distance = speed*(t1-t0)
        #After the loop, stops the robot
        vel_msg.linear.x = 0
        vel_msg.angular.z = angular_s
        #Force the robot to stop

        t2 = rospy.Time.now().to_sec()
        current_angle = 0

        while(current_angle < (PI/2)):
            publisher.publish(vel_msg)
            t3=rospy.Time.now().to_sec()
            current_angle = angular_s*(t3-t2)
        #After the loop, stops the robot
        vel_msg.angular.z = 0
        #Force the robot to stop
        count = count + 1
    publisher.publish(vel_msg)

if __name__ == '__main__':
    try:
        #Testing our function
        square_openloop()
    except rospy.ROSInterruptException: pass
