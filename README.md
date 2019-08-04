# AWS-DeepRacer

Trained an AWS DeepRacer Robot Car using Reinforcement Learning in AWS SageMaker and RoboMaker

<p align="center">
  <img width="580" height="320" src="/images/DeepRacer.gif">
</p>

AWS DeepRacer is a 1/18th scale race car which gives you an interesting and fun way to get started with reinforcement learning (RL). RL is an advanced machine learning (ML) technique which takes a very different approach to training models than other machine learning methods. Its super power is that it learns very complex behaviors without requiring any labeled training data, and can make short term decisions while optimizing for a longer term goal.

With AWS DeepRacer, you now have a way to get hands-on with RL, experiment, and learn through autonomous driving. You can get started with the virtual car and tracks in the cloud-based 3D racing simulator, and for a real-world experience, you can deploy your trained models onto AWS DeepRacer and race your friends, or take part in the global AWS DeepRacer League. Developers, the race is on.

### AWS DeepRacer As an Integrated Learning System

Reinforcement learning, especially deep reinforcement learning, has proven effective in solving a wide array of autonomous decision-making problems. It has applications in financial trading, data center cooling, fleet logistics, and autonomous racing, to name a few.

Reinforcement learning has the potential to solve real-world problems. However, it has a steep learning curve because of the extensive technological scope and depth. Real-world experimentation requires that you construct a physical agent, e.g., an autonomous racing car. It also requires that you secure a physical environment, e.g., a driving track or public road. The environment can be costly, hazardous, and time-consuming. These requirements go beyond merely understanding reinforcement learning.

To help reduce the learning curve, AWS DeepRacer simplifies the process in three ways:

- By offering a wizard to guide training and evaluating reinforcement learning models. The wizard includes pre-defined environments, states, actions, and customizable reward functions.

- By providing a simulator to emulate interactions between a virtual agent and a virtual environment.

- By offering an AWS DeepRacer vehicle as a physical agent. Use the vehicle to evaluate a trained model in a physical environment. This closely resembles a real-world use case.

If you are a seasoned machine learning practitioner, you will find AWS DeepRacer a welcome opportunity to build reinforcement learning models for autonomous racing in both virtual and physical environments. To summarize, use AWS DeepRacer to create reinforcement learning models for autonomous racing with the following steps:

- Train a custom reinforcement learning model for autonomous racing. Do this by using the AWS DeepRacer console integrated with Amazon SageMaker and AWS RoboMaker.

- Use the AWS DeepRacer simulator to evaluate a model and test autonomous racing in a virtual environment.

- Deploy a trained model to AWS DeepRacer model vehicles to test autonomous racing in a physical environment.

### The AWS DeepRacer Console

The AWS DeepRacer console is a graphical user interface to interact with the AWS DeepRacer service. You can use the console to train a reinforcement learning model and to evaluate the model performance in the AWS DeepRacer simulator built upon AWS RoboMaker. In the console, you can also download a trained model for deployment to your AWS DeepRacer vehicle for autonomous driving in a physical environment.

In summary, the AWS DeepRacer console supports the following features:

- Create a training job to train a reinforcement learning model with a specified reward function, optimization algorithm, environment, and hyperparameters.

- Choose a simulated track to train and evaluate a model by using Amazon SageMaker and AWS RoboMaker.

- Clone a trained model to improve training by tuning hyperparameters to optimize your model's performance.

- Download a trained model for deployment to your AWS DeepRacer vehicle so it can drive in a physical environment.

- Submit your model to a virtual race and have its performance ranked against other models in a virtual leaderboard.

### The AWS DeepRacer Vehicle

The AWS DeepRacer vehicle is a Wi-Fi enabled, physical vehicle that can drive itself on a physical track by using a reinforcement learning model.

- You can manually control the vehicle, or deploy a model for the vehicle to drive autonomously.

- The autonomous mode runs inference on the vehicle's compute module. Inference uses images that are captured from the camera that is mounted on the front.

- A Wi-Fi connection allows the vehicle to download software. The connection also allows the user to access the device console to operate the vehicle by using a computer or mobile device.

### The AWS DeepRacer League

The DeepRacer League is an important component of AWS DeepRacer. The DeepRacer League is intended to foster communal learning and collaborative exploration through sharing and competition.

With the DeepRacer League, you can have your development effort compared with other AWS DeepRacer developers in a physical or virtual racing event. Not only do you get a chance to win prizes, you also have a way to measure your reinforcement learning model. You can create opportunities to share your insights with other participants, to learn from each other, and to inspire each other.

### My Approach

When I initially trained for a few times, I did a few mistakes

- Was trying to control too many parameters of the agent and which ultimately messed up with its learning

- Created multiple parameter conditions instead of having them all under just one/few conditions. As a result, the overall reward for the episode did increase, but it failed to learn the optimal policy

- Reduced the parameters under consideration and focused on having an optimal policy to achieve the target of staying within the track and completing the entire track

- Staying within the track was the first condition to be achieved which was rewarded based on the percent of track completed and its current speed. Thereafter, driving on the center lane with minimal deviation was the next goal for the reward function. Avoiding unnecessary steering was the final goal.

- During training, the episodic rewards were more or less the same as my previous trials, however, the percentage of track completion did slightly increase which indicated that the agent was learning the optimal policy.

- In the evaluation phase, out of 5 trial runs, the agent could complete the entire track twice in 22.2 and 23.4 seconds respectively. 

### References

- [AWS DeepRacer Homepage](https://aws.amazon.com/deepracer/)

- [What is DeepRacer?](https://docs.aws.amazon.com/deepracer/latest/developerguide/what-is-deepracer.html)

- [Getting Started with AWS DeepRacer](https://aws.amazon.com/deepracer/getting-started/)

- [AWS DeepRacer Getting Started Guide](https://d1.awsstatic.com/deepracer/AWS-DeepRacer-Getting-Started-Guide.pdf)

- [Online Course on AWS DeepRacer: Driven by Reinforcement Learning](https://www.aws.training/learningobject/wbc?id=32143)

- [AWS DeepRacer Workshops](https://github.com/aws-samples/aws-deepracer-workshops)
