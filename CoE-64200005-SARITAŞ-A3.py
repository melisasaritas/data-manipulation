#!/usr/bin/env python
# coding: utf-8

# In[1]:


###############################################################################
#  Name:         Melisa Sarıtaş
#  Student ID:   64200005
#  Department:   Computer Engineering
#  
#  Assignment ID: A3
###############################################################################


# In[2]:


###############################################################################
#  QUESTION I
#  Description:   
#  In the question, it is dealt with the library pandas and the aim is to create different series. It is done 5 different 
#  series which are from a list, that contains same numbers, from random numbers, with changing the indexes as names and from a 
#  dictionary in parts a, b, c, d and e respectively.
#  Source:
#  towardsdatascience.com
###############################################################################


# In[3]:


import pandas as pd
import random


# In[4]:


#a
a = pd.Series([7,11,13,17])
print(a)


# In[5]:


#b
b = pd.Series([100.0 for b in range(5)])
print(b)


# In[6]:


#c
c = pd.Series([random.randint(0,100) for c in range(20)])
print(c)


# In[7]:


#d
temperatures = pd.Series([98.6,98.9,100.2,97.9], index = ['Julie','Charlie','Sam','Andrea'])
print(temperatures)


# In[8]:


#e
dictionary = {'Julie': 98.6, 'Charlie': 98.9, 'Sam': 100.2, 'Andrea': 97.9}
e = pd.Series(dictionary)
print(e)


# In[9]:


###############################################################################
#  QUESTION II
#  Description:   
#  In the question, it is dealt with the library pandas and the aim is to create dataframe and playing with it. It is created a
#  dataframe in part a. It is changed the index of the same dataframe in part b. It is chosen a column from the dataframe in 
#  part c. It is chosen a row ,two rows and two columns in parts d, e and f respectively. It is chosen two rows and two columns 
#  in part g with the help of the dataframe that created in part f. It is described the dataframe in part h, transposed in part 
#  i and sorted the temperature values in part j. 
#  Sources:
#  realpython.com
#  stackoverflow.com
#  towardsdatascience.com
###############################################################################


# In[10]:


import pandas as pd


# In[11]:


#a
dictionary = {'Maxine': [98.6, 96.5, 95.8], 'James': [98.9, 97.3, 96.8], 'Amanda': [100.2, 99.8, 100.8]}
temperatures = pd.DataFrame(dictionary)
print(temperatures)


# In[12]:


#b
list = ['Morning', 'Afternoon', 'Evening']
temperatures = pd.DataFrame(dictionary, index = list)
print(temperatures)


# In[13]:


#c
c = temperatures['Maxine']
print(c)


# In[14]:


#d
d = temperatures.iloc[0]
print(d)


# In[15]:


#e
e = temperatures.iloc[[0,2]]
print(e)


# In[16]:


#f
f = temperatures[['Amanda', 'Maxine']]
print(f)


# In[17]:


#g
g = f.iloc[[0,1]]
print(g)


# In[18]:


#h
h = temperatures.describe()
print(h)


# In[19]:


#i
i = temperatures.transpose()
print(i)


# In[20]:


#j
j = temperatures[sorted(temperatures)]
print(j)


# In[21]:


###############################################################################
#  QUESTION III
#  Description:   
#  In the question, it is dealt with the library pandas and the aim is to read datas from the csv files and playing with them.
#  In part a, it is printed a file as a dataframe. With looking at the length of the index numbers for each dataframe, it is 
#  printed the records in part b. It is filtered the dataframe employees in part c. It is filled the NaN values with zeros in 
#  part d. It is filtered the dataframe respect to the department_id numbers and chosen only four columns in part e. It is 
#  collected two dataframes on a specific column that is same for both in part f. It is found min, max and mean salaries respect
#  to the department_name in part g. It is found mean salaries for each city in different ranges in part h.
#  Sources:
#  stackoverflow.com
#  towardsdatascience.com
#  datatofish.com
###############################################################################


# In[22]:


import pandas as pd
import numpy as np


# In[23]:


pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
employees = pd.read_csv(r"EMPLOYEES.csv")
departments = pd.read_csv(r"DEPARTMENTS.csv")
job_history = pd.read_csv(r"JOB_HISTORY.csv")
jobs = pd.read_csv(r"JOBS.csv")
countries = pd.read_csv(r"COUNTRIES.csv")
regions = pd.read_csv(r"REGIONS.csv")
locations = pd.read_csv(r"LOCATIONS.csv")


# In[24]:


#a
print(departments)


# In[25]:


