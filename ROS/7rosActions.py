'''
Actions have a goal, feedback, and result
built on top of services and topics
Similar to services but can be canceled and steady feedback

client-server model, 
action client sends goal to action server 
action server acknowedleges goal, returns stream of feedback and result

In turtlesim when you press a key, sending goal to action server
goal to rotate turtle
message sent
can stop goal by sending f (cancellable)

Look at nodes actions by:
ros2 node info /turtlesim
    under action servers


List actions by:
ros2 action list
ros2 action list -t

Action info:
ros2 action info /turtle1/rotate_absolute

ros2 interface show turtlesim/action/RotateAbsolute
shows the type

send an action goal from command line
ros2 action send_goal <action_name> <action_type> <values>
To see feedback:
ros2 action send_goal /turtle1/rotate_absolute turtlesim/action/RotateAbsolute "{theta: -1.57}" --feedback
'''