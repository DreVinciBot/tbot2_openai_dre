# tbot2_openai_dre

![turtlebot2 openai](/images/tbot2_training.gif)

Screen capture of Turtlebot simulator during training.



This project explores Aumgented reality (AR)'s role in human-in-the-loop techniques to enhance Reinforcement Learning algorithms.
Here, the Turtlebot2 simulator in the openai_ros package is leveraged and modified to prompt a user for reasonable actions during the learning process. For further information read [Learn the basics of openai_ros using a Turtlebot2 simulation](http://wiki.ros.org/openai_ros/TurtleBot2%20with%20openai_ros).  The robot's goal is to navigate through an enviornment while avoiding obstacles. A Q-learning approached is utilized  
and the inputs are the robot's :   and the output is the robot's :

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Make sure your computer is up-to-date
```
sudo apt-get update
```

Install the following:

git
```
pip install gcg
```
gym-ros
```
pip install gym
```

The Turtlebot package and Gazebo Simulator
```
cd catkin_ws/src
git clone https://github.com/turtlebot/turtlebot.git
git clone https://github.com/turtlebot/turtlebot_simulator
cd ..
```
Install dependency of all packages in the workspace
```
rosdep install --from-paths src --ignore-src -r -y
```

Compile package and source the enviornment
```
catkin_make
source devel/setup.bash
```

### File modification

In order to start training
```
roslaunch tbot_training start_training.py
```


The reward is published to the topic: /openai/reward

