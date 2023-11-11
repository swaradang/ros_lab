from setuptools import find_packages, setup

package_name = 'turtlesim_lab'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='swaraj',
    maintainer_email='swaraj@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "gotogoal = turtlesim_lab.gotogoal:main",
            'spawn_turtle = turtlesim_lab.spawn_turtle:main',
            'catch_turtle = turtlesim_lab.catch_turtle:main'
        ],
    },
)
