#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import numpy as np


# In[9]:


df=pd.read_csv(r"E:\Downloads\clean_FineTech_appData.csv")


# In[10]:


df


# In[11]:


df.shape


# In[12]:


df.describe()


# In[13]:


df.head()


# In[14]:


df.tail()


# In[15]:


df.head(12)


# In[16]:


df.tail(13)


# In[17]:


df.info()


# In[18]:


df.isnull().sum()


# In[19]:


df.mean()


# In[20]:


df.std()


# In[22]:


df['minigame']


# In[24]:


df.loc[2]


# In[25]:


df.values


# In[26]:


df.iloc[1:3]


# # numpy basic programs
# 

# In[31]:


import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)


# In[32]:



arr = np.array([1, 2, 3, 4, 5])

print(arr)

print(type(arr))


# In[33]:



arr = np.array(42)

print(arr)


# In[34]:


arr = np.array([1, 2, 3, 4, 5])

print(arr)


# In[35]:


arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr)


# In[36]:


arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(arr)


# In[37]:


a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)


# In[38]:


arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)


# In[39]:


arr = np.array([1, 2, 3, 4])

print(arr[1])


# In[40]:


arr = np.array([1, 2, 3, 4])

print(arr[2] + arr[3])


# In[41]:


arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('2nd element on 1st dim: ', arr[0, 1])


# In[42]:


arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr[0, 1, 2])


# In[43]:


arr = np.array([1, 2, 3, 4])

print(arr.dtype)


# In[44]:


arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))

print(arr)


# In[45]:


arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)

print(arr)


# # pandas basic programs

# In[46]:


data = [['Alex',10],['Bob',12],['Clarke',13]]

df = pd.DataFrame(data,columns=['Name','Age'],dtype=float)

print(df)


# In[47]:


data = {'Name':['Tom', 'Jack', 'Steve',
'Ricky'],'Age':[28,34,29,42]}

df = pd.DataFrame(data)

print(df)


# In[50]:




d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),

'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)

print ("Adding a new column by passing as Series:")

df['three']=pd.Series([10,20,30],index=['a','b','c'])

print(df)

print ("Adding a new column using the existing columns in Data")

df['four']=df['one']+df['three']

print(df)


# In[51]:


data = [['Alex',10],['Bob',12],['Clarke',13]]

df = pd.DataFrame(data,columns=['Name','Age'],dtype=float)

print(df)


# In[ ]:




