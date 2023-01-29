# CUMULATIVE METRICS CALCULATOR

## Description
A function that calculates cumulative metrics from a DataFrame. Created especially for A/B testing in EDA.

## Dataset
`ab_data`: a data with conversion from unknown site. Users are divided in two groups, A and B. Every row fixes user's ID and conversion at certain timestamp. 

## Instructions
* This function was written in `python 3.11` and using `pandas 1.5.3`. So it requires that stuff.
* You just need to have file `cumcalc.py` in the same folder with your project. So you can use it with `from cumcalc import get_cumseries`.

## Conclusion
You can get cumulative metrics easily and effectively. The evidence you will see in `cumcalc_test.ipynb` notebook. Just try it!