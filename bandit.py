import numpy as np

# Initialization
k = 3                          # Number of bandits
Q = [0 for _ in range(k)]      # Our estimated reward
N = [0 for _ in range(k)]      # Count for each bandit
eps = 0.1                      # Epsilon value for exploration
alpha = 0.00001                # Exploration decay, 0 if no decay
p_bandits = [0.35, 0.40, 0.80] # True probability of winning for each bandit
iteration = 10000              # Number of iteration

def pull(a):
    """Pull arm of bandit with index `i` and return 1 if win, 
    else return 0."""
    if np.random.rand() < p_bandits[a]:
        return 1
    else:
        return 0


while iteration>0:

    if np.random.rand() > eps:
        # Take greedy action most of the time
        a = np.argmax(Q)
    else:
        # Take random action with probability eps
        a = np.random.randint(0, k)
    
    # Collect reward
    reward = pull(a)
    
    # Incremental average
    N[a] += 1
    Q[a] += 1/N[a] * (reward - Q[a])
    
    Q1 = [round(x,3) for x in Q]
    
    print(str(iteration) + ' left - ' + str(N) + ' : ' + str(Q1))
    iteration -= 1
    
    # Decay exploration rate
    eps -= alpha