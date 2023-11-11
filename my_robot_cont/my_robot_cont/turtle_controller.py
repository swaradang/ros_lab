#! /usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from math import radians, pi


class Turtlecontroller(Node):   
    
    def __init__(self):
        super().__init__("turtle_controller")
        self.cmd_vel_pub=self.create_publisher(
            Twist,"/turtle1/cmd_vel",10)
        self.pose_subscriber_=self.create_subscription(
            Pose,"/turtle1/pose",self.pose_callback,10)

    def pose_callback(self, pose: Pose):
        cmd=Twist()
        
        if((pose.x==7.5 and pose.theta==(22/15))or
           (pose.y==7.5 and pose.theta==(45.5/15))or
           (pose.x==5.5 and pose.y==7.5 and pose.theta==(-(66/14)/3))or
           (pose.x==5.5 and pose.y==5.5 and pose.y==7.5 and pose.theta==(90/14))):
            cmd.linear.x=0.0
            cmd.angular.z=1.0
        else:
            cmd.linear.x=1.0

        self.cmd_vel_pub.publish(cmd)

def main():
    rclpy.init()
    node=Turtlecontroller()
    rclpy.spin(node)
    rclpy.shutdown()
