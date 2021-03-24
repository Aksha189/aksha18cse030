#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
data=pd.read_csv(r"https://raw.githubusercontent.com/archana1822/DMDW-Lab/main/Toyota.csv")
data


# In[2]:


type(data)


# In[3]:


data.shape


# In[4]:


data.info()


# In[5]:


data.index


# In[8]:


data.columns


# In[9]:


data.head()


# In[10]:


data.tail()


# In[11]:


data.head(5)


# In[12]:


data[['Price',"Age"]].head(10)


# In[13]:


data.isnull().sum()


# In[14]:


data.dropna(inplace=True)
data.isnull().sum()


# In[15]:


data.shape


# In[16]:


data.head(10)


# In[17]:


data['MetColor'].mean()


# In[18]:


data['MetColor'].head()


# In[19]:


import numpy as np


# In[20]:


data['MetColor'].replace(np.NaN,data['MetColor'].mean()).head()


# In[21]:


data.head(10)


# In[23]:


data['CC'].mean()


# In[24]:


data['CC'].head()


# In[25]:


data[['Age',"KM"]].head(20)


# In[ ]:




