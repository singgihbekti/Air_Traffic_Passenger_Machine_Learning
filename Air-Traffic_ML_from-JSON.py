#!/usr/bin/env python
# coding: utf-8

# # Necessary Libraries
# Define the necessary libraies.
# Data can be accessed by both JSON and CSV. 
# In this part, we will read from JSON format and create simple ML.

# In[1]:


#source: 
#https://data.sfgov.org/resource/rkru-6vcg.json
#https://data.world/singgih/airtrafficpassengerdataproject-4-11-2021/workspace/file?agentid=data-society&datasetid=air-traffic-passenger-data&filename=Air_Traffic_Passenger_Statistics.csv


import requests
import pandas as pd
from pandas.io.json import json_normalize
#from mlxtend.plotting import plot_decision_regions
from sklearn.metrics import confusion_matrix,classification_report
import matplotlib.pyplot as plt #ใช้ plot graph
import numpy as np
from sklearn import datasets, neighbors
import itertools
import random
from sklearn.cluster import KMeans
import csv


# # Get Response Air Traffic API:

# In[2]:


data_response = requests.get("https://data.sfgov.org/resource/rkru-6vcg.json") ## <== Air Traffic API


# # See Response Code (you should get 200 OK)
# for more information : https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
# 
# 200 means that the response is successfully sent

# In[3]:


print(data_response.status_code)


# # Let's see your Raw Data

# In[4]:


print(data_response.json())


# Now, put the JSON format in the frame to make it easier to understand

# In[5]:


data_json = pd.read_json("https://data.sfgov.org/resource/rkru-6vcg.json")
data_json.head(5)


# See the data only based on "activity period" and Passenger Count" (coloumn)

# In[6]:


df1=data_json[["activity_period", "geo_region", "activity_type_code", "passenger_count"]]
df1.head()


# # Now We want to see specifically for "deplaned" activity
# It can be use to predict how many tourist come to this airport

# In[ ]:





# In[ ]:





# # Predict the Air Traffic in the future
# Using the data in 2020, we want to predict tourist coming to the airport

# In[ ]:





# In[ ]:




