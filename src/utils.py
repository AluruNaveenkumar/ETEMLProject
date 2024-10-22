import sys
import os
from src.exception import CustomException
from src.logger import logging
import dill
import pickle
from sklearn.metrics import r2_score


def save_object(file_path,obj):
    try:
        dir=os.path.dirname(file_path)
        os.makedirs(dir,exist_ok=True)
        with open(file_path,'wb') as file_obj:
            pickle.dump(obj,file_obj)
    except Exception as e:
        raise CustomException(e,sys)
    
def evaluate_models(X_train,y_train,X_test,y_test,models:dict):
    try:
        report={}
        for i in range(len(list(models))):
            model=list(models.values())[i]

            model.fit(X_train,y_train)
            logging.info("fit the model with train data")
            
            y_train_predict=model.predict(X_train)
            logging.info('model train data prediction')

            y_test_predict=model.predict(X_test)
            logging.info('model test data prediction')

            train_model_score = r2_score(y_pred=y_train_predict,y_true=y_train)
            test_model_score = r2_score(y_pred=y_test_predict,y_true=y_test)

            report[list(models.keys())[i]]=test_model_score

            logging.info('successfully returned the models along with R2 Scores')

            return report
        

    except Exception as e:
        raise CustomException(e,sys)