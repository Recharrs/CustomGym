import gym
import custom_gym
#from gym import wrappers

# Create Environment
env = gym.make('MountainCarEx-v0')

# Print action & observation space
print(env.action_space)
print(env.observation_space)

# Recode
#env = wrappers.Monitor(env, './Movie', force=True)

# Test Environment
for i_episode in range(10):

  # Reset Environment
  task, obs = env.reset()
  t = 0
  print('task id: {}'.format(task))

  # Run Episode
  while True:
    # Render Environment
    env.render()
    
    # Interact with Environment
    action = env.action_space.sample()
    obs, reward, done, info = env.step(action)
    #print("Reward: {}".format(reward))
    #print(obs)
    #print(info)
    t = t+1

    # Check Done
    if done:
      print("Episode finished after {} timesteps".format(t+1))
      break

# Close Environment
env.close()
