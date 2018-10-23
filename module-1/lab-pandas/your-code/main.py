#1. Import the PANDAS package under the name pd. Import the NUMPY package under the name np

import pandas as pd
import numpy as np

#2. Define a variable called `url` that contains the path to the csv file you downloaded. 

url = pd.read_csv('apple_store.csv')

# Alternatively, you can also assign the hyperlink value to `url`.

"""
url = "https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/data-static/data/apple_store.csv"
"""

#3. Using Pandas' `read_csv()` method, import the csv file at the url above. 
# Assign the returned value to a variable called `data`.
# Note: you can omit the `sep` parameter for `read_csv()` because the csv file uses the default separator of ",".

data = pd.read_csv('apple_store.csv')

"""
data = pd.read_csv(url)
"""

#4. Print the first 5 rows of `data` to see what the data look like.
# A data analyst usually does this to have a general understanding about what the data look like before digging deep.

data.head()

"""
	id	track_name	size_bytes	price	rating_count_tot	rating_count_ver	user_rating	user_rating_ver	prime_genre
0	281656475	PAC-MAN Premium	100788224	3.99	21292	26	4.0	4.5	Games
1	281796108	Evernote - stay organized	158578688	0.00	161065	26	4.0	3.5	Productivity
2	281940292	WeatherBug - Local Weather, Radar, Maps, Alerts	100524032	0.00	188583	2822	3.5	4.5	Weather
3	282614216	eBay: Best App to Buy, Sell, Save! Online Shop...	128512000	0.00	262241	649	4.0	4.5	Shopping
4	282935706	Bible	92774400	0.00	985920	5320	4.5	5.0	Reference
"""

#5.  Print the summary (info) of the data.

data.info()

"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 7197 entries, 0 to 7196
Data columns (total 9 columns):
id                  7197 non-null int64
track_name          7197 non-null object
size_bytes          7197 non-null int64
price               7197 non-null float64
rating_count_tot    7197 non-null int64
rating_count_ver    7197 non-null int64
user_rating         7197 non-null float64
user_rating_ver     7197 non-null float64
prime_genre         7197 non-null object
dtypes: float64(3), int64(4), object(2)
memory usage: 506.1+ KB
"""

#6 Print the number of columns in the data.

data.shape

"""
(7197, 9)
9
"""

#7. Print all column names.

data.columns

"""
Index(['id', 'track_name', 'size_bytes', 'price', 'rating_count_tot',
       'rating_count_ver', 'user_rating', 'user_rating_ver', 'prime_genre'],
      dtype='object')
"""

# Q1: How many apps are there in the data source?

#8. Print the # of observations of the data.

data['id'].count()

"""
7197
"""

# Q2: What is the average rating of all apps?

#9. First, read the `user_rating` column into a varialbe named `user_rating`. Define 'user rating'

user_rating = data['user_rating']

#10. Now you can calculate the average of the `user_rating` data.

print(user_rating.mean())

"""
3.526955675976101
"""

# Q3: How many apps have an average rating no less than 4?

#11. First, filter `user_rating` where its value >= 4. Assign the filtered dataframe to a new variable called `user_rating_high`.

user_rating_high = data[data['user_rating'] >=4]

#12. Now obtain the length of `user_rating_high`.

len(user_rating_high)

"""
4781
"""

# Of course you don't have to define `user_rating_high` because you only use it once.
# You can directly print the length of the filtered dataframe if you want.

"""
len(data[data['user_rating']>=4])
"""

"""
Revision con Marc
(data.user_rating >= 4).sum()
"""

# Q4: How many genres are there in total for all the apps?

#12. Define a new varialbe named `genres` that contains the `prime_genre` column of `data`.

genres = data['prime_genre']

#13. Google for how to obtain unique values of a dataframe column. 
# Print the length of the unique values of `genres`. 

len(genres.unique())

"""
23
"""

# Q5: What are the top 3 genres that have the most number of apps?

"""
14. What you want to do is to count the number of occurrences of each unique genre values.
 Because you already know how to obtain the unique genre values, you can of course count the # of apps of each genre one by one.
 However, Pandas has a convient function to let you count all values of a dataframe column with a single command.
 Google for "pandas count values" to find the solution. Your code should return the following:
