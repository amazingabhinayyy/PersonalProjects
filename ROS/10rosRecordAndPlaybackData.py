'''

ros2 bag records data published on topics

ros2 bag record <topic_name>
ex: ros2 bag record /turtle1/cmd_vel

This is better:
ros2 bag record -o subset /turtle1/cmd_vel /turtle1/pose
-o let's you choose name
subset is file name
listen to multiple topics by topic space topic

see details by doing
ros2 bag info <bag_file_name>
ex: ros2 bag info subset

can play bag file:
ros2 bag play subset

'''