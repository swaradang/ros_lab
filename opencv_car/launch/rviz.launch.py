import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
def generate_launch_description():
    package_dir = '/home/swaraj/ros2_lab/src/opencv_car/urdf'
    urdf = os.path.join(package_dir,'car.urdf')
    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            arguments=[urdf]),
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            name='joint_state_publisher_gui',
            arguments=[urdf]),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen'),
        ])