import numpy as np
import pandas as pd


def data_correlator(data: pd.DataFrame, 
                    correlation: list = None,
                    thresh: float = None):
    
    data_corr = data.corr(method='pearson') 
    
    return data_corr