#!/usr/bin/env python
# coding: utf-8

# # Exercise 6: Weather data calculation
# 
# ### Part 1 
# 
# You should start by reading the data file.
# 
# - Read the data file into variable the variable `data`
#     - Skip the second row
#     - Convert the no-data values (`-9999`) into `NaN`

import pandas as pd
import numpy as np

data = None

# YOUR CODE HERE 1

 #Read the data File / skip rows 2 / convert nulldata/ split with whitespace
data = pd.read_csv('data/1091402.txt',skiprows=[1],na_values=-9999,delim_whitespace=True)


# ### Part 2 
# 
# In this section, you will calculate simple statistics based on the input data:
# 
# - Calculate how many no-data (NaN) values there are in the `TAVG` column
#     - Assign your answer to a variable called `tavg_nodata_count`.

tavg_nodata_count = None
#YOUR CODE HERE 2
 #variable "s" is the data of line TAVG
s=data['TAVG']
 #count the number of null functions
tavg_nodata_count = s.isnull().sum()

#CAUTION!!! DON'T EDIT THIS PART START
# Print out the solution:
print('Number of no-data values in column "TAVG":',tavg_nodata_count)
#CAUTION!!! DON'T EDIT THIS PART END


# - Calculate how many no-data (NaN) values there are for the `TMIN` column
#     - Assign your answer into a variable called `tmin_nodata_count`

tmin_nodata_count = None
#YOUR CODE HERE 3
 #variable "t" is the data of line TAVG
t=data['TMIN']
 #count the number of null functions
tmin_nodata_count = t.isnull().sum()

#CAUTION!!! DON'T EDIT THIS PART START
# Print out the solution:
print('Number of no-data values in column "TMIN":', tmin_nodata_count)
#CAUTION!!! DON'T EDIT THIS PART END


# - Calculate the total number of days covered by this data file
#     - Assign your answer into a variable called day_count

day_count = None 
#YOUR CODE HERE 4
 #variable "u" is the data of line 'DATE'
u=data['DATE']
 #count the number of days
day_count=u.count()

#CAUTION!!! DON'T EDIT THIS PART START
# Print out the solution:
print("Number of days:", day_count)
#CAUTION!!! DON'T EDIT THIS PART END

# - Find the date of the oldest (first) observation
#     - Assign your answer into a variable called `first_obs`


first_obs = None
 
# YOUR CODE HERE 5
 #Find the oldest observation
first_obs = data['DATE'][0]

#CAUTION!!! DON'T EDIT THIS PART START
# Print out the solution:
print('Date of the first observation:',first_obs)
#CAUTION!!! DON'T EDIT THIS PART END

# - Find the date of the most recent (last) observation
#     - Assign your answer into a variable called `last_obs`

last_obs = None

# YOUR CODE HERE 6
 #Find the recent observation
last_obs = data['DATE'][len(data['DATE'])-1]

#CAUTION!!! DON'T EDIT THIS PART START
# Print out the solution:
print('Date of the last observation:', last_obs)
#CAUTION!!! DON'T EDIT THIS PART END


# - Find the average temperature for the whole data file (all observtions) from column `TAVG`
#     - Assign your answer into a variable called `avg_temp`

avg_temp = None

# YOUR CODE HERE 7
 #calculate average temp
avg_temp = s.sum()/(len(data['TAVG'])-tavg_nodata_count)

#CAUTION!!! DON'T EDIT THIS PART START
# Print out the solution:
print('Average temperature (F) for the whole dataset:', round(avg_temp, 2))
#CAUTION!!! DON'T EDIT THIS PART END


# - Find the average `TMAX` temperature over the Summer of 1969 (months May, June, July, and August of the year 1969)
#     - Assign your answer into a variable called `avg_temp_1969`

avg_temp_1969 = None

# YOUR CODE HERE 8
#"data_count" is the variable of dates in summer
data_count = 0
#"sum" is sum of `TMAX` temperature over the Summer of 1969 (months May, June, July, and August of the year 1969)
sum = 0
# count the sum of temprature and data_count
for i in range(len(data['TMAX'])-1):
  if(data['DATE'][i]>=19690501):
    if(data['DATE'][i]<=19690831):
      if(np.isnan(data['DATE'][i])==False):
        sum += data['TMAX'][i]
        data_count+=1  
#calcurate average of temp
avg_temp_1969 = sum/data_count

#CAUTION!!! DON'T EDIT THIS PART START
# This test print should print a number
print('Average temperature (F) for the Summer of 69:', round(avg_temp_1969, 2))
#CAUTION!!! DON'T EDIT THIS PART END


# ## Problem 2 - Calculating monthly average temperatures (*3 points*)
# 

monthly_data = None

# YOUR CODE HERE 9
month=[] #month in data['DATE'] 1~12
celtem=[] #temp_celsius in data['TAVG']
for i in range(len(data['DATE'])-1):
  month.append(int(data['DATE'][i]%10000/100))
  celtem.append(data['TAVG'][i]-32)
#calcurate monthly temp average
monthly_average = []
total_temp=0
days_count=0 #We must count the number of monthly data, because there might be null data.
for i in range(len(data['DATE'])-1): #see all celtem
  if(i==0): #first day
    total_temp+=celtem[i]
    days_count+=1
  else:
    if(month[i] != month[i-1]): #when the month changed
      monthly_average.append(total_temp/days_count) #append the average of celtem
      total_temp=celtem[i] #reset the total and plus
      days_count=1 #reset the count and plus
    else:
      total_temp += celtem[i]
      days_count +=1

monthly_average.append(total_temp/days_count)  #append last month (2017/Oct)  
monthly_data=pd.DataFrame({'temp_celsius':monthly_average})

#CAUTION!!! DON'T EDIT THIS PART START
# This test print should print the length of variable monthly_data
print(len(monthly_data))

# This test print should print the column names of monthly_data
print(monthly_data.columns.values)

# This test print should print the mean of temp_celsius
print(round(monthly_data['temp_celsius'].mean(),2))

# This test print should print the median of temp_celsius
print(round(monthly_data['temp_celsius'].median(), 2))
#CAUTION!!! DON'T EDIT THIS PART END

def func1():
    return tavg_nodata_count
def func2():
    return tmin_nodata_count
def func3():
    return day_count
def func4():
    return first_obs
def func5():
    return last_obs
def func6():
    return round(avg_temp,2)
def func7():
    return round(avg_temp_1969,2)
def func8():
    return len(monthly_data)
def func9():
    return monthly_data.columns.values
def func10():
    return round(monthly_data['temp_celsius'].mean(),2)
def func11():
    return round(monthly_data['temp_celsius'].median(),2)