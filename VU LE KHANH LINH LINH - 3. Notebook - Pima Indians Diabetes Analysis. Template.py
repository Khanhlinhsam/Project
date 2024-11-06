#!/usr/bin/env python
# coding: utf-8

# # Foundations of Data Science Project - Diabetes Analysis
# 
# ---------------
# ## Context
# ---------------
# 
# Diabetes is one of the most frequent diseases worldwide and the number of diabetic patients are growing over the years. The main cause of diabetes remains unknown, yet scientists believe that both genetic factors and environmental lifestyle play a major role in diabetes.
# 
# A few years ago research was done on a tribe in America which is called the Pima tribe (also known as the Pima Indians). In this tribe, it was found that the ladies are prone to diabetes very early. Several constraints were placed on the selection of these instances from a larger database. In particular, all patients were females at least 21 years old of Pima Indian heritage. 
# 
# -----------------
# ## Objective
# -----------------
# 
# Here, we are analyzing different aspects of Diabetes in the Pima Indians tribe by doing Exploratory Data Analysis.
# 
# -------------------------
# ## Data Dictionary
# -------------------------
# 
# The dataset has the following information:
# 
# * Pregnancies: Number of times pregnant
# * Glucose: Plasma glucose concentration over 2 hours in an oral glucose tolerance test
# * BloodPressure: Diastolic blood pressure (mm Hg)
# * SkinThickness: Triceps skin fold thickness (mm)
# * Insulin: 2-Hour serum insulin (mu U/ml)
# * BMI: Body mass index (weight in kg/(height in m)^2)
# * DiabetesPedigreeFunction: A function that scores the likelihood of diabetes based on family history.
# * Age: Age in years
# * Outcome: Class variable (0: a person is not diabetic or 1: a person is diabetic)

# ## Q 1: Import the necessary libraries and briefly explain the use of each library (3 Marks)

# In[1]:


# Remove _____ & write the appropriate library name

import numpy as np          
import pandas as pd          
import seaborn as sns        
import matplotlib.pyplot as plt  

get_ipython().run_line_magic('matplotlib', 'inline')


# #### Write your Answer here: 
Ans 1:
numpy is library for numerical operations
pandas is library for data manipulation and analysis
seaborn is library for statistical data visualization
matplotlib.pyplot is library for creating static, animated, and interactive visualizations




# ## Q 2: Read the given dataset (2 Marks)

# In[2]:


pima = pd.read_csv('VU LE KHANH LINH LINH - 2. diabetes.csv')





# ## Q3. Show the last 10 records of the dataset. How many columns are there? (2 Marks)

# In[3]:


# Remove ______ and write the appropriate number in the function

pima.tail(10)


# #### Write your Answer here: 
# 
Ans 3:The dataset has 9 columns.
# ## Q4. Show the first 10 records of the dataset (2 Marks)

# In[8]:


# Remove _____ & write the appropriate function name and the number of rows to get in the output

pima.head(10)
first_10_records


# ## Q5. What do you understand by the dimension of the dataset? Find the dimension of the `pima` dataframe. (3 Marks)

# In[7]:


pima.shape


# #### Write your Answer here: 
# 
Ans 5: Dimension of a dataset mean understanding how many rows and columns it contains. For a DataFrame, these dimensions tell us the number of observations (or rows) and the number of attributes or features recorded (or columns).


# ## Q6. What do you understand by the size of the dataset? Find the size of the `pima` dataframe. (3 Marks)

# In[9]:


# Remove _____ & write the appropriate function name

pima.size


# #### Write your Answer here: 
# 
Ans 6:
size of a dataset is the total number of elements it contains. This size is calculated by multiplying the number of rows by the number of columns in the DataFrame, meaning it shows the total number of individual data values the dataset holds.
# ## Q7. What are the data types of all the variables in the data set? (2 Marks)
# **Hint: Use the info() function to get all the information about the dataset.**

# In[10]:


# Remove _____ & write the appropriate function name
pima.info()


# #### Write your Answer here: 
# 
Ans 7:
The data type of a variable indicates what kind of data it stores, such as integers, floats, or strings. Knowing data types helps us choose the right methods for data analysis and manipulation.
# ## Q8. What do we mean by missing values? Are there any missing values in the `pima` dataframe? (4 Marks)

# In[12]:


# Remove _____ & write the appropriate function name
pima.isnull().values.any()


