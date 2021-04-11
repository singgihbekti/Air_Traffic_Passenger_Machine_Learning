#!/usr/bin/env python
# coding: utf-8

# In[20]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
get_ipython().run_line_magic('matplotlib', 'inline')


# In[23]:


#https://data.world/singgih/airtrafficpassengerdataproject-4-11-2021/workspace/file?agentid=data-society&datasetid=air-traffic-passenger-data&filename=Air_Traffic_Passenger_Statistics.csv

df = pd.read_csv('https://query.data.world/s/ns3l3xcga6fa4ypmv4p6znhwna7kke')
print(df)


# In[ ]:




