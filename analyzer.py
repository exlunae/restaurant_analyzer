
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data_table = pd.read_csv('data/data.txt',encoding='latin-1')
data_table


# In[2]:


data_table = data_table.dropna(subset = ['ZIPCODE'])
#data_table = data_table[np.isfinite(data_table['ZIPCODE'])]
data_table


# In[3]:


#Drop duplicate zipcodes and keep the most recent ones
duplicated = data_table.duplicated(subset='CAMIS')
duplicated


# In[4]:


data_table = data_table.sort_values(by=['INSPDATE'])

data_table = data_table.drop_duplicates(subset='CAMIS',keep='last')
data_table

#^^^ WILL SORT THEN KEEP LAST ONES


# In[10]:


#Drop all rows in the series with zipcodes that appear less than 100 times 
def display_valid_zips(zip_series):
    for zip, frequency in zip_series.iteritems():
        if frequency <= 100:
            zip_series = zip_series.drop(zip)
    return zip_series

zip_restaurants = display_valid_zips(data_table['ZIPCODE'].value_counts())
zip_restaurants

#display_valid_zips(data_table['ZIPCODE'].value_counts)
#data_table['ZIPCODE'].value_counts()


# In[9]:


#data_table.groupby(['CAMIS', 'ZIPCODE'])['SCORE'].sum().sort_values(ascending=False)


# In[55]:


#Gather 92 series/list of all 92 restaurants and tally up the average scores
average_scores = {}
for k,v in zip_restaurants.iteritems():
    zip_df = data_table[data_table['ZIPCODE'] == k]
    zip_average = zip_df['SCORE'].sum() / v
    
    average_scores.update({k:float('%.1f'%zip_average)})
    
print(average_scores)
                           


# In[56]:


final_data = []
for k,v in zip_restaurants.iteritems():
    score = average_scores.get(k)
    data = (k, score, v)
    final_data.append(data)
    
print(final_data)


# In[57]:


sorted_by_second = sorted(final_data, key=lambda tup: tup[1], reverse=True)
print(sorted_by_second)

