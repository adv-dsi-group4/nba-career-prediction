#A module to read raw data from source for further analysis.
#Data are stored in the raw_data folder for the original dataset and processed_data for the cleaned dataset.

from enum import Enum
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from imblearn.over_sampling import SMOTE

class NBARawData(Enum):
    '''List of members to identify the name of each dataset stored in the raw_data folder.
       One enumerator member represents one file in the folder.
    '''
    TRAIN = 0
    TEST = 1

class DataReader:
    def __init__(self, relative_path = "../"):
    

        self.filepath = {}
        #raw data
        self.filepath.update({NBARawData.TRAIN : relative_path + "data/raw/train.csv"})
        self.filepath.update({NBARawData.TEST : relative_path + "data/raw/test.csv"})

   
    def read_data(self, source, relative_path = "../"):
        '''Read the CSV file and load it into a data frame.
        
           Argument:
               source (enum): the member name of the dataset that will be loaded, e.g., NBARawData.TRAIN 
           
           Return:
               a data frame that store the dataset
        '''
        if (not isinstance(source,NBARawData)):
            raise Exception("argument should be filled with SuicideRawData or SuicideProcessedData. "
                            "Try SuicideRawData.AGE_STANDARDIZED and/or SuicideProcessedData.FACILITIES")
            
        #read the data and load them into a dataframe
        data = pd.read_csv(self.filepath[source])
        #for consistency purposes, change the case of the column names into a lower case and remove extra spaces
        data = data.rename(columns = lambda x: x.strip(" "))
        return(data)

    def split_data(self, data, relative_path = "../"):
        data = pd.DataFrame(data)
        target = data.pop('TARGET_5Yrs')
        X_train, X_val, y_train, y_val = train_test_split(data, target, test_size = 0.2, random_state=8, shuffle=True )

        # Save the splited data
        np.save(relative_path+ "data/processed/X_train", X_train)
        np.save(relative_path+ "data/processed/X_train", X_val)

        np.save(relative_path+ "data/processed/X_train", y_train)
        np.save(relative_path+ "data/processed/X_train", y_val)
        return(X_train, X_val, y_train, y_val)

    def select_feature_by_correlation(self, data):
        '''This function select the features according to the correlation result.
            The features which have correlation > 0.9 are filter out.
        '''
        
        data.drop(["Id", "Id_old"], axis=1, inplace=True )
        corr = data.corr()
        sns.heatmap(corr)

        columns = np.full((corr.shape[0],), True, dtype=bool)
        for i in range(corr.shape[0]):
            for j in range(i+1, corr.shape[0]):
                if corr.iloc[i,j] >= 0.9:
                    if columns[j]:
                        columns[j] = False
        selected_columns = data.columns[columns]
        return selected_columns

    
    def scale_features_by_standard_scaler(self, df):
        '''
        '''
    

        scaler = StandardScaler()
        train_df_scaled = scaler.fit_transform(df)
        
        train_df_scaled = pd.DataFrame(train_df_scaled)
        train_df_scaled.columns = df.columns
        return train_df_scaled
    
    def polynomialize_data(self, df, degree):
        '''
        '''
        # Polynomialise
        poly = PolynomialFeatures(degree)
        data_poly = poly.fit_transform(df)
        
#         data_poly = pd.DataFrame(data_poly)
#         data_poly.columns = df.columns
        return data_poly
        
        return(data_poly)
    
    def plot_class_balance(self, df):
        '''
        '''
        
        pl = pd.DataFrame(df)
        pl.columns = ['Target']
        pl.Target.value_counts().plot(kind="bar", title="Count Target")
        
    def resample_data_upsample_smote(self, X, y):
        '''
        '''
        
        sm = SMOTE(random_state = 23, sampling_strategy = 1.0)
        X_res, y_res = sm.fit_sample(X, y.ravel())
        return( X_res, y_res)
        