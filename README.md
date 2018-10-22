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
  _pixy.so
```
if it does nto work, plz also copy the following
```
  pixy.i
  pixy.py
  pixy_python_interface.cpp
  pixy_wrap.cxx
  setup.py
```
After replacing the documents, try the following and it should be workable.

`$ rosrun pixy2_ros pixy2_getlines` and `$ rostopic echo /pixy2lines`

`$ rosrun pixy2_ros pixy2_getblocks` and `$ rostopic echo /pixy2blocks`

If you cannot run this python and get the error **Segmentation fault (core dumped)**, check the pixy2 has been connected and the permission was given or not.

# More about pixy2
Only a few of the function is work in this pixy2_ros as they dows not support python. To find out which function can be run in python, you can look at the **pixy2_ros/src/pixy_python_interface.cpp**. Also, some information were not used in this pixy2_ros and you have to read the reference website to get more information.

## More about pixy2 get lines feature
The reference of this part : https://docs.pixycam.com/wiki/doku.php?id=wiki:v2:line_api

The output of pixy2_getlines
```
> m_xa: 
This variable contains the x location of the tail of the Vector or line. 
The value ranges between 0 and frameWidth

> m_ya:
This variable contains the y location of the tail of the Vector or line. 
The value ranges between 0 and frameWidth

> m_xb:
This variable contains the x location of the head (arrow end) of the Vector or line.
The value ranges between 0 and frameWidth

> m_yb:
This variable contains the y location of the head (arrow end) of the Vector or line. 
The value ranges between 0 and frameWidth   

> m_index:
This variable contains the tracking index of the Vector or line. 
Each line index will be kept for that line until the line either leaves Pixy2's field-of-view,
or Pixy2 can no longer find the line in subsequent frames

> i_index:
This variable contains the tracking index of the line.

> i_angle:
This variable contains the angle in degrees of the line.
```

## More about pixy2 get blocks feature
The reference of this part : https://docs.pixycam.com/wiki/doku.php?id=wiki:v2:ccc_api

The output of pixy2_getblocks
```
> m_signature: 
This variable contains the signature number or color-code number.

> m_x:
This variable contains the x location of the center of the block. 
The value ranges between 0 and frameWidth

> m_y:
This variable contains the y location of the center of the block. 
The value ranges between 0 and frameHeight

> m_width:
This variable contains the width of the block. The value ranges between 0 and frameWidth

> m_height:
This variable contains the height of the block. The value ranges between 0 and frameHeight
```
