#!/usr/bin/env python
# coding: utf-8

# # More On Geometric Distribution
# ## Let's Take A Deeper Dive Into Geometric Distribution

# To better understand what [](section-label) looks like, let's visualize what the distribution actually looks like. Here is an example:

# In a certain coin game, a fair coin is flipped so that there is a 50% chance of getting heads and a 50% chance of getting tails.  In order to win this game, you must get a 'heads'.  Let's visualize what this probability distribution would be of winning this game for a given number of tosses.  The number of unsuccessful throws can be modeled using a [](section-label2) distribution.

# In[1]:


# Importing the necessary libraries
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


sample = np.random.geometric(0.5, 1000)
bin = np.arange(0,20,1)

plt.hist(sample, bins=bin, edgecolor='blue') 
plt.title("Geometric Distribution") 
plt.ylabel("Probability", fontsize="15")
plt.xlabel("Number of Tosses", fontsize="15")
plt.show()




# Let's try another one...

# In another game, cards are chosen at random (with replacement) from a full deck of 52 cards. The object of the game is to get a "clubs" suited card.  Let's visualize what this probability distribution would be of winning this game for a given number of drawn cards. The number of the winning draw can be modeled with [](section-label).  As a reminder, the probability of drawing a clubs-suited card is 0.25 (13/52).

# In[3]:


sample2 = np.random.geometric(0.25, 1000)
bin = np.arange(0,20,1)

plt.hist(sample2, bins=bin, edgecolor='green') 
plt.title("Geometric Distribution") 
plt.ylabel("Probability", fontsize="15")
plt.xlabel("Number of Draws", fontsize="15")
plt.show()


# In[ ]:





# In[ ]:





# [](section-label2)
