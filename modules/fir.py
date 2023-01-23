import pandas as pd


def pvaluetest(df: pd.Series, 
               val, 
               how: str = ['==', '>', '<', '>=', '<='],
               times = int, 
               statalpha: float = [0.01, 0.05, 0.10], 
               h_zero = str, 
               h_alt = str) -> None:
    
    
    """
    Description
    -----------
    Let's test the <h_zero> that 
    <df> has an equal chance of being <how> <val>, 
    compared to the <h_alt> that 
    the probability of having a <df[<df> <how> <val>]> is higher or lower.
    We will agree that 
    if the observed result has a probability of lower than <statalpha> according to the <h_zero>, 
    the <h_zero> is rejected.
    
    Arguments
    ---------
        df (pandas.Series|pandas.DataFrame): 
            data itelf
        val (int|float|str): 
            which variables we choose
        how (None|str): 
            equality or inequality sign, literally [==, >, <, >=, <=]
        times (int): 
            how many times we choose
        statalpha (float): 
            statistical significance, can be only [0.01, 0.05, 0.10]
        h_zero (str): 
            assumption of no correlation between variables 
        h_alt (str): 
            assumption that variables have correlation

    Returns
    -------
        None: 
            final probability and the only valid assumption
    """
    

    if type(val) == str:
        mask = df == val
        
    if type(val) == int or type(val) == float:
        if how == '>':
            mask = df > val  
        elif how == '<':
            mask = df < val
        elif how == '>=':
            mask = df >= val
        elif how == '<=':
            mask = df <= val
        else:
            mask = df == val 
    
    a = df[mask].shape[0]
    b = df.shape[0]
    
    p = round(a / b, 2)
    
    alphalist = [0.01, 0.05, 0.1]
    
    if statalpha not in alphalist:
        return 'incorrect number'
    
    if p ** times > statalpha:
        print(h_zero)
    if p ** times < statalpha:
        print(h_alt)
    
    return print(f'p = {p ** times}')

