import sys
import os
from src.exception import CustomException
from src.logger import logging
import dill
import pickle


def save(file,obj):
    try:
        dir=os.path.dirname(file)
        os.makedirs(dir,exist_ok=True)
        with open(file,'wb') as file_obj:
            pickle.dump(obj,file_obj)
    except Exception as e:
        raise CustomException(e,sys)


