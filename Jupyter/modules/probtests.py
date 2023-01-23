import pandas as pd


def get_probability(df: pd.Series, 
                    val, 
                    how: str = ['==', '>', '<', '>=', '<=']) -> float:

    """
    Description
    -----------
    What is the probability that 
    random value of <df> will be <how> than <val>

    Arguments
    ---------
        df (pandas.Series): 
            Data itelf
        val (None): 
            Which variables we choose, can be int, float or str
        how (str): 
            Comparison sign, literally [==, >, <, >=, <=]
            
    Result
    ------
        p (float): 
            The very probability 
    """
    
    
    if how is None or type(val) == str:
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
    print(p)
    
    return p


def pvalue_test(df: pd.Series, 
                val = None, 
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
        df (pandas.Series): 
            Data itelf
        val (None): 
            Which variables we choose, can be int, float or str
        how (str): 
            Comparison sign, literally [==, >, <, >=, <=]
        times (int): 
            How many times we choose
        statalpha (float): 
            Statistical significance, can be only [0.01, 0.05, 0.10]
        h_zero (str): 
            Assumption of no correlation between variables 
        h_alt (str): 
            Assumption that variables have correlation

    Result
    ------
        h_zero | h_alt & p ** times (None): 
            Final probability and the only valid assumption
    """
    
    p = get_probability(df=df, 
                        val=val,
                        how=how)
    
    alphalist = [0.01, 0.05, 0.1]
        
    if statalpha not in alphalist:
        return 'Incorrect number'
    
    if type(p) != float:
        return p
    else:
        if p ** times > statalpha:
            print(h_zero)
        if p ** times < statalpha:
            print(h_alt)
        
    return print(f'p = {p ** times}')


def multiprob(args: list = None):
    
    if args is None:
        args = []
    
    #print(args)
    
    problist = []
    
    for arg in args:
        p = get_probability(df=arg[0], val=arg[1], how=arg[2])
        problist.append(p)
    
    return problist


#sb = pd.read_csv('probtests/sber_data.csv')

#print(sb)


#get_probability(df=sb['full_sq'], val=33, how='aaa')

#get_probability(df=sb['ecology'], val='good', how='bbb')

#pvalue_test(df=sb['full_sq'], val=33, how='>=', times=3, statalpha=0.05, h_zero='a', h_alt='b')


#multiprob(args=[[sb['full_sq'], 33, '>='], [sb['ecology'], 'good', '']])

