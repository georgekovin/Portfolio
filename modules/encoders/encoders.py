import pandas as pd
import category_encoders as ce 


def data_encoder(data: pd.DataFrame, 
                 cols: list = None, 
                 encoder: str = ['ordinal', 
                                 'onehot', 
                                 'binary'], 
                 concat: bool = True) -> pd.DataFrame:
    
    """ 
    Description
    -----------  
        Helps in Feature Engeneering to encode features for ML.
    
    Parameters
    ----------
        data (DataFrame): Dataframe with features \n
        cols (list): columns of data that need to encode \n
        encoder (str): encoder's type, `ordinal`, `onehot`, `binary` \n
        concat (bool): concatenate or not to concatenate new features with `data`
    
    Returns
    -------
        DataFrame: new Dataframe with encoded features or just encoded features
        
    """
    
    
    if cols is None:
        cols = []
        for col in data.columns:
            cols.append(col)
    else:
        pass
    
    if encoder == 'ordinal':
        encoded = ce.OrdinalEncoder(cols=cols)
    elif encoder == 'onehot':
        encoded = ce.OneHotEncoder(cols=cols)
    elif encoder == 'binary':
        encoded = ce.BinaryEncoder(cols=cols)
    else:
        print("Encoder not found")
        return None

    
    type_bin = encoded.fit_transform(data[cols])
    
        
    if concat:
        data = pd.concat([data, type_bin], axis=1)
    else: 
        data = type_bin

    
    return data

