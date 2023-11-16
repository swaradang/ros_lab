#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import transforms3d
import math

class GotoGoalNode(Node):
    def __init__(self):
        super().__init__("move_robot")
        self.target_points = [(3, 0), (0, 3), (-3, 0), (0, -3)]  # Square path points
        self.current_point_index = 0
        self.publisher = self.create_publisher(Twist, "cmd_vel", 10)
        self.subscriber = self.create_subscription(Odometry, "odom", self.control_loop, 10)
        self.target_x, self.target_y = self.target_points[self.current_point_index]

    def control_loop(self, msg):
        dist_x = self.target_x - msg.pose.pose.position.x
        dist_y = self.target_y - msg.pose.pose.position.y
        print('Current position: {} {}'.format(msg.pose.pose.position.x, msg.pose.pose.position.y))
        distance = math.sqrt(dist_x * dist_x + dist_y * dist_y)
        print('Distance to target: {}'.format(round(distance, 3)))

        goal_theta = math.atan2(dist_y, dist_x)
        quat = msg.pose.pose.orientation
        roll, pitch, yaw = transforms3d.euler.quat2euler([quat.w, quat.x, quat.y, quat.z])
        diff = math.pi - round(yaw, 2) + round(goal_theta, 2)
        print('Yaw: {}'.format(round(yaw, 2)))
        print('Target angle: {}'.format(round(goal_theta, 2)))

        if diff > math.pi:
            diff -= 2 * math.pi
        elif diff < -math.pi:
            diff += 2 * math.pi
        print('Orientation difference: {}'.format(round(diff, 2)))

        vel = Twist()

        if abs(diff) > 0.2:
            vel.linear.x = 0.0
            vel.angular.z = 0.4 * round(diff, 2)
        else:
            if abs(distance) > 0.2:
                vel.linear.x = 0.5 * round(distance, 3)
                vel.angular.z = 0.0
            else:
                # Reached target point, update the next target
                self.current_point_index = (self.current_point_index + 1) % len(self.target_points)
                self.target_x, self.target_y = self.target_points[self.current_point_index]
                vel.linear.x = 0.0
                vel.angular.z = 0.0
                print(f"Reached point {self.current_point_index}: {self.target_x}, {self.target_y}")

        print('Speed: {}'.format(vel))
        self.publisher.publish(vel)

def main(args=None):
    rclpy.init(args=args)
    node = GotoGoalNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
