"""
A library with functions that clean DataFrames from missing values, outliers and useless information. \n
This library was made for Exploratory Data Analysis or preparing data for Machine Learning.

"""


import pandas as pd
from scipy.stats import (shapiro, norm, t)
from statsmodels.stats.proportion import proportions_ztest 
import warnings

warnings.filterwarnings("ignore")



### --- DATA DIVIDER ---

def data_divider(data: pd.DataFrame, divider: str):
    
    # documentation
    """
    Description
    -----------
        Dividing data by any categorical feature.
    
    Parameters
    ----------
        data (DataFrame): a data that need to be divided \n
        divider (str): a categorical feature, that divides the data
        
    Returns
    -------
        tuple: a tuple with new divided datas
    
    """
    
    # making a divider feature
    div_series = data[divider].sort_values()
    
    # datatype checking
    if div_series.dtype != 'category':
        div_series = div_series.astype('category')
    
    # picking categories from a divider
    div_set = set(div_series)
    data_list = []
    
    # dividing data by divider feature
    for div in div_set:
        cat_data = data[div_series == div]
        data_list.append(cat_data)

    # returning tuple with new datas
    return tuple(data_list)



### --- DATA INTERSECT CLEANER ---

def data_intersect_cleaner(data_1: pd.DataFrame, 
                           data_2: pd.DataFrame,
                           intersect: str):
    
    # documentation
    """
    Description 
    -----------
        Finds intersections of two datas by one feature, and cleans the whole one data from them
    
    Parameters
    ----------
        data_1 (DataFrame): first data \n
        data_2 (DataFrame): second data \n
        intersect (str): a feature of both datas, where may be intersections
        
    Returns
    -------
        DataFrame: new data cleaned from intersections
    
    """
    
    # creating sets with unique values of intersected columns
    set_1 = set(data_1[intersect])
    set_2 = set(data_2[intersect])
    sets_insec = set_1.intersection(set_2)
    
    # concatenation of two datas in one
    data = pd.concat([data_1, data_2], axis=0)
    
    # returning concatenated data if there was no intersections, and cleaned data if was
    cleaned_data = data[data[intersect].apply(lambda x: x not in sets_insec)]
    
    return cleaned_data
    


### --- PIVOT AND CONVERSION ---

def pivot_and_conversion(data: pd.DataFrame, 
                         groupby: str|list, 
                         count: str, 
                         converted: str, 
                         rename: list = None) -> pd.DataFrame:
    
    # documentation
    """
    Description 
    -----------
        Makes pivot data with numbers of successful cases and whole sample, and calculates conversion from it
    
    Parameters
    ----------
        data (DataFrame): a data for pivot \n
        groupby (str | list): columns for groupping \n
        count (str): column for calculating the whole sample number \n
        converted (str): column for calculating the number of successful cases \n
        rename (list): list of two strings to rename 'count' and 'converted' columns
        
    Returns
    -------
        DataFrame: pivot data with conversion
    
    """
    
    # groupping data and arrgegating features
    foragg = {count: 'count', converted: 'sum'}
    groupped = data.groupby(groupby).agg(foragg).reset_index()
    
    # calculating conversion
    groupped['conversion'] = groupped[converted] / groupped[count] * 100
    
    # renaming aggregated columns
    if rename is not None:
        if len(rename) != 2 or type(rename) != list:
            print("In 'rename' list must be 2 names: first is for 'count', second is for 'converted'")
            return None
        
        names = {count: rename[0], converted: rename[1]}
        renamed = groupped.rename(columns=names)
       
        return renamed
    
    return groupped



### --- GET CUMULATIVE SERIES ---

def cumulative_metrics(data: pd.DataFrame, 
                       cols: str|list, 
                       groupby: str = None) -> pd.DataFrame:
    
    # documentation
    """ 
    Description
    -----------  
        Calculating cumulative metrics for A/B test.
    
    Parameters
    ----------
        data (DataFrame): Dataframe with metrics \n
        cols (list): columns of data that need to calculate \n
        groupby (str): what cols need to group by
    
    Returns
    -------
        DataFrame: new Dataframe with cumulative metrics
        
    """
    
    # making list from string
    if type(cols) == str:
        cols = [cols]
    
    # creating cumulative metrics
    for col in cols:
        cum_col = 'cum_' + col
        
        # groupping 
        if groupby is not None: 
            data[cum_col] = data.groupby([groupby])[col].cumsum()
        
        # final result
        data[cum_col] = data[col].cumsum()
    
    return data



