import os

from ament_index_python.packages import get_package_share_directory


from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():

    package_name='fivedofarmzup_description'

    sim = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory(package_name),'launch','robot_description.launch.py'
                )])
    )

    rviz2 = Node(
        package= 'rviz2',
        namespace ='',
        executable='rviz2',
        name='rviz2',
    )

    joint = Node(
        package='joint_state_publisher_gui',
        namespace='',
        executable='joint_state_publisher_gui'
    )

    gazebo = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')]),
             )
    
    return LaunchDescription([
        sim,
        joint,
        rviz2,
        gazebo,
        # mapping,
    ])