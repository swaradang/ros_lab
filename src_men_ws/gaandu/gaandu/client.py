#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_srvs.srv import Empty 
import sys

class AddTwoIntClient(Node):

    def __init__(self):
        super().__init__("add_two_ints_client")
        self.client_ = self.create_client(Empty, "reset")
        while not self.client_.wait_for_service(1):
            self.get_logger().warn("service not up yet!")
        self.send_request()
        

    def send_request(self):
        request = Empty.Request()
        self.future = self.client_.call_async(request)
        rclpy.spin_until_future_complete(self,self.future)
        self.get_logger().info("requested reset")


def main(args=None):
    rclpy.init(args=args)
    node = AddTwoIntClient()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=='__main__':
    main()