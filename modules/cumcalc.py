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
        
        
        

# ---------

#df = pd.read_csv('data/ab_data.zip')

#daily_data = df.groupby(['timestamp','group']).agg({
#    'user_id':'count',
#    'converted':'sum'
#}).reset_index().rename(columns={'user_id': 'users_count'})

#daily_data['conversion'] = daily_data['converted'] / daily_data['users_count'] * 100


#get_cumseries(data=daily_data, cols=['users_count', 'converted'])

#get_cumseries(data=daily_data, cols=['users_count', 'converted'], groupby='group')

#get_cumseries(data=daily_data, cols=['users_count', 'converted', 'conversion'])

#get_cumseries(data=daily_data, cols=['users_count', 'converted', 'conversion'], groupby='group')