#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts
import sys

class AddTwoIntClient(Node):

    def __init__(self):
        super().__init__("add_two_ints_client")
        self.client_ = self.create_client(AddTwoInts, "add_two_ints")
        while not self.client_.wait_for_service(1):
            self.get_logger().warn("service not up yet!")
        self.a = int(sys.argv[1])
        self.b = int(sys.argv[2])
        self.send_request()
        

    def send_request(self):
        request = AddTwoInts.Request()
        request.a = self.a
        request.b = self.b
        self.future = self.client_.call_async(request)
        rclpy.spin_until_future_complete(self,self.future)
        sum = self.future.result()
        self.get_logger().info("Result of " + str(self.a) + " + " + str(self.b) + " is " + str(sum.sum))


def main(args=None):
    rclpy.init(args=args)
    node = AddTwoIntClient()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=='__main__':
    main()
