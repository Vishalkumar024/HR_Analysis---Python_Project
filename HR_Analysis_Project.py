
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import openpyxl as op
from pandas.io.formats.style import coloring_args
from pandas.plotting import boxplot

df = pd.read_excel("employee_salary_dataset.xlsx")

# For checking total rows and columns in our dataset
df.shape

# For checking columns name
df.columns

# Checking our dataset
df.head

# To getting information about our dataset.
df.info()

# ----------------- Performing data cleaning process --------------------

# Checking null values in dataset
pd.isnull(df).sum()

# By above function we got to know that there are 16 null values in are salary.
# Now we delete those null values.
df.dropna(inplace=True)

# Now we can use above "isnull" function to know that whether those null values deleted or not.
pd.isnull(df).sum()

# Checking duplicate entries in dataset
Duplicate_count = df.duplicated().sum()
print(f"Number of duplicate entries: {Duplicate_count}")

# Removing duplicate entries from dataset
df.drop_duplicates(inplace=True)

# Changing datatype of "salary column" from "flot" to "int".
df['Salary'] = df['Salary'].astype('int')

# Checking the above code run successfully or not.
df['Salary'].dtype

# Use "describe()" function to know (count , max, min, mean, std, etc. ) of "Salary" Column.
df['Salary'].describe()

# we perform all necessary data cleaning process for our dataset
# ----------------- Now we done with our data cleaning process for our dataset -----------------

 # ------------------------------------- Exploratory Data Analysis ------------------------------------------------

#1. Count of each department
ax = sns.countplot(x = 'Department', data = df, color='blue')
plt.title("Count of each department")
sns.set(rc={'figure.figsize':(6,4)})
for bars in ax.containers:
    ax.bar_label(bars)
plt.show(block = True)

#2. Frequency of job title
sns.countplot(y='Job Title', hue='Job Title', data=df, palette='coolwarm',
              order=df['Job Title'].value_counts().index)
plt.title("Frequency of job title")
plt.show(block = True)

#3. Department wise salary
department_wise_salary = df.groupby(['Department'],
                                    as_index=False) ['Salary'].sum().sort_values(by='Salary', ascending=False)

sns.set(rc={'figure.figsize':(8,5)})
sns.barplot(x = 'Department', y = 'Salary', hue= 'Department',  data = department_wise_salary, palette='Pastel1')
plt.title("Department wise salary")
plt.show(block = True)

#4. Finding Age distribution of employees
sns.histplot(df['Age'], bins=10, kde=True)
plt.title("Age distribution of employees")
plt.show(block = True)

#5. Salary distribution by experience level
sns.boxplot(x= 'Experience Level', y= 'Salary', data=df)
plt.title("Salary distribution by experience level")
plt.show(block=True)



# -------------------- Now we done with our EDA (Exploratory Data Analysis) ----------------------------------









