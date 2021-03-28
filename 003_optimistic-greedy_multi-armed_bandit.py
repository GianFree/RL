import random

# init the rewards
rewards = [1.0, 0.5, 0.2, 0.5, 0.6, 0.1, -0.5]
arms = len(rewards)
#number of training "episode" of the agent
episodes = 10000000

learning_rate = 0.1
# init values of each action. Now we make an optimistic guess.
Value = [3.0] * arms
print(Value)

def greedy(values):
    return values.index(max(values))

# learning process:
# at each iteration it chooses a random action and update the Value
for i in range(episodes):
    action = greedy(Value)
    Value[action] = Value[action] + learning_rate*(rewards[action] - Value[action])

print(rewards)
print(Value)
