#We import the required libraries

try:
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
except ImportError:
    print('You should install the libraries before importing')

# The goals of this data pipeline are getting:
# 1. Table of basic statistics for price-points
# 2. Top 10 vintages, countries and variety by average score (data visualization)
# 3. First insights on price-points(scores) relationship

#We get the dataset wine reviews from Kaggle

def acquire():
    try:
        data = pd.read_csv('../data folder/winemag-data.csv', usecols=range(1,14))
    except OSError:
        print('The file is not available on that path')
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

# We are going to save a pretty table with the basic statistics

def stats(df):
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
    # By points
    grouped_points= filtered.groupby('points').aggregate(aggregations).reset_index()
    score_results= grouped_points.sort_values('points',ascending=False).head(10)
    #By Score Bucket
    grouped_score_buckets=filtered.groupby('score_bucket').agg(aggregations).reset_index()
    bucket_score_results=grouped_score_buckets.sort_values('score_bucket',ascending=False).head(10)
    return score_results,bucket_score_results


if __name__ == '__main__':
    data = acquire()
    filtered = wrangle(data)
    score_results = stats(filtered)
    bucket_score_results = stats(filtered)
    #barchart = visualize(results)
    #save_viz(barchart)