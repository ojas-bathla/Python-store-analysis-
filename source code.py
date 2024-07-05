#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# In[2]:


df = pd.read_csv(r"C:\Users\DELL\Downloads\SampleSuperstore.csv")


# In[3]:


# Check for missing values
print(df.isnull().sum())


# In[4]:


# Handle missing values (example: filling or dropping)
df = df.dropna()


# In[5]:


df.head()


# In[6]:


print(df.dtypes)


# In[7]:


# Sales by Region
sales_by_region = df.groupby('Region')['Sales'].sum().reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(x='Sales', y='Region', data=sales_by_region)
plt.title('Sales by Region')
plt.show()


# In[8]:


# Profit by Region
profit_by_region = df.groupby('Region')['Profit'].sum().reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(x='Profit', y='Region', data=profit_by_region)
plt.title('Profit by Region')
plt.show()


# In[9]:


# Discount vs Sales
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Discount', y='Sales', data=df)
plt.title('Discount vs Sales')
plt.show()


# In[10]:


# Discount vs Profit
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Discount', y='Profit', data=df)
plt.title('Discount vs Profit')
plt.show()


# In[11]:


# Profit by Ship Mode
profit_by_ship_mode = df.groupby('Ship Mode')['Profit'].sum().reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(x='Profit', y='Ship Mode', data=profit_by_ship_mode)
plt.title('Profit by Ship Mode')
plt.show()


# In[12]:


# Sales by Segment
sales_by_segment = df.groupby('Segment')['Sales'].sum().reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(x='Sales', y='Segment', data=sales_by_segment)
plt.title('Sales by Segment')
plt.show()


# In[13]:


# Profit by Segment
profit_by_segment = df.groupby('Segment')['Profit'].sum().reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(x='Profit', y='Segment', data=profit_by_segment)
plt.title('Profit by Segment')
plt.show()


# In[14]:


# Sales by Category
sales_by_category = df.groupby('Category')['Sales'].sum().reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(x='Sales', y='Category', data=sales_by_category)
plt.title('Sales by Category')
plt.show()


# In[15]:


# Profit by Sub-Category
profit_by_sub_category = df.groupby('Sub-Category')['Profit'].sum().reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(x='Profit', y='Sub-Category', data=profit_by_sub_category)
plt.title('Profit by Sub-Category')
plt.show()


# In[16]:


# Quantity vs Profit
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Quantity', y='Profit', data=df)
plt.title('Quantity vs Profit')
plt.show()


# In[17]:


# Calculate average discount by segment
avg_discount_by_segment = df.groupby('Segment')['Discount'].mean().reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(x='Discount', y='Segment', data=avg_discount_by_segment)
plt.title('Average Discount by Segment')
plt.xlabel('Average Discount')
plt.ylabel('Segment')
plt.show()

