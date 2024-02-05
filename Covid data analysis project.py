#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from datetime import datetime 


# In[2]:


covid_df=pd.read_csv("D:\Rambabu Contract\Training\Projects\covid_19-india Project\covid_19_india.csv")


# In[3]:


covid_df.head()


# In[4]:


print(covid_df[-5:])


# In[5]:


covid_df.info()


# In[6]:


covid_df.describe() #### used for numerical value only


# In[7]:


vaccine_df=pd.read_csv("D:\Rambabu Contract\Training\Projects\covid_19-india Project\covid_vaccine_statewise.csv")


# In[8]:


vaccine_df.head()


# In[9]:


covid_df.drop(["Sno","Time","ConfirmedIndianNational","ConfirmedForeignNational"], inplace=True,axis=1)


# In[10]:


covid_df


# In[11]:


covid_df["Date"] = pd.to_datetime(covid_df["Date"], format = '%Y-%m-%d')


# In[12]:


covid_df.head(15000)


# In[13]:


covid_df.tail(40)


# In[14]:


covid_df = covid_df.dropna()


# In[15]:


### find the active cases

covid_df['Active_Cases'] = covid_df['Confirmed'] - covid_df['Cured'] + covid_df['Deaths']


# In[16]:


covid_df


# In[17]:


covid_df.tail()


# In[18]:


covid_df = covid_df.dropna()


# In[19]:


covid_df


# In[20]:


statewise = pd.pivot_table(covid_df, values = ["Confirmed","Deaths","Cured","Active_Cases"], index="State/UnionTerritory", aggfunc = max)


# In[21]:


statewise["Recovery Rate"] = statewise["Cured"]*100/statewise["Confirmed"]


# In[22]:


statewise["Mortality Rate"] = statewise["Deaths"]*100/statewise["Confirmed"]


# In[23]:


statewise 


# In[24]:


statewise = statewise.sort_values(by = "Confirmed", ascending = False)


# In[25]:


statewise


# In[26]:


statewise.style.background_gradient(cmap = "cubehelix")


# In[27]:


statewise.style.background_gradient(cmap = "viridis")


# In[28]:


statewise.style.background_gradient(cmap = "plasma")


# In[29]:


statewise.style.background_gradient(cmap = "inferno")


# In[30]:


statewise.style.background_gradient(cmap = "magma")


# In[31]:


## top 10 active cases states 

top_10_active_cases = covid_df.groupby(by = 'State/UnionTerritory').max()[['Active_Cases','Date']].sort_values(by = ['Active_Cases'],ascending=False).reset_index()


# In[32]:


top_10_active_cases


# In[33]:


fig = plt.figure(figsize=(16,9))


# In[34]:


plt.title("Top 10 states with most active cases in India", size=20)


# In[35]:


ax = sns.barplot(data = top_10_active_cases.iloc[:10], 
                 y = "Active_Cases", x = "State/UnionTerritory", linewidth = 2, edgecolor = "Black")
plt.show()


# In[36]:


top_10_active_cases = covid_df.groupby(by = 'State/UnionTerritory').max()[['Active_Cases','Date']].sort_values(by = ['Active_Cases'],ascending=False).reset_index()
fig = plt.figure(figsize=(16,9))
plt.title("Top 10 states with most active cases in India", size=20)
ax = sns.barplot(data = top_10_active_cases.iloc[:10], y = "Active_Cases", x = "State/UnionTerritory", linewidth = 2, edgecolor = "Black")
plt.xlabel("State")
plt.ylabel("Total Active Cases")
plt.show()


# In[37]:


### Top states with highest death 

top_10_deaths = covid_df.groupby(by = 'State/UnionTerritory').max()[['Deaths','Date']].sort_values(by = ['Deaths'],ascending=False).reset_index()


# In[38]:


top_10_deaths.dtypes


# In[39]:


top_10_deaths["Date"] = pd.to_datetime(top_10_deaths["Date"], format = '%Y-%m-%d')


# In[40]:


top_10_deaths.dtypes


# In[41]:


fig = plt.figure(figsize=(16,9))


# In[42]:


plt.title("Top 10 states with most deaths in India", size=20)


# In[43]:


ax = sns.barplot(data = top_10_deaths.iloc[:10], 
                 y = "Deaths", x = "State/UnionTerritory", linewidth = 2, edgecolor = "Black")
plt.show()


# In[44]:


top_10_deaths = covid_df.groupby(by = 'State/UnionTerritory').max()[['Deaths','Date']].sort_values(by = ['Deaths'],ascending=False).reset_index()
fig = plt.figure(figsize=(16,9))
plt.title("Top 10 states with most deaths in India", size=20)
ax = sns.barplot(data = top_10_deaths.iloc[:10], y = "Deaths", x = "State/UnionTerritory", linewidth = 2, edgecolor = "Black")
plt.xlabel("State")
plt.ylabel("Total Deaths")
plt.show()


# In[45]:


### Growth Trend (hue is used for different color for lines)

fig = plt.figure(figsize=(12, 6))

ax = sns.lineplot(data=covid_df[covid_df['State/UnionTerritory'].isin(['Maharashtra', 'Karnataka', 'Kerala', 'Tamil Nadu', 'Uttar Pradesh'])],
                  x="Date", y="Active_Cases", hue="State/UnionTerritory")

ax.set_title("Top 5 Affected States in India", size=16)


# In[ ]:





# In[46]:


vaccine_df


# In[47]:


vaccine_df.rename(columns = {'Updated On' : 'Vaccine_Date'}, inplace=True)


# In[48]:


vaccine_df.head(10)


# In[49]:


vaccine_df.describe()


# In[50]:


vaccine_df.info()


# In[51]:


vaccine_df.isnull().sum()


# In[52]:


vaccination = vaccine_df.drop(columns = ['Sputnik V (Doses Administered)', 'AEFI', '18-44 Years (Doses Administered)','45-60 Years (Doses Administered)','60+ Years (Doses Administered)'], axis = 1)


# In[53]:


vaccination 


# In[54]:


vaccination.head(5)


# In[55]:


vaccination.tail(10)


# In[56]:


## Male Vs Female vaccination 
   
male = vaccination["Male(Individuals Vaccinated)"].sum()
female = vaccination["Female(Individuals Vaccinated)"].sum()
px.pie(names=["Male","Female"],values=[male,female], title = "Male and Female Vaccination")


# In[57]:


## remove rows where state is India 

vaccine = vaccine_df[vaccine_df.State!='India']


# In[58]:


vaccine


# In[59]:


vaccine.rename(columns = {"Total Individuals Vaccinated" : "Total"}, inplace=True)


# In[60]:


vaccine.head()


# In[61]:


### Most vaccinated state 

max_vac = vaccine.groupby('State')['Total'].sum().to_frame('Total')
max_vac = max_vac.sort_values('Total', ascending=False)[:5]
max_vac


# In[ ]:





# In[ ]:





# In[62]:


fig = plt.figure(figsize=(10, 5))
plt.title("Top 5 Vaccinated States in India", size=20)
x = sns.barplot(data=max_vac, y=max_vac.Total, x=max_vac.index, linewidth=2, edgecolor='red')
plt.xlabel("States")
plt.ylabel("Vaccination")
plt.show()


# In[63]:


min_vac = vaccine.groupby('State')['Total'].sum().to_frame('Total')
min_vac = min_vac.sort_values('Total', ascending=True)[:5]
min_vac


# In[64]:


min_vac = vaccine.groupby('State')['Total'].sum().to_frame('Total')
min_vac = min_vac.sort_values('Total', ascending=True)[:5]
fig = plt.figure(figsize=(15, 5))
plt.title("Bottom 5 Vaccinated States in India", size=20)
x = sns.barplot(data=min_vac, y=min_vac.Total, x=min_vac.index, linewidth=2, edgecolor='red')
plt.xlabel("States")
plt.ylabel("Vaccination")
plt.show()


# In[ ]:




