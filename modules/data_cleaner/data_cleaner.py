import numpy as np
import pandas as pd


def drop_data(data: pd.DataFrame, 
              axis: int = [0, 1],
              threshold: int | float = None) -> pd.DataFrame:
    
    """ 
    Description
    -----------  
        Dropping data with a certain threshhold of null values (NaN)
    
    Parameters
    ----------
        data (DataFrame): data itself \n
        axis (int): dropping axis: 0 is columns, 1 is rows \n
        threshold (int | float): dropping limit
        
    Returns
    -------
        DataFrame: new Dataframe without dropped data
        
    """
    
    if threshold is None:
        print("Enter the 'threshold' value")
        
        if axis == 0:
            print("'axis = 0', hence it must be 'int'")
        elif axis == 1:
            print("'axis = 1', hence it must be 'float'")
        else:
            print("Invalid value for axis or no axis")
        
        return None
    
    if axis == 0: # drop rows
        if type(threshold) != int:
            print("For dropping rows 'threshold' value must be 'int'")
            return None
        
        else:
            shape = data.shape[1]
            thresh = shape - threshold
            dropped = data.dropna(axis=axis, thresh=thresh)
        
    elif axis == 1: # drop cols
        if type(threshold) != float:
            print("For dropping columns 'threshold' value must be 'float'")
            return None
        
        else:
            shape = data.shape[0]
            thresh = shape * threshold
            dropped = data.dropna(axis=axis, thresh=thresh)
        
    else:
        print("Invalid value for axis or no axis")
        return None
    
    return dropped



def outliers_iqr(data: pd.DataFrame, 
                 feature: str, 
                 left: float = 1.5, 
                 right: float = 1.5):
    
    """ 
    Description
    -----------  
        Finds outliers and cleans data from it with IQR method.
    
    Parameters
    ----------
        data (DataFrame): data itself \n
        feature (str): column of data \n
        left (float): value for lower bound of cleaning \n
        right (float): value for upper bound of cleaning
        
    Returns
    -------
        tuple: two Dataframes, first is outliers only and second is cleaned data
        
    """
    
    x = data[feature]
    
    quartile_1, quartile_3 = x.quantile(0.25), x.quantile(0.75)
    
    iqr = quartile_3 - quartile_1
    
    lower_bound = quartile_1 - (iqr * left)
    upper_bound = quartile_3 + (iqr * right)
    
    outliers = data[(x < lower_bound) | (x > upper_bound)]
    cleaned = data[(x > lower_bound) & (x < upper_bound)]
    
    return (outliers, cleaned)



def outliers_sigmas(data: pd.DataFrame, 
                    feature: str, 
                    left: int = 3,
                    right: int = 3,
                    log_scale: bool = False):
    
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
        log_scale (bool): logarithming the feature for more normal distribution
        
    Returns
    -------
        tuple: two Dataframes, first is outliers only and second is cleaned data
        
    """
    
    if log_scale:
        x = np.log(data[feature]+1)
    else:
        x = data[feature]
        
    mu = x.mean()
    sigma = x.std()
    
    lower_bound = mu - (left * sigma)
    upper_bound = mu + (right * sigma)
    
    outliers = data[(x < lower_bound) | (x > upper_bound)]
    cleaned = data[(x > lower_bound) & (x < upper_bound)]
    
    return (outliers, cleaned)



def drop_low_information(data: pd.DataFrame, limit: float = 0.95) -> pd.DataFrame:

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
    
    low_information_cols = [] 

    for col in data.columns:
        
        top_freq = data[col].value_counts(normalize=True).max()
        
        nunique_ratio = data[col].nunique() / data[col].count()
        
        if (top_freq > limit) or (nunique_ratio > limit):
            low_information_cols.append(col)
            
    information_data = data.drop(low_information_cols, axis=1)
    
    return information_data 