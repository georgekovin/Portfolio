# DATA CLEANER LIBRARY

## Description
A library with functions that clean DataFrames from missing values, outliers and useless information.
This library was made for Data Cleaning and preparing data for Machine Learning.

## Dataset
`data` : a DataFrame I made with missing values arranged diagonally.
\
`sber_data.csv` : DataFrame with information about real estate market in Moscow, made by SberBank, the largest bank in Russia. 

## Content
* `drop_data` : Dropping data with a certain threshhold of null values (NaN).
* `outliers_iqr` : Finds outliers and cleans data from it with IQR method.
* `outliers_sigmas` : Finds outliers and cleans data from it with Z-score method.
* `drop_low_information` : Cleans data from low or uninformative features.

## Instructions
* This library is written in `python 3.11` and requires `numpy` and `pandas` libraries, preferably last versions. So you need it installed in your IDE. 
* You need to have the `data_cleaner` file in a same directory with your current project, so you can import it with simple `from data_cleaner import <function>` or `import *` if you want to get all functions. 

## Conclusion
I've tested my library in Jupyter-notebook file `cleaner_test.ipynb`, and it has showed me it's efficiency. Try it in your Data Analysis and you will see that too.