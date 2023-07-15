import gymnasium as gym
#imports are super important here because the brunt of the code is part of the library

env = gym.make("LunarLander-v2", render_mode="human")
# Here we make the specific environment from the library, make sure this matches the code

observation, info = env.reset(seed=42)
# Here we reset the seed so that the program will create different landscapes
for _ in range(1000): # For loop
   action = env.action_space.sample()  # this is where you would insert your policy
   observation, reward, terminated, truncated, info = env.step(action)
# if statement that resets the AI when the window terminates
   if terminated or truncated:
      observation, info = env.reset()
      # Close the environment
env.close()