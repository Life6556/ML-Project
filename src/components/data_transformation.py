from dataclasses import dataclass
import os,sys

import numpy as np 
from src.utils import save_object
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler

from src.exception import CustomException
from src.logger import logging



@dataclass
class DataTransformationConfig:
    processor_obj_file_path=os.path.join("artifacts","processor.pkl")

class DataTransformation:
    def __init__(self):
        self.dataTransformationConfig=DataTransformationConfig()
    def getDataTransformationObj(self):
        '''
        this function responsible for data tranformation
        '''
        try:
            numerical_columns = ["writing_score", "reading_score"]
            categorical_columns = [
                            "gender",
                            "race_ethnicity",
                            "parental_level_of_education",
                            "lunch",
                            "test_preparation_course",
                        ]
        except Exception as e:
            logging.exception("an error occured")
            raise CustomException(e,sys)
        try:
            num_pipeline=Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy='median')),
                    ("Scaler",StandardScaler())
                ]
            )
            cat_pipeline=Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy='most_frequent')),
                    ("encoder",OneHotEncoder()),
                    ("scaler",StandardScaler(with_mean=False))
                ]
            )
            
            preprocessor=ColumnTransformer(
                [
                    ("num_pipeline",num_pipeline,numerical_columns),
                    ("cat_pipeline",cat_pipeline,categorical_columns)
                ]
            )
            logging.info("data transformation object created")
            return preprocessor
        
        except Exception as e:
            raise CustomException(e,sys)

    def initiateDataTranformation(self,train_path,test_path):
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)
            logging.info("read dataframe completed")

            X_train=train_df.drop("math_score",axis=1)
            y_train=train_df["math_score"]

            X_test=test_df.drop("math_score",axis=1)
            y_test=test_df["math_score"]
            logging.info("train test split completed")


            preprocessor_obj=self.getDataTransformationObj()
            X_train_scaled=preprocessor_obj.fit_transform(X_train)
            X_test_scaled=preprocessor_obj.transform(X_test)
            logging.info("applied preprocessor obj on train test dataframes")

            train_arr=np.c_[X_train_scaled,y_train]
            test_arr=np.c_[X_test_scaled,y_test]
            save_object(
                file_path=self.dataTransformationConfig.processor_obj_file_path,
                obj=preprocessor_obj
            )
            logging.info("preprocessor object saved")

            return (train_arr,test_arr)
        except  Exception as e:
            logging.exception("an error occured")
            raise CustomException(e,sys)
st=DataTransformation()

train_arr,test_arr=st.initiateDataTranformation(r'artifacts\train.csv',r'artifacts\test.csv')
logging.info("train_arr and test_arr returned successuflly")
