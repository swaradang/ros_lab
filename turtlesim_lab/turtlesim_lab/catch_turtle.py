#!/usr/bin/env python3

import rclpy
import rclpy.node as node
import math
from turtlesim.msg import Pose
from turtlesim.srv import Kill
from geometry_msgs.msg import Twist

class CatchTurtle(node.Node):
    def __init__(self):
        super().__init__("catch_turtle")
        self.catch = self.create_subscription(Pose,"new_turtle/pose",self.target,10)
        self.pose = self.create_subscription(Pose,"turtle1/pose",self.move,10)
        self.cmd_vel = self.create_publisher(Twist,"turtle1/cmd_vel",10)
        self.service_client = self.create_client(Kill, 'kill')

        self.x = None
        self.y = None
    
    def target(self,msg):
        self.x = msg.x
        self.y = msg.y

    def despawn_turtle(self):
        while not self.service_client.wait_for_service(timeout_sec=1.0):
            continue

        self.despawn_request = Kill.Request()
        self.despawn_request.name = 'new_turtle'
        future = self.service_client.call_async(self.despawn_request)

    def move(self, msg):
        if self.x is None or self.y is None:
            return
        
        distance = ((self.x - msg.x)**2 + (self.y - msg.y)**2)**0.5
        
        angle_to_goal = math.atan2(self.y - msg.y, self.x - msg.x)
        twist_msg = Twist()
        
        if distance > 0.2:
            twist_msg.linear.x = 2 * distance
            ang_diff = angle_to_goal - msg.theta
            
            # Ensure that angle_difference is within the range of -π to π
            if ang_diff > math.pi:
                ang_diff -= 2 * math.pi
            elif ang_diff < -math.pi:
                ang_diff += 2 * math.pi
                
            twist_msg.angular.z = 6 * ang_diff
        else:
            self.x = None
            self.y = None
            self.despawn_turtle()
            twist_msg.linear.x = 0.0
            twist_msg.angular.z = 0.0
        
        # Perform the necessary action with twist_msg (publishing, etc.)

        self.get_logger().info(f"distance: {distance}")
        self.get_logger().info(f"angle: {angle_to_goal}")
        self.cmd_vel.publish(twist_msg)
        

def main(args = None):
    rclpy.init(args = args)
    node1 = CatchTurtle()
    rclpy.spin(node1)
    rclpy.shutdown()