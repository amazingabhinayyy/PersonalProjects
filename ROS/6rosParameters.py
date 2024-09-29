'''
Can see param list by doing
ros2 param list
    shows you the param list for nodes teleop_turtle and turtlesim

Get parameter type by doing
ros2 param get <node_name> <parameter_name>

Set a parameter value by doing
ros2 param set <node_name> <parameter_name> <value>

View all params for a node doing:
ros2 param dump <node_name>

Load params:
ros2 param load <node_name> <parameter_file>

start a node with param values:
ros2 run <package_name> <executable_name> --ros-args --params-file <file_name>
'''