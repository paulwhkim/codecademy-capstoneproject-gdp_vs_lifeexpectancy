#!/usr/bin/env python
# coding: utf-8

# # Introduction
# 
# For this project, you will act as a data researcher for the World Health Organization. You will investigate if there is a strong correlation between the economic output of a country and the life expectancy of its citizens.  
# 
# During this project, you will analyze, prepare, and plot data, and seek to answer questions in a meaningful way.
# 
# After you perform analysis, you'll be creating an article with your visualizations to be featured in the fictional "Time Magazine".
# 
# **Focusing Questions**: 
# + Has life expectancy increased over time in the six nations?
# + Has GDP increased over time in the six nations?
# + Is there a correlation between GDP and life expectancy of a country?
# + What is the average life expactancy in these nations?
# + What is the distribution of that life expectancy?
# 
# GDP Source:[World Bank](https://data.worldbank.org/indicator/NY.GDP.MKTP.CD)national accounts data, and OECD National Accounts data files.
# 
# Life expectancy Data Source: [World Health Organization](http://apps.who.int/gho/data/node.main.688)
# 

# ## Step 1. Import Python Modules

# Import the modules that you'll be using in this project:
# - `from matplotlib import pyplot as plt`
# - `import pandas as pd`
# - `import seaborn as sns`

# In[1]:


from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns


# ## Step 2 Prep The Data

# To look for connections between GDP and life expectancy you will need to load the datasets into DataFrames so that they can be visualized.
# 
# Load **all_data.csv** into a DataFrame called `df`. Then, quickly inspect the DataFrame using `.head()`.
# 
# Hint: Use `pd.read_csv()`
# 

# In[3]:


df = pd.read_csv('all_data.csv')
print(df.head())


# ## Step 3 Examine The Data

# The datasets are large and it may be easier to view the entire dataset locally on your computer. You can open the CSV files directly from the folder you downloaded for this project.
# 
# Let's learn more about our data:
# - GDP stands for **G**ross **D**omestic **P**roduct. GDP is a monetary measure of the market value of all final goods and services produced in a time period. 
# - The GDP values are in current US dollars.

# What six countries are represented in the data?

# In[8]:


print(df.groupby('Country').head(1))
print('\n')
print('The countries represented are: Chile, China, Germany, Mexico, USA, Zimbabwe.')


# What years are represented in the data?

# In[9]:


print(df.groupby('Year').head(1))
print('\n')
print('The years represented are: 2000-2015.')


# ## Step 4 Tweak The DataFrame
# 
# Look at the column names of the DataFrame `df` using `.head()`. 

# In[10]:


df.head(1)


# What do you notice? The first two column names are one word each, and the third is five words long! `Life expectancy at birth (years)` is descriptive, which will be good for labeling the axis, but a little difficult to wrangle for coding the plot itself. 
# 
# **Revise The DataFrame Part A:** 
# 
# Use Pandas to change the name of the last column to `LEABY`.
# 
# Hint: Use `.rename()`. [You can read the documentation here.](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.rename.html)). </font>

# In[11]:


df=df.rename(columns={"Life expectancy at birth (years)": "LEABY"})


# Run `df.head()` again to check your new column name worked.

# In[12]:


df.head(1)


# ---

# ## Step 5 Bar Charts To Compare Average

# To take a first high level look at both datasets, create a bar chart for each DataFrame:
# 
# A) Create a bar chart from the data in `df` using `Country` on the x-axis and `GDP` on the y-axis. 
# Remember to `plt.show()` your chart!

# In[13]:


ax = plt.subplot()
plt.bar(df['Country'], df['GDP'])
labels = ['Chile', 'China', 'Germany', 'Mexico', 'USA', 'Zimbabwe']
ax.set_xticks(range(6))
ax.set_xticklabels(labels, rotation=30)
plt.title("GDP by Country")
plt.ylabel("GDP in USD (x 10^13)")
plt.show()
plt.savefig("GDP_Country_bar.png")


