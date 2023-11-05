#!/usr/bin/env python
# coding: utf-8

# # Import all the necessary liabrarys

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# # Load the data set and did some basic analysis

# In[2]:


df = pd.read_csv(r"C:\Users\Najla\Downloads\riyadh_cafes.csv")
df = df.drop("index", axis=1)
df.head()


# In[3]:


df.dtypes


# In[4]:


df.columns


# In[5]:


df.info()


# In[6]:


df.describe()


# In[7]:


df['coffeeName'].value_counts()


# In[8]:


df['coffeeName']


# In[9]:


df = df.dropna()


# In[10]:


df


# In[11]:


len(df['coffeeName'])


# In[12]:


# Calculate the average rating
average_rating = df['rating'].mean()

# Print the result
print("Average rating of cafes in Riyadh:", average_rating)


# In[13]:


#filter the cafees that operates 24 hours
operates_24_hours = df[df['24_hours'] == True]

# Count the number of cafes that operate 24 hours
num_cafes_24_hours = len(operates_24_hours)

#print the result
print("Number of cafes that operate 24 hours:", num_cafes_24_hours)


# In[14]:


#Find the cafe with the highest rating
highest_rating_cafe = df.loc[df['rating'].idxmax()]

#Extract the cafe name and its rating
cafe_name = highest_rating_cafe['coffeeName']
rating = highest_rating_cafe['rating']

#print the result
print("Cafe with the highest rating:", cafe_name)
print('Rating:', rating)


# In[15]:


#Find the cafe with the most ratings
most_popular_cafe = df.loc[df['rating_count'].idxmax()]

#Extract the cafe name and its rating count
cafe_name = most_popular_cafe['coffeeName']
rating_count = most_popular_cafe['rating_count']

# Print the result
print("Cafe with the most ratings:", cafe_name)
print("Rating count:", rating_count)


# In[16]:


#Extract the 'rating' column from the dataset
ratings = df['rating']

#Plot the distribution of ratings
plt.hist(ratings, bins=10, edgecolor='black')

# Set labels and title
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.title('Distribution of Ratings of Cafes')


# In[17]:


# Sort the cafes based on rating count in descending order and select top 5
top_cafes = df.nlargest(5, 'rating_count')

# Extract the cafe names and their rating counts
cafe_names = top_cafes['coffeeName']
rating_counts = top_cafes['rating_count']

custom_colors = ['#071952', '#0B666A', '#35A29F', '#97FEED']

# Create a bar plot to visualize the top 5 cafes
plt.bar(cafe_names, rating_counts, color=custom_colors)

# Set labels and title
plt.xlabel('Cafe')
plt.ylabel('Rating Count')
plt.title('Top 5 Most Popular Cafes')

# Add rating count values on top of each bar
for i, v in enumerate(rating_counts):
    plt.text(i, v, str(v), ha='center', va='bottom')

# Add legend
plt.legend(['Rating Count'])
plt.xticks(rotation=45)


# In[18]:


# Define custom color palette
custom_colors = ['#6F61C0', '#A084E8', '#8BE8E5', '#D5FFE4']


# In[19]:


# Count the number of cafes operating 24 hours vs not
operating_hours = df['24_hours'].value_counts()

# Define custom colors for open and closed cafes
custom_colors = ['#071952', '#0B666A', '#35A29F', '#97FEED']

# Create a bar plot to compare cafes operating 24 hours vs not
plt.bar(operating_hours.index, operating_hours.values, color=custom_colors)

# Set labels and title for the bar plot
plt.xlabel('Operating Hours')
plt.ylabel('Count')
plt.title('Cafes Operating 24 Hours vs Not')

# Add count values on top of each bar
for i, v in enumerate(operating_hours.values):
    plt.text(i, v, str(v), ha='center', va='bottom')

# Add a legend
plt.legend(['No', 'Yes'], title='Open')


# In[20]:


# Sort the cafes by rating in descending order and select the top 5
top_cafes = df.nlargest(5, 'rating')

#Display the top 5 cafes with the highest ratings
print(top_cafes[['coffeeName', 'rating']])


# In[21]:


# Sort the cafes by rating in descending order and select the top 5
top_cafes = df.nlargest(10, 'rating')

# Create a figure with a larger size
plt.figure(figsize=(12, 8))

custom_colors = ['#071952', '#0B666A', '#35A29F', '#97FEED']

# Create a horizontal bar plot to visualize the top 5 cafes with the highest ratings
plt.barh(top_cafes['coffeeName'], top_cafes['rating'], color=custom_colors)

# Set labels and title for the plot
plt.xlabel('Rating')
plt.ylabel('Cafes')
plt.title('Top 5 Cafes with the Highest Ratings')

# Add ratings values on the right side of each bar
for i, v in enumerate(top_cafes['rating']):
    plt.text(v + 0.1, i, str(v), va='center')

# Invert the y-axis to display the highest rating at the top
plt.gca().invert_yaxis()

# Adjust spacing and layout
plt.tight_layout()


# In[22]:


top_rated_caffee = df[df['rating'] == 5]
print(top_rated_caffee[['coffeeName', 'rating']])


# In[23]:


specific_cafes = df[df['rating'] == 4.5]

# Select the top 10 cafes
top_10_cafes = specific_cafes.head(10)

# Print the top 10 cafes
print(top_10_cafes[['coffeeName', 'rating']])


# In[24]:


custom_colors = ['#461959', '#7A316F', '#CD6688', '#AED8CC']

# Create a bar chart to visualize the ratings of the top 10 cafes
plt.figure(figsize=(12, 8))
plt.bar(top_10_cafes['coffeeName'], top_10_cafes['rating'], color=custom_colors)
plt.xlabel('Cafe')
plt.ylabel('Rating')
plt.title('Top 10 Cafes with a Rating of 4.5')

# Add data labels above each bar
for i, rating in enumerate(top_10_cafes['rating']):
    plt.text(i, rating + 0.1, str(rating), ha='center')

plt.xticks(rotation=75)
plt.ylim(0, 5)  # Set the y-axis range
plt.tight_layout()  # Adjust spacing
plt.show()


# In[25]:


# Filter the cafes with ratings from 3.7 to 5
filtered_cafes = df[(df['rating'] >= 3.7) & (df['rating'] <= 5)]

# Count the number of cafes in each rating category
rating_counts = filtered_cafes['rating'].value_counts().sort_index()

# Select the top 15 rating categories based on the count
top_15_categories = rating_counts.nlargest(14)

custom_colors = ['#071952', '#0B666A', '#35A29F', '#97FEED']

# Create a bar chart to visualize the number of cafes in each rating category
plt.figure(figsize=(10, 8))
width = 0.1

# Plot the bars
bars = plt.bar(top_15_categories.index, top_15_categories.values, color=custom_colors, width=width)

# Add cafe counts on top of each bar
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height, int(height), ha='center', va='bottom')

plt.xlabel('Rating')
plt.ylabel('Number of Cafes')
plt.title('Cafes in Each Rating Category (3.7-5)')
plt.xticks(rotation=45)
plt.ylim(0, top_15_categories.max() + 10)  # Set the y-axis range
plt.grid(axis='y', linestyle='--', alpha=0.5)  # Add horizontal grid lines
plt.tight_layout()  # Adjust spacing


# In[26]:


filtered_cafes['rating'].value_counts().sort_index()


# In[27]:


operate_24_hours = df[df['24_hours'] == True]

# Find the highest-rated cafe among those that operate 24 hours
highest_rated_cafe = operate_24_hours.loc[operate_24_hours['rating'].idxmax()]


# In[28]:


highest_rated_cafe


# In[29]:


# Filter cafes that operate 24 hours
cafes_24h = df[df['24_hours'] == 'Yes']

# Filter cafes that do not operate 24 hours
cafes_non_24h = df[df['24_hours'] != 'Yes']

if cafes_24h.empty:
    print("No rating counts available for cafes operating 24 hours.")
else:
    # Calculate the average rating count for cafes operating 24 hours
    avg_rating_24h = np.nanmean(cafes_24h['rating_count'])
    print("Average rating count for cafes operating 24 hours:", avg_rating_24h)

# Calculate the average rating count for cafes not operating 24 hours
avg_rating_non_24h = cafes_non_24h['rating_count'].mean()
print("Average rating count for cafes not operating 24 hours:", avg_rating_non_24h)


# In[30]:


df


# # Add distance feature to dataset and also if you select any caffe it will give you 5 nearest caffee to that withtheir distance using geodesic liabrary

# In[31]:


from geopy.distance import geodesic


# In[32]:


def find_nearest_cafes(name, df, top=5):
    target_cafe = df[df['coffeeName'] == name]
    
    if target_cafe.empty:
        print("No cafe found with the given name.")
        return
    
    target_location = (target_cafe['lan'].values[0], target_cafe['lon'].values[0])

    df['distance'] = df.apply(lambda row: calculate_distance(row, target_location), axis=1)
    nearest_cafes = df[df['coffeeName'] != name].sort_values('distance').head(top)

    return nearest_cafes

def calculate_distance(row, target_location):
    try:
        if isinstance(row['lan'], str) and row['lan'].lower() == 'null':
            return None
        if isinstance(row['lon'], str) and row['lon'].lower() == 'null':
            return None

        return geodesic(target_location, (float(row['lan']), float(row['lon']))).km
    except (ValueError, TypeError):
        return None


# In[33]:


find_nearest_cafes('Double one', df)
#nearest_cafes = find_nearest_cafes('PEAKS', df)
#if nearest_cafes is not None:
    #for _, row in nearest_cafes.iterrows():
        #print(f"Caffe {row['coffeeName']}, Distance: {row['distance']} km")


# # If you like and did you learn anything new please do consider to upvote

# In[ ]:




