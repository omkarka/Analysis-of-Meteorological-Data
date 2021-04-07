# Analysis Of Meteorological Data

# Import Libraries

import numpy as np 
import pandas as pd 
%matplotlib inline
import matplotlib.pyplot as plt

# Load DataSet
df = pd.read_csv('WeatherHistory.csv')
df.shape

df.dtypes

df['Formatted Date'] = pd.to_datetime(df['Formatted Date'], utc=True)
df['Formatted Date']

df.dtypes

df=df.set_index('Formatted Date')
df.head()

# After Resampling
data_columns = ['Apparent Temperature (C)', 'Humidity']
df_monthly_mean = df[data_columns].resample('MS').mean()
df_monthly_mean.head()

# Plotting the variation in Apparent Temperature and Humidity with time
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
plt.figure(figsize=(14,6))
plt.title("Variation in Apparent Temperature and Humidity with time")
sns.lineplot(data=df_monthly_mean)

# retrieving the data of a particular month from every year, say April
mon_april = df_monthly_mean[df_monthly_mean.index.month==4]
print(mon_april) 

mon_april.dtypes

plt.figure(figsize=(14,6))
plt.title("plot of average temperature and humidity of the month of april over 10 years")
plt.plot(mon_april)