# B) Create a bar chart using the data in `df` with `Country` on the x-axis and `LEABY` on the y-axis.
# Remember to `plt.show()` your chart!

# In[14]:


ax = plt.subplot()
plt.bar(df['Country'], df['LEABY'])
labels = ['Chile', 'China', 'Germany', 'Mexico', 'USA', 'Zimbabwe']
ax.set_xticks(range(6))
ax.set_xticklabels(labels, rotation=30)
plt.title("Life Expectancy by Country")
plt.ylabel("Life Expectancy (Years)")
plt.show()
plt.savefig("Life_Country_bar.png")


# What do you notice about the two bar charts? Do they look similar?

# In[17]:


print('• No, the two bar charts do not look similar. The life expectancy is roughly the same for all countries, except for Zimbabwe.')


# ## Step 6. Violin Plots To Compare Life Expectancy Distributions 

# Another way to compare two datasets is to visualize the distributions of each and to look for patterns in the shapes.
# 
# We have added the code to instantiate a figure with the correct dimmensions to observe detail. 
# 1. Create an `sns.violinplot()` for the dataframe `df` and map `Country` and `LEABY` as its respective `x` and `y` axes. 
# 2. Be sure to show your plot

# In[24]:


fig = plt.subplots(figsize=(15, 10))
sns.set(style='whitegrid', context='talk')
sns.violinplot(data=df, x='Country', y='LEABY', palette='deep')
ax.set_ylabel("Life Expectancy (Years)")
labels = ['Chile', 'China', 'Germany', 'Mexico', 'USA', 'Zimbabwe']
ax.set_xticks(range(6))
ax.set_xticklabels(labels)
ax.set_xlabel("Country")
plt.title("Distribution of Life Expectancies per Country")
plt.savefig("Life_Country_violin.png")
plt.show()


# What do you notice about this distribution? Which country's life expactancy has changed the most?

# In[25]:


print('• For distribution, Zimbabwe has a much larger distribution than the other countries. Similarly, the life expectancy of Zimbabwe has changed the most as there is a greater range of life expectancy to make up the average around 46 years.')


# ## Step 7. Bar Plots Of GDP and Life Expectancy over time
# 
# We want to compare the GDPs of the countries over time, in order to get a sense of the relationship between GDP and life expectancy. 
# 
# First, can plot the progession of GDP's over the years by country in a barplot using Seaborn.
# We have set up a figure with the correct dimensions for your plot. Under that declaration:
# 1. Save `sns.barplot()` to a variable named `ax`
# 2. Chart `Country` on the x axis, and `GDP` on the `Y` axis on the barplot. Hint: `ax = sns.barplot(x="Country", y="GDP")`
# 3. Use the `Year` as a `hue` to differentiate the 15 years in our data. Hint: `ax = sns.barplot(x="Country", y="GDP", hue="Year", data=df)`
# 4. Since the names of the countries are long, let's rotate their label by 90 degrees so that they are legible. Use `plt.xticks("rotation=90")`
# 5. Since our GDP is in trillions of US dollars, make sure your Y label reflects that by changing it to `"GDP in Trillions of U.S. Dollars"`. Hint: `plt.ylabel("GDP in Trillions of U.S. Dollars")`
# 6. Be sure to show your plot.
# 

# In[28]:


f, ax = plt.subplots(figsize=(10, 15))
sns.set(style='whitegrid', context='talk')
ax = sns.barplot(x="Country", y="GDP", hue="Year", data=df)
ax.set_ylabel("GDP in USD x 10^13")
labels = ['Chile', 'China', 'Germany', 'Mexico', 'USA', 'Zimbabwe']
ax.set_xticks(range(6))
ax.set_xticklabels(labels)
ax.set_xlabel("")
plt.title("GDP in each Country over Time")

plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

plt.savefig("GDP_Country_Year_bar.png")


