# DCS (Distributed Control System)
The DCS will use the ROS (Robot Operation System) based on Pi to realize the coordination among devives in the system.
ROS Melodic Morenia, Released May, 2018, LTS, supported until May, 2023, Recommended for Ubuntu 18.04

1. Download ubuntu mate 18.04 for Pi3 B  
  goto http://wiki.ros.org/melodic/Installation/Ubuntu

2. Update and upgrade system
  $ sudo apt-get update;
  $ sudo apt-get install ros-melodic-desktop;
  $ sudo rosdep init;
  $ rosdep upgdate;
  $ sudo reboot.

3. Access spyder
  $ sudo apt-get install spyder3;

4. Run ROS
  $ roscore;
  
5. Test ROS
  $ rosrun turlesim turlesim_node;
  $ rosrun turlesim turle_teleop_key.
