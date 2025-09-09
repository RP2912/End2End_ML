from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    "this functions will return a list of req"
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]



setup (
name='END2END_ML'
version='0.0.1',
author='Rinkey',
author_email='rinkeypal2419@gmail.com',
pacakages=find_packages(),
install_requires=get_requirements('requirement.txt')
)