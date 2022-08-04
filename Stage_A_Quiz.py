
# ## Stage A Quiz

# #### Stage A: Introduction to Python for Machine Learning


#Importing useful libraries and packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# **********************************************

# Question 1
# Creating a pandas DataFrame using a given list

lst = [[35, 'Portugal', 94], [33, 'Argentina', 93], [30 , 'Brazil', 92]]
col = ['Age','Nationality','Overall']

#pd.Dateframe(lst, column = ['Age','Nationality','Overall'], index = [1,2,3])
pd.DataFrame(lst, columns = col, index = [i for i in range(1,4)])
#pd.datframe(lst, column = ['Age','Nationality','Overall'],index = [1,2,3])
#pd.Dataframe(lst, columns = col, index = [1,2,3])

# Out[1]:
#	    Age	Nationality	Overall
#   1	35	Portugal	94
#   2	33	Argentina	93
#   3	30	Brazil	    92

# **********************************************


#   Question 2
#   Selecting a matrix from an array

array = np.array([[94, 89, 63],[93, 92, 48], [92, 94, 56]])
#array[ : 1, 1 : ]
#array[ : 2, 0 : ]
#array[ 1 : , : ]
#array[ : 1, 1 :] 
array[ : 2, 1 : ] 

# Out[2]:
array([[89, 63],
       [92, 48]])
       
# **********************************************


#Question 5
#List Comprehension

S = [['him', 'sell'], [90, 28, 43]]
S[0][1][1]

# Out[5]: 
     'e' 
     
# **********************************************


#Question 6
# Type Error
my_tuppy = (1,2,5,8)
my_tuppy[2] = 6

## TypeError: 'tuple' object does not support item assignment

# **********************************************


#Question 7
#Assigning an element from a list to a variable x

y = [(2, 4), (7, 8), (1, 5, 9)]
x = y[1][-1]
x
# Out[7]:
    8
# **********************************************

# #### Analysis of a given Data Set (Food Balance Sheet)


# Code to read csv file
df = pd.read_csv("FoodBalanceSheets_E_Africa_NOFLAG.csv",encoding='latin-1')
df.head()

# **********************************************

#Question 11
# Finding the total sum of Animal Fat produced in 2014 and 2017 respectively

#df.groupby("Item")[["Y2014", "Y2017"]].sum().loc["Animal fats"]
df.groupby('Item').sum().loc[['Animal fats'],['Y2014','Y2017']]


# Out[11]:
                    Y2014	    Y2017
Item		
Animal fats	    209460.54	269617.53

# **********************************************

#Question 12
# Finding  the mean and standard deviation across the whole dataset
# for the year 2015 to 3 decimal places

# round(df.describe()["Y2015"], 3)
round(df.describe().loc[['mean','std'], ['Y2015']], 3)


# Out[12]:
              Y2015
mean	    135.236
std	       1603.404

# **********************************************

#Question 13
# Finding the total number of missing data in 2016 to 2 decimal places

#sum_2016 = round(df.isnull().sum()['Y2016'], 2)
missing_data = df["Y2016"] .isna().sum()
print(missing_data)


# Out[13]:
    1535
    
# **********************************************

# Question 13 
# Finding the percentage of missing data in 2016 to 2 decimal places

missing_data = df["Y2016"] .isna().sum()
percentage = (missing_data / df.shape[0]) * 100
print(round(percentage, 2))
missing_data, round(percentage, 2)


# Out[14]:
       2.52
(1535, 2.52)
# **********************************************

# Question 14
# Getting the highest correlation with ‘Element Code'

#df.corr()["Element Code"]["Y2014":]

years= ['Y2014', 'Y2015', 'Y2016','Y2017', 'Y2018']
x=df.corr().abs()
y=x.unstack()
so=y.sort_values(kind='quicksort')
print(so['Element Code'][years].idxmax())

# In[14]:
    Y2014
    
# **********************************************

#Question 15
# Getting the highest sum of Import Quantity

# df.groupby("Element").sum().loc["Import Quantity", "Y2014":]

df.groupby('Element').sum().loc[['Import Quantity'],years].idxmax(axis=1).reset_index(drop=True)

# Out[15]:
    0    Y2017
    dtype: object

# **********************************************

#Question 16
# Finding the total number of the sum of Production in 2014

#round(df.groupby('Element').sum().loc['Production']['Y2014'], 2)
df.groupby("Element").sum().loc["Production", "Y2014":]


# Out[16]:

Y2014    1931287.75
Y2015    1947019.39
Y2016    1943537.15
Y2017    2030056.89
Y2018    2075072.89
Name: Production, dtype: float64


# **********************************************

#Question 17
#  Finding the Element that had the highest sum in 2018

# print(df.groupby('Element').sum()['Y2018'].idxmax())
#df.groupby('Element').sum()
df[['Element','Y2018']].groupby('Element').sum().sort_values(by='Y2018', ascending = False)


# Out[17]:
                             Element           Y2018
                	
             Domestic supply quantity	    2161192.10
                           Production	    2075072.89
                                 Food	    1303841.28
        Total Population - Both sexes	    1140605.00
         Food supply (kcal/capita/day)	     455261.00
                           Processing	     308429.00
                      Import Quantity	     287997.09
                                 Feed	     233489.68
                      Export Quantity        181594.80
                               Losses	     163902.00
                 Other uses (non-food)	      91300.97
   Food supply quantity (kg/capita/yr)	      49056.85
                            Residuals	      34864.00
                                 Seed	      25263.14
                      Stock Variation	      20577.91
Protein supply quantity (g/capita/day)	      11833.56
    Fat supply quantity (g/capita/day)	      10258.69
                   Tourist consumption	         90.00

# **********************************************


#Question 18
# Finding the Element that had the 3rd lowest sum in 2018

# print(df.groupby('Element').sum()['Y2018'].nsmallest(3).idxmax())
df.groupby("Element")["Y2018", "Element"].sum().sort_values(by = "Y2018", ascending = True)


# Out[18]:
 
                              Element     	     Y2018
	
                  Tourist consumption	         90.00
    Fat supply quantity (g/capita/day)	      10258.69
Protein supply quantity (g/capita/day)	      11833.56
                      Stock Variation	      20577.91
                                 Seed	      25263.14
                            Residuals	      34864.00
   Food supply quantity (kg/capita/yr)	      49056.85
                 Other uses (non-food)	      91300.97
                               Losses	     163902.00
                      Export Quantity	     181594.80
                                 Feed	     233489.68
                      Import Quantity	     287997.09
                           Processing	     308429.00
         Food supply (kcal/capita/day)	     455261.00
        Total Population - Both sexes	    1140605.00
                                 Food	    1303841.28
                           Production	    2075072.89
             Domestic supply quantity	    2161192.10
 
 # **********************************************
 

#Question 19
# Finding the total Import Quantity in Algeria in 2018

df.groupby(['Element', 'Area']).sum().loc[['Import Quantity']]['Y2018'].reset_index()[['Area','Y2018']].iloc[[0]]
# df[['Element','Y2018']].groupby('Element').sum().sort_values(by='Y2018')

# Out[19]:
	   Area	       Y2018
0	Algeria	    36238.29

# **********************************************
 
# Question 20
# Finding the total number of unique countries in the dataset

df.groupby('Area').nunique().sum()['Area Code']

# Out[20]:
        49
       
 # **********************************************
