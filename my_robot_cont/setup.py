from setuptools import setup

package_name = 'my_robot_cont'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ubuntu',
    maintainer_email='ubuntu@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "test_node = my_robot_cont.node1:main",
            "draw_circle=my_robot_cont.draw_circle:main",
            "draw_square=my_robot_cont.draw_square:main",
            "turtle_controller=my_robot_cont.turtle_controller:main"
        ],
    },
)
