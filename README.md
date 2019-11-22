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
pip install gym-ros
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

Continuing to edit
####################################################################################################################################

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Andre Cleaver** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

