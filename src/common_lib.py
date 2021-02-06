#A module to read raw data from source for further analysis.
#Data are stored in the raw_data folder for the original dataset and processed_data for the cleaned dataset.

from enum import Enum
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

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

   
    def read_data(self, source, split = False, relative_path = "../"):
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
        data = data.rename(columns = lambda x: x.strip(" ").lower())

        if(split == True):
            target = data.pop('target_5yrs')
            X_train, X_val, y_train, y_val = train_test_split(data, target, test_size = 0.2, random_state=8 )

            # Save the splited data
            np.save(relative_path+ "data/raw/X_train", X_train)
            np.save(relative_path+ "data/raw/X_train", X_val)

            np.save(relative_path+ "data/raw/X_train", y_train)
            np.save(relative_path+ "data/raw/X_train", y_val)
            return(X_train, X_val, y_train, y_val)
        else:
            return(data)

    