#b
print('Number of records for employees is:',len(employees.index))
print('Number of records for departments is:',len(departments.index))
print('Number of records for job_history is:',len(job_history.index))
print('Number of records for jobs is:',len(jobs.index))
print('Number of records for countries is:',len(countries.index))
print('Number of records for regions is:',len(regions.index))
print('Number of records for locations is:',len(locations.index))


# In[26]:


#c
c = employees.loc[employees['salary'] > 10000]
print(c)


# In[27]:


#d
df = pd.DataFrame(np.zeros((107,1)), columns=['commission_pct'])
d=employees.fillna(df)
print(d)


# In[28]:


#e
q = employees.loc[(employees['department_id'] == 30)| (employees['department_id'] == 50)| (employees['department_id'] == 80)]
e = q[['first_name', 'last_name', 'salary', 'department_id']]
print(e)


# In[29]:


#f
emp_dept = pd.merge(employees, departments, on='department_id')
print(emp_dept)


# In[30]:


#g
list1 = ['Executive', 'IT', 'Finance', 'Purchasing', 'Shipping', 'Sales', 'Administration', 'Marketing', 'Human Resources',
         'Public Relations', 'Accounting']
max = []
min = []
mean = []
for a in range(11):
    s = emp_dept.loc[emp_dept['department_name'] == list1[a]]
    k = s['salary']
    max.append(k.max())
    min.append(k.min())
    mean.append(k.mean())
g = pd.DataFrame({'department_name': list1, 'min salary': min,'max salary': max, 'mean salary': mean})
print(g)


# In[31]:


#h
merg = pd.merge(emp_dept, locations)
list2 = ['Seattle', 'Southlake', 'South San Francisco', 'Oxford', 'Toronto', 'London', 'Munich']
a = merg.loc[merg['salary'] <= 5000]
b = merg.loc[(merg['salary'] > 5000) & (merg['salary'] <= 10000)]
c = merg.loc[(merg['salary'] > 10000) & (merg['salary'] <= 15000)]
d = merg.loc[(merg['salary'] > 15000) & (merg['salary'] <= 25000)]
mean1 = []
mean2 = []
mean3 = []
mean4 = []
for e in range(7):
    f = a.loc[a['city'] == list2[e]]
    g = b.loc[b['city'] == list2[e]]
    i = c.loc[c['city'] == list2[e]]
    j = d.loc[d['city'] == list2[e]]
    k = f['salary']
    l = g['salary']
    m = i['salary']
    n = j['salary']
    mean1.append(k.mean())
    mean2.append(l.mean())
    mean3.append(m.mean())
    mean4.append(n.mean())
o = pd.DataFrame({'country_id': ['US', 'US', 'US', 'UK', 'CA', 'UK', 'DE'], 'city': list2, 'mean salaries in range(0,5000]': 
                  mean1, 'in range(5000,10000]': mean2, 'in range(10000,15000]': mean3, 'in range(15000,25000]': mean4})
df = pd.DataFrame(np.zeros((7,4)), columns = ['mean salaries in range(0,5000]', 'in range(5000,10000]', 'in range(10000,15000]',
                                              'in range(15000,25000]'])
h = o.fillna(df)
print(h)


# In[32]:


###############################################################################
#  QUESTION VI
#  Description:   
#  In the question, it is dealt with the library pandas and the aim is to read two csv files and playing with them. In part a, 
#  it is read the first 5 rows for both. It is sorted the dataframe respect to the column Active from bigger to smaller and 
#  showed 5 columns in part b. It is found Death_Confirmed_Ratio values with a calculation and sorted from bigger to smaller in
#  part c. In part d, it is sorted the dataframe from part b respect to the Confirmed values and chosen first 10 rows. After 
#  that it is read covid_series dataframe respect to the country names of these 10 rows and it is summed the cases for each date
#  in same country names because there is more than 1 row for some countries. It is filtered the dataframe with choosing after 
#  the date 3/11/20. Finally, it is plotted the dataframe respect to the case values for each date.
#  Sources:
#  www.tutorialspoint.com
#  pythonguides.com
#  stackoverflow.com
###############################################################################


# In[33]:


import pandas as pd
covid_data= pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/05-10-2022.csv')
covid_series= pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')


# In[34]:


#a
a = covid_data.head(5)
b = covid_series.head(5)
print(a)


# In[35]:


print(b)


# In[36]:


#b
a = {'Country Region': covid_data['Country_Region'], 'Confirmed': covid_data['Confirmed'], 
     'Deaths': covid_data['Deaths'], 'Recovered': covid_data['Recovered'], 'Active': covid_data['Active']}
