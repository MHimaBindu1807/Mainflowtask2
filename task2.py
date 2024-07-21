#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd


# In[13]:


data = pd.read_csv("H:\\ml lab\\01.Data Cleaning and Preprocessing.csv")


# In[14]:


type(data)


# In[15]:


data.info


# In[16]:


data=data.drop_duplicates()
data


# In[18]:


data.isnull().sum()


# In[19]:


data2=data.fillna(value=0)
data2


# In[20]:


import numpy as np
from scipy import stats


# In[21]:


data2.columns


# In[23]:


data2.drop(['Observation'],axis=1,inplace=True)
data2


# In[24]:


data.notnull()


# In[26]:


data3=data.fillna(method='pad')
data3


# In[27]:


data4=data.fillna(method='bfill')
data4


# In[29]:


data2.describe()


# In[ ]:




