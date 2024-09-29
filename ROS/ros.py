'''
The command ros2 run launches an executable from a package.
Basically creates nodes

ros2 run <package_name> <executable_name>
ex...
    ros2 run turtlesim turtlesim_node
    ros2 run turtlesim turtle_teleop_key

ros2 run turtlesim turtlesim_node --ros-args --remap __node:=my_turtle
- reassigns name of /turtlesim node

To know which nodes are runnning, in another terminal
Need to be running to do it

ros2 node list

Get info from nodes:
ros2 node info <node_name>

in ros2, info goes from publishers to topic to subscribers
rqt_graph - to see interaction btwn nodes and topics make groups 0

ros2 topic list -t - give topics with topic type appended

To see the data being published on a topic, use:
ros2 topic echo <topic_name>
ros2 topic info /turtle1/cmd_vel 
topic info shows type, # publishers, # subscribers

for types can do below command on type to learn its details
ros2 interface show geometry_msgs/msg/Twist


can publish data using, args is actual data, --once is optional, publish once and exit. --rate 1 is 1 hZ
ros2 topic pub <topic_name> <msg_type> '<args>'
ros2 topic pub --once /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 1.8}}"
ros2 topic pub --rate 1 /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 1.8}}"

to put in times, dependent on whether there is a message with stds_msgs/msg/Header
ros2 topic pub /pose geometry_msgs/msg/PoseStamped '{header: "auto", pose: {position: {x: 1.0, y: 2.0, z: 3.0}}}'
ros2 topic pub /reference sensor_msgs/msg/TimeReference '{header: "auto", time_ref: "now", source: "dumy"}'

view rate
ros2 topic hz /turtle1/pose

SERVICES

Call - response model
Tells you all the services available now:
ros2 service list

Type of service:
ros2 service type <service_name>
 ex output
    std_srvs/srv/Empty - Empty means no data when making request or to give for response
ros2 service list -t (see types as well)

Find services of a particular type:
ros2 service find <type_name>
    ex ros2 service find std_srvs/srv/Empty

To call a service from command line need to know structure of input args
    ros2 interface show <type_name>
     ex: ros2 interface show turtlesim/srv/Spawn

ros2 service call <service_name> <service_type> <arguments>
    ex: ros2 service call /clear std_srvs/srv/Empty
    ex: ros2 service call /spawn turtlesim/srv/Spawn "{x: 2, y: 2, theta: 0.2, name: ''}"


































'''