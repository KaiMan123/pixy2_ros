#!/usr/bin/env python

import rospy
import pixy
from ctypes import *
from pixy import *
from pixy2_ros.msg import pixy2blocks

# Pixy2 Python SWIG get blocks example #

print ("Pixy2 Python SWIG Example -- Get Blocks")

pixy.init ()
pixy.change_prog ("color_connected_components");

rospy.init_node("pixy2_getblocks")
pixy2blocks_pub = rospy.Publisher("pixy2blocks", pixy2blocks, queue_size=1)
pixy2blocks_msg = pixy2blocks()

class Blocks (Structure):
  _fields_ = [ 
	#This variable contains the signature number or color-code number.
	("m_signature", c_uint),
	#This variable contains the x location of the center of the block. The value ranges between 0 and frameWidth    
	("m_x", c_uint),
	#This variable contains the y location of the center of the block. The value ranges between 0 and frameHeight    
	("m_y", c_uint),
	#This variable contains the width of the block. The value ranges between 0 and frameWidth    
	("m_width", c_uint),
	#This variable contains the height of the block. The value ranges between 0 and frameHeight    
	("m_height", c_uint),
	#This variable contains the angle of color-code in degrees. The value ranges between -180 and 180. If the block is a regular signature (not a color-code), the angle value will be 0
    ("m_angle", c_uint),
	#This variable contains the tracking index of the block.
    ("m_index", c_uint),
	#This variable contains the number of frames a given block has been tracked. When the age reaches 255, it remains at 255.     
	("m_age", c_uint) ]

blocks = BlockArray(100)
frame = 0

while not rospy.is_shutdown():
  count = pixy.ccc_get_blocks (100, blocks)

  if count > 0:
    print 'frame %3d:' % (frame)
    frame = frame + 1
    for index in range (0, count):
      print '[BLOCK: SIG=%d X=%3d Y=%3d WIDTH=%3d HEIGHT=%3d]' % (blocks[index].m_signature, blocks[index].m_x, blocks[index].m_y, blocks[index].m_width, blocks[index].m_height)
      pixy2blocks_msg.m_signature = blocks[index].m_signature
      pixy2blocks_msg.m_x = blocks[index].m_x
      pixy2blocks_msg.m_y = blocks[index].m_y
      pixy2blocks_msg.m_width = blocks[index].m_width
      pixy2blocks_msg.m_height = blocks[index].m_height
    pixy2blocks_pub.publish(pixy2blocks_msg)
