"""
A library with functions that clean DataFrames from missing values, outliers and useless information. \n
This library was made for Data Cleaning and preparing data for Machine Learning.

"""

import numpy as np
import pandas as pd


def drop_data(data: pd.DataFrame, 
              axis: str = ['rows', 'cols'],
              threshold: int | float = None) -> pd.DataFrame:
    
    # documentation
    """ 
    Description
    -----------  
        Dropping data with a certain threshhold of null values (NaN)
    
    Parameters
    ----------
        data (DataFrame): data itself \n
        axis (str): dropping axis, rows or columns \n
        threshold (int | float): dropping limit
        
    Returns
    -------
        DataFrame: new Dataframe without dropped data
        
    """
    
    # setting default values for 'threshold'
    if threshold is None:
        if axis == 'rows':
            threshold = 3
            
        elif axis == 'cols':
            threshold = 0.7
        
        else:
            print("Invalid axis or no axis")
            return None
    
    # 'threshold' is always more than 0
    if threshold <= 0:
        print("Threshhold cannot be zero or negative")
        return None
    
    # the result 'dropped_data' depends on axis
    if axis == 'rows': 
        if type(threshold) != int:
            print("For dropping rows 'threshold' value must be 'int'")
            return None
        
        if threshold > data.shape[1]:
            print("Threshold cannot be more than number of columns")
            return None
        
        shape = data.shape[1]
        thresh = shape - threshold
        dropped_data = data.dropna(axis=0, thresh=thresh)
        
    elif axis == 'cols': 
        if type(threshold) != float:
            print("For dropping columns 'threshold' value must be 'float'")
            return None
        
        if threshold >= 1:
            print("Threshold cannot be equal to 1 or more")
            return None
        
        shape = data.shape[0]
        thresh = shape * threshold
        dropped_data = data.dropna(axis=1, thresh=thresh)
        
    else:
        print("Invalid axis or no axis")
        return None
    
    # returning the result
    return dropped_data


def outliers_iqr(data: pd.DataFrame, 
                 feature: str, 
                 left: float = 1.5, 
                 right: float = 1.5, 
                 what: str = ['outliers', 'cleaned']) -> pd.DataFrame:
    
    # documentation
    """ 
    Description
    -----------  
        Finds outliers and cleans data from it with IQR method.
    
    Parameters
    ----------
        data (DataFrame): data itself \n
        feature (str): column of data \n
        left (float): value for lower bound of cleaning \n
        right (float): value for upper bound of cleaning \n
        what (str): what you need to return, outliers or cleaned
        
    Returns
    -------
        DataFrame: data with outliers only or already cleaned data
        
    """
    
    # selecting a feature 
    if feature not in data.columns:
        print("No such feature in data's columns")
        return None
    
    x = data[feature]
    
    # setting IQR
    quartile_1, quartile_3 = x.quantile(0.25), x.quantile(0.75)
    
    iqr = quartile_3 - quartile_1
    
    # setting bounds 
    if (left <= 0) or (right <= 0):
        print("Bounds cannot be zero or negative")
        return None
    
    lower_bound = quartile_1 - (iqr * left)
    upper_bound = quartile_3 + (iqr * right)
    
    # final result
    outliers = data[(x < lower_bound) | (x > upper_bound)]
    cleaned = data[(x > lower_bound) & (x < upper_bound)]
    
    if what == 'outliers':
        return outliers
    elif what == 'cleaned':
        return cleaned
    else:
        print("Invalid literal for 'what'")
        return None
    

def outliers_sigmas(data: pd.DataFrame, 
                    feature: str, 
                    left: int = 3,
                    right: int = 3,
                    log_scale: bool = False, 
                    what: str = ['outliers', 'cleaned']) -> pd.DataFrame:
    
    # documentation
    """ 
    Description
    -----------  
        Finds outliers and cleans data from it with Z-score method.
    
    Parameters
    ----------
        data (DataFrame): data itself \n
        feature (str): column of data \n
        left (float): value for lower bound of cleaning \n
        right (float): value for upper bound of cleaning \n
        log_scale (bool): logarithming the feature for more normal distribution \n
        what (str): what you need to return, outliers or cleaned
        
    Returns
    -------
        DataFrame: data with outliers only or already cleaned data
        
    """
    
    # checking a feature 
    if feature not in data.columns:
        print("No such feature in data's columns")
        return None
    
    # logarithming
    if log_scale:
        x = np.log(data[feature]+1)
    else:
        x = data[feature]
    
    # setting mu and sigma
    mu = x.mean()
    sigma = x.std()
    
    # setting bounds
    if (left <= 0) or (right <= 0):
        print("Bounds cannot be zero or negative")
        return None
    
    lower_bound = mu - (left * sigma)
    upper_bound = mu + (right * sigma)
    
    # final result
    outliers = data[(x < lower_bound) | (x > upper_bound)]
    cleaned = data[(x > lower_bound) & (x < upper_bound)]
    
    if what == 'outliers':
        return outliers
    elif what == 'cleaned':
        return cleaned
    else:
        print("Invalid literal for 'what'")
        return None


def drop_low_information(data: pd.DataFrame, limit: float = 0.95) -> pd.DataFrame:

    # documentation
    """ 
    Description
    -----------  
        Cleans data from low or uninformative features
    
    Parameters
    ----------
        data (DataFrame): data itself \n
        limit (float): threshhold of informativeness
        
    Returns
    -------
        DataFrame: new Dataframe without uninformative features
        
    """
    
    # cheching limit
    if (limit <= 0) or (limit >= 1):
        print("Invalid value for 'limit'")
        return None
    
    # selecting low information columns
    low_information_cols = [] 

    for col in data.columns:
        top_freq = data[col].value_counts(normalize=True).max()
        nunique_ratio = data[col].nunique() / data[col].count()
        
        if (top_freq > limit) or (nunique_ratio > limit):
            low_information_cols.append(col)
    
    # final result
    information_data = data.drop(low_information_cols, axis=1)
    
    return information_data 

