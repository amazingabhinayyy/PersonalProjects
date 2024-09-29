'''
ros2 run rqt_console rqt_console

Fatal messages indicate the system is going to terminate to try to protect itself from detriment.
Error messages indicate significant issues that won’t necessarily damage the system, but are preventing it from functioning properly.
Warn messages indicate unexpected activity or non-ideal results that might represent a deeper issue, but don’t harm functionality outright.
Info messages indicate event and status updates that serve as a visual verification that the system is running as expected.
Debug messages detail the entire step-by-step process of the system execution

set default logger level, noramlly info default
ros2 run turtlesim turtlesim_node --ros-args --log-level WARN

'''