### --- DECISION ABOUT HYPOTHESISES ---

def hypothesis_decision(pvalue: float, 
                        alpha: float, 
                        h0: str, 
                        h1: str):
    
    # documentation
    """
    Description 
    -----------
        Printing the decision about hypothesises
    
    Parameters
    ----------
        pvalue (float): result of any statistical test \n
        alpha (float): level of statistical significance, can be 0.01, 0.05 or 0.1 \n
        h0 (str): null hypothesis \n
        h1: (str): alternative hypothesis
        
    Returns
    -------
        None
    
    """
    
    # the decision itself
    if pvalue > alpha:
        print(f"{pvalue} > {alpha} \n"
              f"We accept null hypothesis. {h0}.")
    else:
        print(f"{pvalue} <= {alpha} \n"
              f"We reject null hypothesis. {h1}.")
        


# --- ADVANCED Z-PROPORTIONS TEST ---

def z_proportions_advanced(data: pd.DataFrame, 
                           togroup: str, 
                           toagg: str,
                           alternative: str = ['two-sided', 
                                               'smaller', 
                                               'larger']) -> float:
    
    # documentation
    """
    Description 
    -----------
        The advanced Z-proportions statistical test, that makes all the work for you
    
    Parameters
    ----------
        data (DataFrame): a data for testing \n
        togroup (str): column for groupping \n
        toagg (str): column for aggregating, 'sum' and 'count' \n
        alternative: alternative hypothesis, can be 'two-sided', 'smaller' or 'larger'
        
    Returns
    -------
        float: p-value, the result of testing
    
    """
    
    # pivot data for test
    piv_data = data.groupby(togroup)[toagg].agg(['sum', 'count'])
    
    # test itself and p-value
    z_result = proportions_ztest(count=piv_data['sum'], 
                                 nobs=piv_data['count'], 
                                 alternative=alternative)
    pvalue = round(z_result[1], 2)
    
    return pvalue



### --- CONFIDENT INTERVAL ---

def conf_interval(data: pd.Series, 
                  gamma: float = 0.95, 
                  rnd: int = None):
    
    # documentation
    """
    Description 
    -----------
        Calculates confident interval for any metrics
    
    Parameters
    ----------
        data (Series): a data with metrics \n
        gamma (float): level of confidence \n
        rnd (int): rounding bounds to some numbers after comma
        
    Returns
    -------
        tuple: lower bound and upper bound of the confident interval
    
    """
    
    # data must be Series
    if type(data) == pd.DataFrame:
        print("The 'data' must be a single column, not a 2D table.")
        return None
    
    # gamma must be positive and less than 1
    if (gamma < 0) or (gamma >= 1):
        print("Level 'gamma' must be from 0 to 1")
        return None
    
    # main variables
    n = data.shape[0] 
    x_mean = data.mean() 
    x_std = data.std() 
    alpha = 1 - gamma 
    root = x_std / (n**0.5) 

    # choosing criticals, T or Z
    if n >= 30:
        z_crit = -(norm.ppf(alpha/2)) 
        eps = z_crit * root
    
    else:
        k = n - 1 
        t_crit = -(t.ppf(alpha/2, k))
        eps = t_crit * root
    
    # calculating bounds
    lower_bound = x_mean - eps 
    upper_bound = x_mean + eps 
    
    return round(lower_bound, rnd), round(upper_bound, rnd)
    


### --- CONFIDENT INTERVAL FOR PROPORTIONS ---

