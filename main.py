def reward_function(params):

    # Initializing Params
    all_wheels_on_track = params['all_wheels_on_track']         # Flag to indicate if the Vehicle is On the Track (boolean)
    distance_from_center = params['distance_from_center']       # Distance from the Track Center in meters (float)
    progress = params['progress']                               # Percentage of Track Completed (float)
    steps = params['steps']                                     # Number of Steps Completed (int)
    speed = params['speed']                                     # Vehicle's Speed in meters per second (float)
    steering_angle = abs(params['steering_angle'])              # Vehicle's Steering Angle in Degrees (float)
    track_width = params['track_width']                         # Width of the Track (float)

    # Initializing Rewards
    reward = 1e-3       # Default Reward
    
    # Prevent Zig-zag Behavior and Keep the Agent on the Track
    # Markers based on the Track Width
    marker_0 = 0.05 * track_width
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

	# Keep the Agent on the Track and Progressing
    if (all_wheels_on_track and (steps > 0)):
        reward = ((progress / steps) * 100) + (speed ** 2)
        # Higher Reward if the Agent is Closer to Center Line and vice versa
        if (distance_from_center >= 0.0 and distance_from_center <= marker_0):
            reward += 7.5
        elif (distance_from_center <= marker_1):
            reward += 4.0
        elif (distance_from_center <= marker_2):
            reward += 2.5
        elif (distance_from_center <= marker_3):
            reward += 0.1
    else:
        reward -= 0.01
     
    # Penalize if the Agent is Steering too much
    ABS_STEERING_THRESHOLD = 22			    # Steering Penality threshold
    if steering_angle > ABS_STEERING_THRESHOLD:
        reward *= 0.8
	
    return float(reward)
