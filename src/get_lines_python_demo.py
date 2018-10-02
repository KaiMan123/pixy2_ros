#!/usr/bin/env python

import rospy
import pixy
from ctypes import *
from pixy import *
from ros_pixy.msg import pixyData
# pixy2 Python SWIG get line features example #

print ("Pixy2 Python SWIG Example -- Get Line Features")

pixy.init ()
pixy.change_prog ("line")
rospy.init_node("pixy2_getlines")
pixy_pub = rospy.Publisher("pixyData",pixyData, queue_size=1)
pixyData_msg = pixyData()

class Vector (Structure):
  _fields_ = [
    ("m_x0", c_uint),
    ("m_y0", c_uint),
    ("m_x1", c_uint),
    ("m_y1", c_uint),
    ("m_index", c_uint),
    ("m_flags", c_uint) ]

class IntersectionLine (Structure):
  _fields_ = [
    ("m_index", c_uint),
    ("m_reserved", c_uint),
    ("m_angle", c_uint) ]

vectors = VectorArray(100)
intersections = IntersectionLineArray(100)
frame = 0

while not rospy.is_shutdown():
  line_get_main_features ()
  i_count = line_get_intersections (100, intersections)
  v_count = line_get_vectors (100, vectors)

  if i_count > 0 or v_count > 0:
    print 'frame %3d:' % (frame)
    frame = frame + 1
    for index in range (0, i_count):
      print '[INTERSECTION: INDEX=%d ANGLE=%d]' % (intersections[index].m_index, intersections[index].m_angle)
      pixyData_msg.i_index = intersections[index].m_index
      pixyData_msg.i_angle = intersections[index].m_angle
    for index in range (0, v_count):
      print '[VECTOR: INDEX=%d X0=%3d Y0=%3d X1=%3d Y1=%3d]' % (vectors[index].m_index, vectors[index].m_x0, vectors[index].m_y0, 
                                                                  vectors[index].m_x1, vectors[index].m_y1)
      pixyData_msg.m_index = vectors[index].m_index
      pixyData_msg.m_xa = vectors[index].m_x0
      pixyData_msg.m_ya = vectors[index].m_y0
      pixyData_msg.m_xb = vectors[index].m_x1
      pixyData_msg.m_yb = vectors[index].m_y1
    pixy_pub.publish(pixyData_msg)