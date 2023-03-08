#!/usr/bin/env python
# coding: utf-8

# # Analysis of the CDC's data on Covid19 from January 2020 to January 2022

# ## Romzy Safadi 
# ## March 10th, 2022

# # Introduction

# ### Overview of Project and specific goals: 

# The overall goal of this product was to see if I could accurately show covid-19 trends throughout the pandemic with the data that the CDC provided. More specifically, a deeper dive into which states were effected the most, as well as how each varient effected the overall population within the United States. I wanted to accomplish this through accurate visual representations of the CDC's data. The data was grouped by state, from January 20th, 2020, all the way to January 28th, 2022. The main parts that I kept from the original data frame included total cases, number of new cases daily, total deaths, new deaths daily, submission dates, and the main 50 states + American territories. 

# ### Explain why this project was import to you 

# This project was important to me as this was something that not only effected my life, but the lives of billions across the World. It's effected both my personal and professional career. Since the pandemic, our lives have been changed. We all had to adapt to working remotely, learning remotely, being careful as to who we see, when we see them, and how we see them. For many of us, this has played a role in our lives to this day, it could even effect our life style for the rest of our lvies. Some of us may never return to fully working in person. For me personally, I was not able to see my mother for nearly two whole years because of the pandemic. She is considered a high risk individual, due to prior health problems. Being that I lived not more than an hour away from her, this was unfortunate. My undergraduate program completely switched to online, I was not able to attend any labs, and even had a very unique graduation ceremony. My going out habits, and views on the world have also been effected during the pandemic. When the pandemic first started, I was constantly keeping up with news outlsets to find the latest news on COVID-19 and how it was effecting our day to day throughout the country. Eventually, after being on lockdown for so long, I just got used to staying indoors and doing my part. I no longer kept up with the trends and current events of COVID-19. This is why I wanted to take a look at the data, and map it out for myself. To see if I could take a look at the pandemics story, as a whole over the past two years. I wanted to see if I could identify when certain variants were present, how they effected us as a country, and other trends throughout. 

# ### Explain your hypothesis (or hypotheses) you set out to test. What hunch(es) did you have about the data? 

# My first hypothesis was that states with more leniant mask mandate like Florida and Texas, would have the highest number of cases, deaths, and suffered the most throughout the pandemic (ratio of deaths per cases). The second hypothesis that I focused on was that I would be able to clearly see when the original first few variants, delta varient, and Omicron varient were present within the United States. A hunch I had when going through the data was that California and New York would also be largely suffering from the pandemic as far as number of cases, deaths, and deaths per cases.  

# ### Provide a link to your data source if applicable

# I found my data on the CDC's website:
# 
# https://data.cdc.gov/Case-Surveillance/United-States-COVID-19-Cases-and-Deaths-by-State-o/9mfq-cb36
# 
# The data can be exported in the top right, and viewed at the bottom of the page. 

# ### A brief overview of the steps needed to clean the data

# Cleaning the data was not as straight forward as I thought it would be. In fact, I found myself working to clean the data through multiple weeks in order to obtain what I needed for each EDA phase. 
# 
# For starters the original data frame had a few columns that I wanted to drop such as:  conf_cases, prob_cases, pnew_case, conf_death, prob_death, pnew_death, created_at, consent_cases, and consent_deaths.
# 
# This left me with five columns: submission_date	state, tot_cases, new_case, tot_death, and new_death.
# 
# I then had to remove all commas in my df so that I could group my data and organize it as I would like. 
# 
# This was followed up by converting my df objects to integers so that I could better work with them. 
# 
# Next, since the state column was in abbreviations, such as 'CA' instead of California, I converted all of the states to full names, as I thought this would be more visually appealing while plotting and reading the data. 
# 
# Throughout the EDA process I found that the American territories were serving as major outliers when plotting, so I decided it would be best to drop them in order to keep the plots and project focused on the main 50 states.  
# 
# I also created a data frame that was grouped by state on the last day of my recoreded data, January 8th, 2022. This was used to plot all of the total values from my data. 
# 
# Lastly, admitedly one I struggled with a lot, was that the CDC placed NYC as a seperate input to NY state. This was very confusing and I eventually had to combine NYC and NY to form one state as it was messing with my plotting results. 
# 
# I eventually added a new column called, percentage_of_Deaths_by_cases, which was the ratio of the total deaths per total cases for each state. This was used to identify help identify which states suffered the most. 
# 

# ### Data Dictionary

# Submission_date: Date when data was submitted to the CDC, should be daily by each 50 states.
# 
# state: The name of the state
# 
# tot_cases: Accumulative number of cases for that state on that day + all the days previous in the dataframe.
# 
# new_case: The accumulative number of new COVID-19 cases on that submission date for that specific state. 
# 
# tot_death: Accumulative number of deaths for that state on that day + all the days previous in the dataframe.
# 
# new_death: Total number of deaths on that submission date for that specific state.
# 
# percentage_of_deaths_by_cases: This is the ratio of total deaths per total cases on the final submission date of January 28th, 2022. 

# # Results

# ### Read in final data

# In[1]:


import pandas as pd
import numpy as np
import seaborn
import matplotlib.pyplot as plt
import plotly.express as px


#multiple outputs per cell

from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"


# In[2]:


#final data file:

df = pd.read_csv('Romzy_Safadi_covid19.csv')
df.info()
df.head()


# ## These are the main data frames I used throughout the project:
# 
# 

# ### df3 is when all states were put into full names, and all columns that needed to be dropped were dropped:
# 
# 

# In[3]:


#dropping columns to create df3

df3 = df.drop( columns = ['conf_cases', 'prob_cases', 'pnew_case', 'conf_death', 'prob_death', 'pnew_death',
          'created_at', 'consent_cases', 'consent_deaths'])

#removing commas in df
df3['tot_death'] = df3['tot_death'].str.replace(',','')
df3['tot_cases'] = df3['tot_cases'].str.replace(',','')
df3['new_case'] = df3['new_case'].str.replace(',','')
df3['new_death'] = df3['new_death'].str.replace(',','')


#convert obects to int
df3["tot_cases"] = df3["tot_cases"].apply(pd.to_numeric)
df3["new_case"] = df3["new_case"].apply(pd.to_numeric)
df3["tot_death"] = df3["tot_death"].apply(pd.to_numeric)
df3["new_death"] = df3["new_death"].apply(pd.to_numeric)

# converting State abreviations to full name (ex: CA --> California)


df3["state"].replace({    "AL":"Alabama",
                      "AK":"Alaska", 
                      "AZ":"Arizona",
                      "AR":"Arkansas", 
                      "CA":"California",
                      "CO":"Colorado",
                      "CT":"Connecticut", 
                      "DC":"Washington DC", 
                      "DE":"Delaware",
                      "FL":"Florida",
                      "GA":"Georgia",
                      "HI":"Hawaii",
                      "ID":"Idaho", 
                      "IL":"Illinois", 
                      "IN":"Indiana",
                      "IA":"Iowa",
                      "KS":"Kansas",
                      "KY":"Kentucky", 
                      "LA":"Louisiana",
                      "ME":"Maine",
                      "MD":"Maryland",
                      "MA":"Massachusetts", 
                      "MI":"Michigan", 
                      "MN":"Minnesota",
                      "MS":"Mississippi",
                      "MO":"Missouri",
                      "MT":"Montana",
                      "NE":"Nebraska",
                      "NV":"Nevada",
                      "NH":"New Hampshire",
                      "NJ":"New Jersey",
                      "NM":"New Mexico",
                      "NYC":"New York", 
                      "NY" : "New York",
                      "NC":"North Carolina",
                      "ND":"North Dakota",
                      "OH":"Ohio", 
                      "OK":"Oklahoma",
                      "OR":"Oregon",
                      "PA":"Pennsylvania", 
                      "RI":"Rhode Island",
                      "SC":"South Carolina",
                      "SD":"South Dakota",
                      "TN":"Tennessee",
                      "TX":"Texas",
                      "UT":"Utah",
                      "VT":"Vermont",
                      "VA":"Virginia",
                      "WA":"Washington",
                      "WV":"West Virginia",
                      "WI":"Wisconsin",
                      "WY":"Wyoming",
                      "DC": "District of Columbia",
                      "AS": "American Samoa",
                      "GU": "Guam",
                      "MP": "Northern MAriana Isdlands",
                      "PR": "Puerto Rico",
                      "United States Minor Outlying Islands": "UM",
                      "VI": "U.S. Virgin Islands",
                      "RMI": "The Marshall Islands",
                      "FSM": "FEDERATED STATES OF MICRONESIA RELATIONS",
                      "PW": "Palau"
                     }, inplace = True)

#dropping everything that is not a part of the 50 major states
df3 = df3[df3["state"].str.contains("American Samoa") == False]
df3 = df3[df3["state"].str.contains("Puerto Rico") == False]
df3 = df3[df3["state"].str.contains("FEDERATED STATES OF MICRONESIA RELATIONS") == False]
df3 = df3[df3["state"].str.contains("Guam") == False]
df3 = df3[df3["state"].str.contains("Northern MAriana Isdlands") == False]
df3 = df3[df3["state"].str.contains("Palau") == False]
df3 = df3[df3["state"].str.contains("The Marshall Islands") == False]
df3 = df3[df3["state"].str.contains("U.S. Virgin Islands") == False]

#adjustdates to datetime64 type
df3['submission_date'] = pd.to_datetime(df3['submission_date'])

df3
df3.info()


# ### df4 was used to plot the totals such as total cases and total deaths by state

# In[4]:


#create df of final date, to gather total numbers by end -->
#true tot_cases/tot_death on final date
df4 = df3[df3['submission_date'] == '2022-01-28']
df4.head()


# ### newdf was used to groupby state in order to plot totals without any duplicates of states, such as New York. 

# In[5]:


newdf = df4.groupby('state').sum().reset_index()
newdf.head()


# ### df5 wascreated to add the percentage of deaths per cases column to the newdf

# In[6]:


#Calculate percentage of deaths from total cases and total deaths ((total deaths/total cases)*100)

df5 = newdf.copy()
df5["percentage_of_deaths_by_cases"] = (df5['tot_death'] / df5['tot_cases'] * 100).round(3)
df5.head()


# ### dfgrouped was used to group by state and submission date in order to plot, state specifically,  new cases and new deaths by date

# In[7]:


#grouping df3 by submission date and state
dfgrouped = df3.groupby(['state', 'submission_date']).sum().reset_index()
dfgrouped.head()


# ### states_few was created to group the 10 states that I felt told the best story of my data

# In[8]:


#create few states so can create scatter of few states
#Top 5 states by total cases and top 5 states by highest ratio of deaths 
states = ['California','New York','Florida','Pennsylvania','Texas',
          'Mississippi', 'New Jersey', 'Michigan', 'Connecticut', 'Arizona']
states_few = dfgrouped[dfgrouped['state'].isin(states)]
states_few


# ### df6 was used to group the dataset y date in order to create Date vs new cases and new deaths plots

# In[9]:


#group by submission dates, in order to show cases per day

df6 = df3.groupby(by = 'submission_date').aggregate(np.sum)
df6.index.name = 'Date'
df6 = df6.reset_index()
df6


# ### df7 adds a column to df6: percentage_of_new_deaths_by_new_cases

# In[10]:


#ratio of new deaths/new cases * 100

df7 = df6.copy()
df7["percentage_of_new_deaths_by_new_cases"] = (df6['new_death'] / df6['new_case'] * 100).round(3)
df7


# # Codes that showed most important findings 

# ### The first important finding of my EDA was the plot of total deaths by State, in descending order. This was able to show the total number of deaths each state had throughout the pandemic and put it in perspective to see what states lost the most lives. 

# In[11]:


#descending states by total death, to show which state had the most, and least, 
#cumulative deaths by January 28, 2022.

tot_death_desc = newdf.sort_values(by = 'tot_death', ascending = False)
bar_desc_tot_death = px.bar(tot_death_desc, x = 'state', y = 'tot_death',title = "Total Deaths by State, Descending",
                            labels = dict(tot_death = "Total Deaths",
                            state = "State"))
bar_desc_tot_death.show()


# Placing these in descending order was important as we are now able to see that California, Texas, Florida, New York, and Pennsylvania had the most deaths due to covid-19 over the past two years. While Vermont, Alaska, and Hawaii, had the least. 

# ### The next significant plot was Total cases by State in descending order 

# In[12]:


# Most cumulative cases by state, as of January 28, 2022
# total cases by state, descending barplot

tot_cases_desc = newdf.sort_values(by = 'tot_cases', ascending = False)
bar_tot_cases_desc = px.bar(tot_cases_desc, x = 'state', y = 'tot_cases',title = "Total Cases by State",
                            labels = dict(tot_cases = "Total Cases",
                            state = "State"))
bar_tot_cases_desc.show()


# This is significant as it shows how many cases each state had over the pandemic. We can see that California, Texas, Florida, New York, and Pennsylvania are all at the top of the plot, with the most number of cases. This lead me to beleive that there is a correlation between total cases and total deaths. 

# # checking for correlation between total cases and total deaths

# In[13]:


#checking correlations
newdf.corr().style.background_gradient(cmap='coolwarm')

#create correlation heat map of total deaths and total cases per state 

plt.figure(figsize=(4,4))
seaborn.heatmap(newdf.corr(), annot = True, cmap = 'coolwarm')


# Heat map and correlation table show strong correlation between total deaths and total cases.
# 
# Although there is a correlation between total deaths and total cases, we cannot say there is a direct causation. As the population of California is still much higher than states like Vermont. A better way to get a deeper understanding of the overall picture is to get the percentage of death rates of total cases per each state to see what states really did end up "suffering" the most

# # Since checking the total deaths and cases cannot show a direct correlation with which states suffered the most, due to population size, it was best to look at the ratio of total deaths by total cases to see which states did suffer the most in terms of percentages

# In[14]:


#plot in descending order to see which state suffered more in relation
#to their number of cases.

relation_death_to_case_per_state = df5.sort_values(by = 'percentage_of_deaths_by_cases',
                                                   ascending = False)
bar_death_per_case_desc = px.bar(relation_death_to_case_per_state, 
                                 x = 'state', y = 'percentage_of_deaths_by_cases',
                                 title = "State vs (Total Death/Total Cases)",
                            labels = dict(percentage_of_deaths_by_cases = "Percentage of total deaths by total cases",
                            state = "State"))
bar_death_per_case_desc.show()

#descending order table; by percentage of deaths

relation_death_to_case_per_state


# We can now clearly see that Pennsylvania, suffered the most with 1.531% of its total cases resulting in deaths. We also know from prior plots and tables that Pennsylvania also was amongst the top 5 total cases and total deaths. Furthermore, states like Mississippi, New Jersey, and Michigan, although not in highest cases and deaths, still suffered the most as they were amongst the top 5 in ratio of deaths per cases.  

# ### I then chose the states with the top 5 deaths and top 5 ratios to plot on a time line next to each other to see their trends throughout the pandemic

# In[15]:


#show in a few states at once, dates vs total deaths scatter: 
#this is a scatter plot of date by total death of the top 5 states by cases and top 5 states by ratio of cases

scatter_few_states = px.scatter(states_few,
            x = 'submission_date', y = 'tot_death', color = 'state',
              title = "Date vs Total Deaths Few States",
                            labels = dict(submission_date = "Date",
                            tot_death = "Total Deaths"))                                 
scatter_few_states.show()


# This was significant because it shows us the trends of the states with the most deaths and highest suffering throughout the pandemic. As well as how the increased over time. We can see that for California, Texas, Florida, and New York, things really started to increase tremendously starting in the end of 2021. While all states saw a jump in the start of 2021. 

# ### To more accurately show the trend of new cases on a daily basis I plotted the cumulative new cases on a daily basis for all of the states on one plot

# In[16]:


#new cases on daily basis

new_cases_daily = px.area(df6, x = 'Date', y = 'new_case', 
              title = "New Cases on Daily Basis",  
             labels = dict(new_case = "New Cases"))
new_cases_daily.show()


# This was important as we can now see the overall story of this pandemic within the United States over the past two years. We can identify that hill over Jan 2021 was the Beta variant, while the hill inbetween Jul 2021 and Oct 2021 is the Delta variant, and the large peaknear Jan 2022 is the Omicron variant. We can also have a hunch that Omicron was the most contageous. We cannot entirely conclude that from this data and graph alone. We would need to know What variant exactly each person tested positive for, to do that. 
# 
# further information on when each variant was introduced to the United States can be found here:
# 
# https://www.who.int/en/activities/tracking-SARS-CoV-2-variants/

# ### Although it is not possible to conclude which variant was the most deadly, I felt like it would still be useful to know how many deaths occured on a dasily basis over the timeline of the pandemic. As it might be able to lead us to new hunches on how the people of the USA reacted to each variant. 

# In[17]:


#New deaths daily to show severity of different varients 

new_deaths_daily = px.area(df6, x = 'Date', y = 'new_death', 
              title = "New Deaths on Daily Basis",  
             labels = dict(new_death = "New Deaths"))
new_deaths_daily.show()


# Here we can see that it looks like the delta variant caused the most deaths. Yet we cannot say it is the most deadly, as the Beta and Alpha variants at the beginning were not far off, and we did not have a vaccine back then, while during the Delta variant, a good number of high risk people were vaccinated by then. In addition to this, based on this data alone, it would be hard to determine which variant is the most deadly as we would need more information. Furthermore, the Omicron variant had significantly more cases, yet we did not have the most deaths during that time. To get a better look as to what variants were the most lethal, we could take a etter look at the percentage of new deaths per new cases.  

# ### Looking at the ratio of new deaths per new cases to give a more clear answer on what variant was th emost deadly.

# In[18]:


#graph of ratio of new deaths per new cases 

new_deaths_per_cases_daily = px.area(df7, x = 'Date', y = 'percentage_of_new_deaths_by_new_cases', 
              title = "Ratio of New Deaths to New Cases",  
             labels = dict(percentage_of_new_deaths_by_new_cases = "Percentage of New Deaths per New Cases"))
new_deaths_per_cases_daily.show()


# Looking at this plot we can see that the Alpha and Beta variants actually killed the most people in ratio to the number of cases we were having within the USA. Although it is compelling to say that these variants were the most deadly because they caused the most deaths, in proportion, we cannot conclude that from this data alone. We can just use this as a hunch or theory. As these results could be due to a multitude of variables. Such as limited testing early on during the pandemic. Furthermore, we can see that the ratio of deaths during the Omicron variant period was very low, even though there was an abundance of testing as well as more people vaccinated.

# # Summary:

# The purpose of this project was to show a timeline of how each state was effected through the pandemic. This was done through visualizing and analyzing the total deaths, total cases, new deaths, new cases, and dates on a cumulative and independent basis for the main fifty states of the USA. 
# 
# My hypothesis was that states with looser mask mandates, such as Florida and Texas were going to be amongst the states that suffered the most. Initially when looking a the total number of cases and deaths, this seemed to be the case. However, when looking at the raito of deaths by cases for each state, we can see that Florida and Texas are not amongst the top five states that suffered through the pandemic. Shockingly, it seemed to have been Pennsylvania, as it was amongst the top five in total cases, total deaths, and number one when it came to the ratio of deaths per cases. At the same time, we saw that California, even though it had a high number of cases and deaths, was at the bottom quarter of states that suffered the most. These contradicting results could be due to a number of different factors. It could have been that the stricter mask mandate in California was helping, yet, Pennsylvania, which also had a relatively strict mask mandate was at the top of the list when it came to suffering. I beleive that there is one key red flag that stood out to me the most upoon completing this project. The fact that this data sent to the CDC was voluntary. This meant that each state could have biases to skew their data as they wished before submitting the data to the CDC. It also meant they could report as they want and as much as they want. 
# 
# My second hypothesis/hunch was that this data could visually represent the story of the pandemic within the USA. My hunch was that looking at the data, one would be able to tell when each variant was entering the United States, and that we would be able to see how we reacted to the variants as a whole. This is evident through the data, we can see when we first started experiencing the alpha and delta varients in the end of 2020, with the delta variant eing right near the end of 2021, and ust before the Omicron variant. We can even see the surge of cases at the beginning of the pandamic. 
# 
# Overall I was able to take the data and visualize the trends of covid throughout the pandamic, along with the varaints and their spikes that came with them. Furthermore, based on the CDC's volunatry data, the ratio of total deaths per total cases disproved my theory that states with loser mask mandates would have suffered the most. As the plots indicate, Pennsylvania is actually the state that suffered the most. Furthermore, although it is difficult to make a decisive conclusion, the ratio of deaths per cases helped theorize that the Delta variant could have been the most deadly covid19 variant within the USA to this date. 
# 
# Possible next steps would be to compare the CDC's data to other instiutions, such as John Hopkins University, and a few other instiutions, to see how accurate the voluntary data. Furthermore, we could take this one step forward and obtain what variant each individual tested positive for (if possible). 