c = pd.DataFrame(a)
sorted = c.sort_values('Active', ascending = False)

print(sorted)


# In[37]:


#c
b = []
df = covid_data.loc[covid_data['Confirmed'] > 1000]
list1 = [i for i in df['Deaths']]
list2 = [j for j in df['Confirmed']]
for k in range(len(list1)):
    l = list1[k]/list2[k]*100
    b.append(l)
a = {'Country Region': df['Country_Region'],'Last_Update': df['Last_Update'] , 'Confirmed': df['Confirmed'], 
     'Deaths': df['Deaths'], 'Recovered': df['Recovered'], 'Active': df['Active'], 'Death_Confirmed_Ratio': b}
d = pd.DataFrame(a)
c = d.sort_values('Death_Confirmed_Ratio', ascending = False)
print(c)


# In[126]:


# d
s = sorted.sort_values('Confirmed', ascending = False)
a = s[:10]
list1 = [i for i in a['Country Region']]
list2 = []
for y in list1:
    list2.append(covid_series.loc[covid_series['Country/Region'] == y])

#list2[6] same with list2[8]
b = pd.concat([list2[0],list2[1],list2[2],list2[3],list2[4],list2[5],list2[6],list2[7],list2[9]])


l = b.iloc[:,4:]
France = l.iloc[:12,:].sum(axis = 0)
UK = l.iloc[12:26,:].sum(axis = 0)
Korea = l.iloc[26:27,:].sum(axis = 0)
Turkey = l.iloc[27:28,:].sum(axis = 0)
Vietnam = l.iloc[28:29,:].sum(axis = 0)
Argentina = l.iloc[29:30,:].sum(axis = 0)
India = l.iloc[30:31,:].sum(axis = 0)
Iran = l.iloc[31:32,:].sum(axis = 0)
Indonesia = l.iloc[32:33,:].sum(axis = 0)

sums = pd.concat([pd.DataFrame(France).transpose(), pd.DataFrame(UK).transpose(), pd.DataFrame(Korea).transpose(), 
               pd.DataFrame(Turkey).transpose(), pd.DataFrame(Vietnam).transpose(), pd.DataFrame(Argentina).transpose(), 
               pd.DataFrame(India).transpose(), pd.DataFrame(Iran).transpose(), pd.DataFrame(Indonesia).transpose()])
df = sums.set_index(pd.Series([0, 1, 2, 3, 4, 5, 6, 7, 8]))

c = df.iloc[:, 49:]
ç = pd.DataFrame({'Country/Region': ['France', 'UK', 'Korea, South', 'Turkey', 'Vietnam', 'Argentina', 'India', 'Iran', 
                                     'Indonesia']})
d = ç.join(c)
print(d)


# In[128]:


import matplotlib.pyplot as plt
e = d.transpose()
arr =[o for o in e.index]
arr1 = [k for k in e[0]]
arr2 = [k for k in e[1]]
arr3 = [k for k in e[2]]
arr4 = [k for k in e[3]]
arr5 = [k for k in e[4]]
arr6 = [k for k in e[5]]
arr7 = [k for k in e[6]]
arr8 = [k for k in e[7]]
arr9 = [k for k in e[8]]

fig = plt.figure(figsize=(15, 15))
axes = fig.subplots(nrows=1, ncols=1)

axes.plot(arr[1:],arr1[1:], color = 'pink',label='France', marker='o',linewidth=8)
axes.plot(arr[1:],arr2[1:], color = 'purple',label='UK', marker='o', linewidth=8)
axes.plot(arr[1:],arr3[1:], color = 'gray',label='Korea, South', marker='o', linewidth=8)
axes.plot(arr[1:],arr4[1:], color = 'green',label='Turkey', marker='o', linewidth=8)
axes.plot(arr[1:],arr5[1:], color = 'blue',label='Vietnam', marker='o', linewidth=8)
axes.plot(arr[1:],arr6[1:], color = 'black',label='Argentina', marker='o', linewidth=8)
axes.plot(arr[1:],arr7[1:], color = 'orange',label='India', marker='o', linewidth=8)
axes.plot(arr[1:],arr8[1:], color = 'brown',label='Iran', marker='o', linewidth=8)
axes.plot(arr[1:],arr9[1:], color = 'yellow',label='Indonesia', marker='o', linewidth=8)


handels = []
labels = []
  
for ax in fig.axes:
    Handel, Label = ax.get_legend_handles_labels()
    handels.extend(Handel)
    labels.extend(Label)
    
fig.legend(handels, labels, loc = 'upper center')


plt.show()


# In[ ]:





# In[ ]:




