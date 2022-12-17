#!/usr/bin/env python
# coding: utf-8

# # More On Negative Binomial
# ## Let's Take A Deeper Dive Into Negative Binomial

# To better understand what Negative Binomial distribution looks like, let's visualize what the distribution actually looks like:

# In[1]:


# Importing the necessary libraries
import numpy as np
from scipy.stats import nbinom
import matplotlib.pyplot as plt


# In a certain coin game, a fair coin is flipped so that there is a 50% chance of getting heads and a 50% chance of getting tails.  In order to win this game, you must get a total of three heads.  Let's visualize what this probability distribution would be of winning this game for a given number of tosses.  The number of unsuccessful throws can be modeled using a [](section-label) distribution.
# 

# In[2]:


# X = Number of throws
# P = Probability of getting 'heads'
# r = number of necessary 'heads' to win the game
X = np.arange(3, 20)
r = 3
p = 0.5

# Negative Binomial distribution for python, scopy.stats

nbinom_pd = nbinom.pmf(X, r, p)

# Show plot of negative binomial distribution

fig, ax = plt.subplots(1, 1, figsize=(10, 8))
ax.plot(X, nbinom_pd, 'bo', ms=8, label='nbinom pmf')
plt.ylabel("Probability", fontsize="15")
plt.xlabel("Number of Tosses", fontsize="15")
plt.title("Negative Binomial Distribution - Flipping A Coin Game", fontsize="18")
ax.vlines(X, 0, nbinom_pd, colors='b', lw=5, alpha=0.5)


# From the graph above, we can see that the probability that a person wins the game on the eighth toss is  approximately 0.023 (from the chart of [](section-label) above).
