# Reinforcement-Learning---k-Armed-Bandit

# Multi-Arm Bandits Problem with Reinforcement Learning

We illustrate Q-learning via the multi-arm bandit or the k-arm bandit problem.

Here, we illustrate the effects of:
- $\epsilon$ or $\alpha$, which is the probability of exploring (in constrast to exploiting)
- Decay, which reduces the probability of exploring over time

The probability of exploring is important as exploring different options allow the agent to find path to a global maxima, in constrast to getting trapped within a local maxima. Meanwhile, decay is important as we wish to stop exploring after a period of time, as the global maxima may have be found. The best implementation is to use both concepts together.

This project is extracted from:
https://towardsdatascience.com/multi-armed-bandits-and-reinforcement-learning-dc9001dcb8da