"""
genres.value_counts().head(3)

"""
Games            3862
Entertainment     535
Education         453
Name: prime_genre, dtype: int64
"""

# Q6. Which genre is most likely to contain free apps?

"""
15. First, filter `data` where the price is 0.00. Assign the filtered data to a new variable called `free_apps`.
 Then count the values in `free_apps`. 
 """

free = data[data['price'] == 0.00]
free_apps = free['prime_genre'].value_counts().sort_index()

"""
Book                   66
Business               20
Catalogs                9
Education             132
Entertainment         334
Finance                84
Food & Drink           43
Games                2257
Health & Fitness       76
Lifestyle              94
Medical                 8
Music                  67
Navigation             20
News                   58
Photo & Video         167
Productivity           62
Reference              20
Shopping              121
Social Networking     143
Sports                 79
Travel                 56
Utilities             109
Weather                31
Name: prime_genre, dtype: int64
"""

"""
16. Now you can calculate the proportion of the free apps in each genre based on the 
 value counts you obtained in the previous two steps. Challenge yourself by achieving 
 that with one line of code. 
"""

total_apps = data['prime_genre'].value_counts().sort_index()

"""
Book                  112
Business               57
Catalogs               10
Education             453
Entertainment         535
Finance               104
Food & Drink           63
Games                3862
Health & Fitness      180
Lifestyle             144
Medical                23
Music                 138
Navigation             46
News                   75
Photo & Video         349
Productivity          178
Reference              64
Shopping              122
Social Networking     167
Sports                114
Travel                 81
Utilities             248
Weather                72
Name: prime_genre, dtype: int64
"""

proportion = (free_apps/total_apps).sort_index()

"""
Book                 0.589286
Business             0.350877
Catalogs             0.900000
Education            0.291391
Entertainment        0.624299
Finance              0.807692
Food & Drink         0.682540
Games                0.584412
Health & Fitness     0.422222
Lifestyle            0.652778
Medical              0.347826
Music                0.485507
Navigation           0.434783
News                 0.773333
Photo & Video        0.478510
Productivity         0.348315
Reference            0.312500
Shopping             0.991803
Social Networking    0.856287
Sports               0.692982
Travel               0.691358
Utilities            0.439516
Weather              0.430556
Name: prime_genre, dtype: float64
"""

"""
Q7. If a developer tries to make money by developing and selling Apple Store apps, 
 in which genre should s/he develop the apps? Please assume all apps cost the same 
 amount of time and expense to develop.
"""
genre_price = data[['prime_genre', 'price']]
average_price = genre_price.groupby(['prime_genre']).mean()
average_price.sort_values(['price'], ascending=False)

"""
	price
prime_genre	
Medical	8.776087
Business	5.116316
Reference	4.836875
Music	4.835435
Productivity	4.330562
Navigation	4.124783
Education	4.028234
Health & Fitness	1.916444
Book	1.790536
Utilities	1.647621
Weather	1.605417
Food & Drink	1.552381
Photo & Video	1.473295
Games	1.432923
Travel	1.120370
Sports	0.953070
Entertainment	0.889701
Lifestyle	0.885417
Catalogs	0.799000
News	0.517733
Finance	0.421154
Social Networking	0.339880
Shopping	0.016311
"""

# Bonus question: What is the proportion of apps that don't have an English `track_name`?

"""
Tip: You can install `langdetect` (https://pypi.org/project/langdetect/) with `pip`, 
 then use `langdetect.detect()` to detect the language of a string. Also, you may need to 
 decode the string with `utf8` if the string is not based on the ASCII encoding. Otherwise 
 `langdetect.detect()` may throw errors.
"""
