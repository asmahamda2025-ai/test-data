#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
df=pd.read_csv("Impact_of_Remote_Work_on_Mental_Health.csv")


# In[3]:


df.dtypes


# In[4]:


df = df.drop_duplicates()


# In[5]:


df.isnull().sum()
df['Mental_Health_Condition'] = df['Mental_Health_Condition'].fillna(df['Mental_Health_Condition'].mode()[0])
df['Physical_Activity'] = df['Physical_Activity'].fillna(df['Physical_Activity'].mode()[0])


# In[6]:


df['Access_to_Mental_Health_Resources'] = df['Access_to_Mental_Health_Resources'].str.capitalize()
df['Stress_Level'] = df['Stress_Level'].str.capitalize()
df['Sleep_Quality'] = df['Sleep_Quality'].str.capitalize()


# In[7]:


#ANALYSE 
#Bar chart stress Level
stress_counts = df["Stress_Level"].value_counts()
stress_counts.plot(kind="bar")
plt.title("Stress Level Distribution")
plt.xlabel("Stress Level")
plt.ylabel("Count")
plt.show()


# In[8]:


#phisical activity pie
plt.figure()#nouvelle page
counts = df["Physical_Activity"].value_counts()
plt.pie(counts, labels=counts.index, autopct='%1.1f%%')
plt.title("Physical Activity Distribution")
plt.show()

