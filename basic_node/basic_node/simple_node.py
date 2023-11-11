#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

def main(args=None):
    rclpy.init(args=args)
    node = Node("simple_node")
    node.get_logger().info("Info msg")
    node.get_logger().warn("Warning msg")
    node.get_logger().error("Error msg")
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
