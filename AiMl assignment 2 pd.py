#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# Assuming "Salaries.csv" is in the current working directory
sal = pd.read_csv("Salaries.csv")

# Display the first few rows of the DataFrame to verify it was read correctly
print(sal.head())


# In[2]:


print(sal.head())


# In[3]:


print(sal.info())


# In[4]:


average_basepay = sal['BasePay'].mean()
print("Average BasePay:", average_basepay)


# In[5]:


highest_overtime_pay = sal['OvertimePay'].max()
print("Highest OvertimePay:", highest_overtime_pay)


# In[6]:


job_title_joseph_driscoll = sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle'].iloc[0]
print("Job title of JOSEPH DRISCOLL:", job_title_joseph_driscoll)


# In[7]:


total_pay_benefits_joseph_driscoll = sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits'].iloc[0]
print("Total pay + benefits of JOSEPH DRISCOLL:", total_pay_benefits_joseph_driscoll)


# In[8]:


highest_paid_index = sal['TotalPayBenefits'].idxmax()
highest_paid_person_name = sal.loc[highest_paid_index, 'EmployeeName']
print("Name of the highest paid person (including benefits):", highest_paid_person_name)


# In[9]:


lowest_paid_index = sal['TotalPayBenefits'].idxmin()
lowest_paid_person_name = sal.loc[lowest_paid_index, 'EmployeeName']
print("Name of the lowest paid person (including benefits):", lowest_paid_person_name)


# In[10]:


# Convert the 'Year' column to string type to handle comparison
sal['Year'] = sal['Year'].astype(str)

# Filter the DataFrame for the years 2011 to 2014
sal_filtered_years = sal[sal['Year'].isin(['2011', '2012', '2013', '2014'])]

# Group the filtered DataFrame by year and calculate the mean BasePay for each year
average_basepay_per_year = sal_filtered_years.groupby('Year')['BasePay'].mean()

print("Average BasePay of all employees per year (2011-2014):")
print(average_basepay_per_year)


# In[11]:


unique_job_titles_count = sal['JobTitle'].nunique()
print("Number of unique job titles:", unique_job_titles_count)


# In[12]:


top_5_common_jobs = sal['JobTitle'].value_counts().head(5)
print("Top 5 most common jobs:")
print(top_5_common_jobs)


# In[13]:


# Filter the DataFrame for the year 2013
sal_2013 = sal[sal['Year'] == 2013]

# Count the occurrences of each job title
job_title_counts_2013 = sal_2013['JobTitle'].value_counts()

# Count the number of job titles represented by only one person
job_titles_one_person_2013 = (job_title_counts_2013 == 1).sum()

print("Number of Job Titles represented by only one person in 2013:", job_titles_one_person_2013)


# In[14]:


# Convert all job titles to lowercase to ensure case-insensitive matching
sal['JobTitle'] = sal['JobTitle'].str.lower()

# Count the number of job titles containing the word "chief"
chief_count = sal['JobTitle'].str.contains('chief').sum()

print("Number of people with the word 'Chief' in their job title:", chief_count)


# In[15]:


# Calculate the length of each job title string and create a new column 'JobTitleLength'
sal['JobTitleLength'] = sal['JobTitle'].str.len()

# Calculate the correlation coefficient between 'JobTitleLength' and 'TotalPayBenefits'
correlation = sal['JobTitleLength'].corr(sal['TotalPayBenefits'])

print("Correlation between length of Job Title string and Salary:", correlation)

