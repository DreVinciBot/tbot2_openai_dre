#! /usr/bin/env python
from __future__ import print_function

import rospy 
import rospkg 
from geometry_msgs.msg import Pose
from gazebo_msgs.msg import ModelStates 
from gazebo_msgs.srv import SetModelState


class gazebo_modelStates:

	def __init__(self):
		rospy.init_node('gazebo_subscriber', anonymous = True)

		self.gazebo_modelsub = rospy.Subscriber("/gazebo/model_states", ModelStates, self.gazebo_modelcallback)
		self.turtlebot_pose_pub = rospy.Publisher("turtlebot/Pose", Pose, queue_size = 10)

		rospy.spin()


	def gazebo_modelcallback(self,data):

		model_array = (data.name)

		turtlebot_index = model_array.index('mobile_base')
		
		turtlebot_pose = data.pose[turtlebot_index]

		self.turtlebot_pose_pub.publish(turtlebot_pose)

if __name__ == '__main__':
    try:
    	print("test")
        test = gazebo_modelStates()
    except rospy.ROSInterruptException:
        pass