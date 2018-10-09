#!/usr/bin/env python

import rospy
import pixy
from ctypes import *
from pixy import *
from pixy2_ros.msg import pixy2lines

# pixy2 Python SWIG get line features example #

## pixy2 lines api : https://docs.pixycam.com/wiki/doku.php?id=wiki:v2:line_api

print ("Pixy2 Python SWIG Example -- Get Line Features")

pixy.init ()
pixy.change_prog ("line")

rospy.init_node("pixy2_getlines")
pixy2lines_pub = rospy.Publisher("pixy2lines", pixy2lines, queue_size=1)
pixy2lines_msg = pixy2lines()

class Vector (Structure):
  _fields_ = [
    #This variable contains the x location of the tail of the Vector or line. The value ranges between 0 and frameWidth (79)
    ("m_x0", c_uint),
	#This variable contains the y location of the tail of the Vector or line. The value ranges between 0 and frameWidth (52)    
	("m_y0", c_uint),
	#This variable contains the x location of the head (arrow end) of the Vector or line. The value ranges between 0 and frameWidth
    ("m_x1", c_uint),
	#This variable contains the y location of the head (arrow end) of the Vector or line. The value ranges between 0 and frameWidth   
	("m_y1", c_uint),
	#This variable contains the tracking index of the Vector or line. 
    #Each line index will be kept for that line until the line either leaves Pixy2's field-of-view, or Pixy2 can no longer find the line in subsequent frames
    ("m_index", c_uint),
	#LINE_FLAG_INTERSECTION_PRESENT: This flag is only available if getMainFeatures() is called and the Vector is provided.
    #This flag indicates that an intersection was detected but may not have met the filtering constraint.
	#LINE_FLAG_INVALID: This flag is only available if getAllFeatures() is called.
	#This flag indicates that the line has been detected but has not met the filtering constraint.
	("m_flags", c_uint) ]

class IntersectionLine (Structure):
  _fields_ = [
	#This variable contains the tracking index of the line. 
    ("m_index", c_uint),
	#This variable contains the angle in degrees of the line.
    ("m_reserved", c_uint),
    ("m_angle", c_uint) ]

vectors = VectorArray(100)
intersections = IntersectionLineArray(100)
frame = 0

while not rospy.is_shutdown():

  #getMainFeatures() tries to send only the most relevant information
  #getMainFeatures()'s best to keep your program simple, and it does a pretty good job
  #line_get_main_features ()
  #Choose one from line_get_main_features () and getAllFeatures(), but not both
  #getAllFeatures() function is for more advanced programs and applications
  line_get_all_features ()

  i_count = line_get_intersections (100, intersections)
  v_count = line_get_vectors (100, vectors)

  if i_count > 0 or v_count > 0:
    print 'frame %3d:' % (frame)
    frame = frame + 1
    for index in range (0, i_count):
      print '[INTERSECTION: INDEX=%d ANGLE=%d]' % (intersections[index].m_index, intersections[index].m_angle)
      pixy2lines_msg.i_index = intersections[index].m_index
      pixy2lines_msg.i_angle = intersections[index].m_angle
    for index in range (0, v_count):
      print '[VECTOR: INDEX=%d X0=%3d Y0=%3d X1=%3d Y1=%3d]' % (vectors[index].m_index, vectors[index].m_x0, vectors[index].m_y0, 
                                                                  vectors[index].m_x1, vectors[index].m_y1)
      pixy2lines_msg.m_index = vectors[index].m_index
      pixy2lines_msg.m_xa = vectors[index].m_x0
      pixy2lines_msg.m_ya = vectors[index].m_y0
      pixy2lines_msg.m_xb = vectors[index].m_x1
      pixy2lines_msg.m_yb = vectors[index].m_y1
    pixy2lines_pub.publish(pixy2lines_msg)
