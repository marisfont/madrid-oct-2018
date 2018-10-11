try:
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
    import os
    from pandas import ExcelWriter
except ImportError:
    print('You should install the libraries before importing')


# The goals of this data pipeline are getting:
# 1. Top 10 vintages, countries and variety by average score (data visualization)##
# 2. Table of basic statistics for price-points
# 3. First insights on price-points(scores) relationship

# We download the dataset wine reviews from Kaggle that is available in the data folder

    try:
        path ='./data folder/winemag-data.csv'
        data = pd.read_csv(path,usecols=range(1,14))
    except OSError:
        print('The file is not available on the path or the path does not exist')
    return data

# The dataset has 129.971 records. There are 120.975 not-null records in price column and some outliers.
# Filtering the dataset by price value <= 100 USD we hold 97% of the data and leave outside the outliers.
# We build a filtered dataset with this price threshold and replacing missing values in price with the average score by score
# We also extract the vintage from the title creating a new column in the datsaset
# We finally create a new column with a score bucket

def wrangle(df):
    # Filtering dataset by prices <= 100 USD
    filtered = df[df['price'] <= 100]
    # Replacing missing values in price column
    filtered['price']= filtered['price'].fillna(filtered.groupby(['points']).price.transform('mean'))
    #Add vintage and score_bucket columns
    filtered['vintage']= filtered['title'].str.extract('(19[7-9]\d|2\d{3})', expand=True)
    filtered['score_bucket'] = pd.cut(filtered['points'], bins=5)
    return filtered

# We get the top 10 vintages, countries and varieties by the average scores in Wine Reviews

def analyze(df):
    results_list = []
    #Average score grouped by vintage, country and variety
    grouped_vintage = filtered.groupby('vintage').agg({'points':'mean'}).reset_index().sort_values('points', ascending=False).head(10)
    grouped_country = filtered.groupby('country').agg({'points':'mean'}).reset_index().sort_values('points', ascending=False).head(10)
    grouped_variety = filtered.groupby('variety').agg({'points':'mean'}).reset_index().sort_values('points', ascending=False).head(10)
    #Top 10 results for vintage, country and variety
    results_vintage = results_list.append (grouped_vintage)
    results_country = results_list.append (grouped_country)
    results_variety = results_list.append (grouped_variety)
    return results_list

# We build a figure with the three barplots generated

def visualize(df):
    # Set up the matplotlib figure
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 16), sharex=True)
    sns.set(style="whitegrid", palette="pastel", color_codes=True)
    fig.suptitle('Top 10 Vintages, Varieties and Countries by Average Score',\
           size = 18, fontweight = 'extra bold', va = 'center')
    x='points'
    for result in results_list:
        sns.barplot(x=x, y='vintage', data = results_list[0], palette ='Blues_d',  ax=ax1, orient = 'h')
        sns.barplot(x=x, y='country', data = results_list[1], palette = 'Blues_d', ax=ax3, orient = 'h')
        sns.barplot(x=x, y='variety', data = results_list[2], palette = 'Blues_d', ax=ax2, orient = 'h')
    plt.subplots_adjust(top=0.85)
    sns.despine(bottom=True)
    plt.tight_layout(rect=[0, 0.03, 1, 0.95],h_pad=2)
    fig.savefig('./output folder/barplots.png', dpi=400)

# We get price basic stastistics (mean, std, percentiles, IQR) by score and by bucket score

def stats(df):
    score_list = []
    aggregations = ({
        'price': {
            'count': 'count',
            'mean': 'mean',
            'std': 'std',
            'min': 'min',
            '25%': lambda x: x.quantile(0.25),
            '50%': lambda x: x.quantile(0.50),
            '75%': lambda x: x.quantile(0.75),
            'max': 'max',
            'IQR': lambda x: x.quantile(0.75) - x.quantile(0.25)

        }
    })
    #By points and by score bucket 
    grouped_points= filtered.groupby('points').aggregate(aggregations).reset_index()
    grouped_score_buckets=filtered.groupby('score_bucket').agg(aggregations).reset_index()
    #Append sorted results to our score_list 
    score_results= score_list.append(grouped_points.sort_values('points',ascending=False))
    bucket_score_results= score_list.append(grouped_score_buckets.sort_values('score_bucket',ascending=False))
    return score_list

    # We finally save the styled tables with the basic statistics

    def tables(list_tables,xls_path = None):
    #save_xls([df1,df2],'output1.xlsx')
    if xls_path == None :
        xls_path = './output folder/scores.xlsx'
    writer = ExcelWriter(xls_path)
    i=0
    for n, table in enumerate(list_tables):
        table.from_dict(table)
        cm = sns.light_palette('seagreen', as_cmap = True)
        styled_table = table.style.background_gradient(cmap = cm)
        styled_table.to_excel(writer,'tables',startcol=0,startrow =i)
        i+= 26
    writer.save()
    os.system('start excel.exe %s' %(writer.path ))

if __name__ == '__main__':
    data = acquire()
    filtered = wrangle(data)
    results_list = analyze(filtered)
    barcharts = visualize(results_list)
    score_list = stats(filtered)
    tables = tables(score_list)