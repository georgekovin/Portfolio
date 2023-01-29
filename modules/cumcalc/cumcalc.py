"""
A function that calculates cumulative metrics from a DataFrame. Created especially for A/B testing in EDA.

"""

import pandas as pd


def get_cumseries(data: pd.DataFrame, 
                  cols: str | list, 
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
        if col not in data.columns:
            print("No such column in data")
            return None
        
        cum_col = 'cum_' + col
        
        # groupping 
        if groupby is not None: 
            if groupby not in data.columns:
                print("No such column in data")
                return None
            
            data[cum_col] = data.groupby([groupby])[col].cumsum()
        
        # final result
        data[cum_col] = data[col].cumsum()
    
    return data

