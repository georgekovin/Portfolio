import pandas as pd 

from scipy.stats import (shapiro, 
                         normaltest, 
                         ttest_ind, 
                         f_oneway, 
                         pearsonr, 
                         spearmanr)

from statsmodels.stats import weightstats


def stattest(data: pd.DataFrame, 
             h_zero: str = None, 
             h_alt: str = None, 
             alpha: float = [0.01, 0.05, 0.1], 
             norm: str = ['shapiro', 'dagostino'], 
             corr: bool = False, 
             pvalue: bool = False):
    
    
    # Normality test
    if norm == 'shapiro':
        p = shapiro(data)
        pv = round(p.pvalue, 3)
        
    if norm == 'dagostino':
        p = normaltest(data)
        pv = round(p.pvalue[0], 3)
        alpha /= 2

    ppv = f'p={pv}'

    h_norm = 'Normal distribution'
    h_abnorm = 'Abnormal distribution'


    # Correlation test
    def corrtest(df=data, 
                 tst=None): 
        
        if tst == 'pearson':
            res = pearsonr(x=df.iloc[:, 0], 
                           y=df.iloc[:, 1])
            
            t = "Pearson's correlation"
            
        if tst == 'spearman':
            res = spearmanr(a=df.iloc[:, 0], 
                            b=df.iloc[:, 1])
            
            t = "Spearman's correlation"
            
        corr_res = round(res[0], 2)
        
        print(f'Correlation is {corr_res}. \n'
              f'Test is {t} \n'
              '')
    
    
    # P-value test
    def pvaltest(df=data, 
                 hz=h_zero, 
                 ha=h_alt, 
                 alp=alpha, 
                 tst=None):

        if tst == 'ttest':
            res = ttest_ind(a=df.iloc[:, 0], 
                            b=df.iloc[:, 1], 
                            equal_var=True)
            
            t = "Independent T-test"
                
        if tst == 'ztest':
            res = weightstats.ztest(x1=df.iloc[:, 0], 
                                    x2=df.iloc[:, 1], 
                                    value=0, 
                                    alternative='two-sided')
                
            t = "Z-test"
            
        if tst == 'anova':
            series = []

            for col in df.columns:
                sd = df[col]
                series.append(sd)

            res = f_oneway(*series)

            t = "ANOVA"

        p = round(res[1], 2)
            
        if p > alp:
            print(f'{p} > {alp}. \n'
                  f'We cannot reject zero hypothesis - {hz}.')
        else:
            print(f'{p} <= {alp}. \n'
                  f'We reject zero hypothesis - {ha}.')
                
        print(f'Test is {t} \n'
              '')

    
    # Data type test
    for col in data.columns:
        if data[col].dtype == 'int' or data[col].dtype == 'float':
            datatype = 'N'
            
        if data[col].dtype == 'category':
            datatype = 'C'
    
    
    # Main test
    if pv > alpha:
        print(f'{ppv} > {alpha} \n{h_norm}'
              '\n')
        
        if datatype == 'N':
            if data.shape[1] == 2:
                if h_zero is None and h_alt is None:
                    pass 
                
                if corr:
                    corrtest(tst='pearson')
                
                if pvalue:
                    if h_zero is None or h_alt is None:
                        print('Missing hypothesises')
                        print('')
                    else:
                        if data.shape[0] < 30:
                            pvaltest(tst='ttest')
                        else:
                            pvaltest(tst='ztest')
            
            if data.shape[1] > 2:
                pvaltest(tst='anova')
        
        if datatype == 'C':
            pass
        
        
        
    else:
        print(f'{ppv} <= {alpha} \n{h_abnorm}')
        print('') 
                
        if h_zero is None and h_alt is None:
            pass 
            
        if corr:
            corrtest(tst='spearman')
        