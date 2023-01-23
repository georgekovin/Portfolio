import pandas as pd 

from scipy.stats import (shapiro, 
                         normaltest, 
                         ttest_ind, 
                         f_oneway, 
                         pearsonr)

from statsmodels.stats import weightstats


def stattest(data: pd.DataFrame, 
             h_zero: str = None, 
             h_alt: str = None, 
             alpha: float = [0.01, 0.05, 0.1], 
             norm: str = ['shapiro', 'dagostino'], 
             corr: bool = False, 
             pvalue: bool = False):
    
    if norm == 'shapiro':
        p = shapiro(data)
        pv = round(p.pvalue, 3)
        
    if norm == 'dagostino':
        p = normaltest(data)
        pv = round(p.pvalue[0], 3)
        alpha = alpha / 2

    ppv = f'p={pv}'

    h_norm = 'Normal distribution'
    h_abnorm = 'Abnormal distribution'


    def result(df=data, 
               hz=h_zero, 
               ha=h_alt, 
               alp=alpha, 
               tst=None):
        
        if tst == 'pearson':
            res = pearsonr(x=df.iloc[:, 0], 
                           y=df.iloc[:, 1])
            
            t = "Pearson's correlation"
            
            print(f"Correlation is {res[0]}. Test is {t}")
            print('')
            
        else:
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
                    series.append(df[col])
                    
                res = f_oneway(*series)
                
                t = "ANOVA"

            p = res[1]
            
            if p > alp:
                print(f"{p} > {alp}. We cannot reject zero hypothesis - {hz}. Test is {t}")
            else:
                print(f"{p} <= {alp}. We reject zero hypothesis - {ha}. Test is {t}")
                
            print('')
    
    
    if pv > alpha:
        print(f'{ppv} > {alpha} \n{h_norm}')
        print('')
        
        for col in data.columns:
            if data[col].dtype == 'int' or data[col].dtype == 'float':
                continue
            else:
                print('Use non-parametric test') 
        
        if data.shape[1] == 2:
            if h_zero is None and h_alt is None:
                pass 
            
            if corr:
                result(tst='pearson')
                
            if pvalue:
                if h_zero is None or h_alt is None:
                    print('Missing hypothesises')
                    print('')
                else:
                    if data.shape[0] < 30:
                        result(tst='ttest')
                            
                    else:
                        result(tst='ztest')
                    
        elif data.shape[1] > 2 and not corr:
            result(tst='anova')
                
        else: 
            print('Number of groups must be >= 2')
            
            
    else:
        print(f'{ppv} <= {alpha} \n{h_abnorm}')
        print('') 
        
        
        
        
        
        
# -----------------------

#pizza = pd.read_csv('https://raw.githubusercontent.com/harika-bonthu/Hypothesis-test-examples/main/pizzas.csv')

#print('1')
#stattest(data=pizza, alpha=0.05, norm='shapiro')

#print('2')
#stattest(data=pizza, alpha=0.05, norm='shapiro', corr=True)

#print('3')
#stattest(data=pizza, h_zero='a', h_alt='b', alpha=0.05, norm='shapiro', pvalue=True)

#print('4')
#stattest(data=pizza, h_zero='a', h_alt='b', alpha=0.05, norm='shapiro', corr=True, pvalue=True)

#print('5')
#stattest(data=pizza, alpha=0.05, norm='shapiro', pvalue=True)