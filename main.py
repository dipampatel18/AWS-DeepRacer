def reward_function(params):

    # Importing Libraries
    import math

    # Initializing Params
    all_wheels_on_track = params['all_wheels_on_track']         # Flag to indicate if the Vehicle is On the Track (boolean)
    x = params['x']                                             # Vehicle's X-coordinate in meters (float)
    y = params['y']                                             # Vehicle's Y-coordinate in meters (float)
    distance_from_center = params['distance_from_center']       # Distance from the Track Center in meters (float)
    is_left_of_center = params['is_left_of_center']             # Flag to indicate if the Vehicle is On the Left side to the Track center or Not (boolean)
    heading = params['heading']                                 # Vehicle's Yaw in Degrees (float)
    progress = params['progress']                               # Percentage of Track Completed (float)
    steps = params['steps']                                     # Number of Steps Completed (int)
    speed = params['speed']                                     # Vehicle's Speed in meters per second (float)
    steering_angle = abs(params['steering_angle'])              # Vehicle's Steering Angle in Degrees (float)
    track_width = params['track_width']                         # Width of the Track (float)
    waypoints = params['waypoints']                             # List of [x, y] as Milestones along the Track Center [[float, float],...]
    closest_waypoints = params['closest_waypoints']             # Indices of the Two Nearest Waypoints [int, int]

    # Initializing Rewards
    reward = 1e-3       # Default Reward
    MAX_REWARD = 1e3
    MIN_REWARD = -1e3


    # Markers based on the Track Width
    marker_0 = 0.05 * track_width
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # Higher Reward if No Wheels go off the Track and the Agent is somewhere in between the Track Borders
    if (all_wheels_on_track and ((0.5*track_width - distance_from_center) >= 0.05)):
        reward += 5
    else:
        reward -= 0.1

    # Higher Reward if the Agent is Closer to Center Line and vice versa
    if (distance_from_center >= 0.0 and distance_from_center <= marker_0):
        reward += 5.0 * speed
    elif (distance_from_center <= marker_1):
        reward += 2.5 * speed
    elif (distance_from_center <= marker_2):
        reward += 1.0 * speed
    elif (distance_from_center <= marker_3):
        reward += 0.5 * speed
    else:
        reward -= 1e-3



    # The Agent should Continue Making Progress
    if progress >= 99:
        reward += MAX_REWARD
    elif progress >= 75:
        reward += (MAX_REWARD / 2) * (progress / 100)
    elif progress >= 50:
        reward += (MAX_REWARD / 4) * (progress / 100)
    elif progress >= 25:
        reward += (MAX_REWARD / 8) * (progress / 100)
    elif progress >= 10:
        reward += (MAX_REWARD / 16) * (progress / 100)
    else:
        reward += (speed / 5)


    # Controlling the Steering Angle of the Agent and Penalizing if the Agent is Steering too much
    STEERING_THRESHOLD = 20
    if steering_angle < STEERING_THRESHOLD:
        reward *= 1.2
    else:
        reward *= 0.85


    # Penalize if the Agent is taking Slow Actions
    SPEED_THRESHOLD = 3
    if speed > SPEED_THRESHOLD:
        reward *= 1.2
    else:
        reward *= 0.8
        
        
    return float(reward)