def proportions_conf_interval(data: pd.DataFrame, 
                              n: str, 
                              xp: str, 
                              gamma: float = 0.95, 
                              rnd: int = None):
    
    # documentation
    """
    Description 
    -----------
        Calculates confident interval for proportions
    
    Parameters
    ----------
        data (DataFrame): a data with metrics \n
        n (str): column to get size of the whole sample \n
        xp (str): column to get mean value of some metrics \n
        gamma (float): level of confidence \n
        rnd (int): rounding bounds to some numbers after comma
        
    Returns
    -------
        tuple: lower bound and upper bound of the confident interval for proportions
    
    """
    
    # main variables
    n_cnt = data[n].count()
    xp_mean = data[xp].mean() 
    alpha = 1 - gamma 
    root = (xp_mean * (1 - xp_mean) / n_cnt) ** 0.5
    
    # Z-critical and eps
    z_crit = -(norm.ppf(alpha/2)) 
    eps = z_crit * root
    
    # calculating bounds
    lower_bound = xp_mean - eps 
    upper_bound = xp_mean + eps 
    
    return round(lower_bound * 100, rnd), round(upper_bound * 100, rnd)



### --- CONFIDENT INTERVALS MESSAGE ---

def conf_message(interval: tuple, 
                 feature: str, 
                 group: str = None):
    
    # documentation
    """
    Description 
    -----------
        Prints message to show the confident interval for any feature
    
    Parameters
    ----------
        interval (tuple): the confident interval itself \n
        feature (str): column of dataset the confident interval was made for \n
        group (str): group which was in dataset, usually A or B
        
    Returns
    -------
        None
    
    """
    
    if group is None:
        print(f"Confident interval for '{feature}' is {interval}")
    else:
        print(f"Confident interval for '{feature}' of {group} group is {interval}")



### --- DIFFERENCE OF PROPORTIONAL CONFIDENT INTERVALS ---

def diff_prop_conf_interval(data_1: pd.DataFrame,
                            data_2: pd.DataFrame,
                            n: str,
                            xp: str, 
                            gamma: float = 0.95, 
                            rnd: int = None):
    
    # documentation
    """
    Description 
    -----------
        Calculates difference between two confident intervals for proportions
    
    Parameters
    ----------
        data_1 (DataFrame): first data with metrics \n
        data_2 (DataFrame): second data with metrics \n
        n (str): column to get size of the whole sample \n
        xp (str): column to get mean value of some metrics \n
        gamma (float): level of confidence \n
        rnd (int): rounding bounds to some numbers after comma
        
    Returns
    -------
        tuple: lower bound and upper bound of the difference of confident interval for proportions
    
    """
    
    n_1 = data_1[n].count()
    n_2 = data_2[n].count()
    
    xp_1 = data_1[xp].mean()
    xp_2 = data_2[xp].mean()
    
    root = ((xp_1 * (1 - xp_1) / n_1) + (xp_2 * (1 - xp_2) / n_2)) ** 0.5 
    
    alpha = 1 - gamma 
    z_crit = -(norm.ppf(alpha/2)) 
    eps = z_crit * root
    
    diff = xp_1 - xp_2
    lower_bound = diff - eps 
    upper_bound = diff + eps 
    
    return round(lower_bound * 100, rnd), round(upper_bound * 100, rnd)



### --- DECISION ABOUT DIFFERENCE OF CONFIDENT INTERVALS ---

def diff_decision(diff: tuple):
    
    # documentation
    """
    Description 
    -----------
        Prints the decision about difference of confident intervals
    
    Parameters
    ----------
        diff (tuple): the difference itself
        
    Returns
    -------
        None
    
    """
    
    print(f"Difference of confident intervals is: {diff}")
    
    a = diff[0]
    b = diff[1]
    
    if (a > 0) and (b > 0):
        print("Variant B is better than A.")
    elif (a < 0) and (b < 0):
        print("Variant A is better than B.")
    else:
        print("Both variants are equivalent.")
        


### --- MULTIPLE DECISION ABOUT HYPOTHESISES ---

def multiple_decision(pv_a: float, 
                      pv_b: float, 
                      alpha: float, 
                      h0: str, 
                      h1: str):
    
    # documentation
    """
    Description 
    -----------
        Printing the multiple decision about hypothesises
    
    Parameters
    ----------
        pv_a (float): first result of any statistical test \n
        pv_b (float): second result of any statistical test \n
        alpha (float): level of statistical significance, can be 0.01, 0.05 or 0.1 \n
        h0 (str): null hypothesis \n
        h1: (str): alternative hypothesis
        
    Returns
    -------
        None
    
    """
    
    # the decision itself
    if (pv_a > alpha) or (pv_b > alpha):
        print(f"We accept null hypothesis. {h0}.")
    else:
        print(f"We reject null hypothesis. {h1}.")