
# coding: utf-8

# # Working on data from 27th January 2020 to 30th April 2020

# In[3]:

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
print("Modules are Imported")


# In[26]:

get_ipython().magic('matplotlib inline')


# # -------------------------------------Confirmed Cases File--------------------------------------------

# # 1.Importing confirmed covid 19 dataset file

# In[9]:

corona_dataset_csv  = pd.read_csv("Datasets/covid19_Confirmed_dataset.csv")  #importing the required file
corona_dataset_csv.head(10)   


# # 2.Checking shape

# In[8]:

corona_dataset_csv.shape


# # 3.Dropping useless column

# In[12]:

corona_dataset_csv.drop(["Lat" , "Long" , "Province/State"] , axis = 1 , inplace = True)  #inplace used to make changes in files itself
corona_dataset_csv.head()   #by default 5 rows


# # 4.Aggregating the rows by the country

# In[17]:

corona_dataset_aggregeted = corona_dataset_csv.groupby("Country/Region").sum()    #sum() uesd to sum all the values of columns with same country name
corona_dataset_aggregeted.head()


# In[45]:

corona_dataset_aggregeted.shape


# # 5.Visualizing Data of a particular country.

# In[85]:

corona_dataset_aggregeted.loc["China"]


# # 6.Graph of data related to a country

# In[27]:

corona_dataset_aggregeted.loc["China"].plot()
corona_dataset_aggregeted.loc["Italy"].plot()
corona_dataset_aggregeted.loc["India"].plot()
plt.legend()


# # 7.Graph for data of a particular time span

# In[36]:

corona_dataset_aggregeted.loc["China"][:3].plot()  #3 days
corona_dataset_aggregeted.loc["India"][:3].plot()
plt.legend()


# # 8.Calculating first derrivative Curve

# clear picture of change in corona cases.

# In[37]:

corona_dataset_aggregeted.loc["China"].diff().plot()


# # 9.Getting max no. of cases ocurred in a single day.

# Maximum infection rate.

# In[38]:

corona_dataset_aggregeted.loc["China"].diff().max()


# In[39]:

corona_dataset_aggregeted.loc["India"].diff().max()


# In[41]:

corona_dataset_aggregeted.loc["Italy"].diff().max()


# # 10.Maximum infection rate for all countries

# In[86]:

countries = list(corona_dataset_aggregeted.index)
max_infection_rates = []
for c in countries:
    max_infection_rates.append(corona_dataset_aggregeted.loc[c].diff().max())
max_infection_rates


# In[87]:

corona_dataset_aggregeted["max_infection_rates"] = max_infection_rates
corona_dataset_aggregeted.head()


# # 11.Forming new data from maximum infection rates only.

# In[74]:

corona_new_data = pd.DataFrame(corona_dataset_aggregeted["max_infection_rates"])
corona_new_data.head()


# # ------------------------------------World Happiness Report----------------------------------------

# # 12.Importing world happiness report

# In[48]:

happiness_report_csv = pd.read_csv("Datasets/worldwide_happiness_report.csv")
happiness_report_csv.head()


# # 13.Dropping the useless columns.

# In[50]:

useless_columns = ["Overall rank" , "Score" , "Generosity" , "Perceptions of corruption"]
happiness_report_csv.drop(useless_columns , axis = 1 , inplace = True)
happiness_report_csv.head()


# # 14.Changing the indices of Dataframe

# In[53]:

happiness_report_csv.set_index("Country or region" , inplace = True)
happiness_report_csv.head()


# # -----------------------------------------Joining two datasets-----------------------------------------

# In[54]:

corona_new_data.shape


# In[56]:

happiness_report_csv.shape


# In[62]:

data = corona_new_data.join(happiness_report_csv , how = "inner")
#Used  inner join because no. of countries in corona_new_data is more than that in happiness_report_csv 
data.head()


# In[60]:

data.shape


# # 15.Correlation Matrix

# In[64]:

data.corr()


# # ------------------------------Visualization of the combined table-------------------------------

# Comparing the results too see how the covid 19 affected the happiness of people around the world

# # 16.Plotting Gdp V.S Maximum infection rate

# In[71]:

x = data["GDP per capita"]
y = data["max_infection_rates"]
sns.regplot(x,y)

#since,it's an older version of jupiter so scatterplot can't be used.
#instead of it regplot() is used.


# In[72]:

#y ranges from 0 to 26849 therefore in such a long range graph formed can't be understood very well 
#Therefore logarithmic function is used to make the range small
#log scaling ranges from 0 - 10

x = data["GDP per capita"]
y = data["max_infection_rates"]
sns.regplot(x,np.log(y))


# # Plotting Social support V.S Maximum infection rate

# In[78]:

x = data["Social support"]
y = data["max_infection_rates"]

sns.regplot(x,np.log(y))


# # Plotting Healthy life expecancy V.S Maximum infection rate

# In[80]:

x = data["Healthy life expectancy"]
y = data["max_infection_rates"]

sns.regplot(x , np.log(y))


# # Plotting Freedom to make life choices V.S Max Infection rate

# In[81]:

x = data["Freedom to make life choices"]
y = data["max_infection_rates"]

sns.regplot(x , np.log(y))

