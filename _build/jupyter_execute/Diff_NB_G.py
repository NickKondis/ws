#!/usr/bin/env python
# coding: utf-8

# # Examining The Differences
# ## Let's Have A Look

# As we have seen, a [](section-label) is used to determine the probability of a defined number of successes in repeated trials.  Examples of this were shown in (section-label3) and (section-label4) in the in depth analysis of [](section-label). The characteristic features of this were both repeated trials and defined number of successes.
# 
# ## Characteristics of Negative Binomial Probability
# - defined, independent probability
# - binary values
# - repeated trials
# - defined number of necessary successes
# 
# In [](section-label2), there are also repeated trials.  However, [](section-label2) is deifined as needing only a single success.
# 
# ## Characteristics of Geometric Probability
# - defined, independent probability
# - binary values
# - repeated trials
# - single necessary success
# 
# 
# 

# Even though,[](section-label) and [](section-label2) are distinct probabilities, [](section-label2) can be considered a subset of [](section-label) where the defined number of successes is exactly one.
# 
# 

# Let's take a look at some examples....

# In[1]:


# Importing the necessary libraries.
import numpy as np
from scipy.stats import nbinom
import numpy as np


# What is the probability of getting 4 heads by flipping a coin 5 times?
# 
# 

# In[2]:


print("Because this requires multiple successes, it is a Negative Binomial.")


# The answer is below.

# In[3]:


nbinom.pmf(5, 4, 0.5)


# What is the likelihood of dealt 4 clubs in a 5 card poker hand?
# 

# The code is below.

# In[4]:


print("Because the probability of getting a club is effected by each removed card, this is neither Negative Binomial or Geometric.")
print("Code is not applicable")


# What is the probability of getting a 6 by rolling 3 dice simultaneously?
# 

# In[5]:


print("This is a Geometric probability")
answer = 1-(1-0.5)**6
print("The answer is " + str(answer))


# ##Great job, that's the end of the lesson.
