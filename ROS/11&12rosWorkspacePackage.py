'''

Revisit to understand better, especially workspace

needed to use parallel processing limiter to work on ubuntu dual boot
colcon build --parallel-workers 10
try more than 10
also only build specific things
colcon build --packages-select my_package

how to create a package
ros2 pkg create --build-type ament_python --license Apache-2.0 <package_name>
ex: 
    ros2 pkg create --build-type ament_python --license Apache-2.0 --node-name my_node my_package
'''

