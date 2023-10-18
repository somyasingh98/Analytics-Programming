#!/usr/bin/env python
# coding: utf-8

# In[26]:


import pandas as pd
import matplotlib.pyplot as plt
# Load the dataset into a pandas dataframe
df = pd.read_csv('M4_Data.csv')

# Display the first few rows of the dataset to understand its structure
df.head()


# In[ ]:





# In[38]:


class Solution:
    def __init__(self, file_path):
        """Initializing the class with the dataset."""
        self.df = pd.read_csv(file_path)
    
    def task_one(self):
        """Calculate the proportion of customers with age > average age and age < 56."""
        avg_age = self.df['age'].mean()
        selected_customers = self.df[(self.df['age'] > avg_age) & (self.df['age'] < 56)]
        proportion = len(selected_customers) / len(self.df)
        return proportion
    
    def task_two(self):
        """Q2. Determine how many customers that have purchased Product B have spent more 
        on Product B than 1.5 times the median amount spent on Product B."""
        median_turnover_B = self.df['turnover_B'].median()
        selected_customers = self.df[(self.df['prod_B'] == 1) & 
                                     (self.df['turnover_B'] > 1.5 * median_turnover_B)]
        return len(selected_customers)
    def task_three(self):
        """Determine how many customers have spent more on Product B than on Product A."""
        selected_customers = self.df[self.df['turnover_B'] > self.df['turnover_A']]
        return len(selected_customers)
    
    def task_four(self):
        """Determine how many customers have purchased either type 6 of Product A or type 9 of Product B."""
        selected_customers = self.df[(self.df['type_A'] == 6) | (self.df['type_B'] == 9)]
        return len(selected_customers)

    def task_five(self):
        """Identify the customer with the highest average monthly spending."""
        self.df['total_spending'] = self.df['turnover_A'] + self.df['turnover_B']
        self.df['avg_monthly_spending'] = self.df['total_spending'] / self.df['lor_M']
        max_avg_spending_idx = self.df['avg_monthly_spending'].idxmax()
        selected_customer = self.df.iloc[max_avg_spending_idx]
        return {
            'row_index': max_avg_spending_idx,
            'ID': selected_customer['ID'],
            'lor_M': selected_customer['lor_M'],
            'total_spending': selected_customer['total_spending'],
            'dataframe_row': selected_customer
        }
    

    def task_six(self):
        """Generate bar plots for 'type_A' and 'type_B'."""
        fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(14, 6))
        
        # Bar plot for 'type_A'
        self.df['type_A'].value_counts().sort_index().plot(kind='bar', ax=ax[0], color='c')
        ax[0].set_title("Distribution of 'type_A'")
        ax[0].set_xlabel('Type of Product A')
        ax[0].set_ylabel('Number of Customers')
        
        # Bar plot for 'type_B'
        self.df['type_B'].value_counts().sort_index().plot(kind='bar', ax=ax[1], color='m')
        ax[1].set_title("Distribution of 'type_B'")
        ax[1].set_xlabel('Type of Product B')
        ax[1].set_ylabel('Number of Customers')
        
        plt.tight_layout()
        plt.show()

    def task_seven(self):
        """Generate boxplots of the 'age' attribute for each type of Product B."""
        plt.figure(figsize=(12, 7))
        ax = plt.gca()
        
        # Box plot for age distribution by 'type_B'
        self.df.boxplot(column='age', by='type_B', ax=ax)
        ax.set_title("Age Distribution by 'type_B'")
        ax.set_xlabel('Type of Product B')
        ax.set_ylabel('Age')
        plt.suptitle('')  # Suppress default title
        plt.show()
        
    def task_eight(self):
        """Generate histograms of the 'age' and 'lor_M' attributes, 
        and boxplots of the 'turnover_A' and 'turnover_B' attributes."""
        fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(14, 10))
        
        # Histogram for 'age'
        self.df['age'].hist(ax=ax[0, 0], color='c', bins=30)
        ax[0, 0].set_title("Distribution of Age")
        ax[0, 0].set_xlabel('Age')
        ax[0, 0].set_ylabel('Number of Customers')
        
        # Histogram for 'lor_M'
        self.df['lor_M'].hist(ax=ax[0, 1], color='m', bins=30)
        ax[0, 1].set_title("Distribution of Length of Relationship (in months)")
        ax[0, 1].set_xlabel('Length of Relationship (lor_M)')
        ax[0, 1].set_ylabel('Number of Customers')
        
        # Boxplot for 'turnover_A'
        self.df.boxplot(column='turnover_A', ax=ax[1, 0])
        ax[1, 0].set_title("Boxplot of Turnover for Product A")
        ax[1, 0].set_ylabel('Turnover Amount')
        
        # Boxplot for 'turnover_B'
        self.df.boxplot(column='turnover_B', ax=ax[1, 1])
        ax[1, 1].set_title("Boxplot of Turnover for Product B")
        ax[1, 1].set_ylabel('Turnover Amount')
        
        plt.tight_layout()
        plt.show()

    def task_nine(self):
        """Generate a scatter plot of 'turnover_A' vs. 'lor_M'."""
        plt.figure(figsize=(12, 7))
        plt.scatter(self.df['lor_M'], self.df['turnover_A'], alpha=0.5, color='b')
        plt.title("Scatter Plot of Turnover for Product A vs. Length of Relationship")
        plt.xlabel('Length of Relationship (lor_M)')
        plt.ylabel('Turnover for Product A')
        plt.show()


# In[39]:


# Initialize the class with the dataset
analysis = Solution('M4_Data.csv')

# Get the result for task two
task_one_result = analysis.task_one()
task_two_result = analysis.task_two()
task_three_result=analysis.task_three()
task_four_result=analysis.task_four()
task_five_result=analysis.task_five()

print(task_one_result)
print(task_two_result)
print(task_three_result)
print(task_four_result)
print(task_five_result)


# ---
# 
# ### Task 1:
# #### What proportion of customers have an age of more than the average customer age but less than 56?
# 
# **Result**: The result was approximately 33% (or 0.33 when expressed as a proportion) of customers have an age greater than the average age but less than 56.
# 
# ---
# 
# ### Task 2:
# #### How many customers that have purchased Product B have spent more on Product B than 1.5x the median amount that customers typically spend on Product B?
# 
# **Result**: 865 customers who purchased Product B have spent more than 1.5 times the median amount typically spent on Product B.
# 
# ---
# 
# ### Task 3:
# #### How many customers have spent more on Product B than they have on Product A?
# 
# **Result**: 756 customers have spent more on Product B than they have on Product A.
# 
# ---
# 
# ### Task 4:
# #### How many customers have purchased either type 6 of Product A or type 9 of Product B?
# 
# **Result**: 55 customers have purchased either type 6 of Product A or type 9 of Product B.
# 
# ---
# 
# ### Task 5:
# #### Which customer has attained the highest average amount of monthly spending across all products during their tenure with the company?
# 
# **Result**: 
# - Row index: 10713
# - Customer ID: 16185
# - Length of relationship (in months): 15
# - Total spending: $12,557.10
# 
# This customer has been with the company for 15 months and has an average monthly spending of approximately $837.14.

# In[34]:


task_six_result=analysis.task_six()


# ---
# 
# ### Task 6:
# #### Analysis of 'type_A' and 'type_B' bar plots:
# 
# - **Distribution of 'type_A'**: 
#   - Type 0 has the highest count, indicating many customers have not purchased Product A. 
#   - Among those who did, type 3 is the most common, followed by types 1, 2, and 4. 
#   - Types 5 and 6 of Product A have comparatively fewer customers.
#   
# - **Distribution of 'type_B'**: 
#   - Similar to Product A, type 0 has the highest count, indicating many customers have not purchased Product B.
#   - Among those who did, type 3 is the most popular, followed by types 6 and 2. 
#   - Types 1, 4, 5, 7, 8, and 9 have fewer customers.
# 
# The bar plots provide a clear representation of the popularity of each product type, aiding in understanding customer preferences.
# 
# ---

# In[35]:


task_seven_result=analysis.task_seven()


# ---
# 
# ### Task 7:
# #### Analysis of 'age' boxplots for each type of Product B:
# 
# Most types of Product B have a median age of customers around 40 to 50 years. However, the age interquartile range (IQR) is fairly consistent across most product types, indicating that the age groups attracted to different product types are relatively similar. There are a few outliers in the age data for certain product types.
# 
# ---

# In[36]:


task_eight_result=analysis.task_eight()


# ---
# 
# ### Task 8:
# #### Analysis of histograms and boxplots:
# 
# - **Distribution of Age**: The age distribution is slightly right-skewed, indicating a higher concentration of younger customers. Most customers fall between 30 and 60 years old.
#   
# - **Distribution of Length of Relationship (`lor_M`)**: The distribution is heavily right-skewed. Most customers have been with the company for a short period, with a few having long relationships.
#   
# - **Turnover for Product A**: Most customers spend between 0 and 1000 on Product A. There are outliers indicating a few customers with very high spending.
# 
# - **Turnover for Product B**: Similar to Product A, most customers spend between 0 and 1000 on Product B. There are fewer extreme outliers compared to Product A.
# 
# The visuals indicate a majority of new customers. Some customers spend significantly more, indicating potential high-value customers.
# 
# ---

# In[37]:


task_nine_result=analysis.task_nine()


# ---
# 
# ### Task 9:
# #### Analysis of scatter plot of `turnover_A` vs. `lor_M`:
# 
# Most customers, irrespective of their relationship length with the company, spend a modest amount on Product A. As the relationship length increases, there's a wider spread in turnover values. This suggests the length of relationship alone doesn't determine spending behavior.
# 
# ---

# In[ ]:




