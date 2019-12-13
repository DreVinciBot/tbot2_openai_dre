#! /usr/bin/env python
from __future__ import print_function

import rospy 
import rospkg 
from openai_ros.msg import RLExperimentInfo
from geometry_msgs.msg import Pose



class gazebo_modelStates:

	def __init__(self):
		rospy.init_node('oprenaiReward_subscriber', anonymous = True)

		self.openai_sub = rospy.Subscriber("/openai/reward", RLExperimentInfo, self.reward_callback)
		self.openai_pub = rospy.Publisher("/openai_reward", Pose, queue_size = 1)	

		rospy.spin()


	def reward_callback(self,data):
		# print(data)
		en = data.episode_number
		er = data.episode_reward

		pose_message = Pose()

		pose_message.position.x = en
		pose_message.position.y = er

		self.openai_pub.publish(pose_message)



if __name__ == '__main__':
    try:
    	print("reward")
        test = gazebo_modelStates()
    except rospy.ROSInterruptException:
        pass