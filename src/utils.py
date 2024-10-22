import sys
import os
from src.exception import CustomException
from src.logger import logging
import dill
import pickle


def save_object(file_path,obj):
    try:
        dir=os.path.dirname(file_path)
        os.makedirs(dir,exist_ok=True)
        with open(file_path,'wb') as file_obj:
            pickle.dump(obj,file_obj)
    except Exception as e:
        raise CustomException(e,sys)


