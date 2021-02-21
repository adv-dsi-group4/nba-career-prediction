import pandas as pd
import numpy as np

def replace_outliers(data, columns):
    '''
        Quantile-based Flooring and Capping
    '''
    df = data.copy()
    for column in columns:
        
        
        ten_percentile = (df[column].quantile(0.10))
        ninety_percentile = (df[column].quantile(0.90))

        df[column] = np.where(df[column] <ten_percentile, ten_percentile,df[column])
        df[column] = np.where(df[column] >ninety_percentile, ninety_percentile,df[column])
                                    
    return df

def add_knn_feature(model, data, columns_to_drop):
    df = data.copy()
    df = df.drop(columns_to_drop, axis = 1)
    pred = model.predict(df)
    df['Knn'] = pred
    return df