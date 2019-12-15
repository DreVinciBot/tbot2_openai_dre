#! /usr/bin/env python
from __future__ import print_function

import rospy 
import rospkg 
import numpy as np  
import gym
import random
import time
from IPython.display import clear_output
from geometry_msgs.msg import Pose


rospy.init_node('frozen_lake', anonymous = True)
state_reward_info_pub = rospy.Publisher("/frozen_lake/state_action", Pose, queue_size = 1) 
q_value_pub = rospy.Publisher("/frozen_lake/q_value", Pose, queue_size = 1)

# env = gym.make("FrozenLake8x8-v0")
env = gym.make("FrozenLake-v0")


action_space_size = env.action_space.n
state_space_size = env.observation_space.n

q_table = np.zeros((state_space_size, action_space_size))

num_episodes = 10000
max_steps_per_episode = 100

learning_rate = 0.1
discount_rate = 0.99

exploration_rate = 1
max_exploration_rate = 1
min_exploration_rate = 0.01
exploration_decay_rate = 0.001

rewards_all_episodes = []

# Q-Learning Algorithm
for episode in range(num_episodes):
	state = env.reset()

	done = False
	rewards_current_episode = 0

	for step in range(max_steps_per_episode):

		message = Pose()
		q_value_message = Pose()

		message.position.z = state

		# Exploration-exploitation trade-off
		exploration_rate_threshold = random.uniform(0,1)
		if exploration_rate_threshold > exploration_rate:
			action = np.argmax(q_table[state, :])
		
		else:
			action = env.action_space.sample()

		new_state, reward, done, info = env.step(action)

		# Update Q-table for Q(s,a)
		q_table[state, action] = q_table[state, action] * (1 - learning_rate) + learning_rate * (reward + discount_rate * np.max(q_table[new_state, :]))

		state = new_state
		rewards_current_episode += reward

		# Publish relavent info
		
		message.position.x = action
		message.position.y = new_state
		message.orientation.x = reward
		message.orientation.y = rewards_current_episode
		message.orientation.z = q_table[state,action]
		message.orientation.w = np.max(q_table[new_state, :])

		state_reward_info_pub.publish(message)


		q_value_message.position.x = q_table[state,0]
		q_value_message.position.y = q_table[state,1]
		q_value_message.position.z = q_table[state,2]
		q_value_message.orientation.x = q_table[state,3]
		q_value_message.orientation.y = action
		q_value_message.orientation.z = state
		q_value_message.orientation.w = new_state

		q_value_pub.publish(q_value_message)

		rate = rospy.Rate(1)
		# rate.sleep()
		# print(message)
		# print(message.position.x, message.position.y)


		if done == True:
			break

	# Exploration rate decay
	exploration_rate = min_exploration_rate + (max_exploration_rate - min_exploration_rate) * np.exp(-exploration_decay_rate*episode)

	rewards_all_episodes.append(rewards_current_episode)

# Calculate and print the average reward per thousang episodes
rewards_per_thousand_episodes = np.split(np.array(rewards_all_episodes),num_episodes/1000)
count = 1000



print("**********Average reward per thousand episodes***********\n")
for r in rewards_per_thousand_episodes:
	print(count, ": ", str(sum(r/1000)))
	count += 1000


# Print updated Q-table
print("\n\n***********Q-table***********\n")
print(q_table)