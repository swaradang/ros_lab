#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
from std_srvs.srv import Empty

class MyPublisher(Node):

    def __init__(self):
        super().__init__("publisher_node")
        self.publishers_ = self.create_publisher(String,"menwillbemen",10)
        self.timer = self.create_timer(0.5, self.timer_callback)
        self.get_logger().info("publisher node started")
        self.counter_ = 0
        self.server_ = self.create_service( Empty , "reset",self.callback)
        self.get_logger().info("Reset server started")

    def callback(self, request , response):
        self.counter_ = 0
        return response
        

    def timer_callback(self):
        self.counter_ += 1
        msg = String()
        msg.data = "Counter: " + str(self.counter_)
        self.get_logger().info(msg.data)
        self.publishers_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = MyPublisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=='__main__':
    main()