from typing import List
from setuptools import find_packages,setup

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    This function returns list of libraries requires for this projects
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n'," ") for req in requirements]

        if HYPEN_E_DOT:
            requirements.remove(HYPEN_E_DOT)



setup(name="End-To-End ML Project",
      version='0.0.1',
      author="Naveen Kumar",
      package=find_packages(),
      install_requires=get_requirements("requirements.txt")
      )