from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='fuckyousuryank',
            namespace='p1',
            executable='publisher',
            name='publisher'
        ),
        Node(
            package='fuckyousuryank',
            namespace='p2',
            executable='subscriber',
            name='subscriber'
        )
    ])