# #### Write your Answer here: 
# 
Ans 8:
Missing values in a dataset refer to instances where no data is recorded for a particular variable in a given observation. This can happen for various reasons, such as data entry errors, incomplete information, or respondents choosing not to answer certain questions. Missing values can pose issues in data analysis, as they may distort the results if not handled properly.
# ## Q9. What do the summary statistics of the data represent? Find the summary statistics for all variables except 'Outcome' in the `pima` data. Take one column/variable from the output table and explain all its statistical measures. (5 Marks)

# In[13]:


# Remove _____ & write the appropriate function name

pima.iloc[:, 0:8].describe()


# #### Write your Answer here: 
# 
Ans 9:
Summary statistics give us an overall picture of the data by showing key numerical metrics for each variable.It's help understand things like the average value, the spread of the data, and any potential outliers. Basically, summary statistics are useful for quickly seeing the general characteristics of each column in the dataset.
# ## Q 10. Plot the distribution plot for the variable 'BloodPressure'. Write detailed observations from the plot. (2 Marks)

# In[14]:


# Remove _____ & write the appropriate library name
sns.displot(pima['BloodPressure'], kind = 'kde')

plt.show()


# #### Write your Answer here: 
# 
Ans 10:
KDE plot to look at the distribution of BloodPressure
Main Peak: Most values cluster around 70 mm Hg, showing a typical range for many individuals.
Zero Values: There’s a spike near zero, likely due to missing or incorrect entries, since blood pressure can’t be zero.
Spread: The curve tails off at higher values, indicating fewer people with high blood pressure.
# ## Q 11. What is the 'BMI' of the person having the highest 'Glucose'? (2 Marks)

# In[15]:


# Remove _____ & write the appropriate function name

pima[pima['Glucose'] == pima['Glucose'].max()]['BMI']


# #### Write your Answer here: 
# 
Ans 11:
The BMI of the person with the highest Glucose is 42.9
# ## Q12.
# ### 12.1 What is the mean of the variable 'BMI'? 
# ### 12.2 What is the median of the variable 'BMI'? 
# ### 12.3 What is the mode of the variable 'BMI'?
# ### 12.4 Are the three measures of central tendency equal?
# 
# ### (4 Marks)

# In[16]:


# Remove _____ & write the appropriate function name

m1 = pima['BMI'].mean()  # mean
print(m1)

m2 = pima['BMI'].median()  # median
print(m2)

m3 = pima['BMI'].mode()[0]  # mode
print(m3)


# #### Write your Answer here: 
# 
Ans 12:
mean: 32.45080515543619
median: 32.0
mode: 32.0
No, the mean, median, and mode of BMI are not equal. This indicates a slight asymmetry in the distribution of BMI values in the dataset, which may suggest skewness
# ## Q13. How many women's 'Glucose' levels are above the mean level of 'Glucose'? (2 Marks)

# In[17]:


# Remove _____ & write the appropriate function name

pima[pima['Glucose'] > pima['Glucose'].mean()].shape[0]


# #### Write your Answer here: 
# 
Ans 13:
There are 343 women in the dataset with Glucose levels above the mean glucose level.
# ## Q14. How many women have their 'BloodPressure' equal to the median of 'BloodPressure' and their 'BMI' less than the median of 'BMI'? (2 Marks)

# In[20]:


# Remove _____ & write the appropriate column name

pima[(pima['BloodPressure'] == pima['BloodPressure'].median()) & (pima['BMI'] < pima['BMI'].median())].shape[0]


# #### Write your Answer here: 
# 
Ans 14: There is 22 woman in the dataset who has a BloodPressure equal to the median blood pressure and a BMI less than the median BMI.
# ## Q15. Create a pairplot for the variables 'Glucose', 'SkinThickness', and 'DiabetesPedigreeFunction'. Write your observations from the plot. (3 Marks)

# In[21]:


# Remove _____ & write the appropriate function name

sns.pairplot(data = pima, vars = ['Glucose', 'SkinThickness', 'DiabetesPedigreeFunction'], hue = 'Outcome')
plt.show()


# #### Write your Answer here: 
# 
Ans 15:
The chart above is a pairplot between the variables Glucose, SkinThickness, and DiabetesPedigreeFunction, categorized by Outcome (0: non-diabetic, 1: diabetic).
Diabetic individuals (orange) generally have higher glucose levels than non-diabetic individuals (blue).
There’s no clear difference between the two groups for this variable.
There’s a wide distribution, but diabetic individuals tend to have slightly higher values.
This pairplot makes it easy to compare the relationships between variables and diabetes status.
# ## Q16. Plot the scatterplot between 'Glucose' and 'Insulin'. Write your observations from the plot. (4 Marks)

# In[22]:


# Remove _____ & write the appropriate function name

sns.scatterplot(x = 'Glucose', y = 'Insulin', data = pima)
plt.show()


# #### Write your Answer here: 
# 
Ans 16:
This scatterplot shows the relationship between Glucose and Insulin levels
There’s a general positive trend, meaning as glucose levels increase, insulin levels also tend to rise.
Many points lie along the zero line for insulin, likely indicating missing or unrecorded values.
A few outliers have very high insulin levels (above 600), which could impact analysis or suggest unique cases.

# ## Q 17. Plot the boxplot for the 'Age' variable. Are there outliers? (2 Marks)

# In[23]:


# Remove _____ & write the appropriate function and column name 

plt.boxplot(pima['Age'])

plt.title('Boxplot of Age')
plt.ylabel('Age')
plt.show()


# #### Write your Answer here: 
# 
Ans 17:
The boxplot shows the distribution of Age
Most ages fall between 20 and 50, with the median around 30.
There are several outliers above 60, represented by individual points, with one reaching around 80.
This means that while most of the group is relatively young, there are a few older individuals in the dataset.
# ## Q18. Plot histograms for the 'Age' variable to understand the number of women in different age groups given whether they have diabetes or not. Explain both histograms and compare them. (5 Marks)

# In[25]:


# Remove _____ & write the appropriate function and column name

plt.hist(pima[pima['Outcome'] == 1]['Age'], bins = 5)
plt.title('Distribution of Age for Women who has Diabetes')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()


# In[26]:


# Remove _____ & write the appropriate function and column name

plt.hist(pima[pima['Outcome'] == 0]['Age'], bins = 5)
plt.title('Distribution of Age for Women who do not have Diabetes')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()


# #### Write your Answer here: 
# 
Ans 18:
Women Without Diabetes: The age distribution is highly concentrated among younger women, particularly in the 20-30 age range, with frequency quickly dropping for older age groups. This suggests that the majority of women without diabetes are younger.

Women With Diabetes: The age distribution is more evenly spread across age groups from 20 to 60, though there’s a slight decrease in older groups. The chart indicates that diabetes is more common across a wider range of ages, not just younger women.

This comparison suggests that diabetes may affect women across a broader age spectrum, while the non-diabetic group is skewed towards younger ages.


# ## Q 19. What is the Interquartile Range of all the variables? Why is this used? Which plot visualizes the same? (5 Marks)

# In[27]:


# Remove _____ & write the appropriate variable name

Q1 = pima.quantile(0.25)
Q3 = pima.quantile(0.75)
IQR = Q3 - Q1
print(IQR)


# #### Write your Answer here: 
# 
Ans 19:
The IQR is used to measure the spread of the middle 50% of the data, giving a robust sense of the data's variability without being affected by extreme values (outliers).
It helps identify outliers. Values beyond 1.5 times the IQR from Q1 or Q3 are considered potential outliers.
The Boxplot visualizes the IQR.
In a boxplot, the box represents the IQR (ranging from the first quartile (Q1) to the third quartile (Q3)). The whiskers extend to show the range, and any points beyond the whiskers are considered outliers.
# ## Q 20. Find and visualize the correlation matrix. Write your observations from the plot. (3 Marks)

# In[28]:


# Remove _____ & write the appropriate function name and run the code

corr_matrix = pima.iloc[ : ,0 : 8].corr()

corr_matrix


# In[29]:


# Remove _____ & write the appropriate function name

plt.figure(figsize = (8, 8))
sns.heatmap(corr_matrix, annot = True)

# Display the plot
plt.show()


# #### Write your Answer here: 
# 
Ans 20:
This heatmap shows the correlation between different variables in the dataset. 
Pregnancies and Age have the strongest positive correlation (0.54), meaning older women tend to have more pregnancies.
BMI and SkinThickness also have a moderate positive correlation (0.53), suggesting a relationship between body mass and skin thickness.
Glucose and Insulin have a moderate correlation (0.4), which makes sense since both relate to blood sugar levels.
Most other variables have weak or no significant correlation, meaning they don't strongly relate to each other.