import pandas as pd


def get_cumseries(data: pd.DataFrame, 
                  cols: list, 
                  groupby: str = None) -> pd.DataFrame:
    
    """ 
    Description
    -----------  
        Calculating cumulative metrics for A/B test
    
    Parameters
    ----------
        data (DataFrame): Dataframe with metrics
        cols (list): columns of data that need to calculate
        groupby (str): what cols need to group by
    
    Returns
    -------
        DataFrame: new Dataframe with cumulative metrics
        
    """
    
    
    for col in cols:
        cum_ = 'cum_' + col
        
        if groupby is not None: 
            data[cum_] = data.groupby([groupby])[col].cumsum()
            
        data[cum_] = data[col].cumsum()
    
    return data

