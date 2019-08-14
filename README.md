# AWS DeepRacer

Trained an AWS DeepRacer Robot Car using Reinforcement Learning in AWS SageMaker and RoboMaker

<p align="center">
  <img width="580" height="320" src="/images/DeepRacer.gif">
</p>

AWS DeepRacer is a 1/18th scale race car which gives you an interesting and fun way to get started with reinforcement learning (RL). RL is an advanced machine learning (ML) technique which takes a very different approach to training models than other machine learning methods. Its super power is that it learns very complex behaviors without requiring any labeled training data, and can make short term decisions while optimizing for a longer term goal.

With AWS DeepRacer, you now have a way to get hands-on with RL, experiment, and learn through autonomous driving. You can get started with the virtual car and tracks in the cloud-based 3D racing simulator, and for a real-world experience, you can deploy your trained models onto AWS DeepRacer and race your friends, or take part in the global AWS DeepRacer League. Developers, the race is on.

### AWS DeepRacer As an Integrated Learning System

Reinforcement learning, especially deep reinforcement learning, has proven effective in solving a wide array of autonomous decision-making problems. It has applications in financial trading, data center cooling, fleet logistics, and autonomous racing, to name a few.

To help reduce the learning curve, AWS DeepRacer simplifies the process in three ways:

- By offering a wizard to guide training and evaluating reinforcement learning models. The wizard includes pre-defined environments, states, actions, and customizable reward functions.

- By providing a simulator to emulate interactions between a virtual agent and a virtual environment.

- By offering an AWS DeepRacer vehicle as a physical agent. Use the vehicle to evaluate a trained model in a physical environment. This closely resembles a real-world use case.

### The AWS DeepRacer Console

The AWS DeepRacer console is a graphical user interface to interact with the AWS DeepRacer service. You can use the console to train a reinforcement learning model and to evaluate the model performance in the AWS DeepRacer simulator built upon AWS RoboMaker. In the console, you can also download a trained model for deployment to your AWS DeepRacer vehicle for autonomous driving in a physical environment. In summary, the AWS DeepRacer console supports the following features:

- Create a training job to train a reinforcement learning model with a specified reward function, optimization algorithm, environment, and hyperparameters.

- Choose a simulated track to train and evaluate a model by using Amazon SageMaker and AWS RoboMaker.

- Clone a trained model to improve training by tuning hyperparameters to optimize your model's performance.

- Download a trained model for deployment to your AWS DeepRacer vehicle so it can drive in a physical environment.

- Submit your model to a virtual race and have its performance ranked against other models in a virtual leaderboard.

### My Approach

When I initially trained for a few times, I did a two mistakes

- Was trying to control too many parameters of the agent and which ultimately messed up with its learning

- Created multiple parameter conditions instead of having them all under just one/few conditions. As a result, the overall reward for the episode did increase, but it failed to learn the optimal policy

I implemented the changes on the final model 'fastest car alive'. It was trained for 5 hours with the following training configurations and a slight modification of the hyperparameters from their default values.

<p align="center">
  <img width="700" height="380" src="/images/Training Configuration.png">
</p>

Reduced the parameters under consideration and focused on having an optimal policy to achieve the target of staying within the track and completing the entire track.

Staying within the track was the first condition to be achieved which was rewarded based on the percent of track completed and its current speed. Thereafter, driving on the center lane with minimal deviation was the next goal for the reward function. Avoiding unnecessary steering was the final goal. Following was the action space for the agent.

<p align="center">
  <img width="700" height="380" src="/images/Action Space.png">
</p>

During training, the episodic rewards were more or less the same as my previous trials, however, the percentage of track completion did slightly increase which indicated that the agent was learning the optimal policy.

<p align="center">
  <img width="700" height="380" src="/images/Training Completed.png">
</p>

In the evaluation phase, out of 5 trial runs, the agent could complete the entire track twice in 23.04 and 22.04 seconds respectively. 

<p align="center">
  <img width="700" height="380" src="/images/Evaluation Results.png">
</p>

### References

- [AWS DeepRacer Homepage](https://aws.amazon.com/deepracer/)

- [What is DeepRacer?](https://docs.aws.amazon.com/deepracer/latest/developerguide/what-is-deepracer.html)

- [Getting Started with AWS DeepRacer](https://aws.amazon.com/deepracer/getting-started/)

- [AWS DeepRacer Getting Started Guide](https://d1.awsstatic.com/deepracer/AWS-DeepRacer-Getting-Started-Guide.pdf)

- [Online Course on AWS DeepRacer: Driven by Reinforcement Learning](https://www.aws.training/learningobject/wbc?id=32143)

- [AWS DeepRacer Workshops](https://github.com/aws-samples/aws-deepracer-workshops)
