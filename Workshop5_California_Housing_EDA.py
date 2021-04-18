# Python Workshop 5 - California Housing Dataset
# More information on this dataset can be found at this link: https://www.kaggle.com/camnugent/california-housing-prices

# author Sai Narendrula
# email sn42@rice.edu
# date April 18th, 2021


# Make sure these packages are available in your project
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# To get the data, use pd.read_csv. The link is to a webpage on github that has the data
housing_data = pd.read_csv('https://raw.githubusercontent.com/mohitgupta-omg/Kaggle-California-Housing-Prices/master/Data/housing.csv')
# The data is stored in a DataFrame called housing_data

# To get the size, use len() or .shape
print(len(housing_data))
print(housing_data.shape)

# To get all columns, use .columns()
print(housing_data.columns())

# Use .head() to see the first five values from each column in the table
print(housing_data.head())

# To get random rows from the dataset, we can use .sample(n) where n is the number of samples you want
print(housing_data.sample(6))

# Use .describe() to get the statistics from all columns that have numbers
print(housing_data.describe())

# To see what unique values or the number of unique values that exist in a Series (column of the DataFrame)
# use .unique() and .nunique()
print(housing_data["ocean_proximity"].unique())
print(housing_data["ocean_proximity"].nunique())

# Visualising geographical data using seaborn

# Use sns.scatterplot() to look at where the house blocks are
sns.scatterplot(x="longitude", y="latitude", data=housing_data)

# alpha allows you to fade out data points
sns.scatterplot(x="longitude", y="latitude", data=housing_data, alpha=0.1)

# Look at how median house incomes changes in where people live
fig = sns.scatterplot(
    x="longitude",
    y="latitude",
    data=housing_data,
    alpha=0.1,
    hue="median_house_value",
    palette="viridis",
    size=housing_data["population"] / 100
)

# place legend outside of figure
fig.legend(loc="center left", bbox_to_anchor=(1.01, 0.6), ncol=1);

# Total median income V/S Median house value
fig, ax = plt.subplots(figsize=(12, 8))
plt.scatter(housing_data['median_income'], housing_data['median_house_value'])
plt.xlabel('Median Income')
plt.ylabel('Median House Value')

# Check for correlation with each features
housing_data_corr = housing_data.corr()
print(housing_data_corr)

# Visualize the correlation with help of heatmap
fig, ax = plt.subplots(figsize=(12,10))
sns.heatmap(housing_data_corr, annot=True)
