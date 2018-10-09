# ros_pixy2
# Installation
The reference of this part : https://docs.pixycam.com/wiki/doku.php?id=wiki:v2:building_libpixyusb_as_a_python_module_on_linux

Before using the pixy2_ros, you have to install the pixy2.
```
  1. sudo apt-get install swig libusb-1.0-0-dev g++ git
  2. git clone https://github.com/charmedlabs/pixy2.git 
  3. cd pixy2/scripts
  4. ./build_python_demos.sh
```
# Setting up the pixy2_ros
After installation of pixy2, copy the following documents from **pixy2/build/python_demos/** to **pixy2_ros/src** and replace the one in `pixy2_ros/src`
```
  pixy.i
  pixy.py
  _pixy.so
  pixy_python_interface.cpp
  pixy_wrap.cxx
  setup.py
```
After replacing the documents, try the following and it should be workable.

`$ rosrun pixy2_ros pixy2_getlines` or 
`$ rosrun pixy2_ros pixy2_getlines`
