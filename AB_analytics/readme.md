# AB-ANALYTICS LIBRARY

## Description
A library with functions for analysis of A/B-test results. This library was made for Exploratory Data Analysis and Machine Learning.

## Content
* `data_divider` : Dividing data by any categorical feature.
* `data_intersect_cleaner` : Finds intersections of two datas by one feature, and cleans the whole one data from them.
* `pivot_and_conversion` : Makes pivot data with numbers of successful cases and whole sample, and calculates conversion from it.
* `cumulative_metrics` : Calculating cumulative metrics for A/B test.
* `hypothesis_decision` : Printing the decision about hypothesises.
* `z_proportions_advanced` : The advanced Z-proportions statistical test, that makes all the work for you.
* `conf_interval` : Calculates confident interval for any metrics.
* `proportions_conf_interval` : Calculates confident interval for proportions. 
* `conf_message` : Prints message to show the confident interval for any feature.
* `diff_prop_conf_interval` : Calculates difference between two confident intervals for proportions.
* `diff_decision` : Prints the decision about difference of confident intervals.
* `multiple_decision` : Printing the multiple decision about hypothesises.

## Dataset
`ab_data_tourist.csv` : a DataFrame with information about sales in unknown touristic agency before and after homepage redesign on their website. 

## Instructions
* This library is written in `python 3.11` and requires `pandas 1.5.3` library. 
* You need to put the `ab_analytics.py` file in a folder with your progect and use it with `from ab_analytics import *`. 

## Conclusion
All tests you can see in `ab_test.ipynb` notebook. I hope this library will help you in Data Analysis!