import pandas as pd


def simple_decorator_with_args(times = int, 
                     statalpha: float = [0.01, 0.05, 0.10], 
                     h_zero = str, 
                     h_alt = str):
    
    def decorator(func):
        
        def decorated_function(*args, **kwargs) -> None:
        
            p = func(*args, **kwargs)
        
            alphalist = [0.01, 0.05, 0.1]
    
            if statalpha not in alphalist:
                return 'incorrect number'
        
            if p ** times > statalpha:
                print(h_zero)
            if p ** times < statalpha:
                print(h_alt)
        
            return print(f'p = {p ** times}')
    
        return decorated_function

    return decorator




sb = pd.read_csv('data/sber_data.csv')

#print(sb)

@simple_decorator_with_args()
def pvaluetest(df: pd.Series, 
            val, 
            how: str = ['==', '>', '<', '>=', '<=']) -> float:
    
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
    print(p)
        
    return p

pvaluetest(
           df=sb['full_sq'], 
           val=33, 
           how='>='
           )

simple_decorator_with_args(h_zero='a', 
           h_alt='b', 
           times=3, 
           statalpha=0.05)
