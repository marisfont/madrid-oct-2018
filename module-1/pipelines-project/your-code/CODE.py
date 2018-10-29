import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Acquisition
def acquire():
    data = pd.read_csv('./Data/countries of the world.csv')
    return data

# Step 2: Wrangling
def wrangle(data, year):
    return data[data['Year']==year]

# Step 3: Analysis
def analyze(filtered):
    grouped_region = data.groupby('Region')
    mean_region = grouped_region.agg({'GDP ($ per capita)':'mean'}).reset_index()
    results_region = mean_region.sort_values('GDP ($ per capita)', ascending=False).head(3)
    return results_region

# Step 4: Reporting
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