# Now that we have plotted a barplot that clusters GDP over time by Country, let's do the same for Life Expectancy.
# 
# The code will essentially be the same as above! The beauty of Seaborn relies in its flexibility and extensibility. Paste the code from above in the cell bellow, and: 
# 1. Change your `y` value to `LEABY` in order to plot life expectancy instead of GDP. Hint: `ax = sns.barplot(x="Country", y="LEABY", hue="Year", data=df)`
# 2. Tweak the name of your `ylabel` to reflect this change, by making the label `"Life expectancy at birth in years"` Hint: `ax.set(ylabel="Life expectancy at birth in years")`
# 

# In[30]:


f, ax = plt.subplots(figsize=(10, 15)) 

ax = sns.barplot(x="Country", y="LEABY", hue="Year", data=df)
ax.set(ylabel="Life Expectancy at Birth (Years)")
labels = ['Chile', 'China', 'Germany', 'Mexico', 'USA', 'Zimbabwe']
ax.set_xticks(range(6))
ax.set_xticklabels(labels)
ax.set_xlabel("")
plt.title("Life Expectancy in each Country over Time")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

plt.savefig("Life_Country_Year_bar.png")


# What are your first impressions looking at the visualized data?
# 
# - Which countries' bars changes the most?
# - What years are there the biggest changes in the data?
# - Which country has had the least change in GDP over time? 
# - How do countries compare to one another?
# - Now that you can see the both bar charts, what do you think about the relationship between GDP and life expectancy?
# - Can you think of any reasons that the data looks like this for particular countries?

# In[37]:


print('• The life expectancy in Zimbabwe changes the most from roughly 45 in year 2000, to over 65 in year 2015.')
print('• The biggest changes in GDP data occur between 2004-2009. The biggest changes in life expectancy seem to occur roughly around 2008-2010.')
print('• The country with the least change in GDP has been Zimbabwe followed by Chile.')
print('• While all the countries have seen an increase in life expectancy over the 15 year timeline, Zimbabwe has seen the greatest growth in the dataset. Excluding Zimbabe, all the countries are roughly the same life expectancy, ranging from 70 to 82 years.')
print('• When analyzing the two bar charts, there appears to be no significant relationship between GDP and life expectancy. Countries that have dispropriately large GDPs do not have an average life expectancy disproportiately longer than other countries.')
print('• Starting with the country Zimbabwe, their GDP is tiny compared to the other world countries. With low GDP, citizens may not have proper access to clean water, sanitary living conditions, modern medicine, and transportation like first world countries. As more countries banded together to help third world countries, particuarly in the years 2004-2009, the life expectancy may have come up with it. Next, looking at countries like Chile and Mexico, while their GDPs are low, they have had relative stable political environments and avoided civil/global wars that often cause turmoil on living conditions and life expectancy. The remaining countries: China, Germany, USA, all have relatively strong GDPs and have seen relatively stable, high average life expectancies.')


# Note: You've mapped two bar plots showcasing a variable over time by country, however, bar charts are not traditionally used for this purpose. In fact, a great way to visualize a variable over time is by using a line plot. While the bar charts tell us some information, the data would be better illustrated on a line plot.  We will complete this in steps 9 and 10, for now let's switch gears and create another type of chart.

# ## Step 8. Scatter Plots of GDP and Life Expectancy Data

# To create a visualization that will make it easier to see the possible correlation between GDP and life expectancy, you can plot each set of data on its own subplot, on a shared figure.
# 
# To create multiple plots for comparison, Seaborn has a special (function)[https://seaborn.pydata.org/generated/seaborn.FacetGrid.html] called `FacetGrid`. A FacetGrid takes in a function and creates an individual graph for which you specify the arguments!
#     
# Since this may be the first time you've learned about FacetGrid, we have prepped a fill in the blank code snippet below. 
# Here are the instructors to fill in the blanks from the commented word bank:
# 
# 1. In this graph, we want GDP on the X axis and Life Expectancy on the Y axis.
# 2. We want the columns to be split up for every Year in the data
# 3. We want the data points to be differentiated (hue) by Country.
# 4. We want to use a Matplotlib scatter plot to visualize the different graphs
# 
# 
# Be sure to show your plot!
# 

