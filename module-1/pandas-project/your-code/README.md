# Pandas Project

## Select the Data Set

I selected the **Countries of the World** data set from [Kaggle Data Sets](https://www.kaggle.com/fernandol/countries-of-the-world).


## About Countries of the World

METER EXPLICACION DE QUE ES Y QUE QUIERO HACER CON ESTO


## Create Jupiter Notebook and Import Pandas Library

- I launched Jupiter Notebook through the terminal 
```
$ jupyter notebook
```

- I created a new Python3 notebook called 
**data-wrangling.ipynb**

- I imported the pandas library
```
import pandas as pd
```


## Import the Data Set using Pandas
I downloaded the data set in csv from Kaggle and saved it in the same folder as the jupyter notebook. 

I went to the jupyter notebook and executed the following actions:

- I defined a variable called 'data' with path to the csv file.
```
dataset = pd.read_csv('countries of the world.csv')
```

- I imported the csv file in 'dataset' and assigned it to the variable 'data'
```
data = pd.read_csv('countries of the world.csv')
```


## Examine the Data Set

- I used the following command to get a 'sneak peak' of the Data Set
```
data.head()
```

- I used the following commanda to get 
