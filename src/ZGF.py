
# coding: utf-8

# # ZGL Analytics
# This document contains analytics samples from ZGL data.
# 
# ## Import required data

# In[3]:


import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')

df = pd.read_excel("/home/Salohy_Mike_2018.xlsx")


# ## Participants statistics
# ### How many men and women participate this year?

# In[4]:


sex = df['Geschlecht'].value_counts()
print(sex)
df['Geschlecht'].value_counts().plot.pie()


# ### Likely Route
# 
# As we see below, the short route is likely. Almost 60 participants have chosen this route

# In[5]:


df['Strecke'].value_counts().plot.bar()


# ### Likely route by women and men respectively

# In[6]:


most_chosen_route_by_all = df.groupby(["Strecke", "Geschlecht"]).size()
print(most_chosen_route_by_all)
df.groupby(["Strecke", "Geschlecht"]).size().plot.bar(stacked=True)


# ### Top 6 women for short route

# In[7]:


is_women = (df['Geschlecht'] == 'w') & (df['Strecke'] == 'k')
df[is_women].sort_values(by=['Zeit']).head(6)


# ### Top 6 women for long route

# In[8]:


is_women = (df['Geschlecht'] == 'w') & (df['Strecke'] == 'l')
df[is_women].sort_values(by=['Zeit']).head(3)


# ### Top 6 men for short route

# In[9]:


is_man = (df['Geschlecht'] == 'm') & (df['Strecke'] == 'k')
df[is_man].sort_values(by=['Zeit']).head(6)


# ### Top 6 men for long route

# In[10]:


is_man = (df['Geschlecht'] == 'm') & (df['Strecke'] == 'l')
df[is_man].sort_values(by=['Zeit']).head(6)