# In[38]:


# WORDBANK:
# "Year"
# "Country" 
# "GDP" 
# "LEABY" 
# plt.scatter


# Uncomment the code below and fill in the blanks
# g = sns.FacetGrid(_____NAME_OF_DATAFRAME_________, col=_______COLUMN_______, hue=________DIFFERENTIATOR________, col_wrap=4, size=2)
# g = (g.map(______MATPLOTLIB_FUNCTION______, ______X_DATA______, ______Y_DATA______, edgecolor="w").add_legend())

sns.set(style='whitegrid', palette='bright')
g = sns.FacetGrid(df, col="Year", hue="Country", col_wrap=4, height=2)
g = (g.map(plt.scatter,"GDP", "LEABY", edgecolor="w").add_legend()).set_titles('{col_name}')
g.fig.suptitle('GDP vs. Life Expectancy per Year',fontsize=16)
g.fig.subplots_adjust(top=0.90)

plt.savefig("GDP_Life_Country_Year_facet.png")
plt.show()


# + Which country moves the most along the X axis over the years?
# + Which country moves the most along the Y axis over the years?
# + Is this surprising?
# + Do you think these scatter plots are easy to read? Maybe there's a way to plot that! 

# In[40]:


print('• China has the biggest GDP growth over the dataset years 2000-2015.')
print('• Zimbabwe has the biggest increase in LEABY over the years.')
print('• No. This is not surprising. The massive increase in the middle class has created a massive increase in the GDP of China. The lack of increase in GDP in Zimbabwe, but significant increases in LEABY I believe can be hypothesized to be a result of globalization and increasing support from first world countries helping third world countries.')
print('• The scatter plots are not the easiest to read. It is hard to analyze big picture all at once with scatter plots')


# ## Step 9. Line Plots for Life Expectancy

# In the scatter plot grid above, it was hard to isolate the change for GDP and Life expectancy over time. 
# It would be better illustrated with a line graph for each GDP and Life Expectancy by country. 
# 
# FacetGrid also allows you to do that! Instead of passing in `plt.scatter` as your Matplotlib function, you would have to pass in `plt.plot` to see a line graph. A few other things have to change as well. So we have created a different codesnippets with fill in the blanks.  that makes use of a line chart, and we will make two seperate FacetGrids for both GDP and Life Expectancy separately.
# 
# Here are the instructors to fill in the blanks from the commented word bank:
# 
# 1. In this graph, we want Years on the X axis and Life Expectancy on the Y axis.
# 2. We want the columns to be split up by Country
# 3. We want to use a Matplotlib line plot to visualize the different graphs
# 
# 
# Be sure to show your plot!
# 
# 

# In[41]:


# WORDBANK:
# plt.plot
# "LEABY"
# "Year"
# "Country"

# Uncomment the code below and fill in the blanks
# g3 = sns.FacetGrid(df, col="__________", col_wrap=3, size=4)
# g3 = (g3.map(__plot___, "___x__", "___y___").add_legend())

sns.set(style='whitegrid')
g2 = sns.FacetGrid(df, col="Country", col_wrap=3, height=4, palette='bright')
g2 = (g2.map(plt.plot, "Year", "LEABY").add_legend()).set_ylabels('Life Expectation').set_titles('{col_name}')
plt.locator_params(axis='x', nbins=4)
g2.fig.suptitle('Life Expectancy vs. Year per Country',fontsize=16)
g2.fig.subplots_adjust(top=0.90)

plt.savefig("Life_Country_Year_facet.png")


# What are your first impressions looking at the visualized data?
# 
# - Which countries' line changes the most?
# - What years are there the biggest changes in the data?
# - Which country has had the least change in life expectancy over time? 
# - Can you think of any reasons that the data looks like this for particular countries?

# In[42]:


print('• Zimbabwe and China have seen the largest increases in Life Expectancy, respectively.')
print('• The years between 2004-2009 saw the greatest changes in life expectancy for Zimbabwe. The other countries increases were not as substantial.')
print('• The United States saw the least change in life expectancy over time. This can be explained by the country being a developed first world country that has already seen massive increases in life expectancy earlier on in its history. There has been no revolutionary changes in modern medicine or GDP/capita')
print('• The massive increase in life expectancy for Zimbabwe, and arguably some for Chile, could be explained by the globalization wave that happened in the early 2000s that resulted in support for third world countries and increased supplies/access to modern medicine.')


# ## Step 10. Line Plots for GDP

# Let's recreate the same FacetGrid for GDP now. Instead of Life Expectancy on the Y axis, we now we want GDP.
# 
# Once you complete and successfully run the code above, copy and paste it into the cell below. Change the variable for the X axis. Change the color on your own! Be sure to show your plot.
# 

# In[43]:


g3 = sns.FacetGrid(df, col="Country", col_wrap=3, height=4)
g3 = (g3.map(plt.plot, "Year", "GDP").add_legend()).set_ylabels('GDP in USD x 10^13').set_titles('{col_name}')
plt.locator_params(axis='x', nbins=4)
g3.fig.suptitle('GDP vs. Year per Country',fontsize=16)
g3.fig.subplots_adjust(top=0.90)
plt.savefig("GDP_Country_Year_facet.png")


# Which countries have the highest and lowest GDP?

# In[44]:


print('• The countries with the highest GDP is the United States of America, followed by China. The countries with the lowest GDP is Zimbabwe, followed by Chile.')


# Which countries have the highest and lowest life expectancy?

# In[46]:


print('• The countries with the highest life expectancy is Chile followed by Germany and the USA. The country with the lowest life expectancy is Zimbabwe.')


# ## Step 11 Researching Data Context 

# Based on the visualization, choose one part the data to research a little further so you can add some real world context to the visualization. You can choose anything you like, or use the example question below.
# 
# What happened in China between in the past 10 years that increased the GDP so drastically?

# In[54]:


print('• In the year 2000, China was just coming out of a slowed economy due to the Asian Financial Crisis. They saw decreased foreign direct investment and a sharp drop in its growth of its exports. However, the GDP was starting to gain momentum after, with the GDP growing at an official 8.0% y/y in 2000, a growth rate 4x as large since 1978. China had huge currency reserves and a sizable inflow of long-term investments in the country, thus the country was largely less affected than other regional countries.')
print('• In order to get their country back on track, they went through impressive economic development changes from reforming the state sector to modernizing the banking system. The following years the Chinese government implement many amendments and investment proposals that continued this momentum. A big turning point occured in 2005, when the country approved the 11th Five-Year Economic Program from 2006-2010 that aimed at building more balanced wealth distribution and improved education, medical care, and social security. The years following, China saw massive growth in the middle class and the standard of living for its citizens. The world Bank confirmed in 2009 that China grew to be the worlds third largest economy by GDP.')


# ## Step 12 Create Blog Post

# Use the content you have created in this Jupyter notebook to create a blog post reflecting on this data.
# Include the following visuals in your blogpost:
# 
# 1. The violin plot of the life expectancy distribution by country
# 2. The facet grid of scatter graphs mapping GDP as a function Life Expectancy by country
# 3. The facet grid of line graphs mapping GDP by country
# 4. The facet grid of line graphs mapping Life Expectancy by country
# 
# 
# We encourage you to spend some time customizing the color and style of your plots! Remember to use `plt.savefig("filename.png")` to save your figures as a `.png` file.
# 
# When authoring your blog post, here are a few guiding questions to guide your research and writing:
# + How do you think the histories and the cultural values of each country relate to its GDP and life expectancy?
# + What would have helped make the project data more reliable? What were the limitations of the dataset?
# + Which graphs better illustrate different relationships??

# In[ ]:





# In[ ]:





# In[ ]:




