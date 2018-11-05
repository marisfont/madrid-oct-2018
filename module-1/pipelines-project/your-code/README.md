# Guided Project: Web Data Pipeline


## Step 1: Acquisition

I selected the Countries of the World data set from [Kaggle Data Sets](https://www.kaggle.com/fernandol/countries-of-the-world), which is the same data set I used for the Pandas Project. This data set has data for all countries in the world. 

For this project, I want to find the 3 regions with the highest GDP per capita in 2010 and I want this to be updated every year going forward.

I downloaded the data from Kaggle, which was as a CSV file.

I imported the pandas library.

```
import pandas as pd
```

I defined a function to import the csv file.

```
def acquire():
    data = pd.read_csv('./Data/countries of the world.csv')
    return data
```


## Step 2: Data Wrangling

I defined a function to include only data for a specific year.

```
def wrangle(data, year):
    return data[data['Year']==year]
```


## Step 3: Data Analysis

To find the 3 regions with highest GDP per capita in a specific year, I will use the 'Region' field which  tells us the region each country is in and the 'GDP ($ per capita)' field which tells us the GDP per capita for each country.

To do the analysis and find the results, I defined a function with the following:
- Group by Region 
- Find Average GDP per capita by region
- Sort by Sverage GDP per capita by region
- Show the top 3 results 

```
def analyze(filtered):
    grouped_region = data.groupby('Region')
    mean_region = grouped_region.agg({'GDP ($ per capita)':'mean'}).reset_index()
    results_region = mean_region.sort_values('GDP ($ per capita)', ascending=False).head(3)
    return results_region
```


## Step 4: Data Reporting

To show a better and more visual representation of the data, I decided to create a bar chart of the results.

I imported pyplot, seaborn, and os to create the bar chart.

```
import matplotlib.pyplot as plt
import seaborn as sns
```

I defined the following function and if condition.

```
def reporting(gdpregions, title):
    fig, ax = plt.subplots(figsize=(5,10))
    barchart = sns.barplot(data=gdpregions, x='Region', y='GDP ($ per capita)')
    plt.title(title + "\n", fontsize=16)
    fig = barchart.get_figure()
    fig.savefig(title + '.png')

if __name__ == '__main__':
    year = int(input('Enter the year: '))
    title = 'Top 3 Regions by GDP per capita ' + str(year)
    data = acquire()
    filtered = wrangle(data, year)
    results = analyze(filtered)
    reporting(results, title)
```
**Please note that given the lack of data on the data set, the automation only works for year 2010**
