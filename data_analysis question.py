
# coding: utf-8

# # Lesson: Let's preprocess the data!
# 
# ## File I/O and exploring the data


import pandas as pd

f = '../data/census_data.csv'

# read in the file


# look at the first 5 lines




# What are the column names?



# Sort the DataFrame by age and print out the last 5 lines


# ## Selecting columns and rows


# create a subset of the data with the columns education, occupation, hours_per_week. Look at the first 5 rows.



# create a subset of the data with the middle 50 rows and the columns work_class and race. Look at the first 5 rows.



# create a subset of the data where education_num is greater than 8 and where sex is equal to female. Look at the first 5 rows


# ## groupby


# Group by work_class and output the group names (hint: add .keys() to the end of your line of code).



# Let's group by work_class and use the mean as the aggregate function



# ## Pivoting


# Let's pivot on education_num and sex, with hours_per_week as the values and mean as the aggfunc




# Create a pivot table of your choosing, with any columns for rows and cols and a numerical columns for values.



# ## Let's do the following:
# 
# For the machine learning section, can you extract a subset of the data where:
# 
# - native_country equals United-States
# - hours_per_week is greater than 10
# - age is greater than 20 and less than 50
# - education is Masters
# 
# It's going to be a bunch of booleans!


# Store that new dataframe in new_df and print out the first five rows.

