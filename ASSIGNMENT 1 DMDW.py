#!/usr/bin/env python
# coding: utf-8

# In[2]:


from collections import Counter

n_num = [1, 2, 3, 4, 5, 5]

n = len(n_num)

data = Counter(n_num)

get_mode = dict(data)

mode = [k for k, v in get_mode.items() if v==
max(list(data.values()))]

if len(mode) == n:

    get_mode = "No mode found"

else:

    get_mode = "Mode is / are: " + ', '.join(map(str, mode))

print(get_mode)


# In[4]:


# Median without using library

n_num = [1, 2, 3, 4, 5]

n = len(n_num)

n_num.sort()

if n % 2 == 0:

    median1 = n_num[n//2]

    median2 = n_num[n//2 - 1]

    median = (median1 + median2)/2

else:

     median = n_num[n//2]

print("Median is: " + str(median))


# In[5]:


# Mean without using library

n_num = [1, 2, 3, 4, 5]

n = len(n_num)

get_sum = sum(n_num)

mean = get_sum / n

print("Mean / Average is: " + str(mean))


# # with using library functions
# 

# In[6]:


#calculating ,ean using mean fumction
import numpy

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.mean(speed)

print(x)


# In[7]:


#median
import numpy

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.median(speed)

print(x)


# In[8]:


#mode
from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = stats.mode(speed)

print(x)


# In[3]:


import numpy

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.mean(speed)

y = numpy.median(speed)

s = numpy.std(speed)

v = numpy.var(speed)

print(x)

print(y)

print(s)

print(v)


# In[19]:


import math

xs = [0.5,0.7,0.3,0.2]     # values (must be floats!)
mean = sum(xs) / len(xs)   # mean
var  = sum(pow(x-mean,2) for x in xs) / len(xs)  # variance
std  = math.sqrt(var)  # standard deviation


# In[20]:


std


# In[21]:


var


# In[22]:


mena


# In[23]:


mean


# In[26]:


# Declaring a list 
L = [1, "a" , "string" , 1+2] 
print(L)
L.append(6) 
print(L) 
L.pop() 
print(L) 
print(L[1]) 


# In[28]:


L = [1, 4, 5, 7, 8, 9] 
for  i in L: 
    print (i) 


# In[27]:


tup = (1, "a", "string", 1+2) 
print(tup) 
print(tup[1]) 


# In[29]:


# Creating an empty Dictionary 
Dict = {} 
print("Empty Dictionary: ") 
print(Dict) 
  

Dict = dict({1: 'LOCK', 2: 'For', 3:'KEYS'}) 
print("\nDictionary with the use of dict(): ") 
print(Dict) 
  
# Creating a Dictionary 
# with each item as a Pair 
Dict = dict([(1, 'Geeks'), (2, 'For')]) 
print("\nDictionary with each item as a pair: ") 
print(Dict) 


# In[ ]:




