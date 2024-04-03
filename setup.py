from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'                                                     # this is added in requirement file and should not be read when installing packages
# this is an indication in requirements.txt file that setup file is also present and to use it.

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:                                   # open file
        requirements = file_obj.readlines()                             # read the lines of the file
        requirements = [req.replace("\n","") for req in requirements]   # using list comprehension we are going to replace \n with spaces 

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
name = 'deploy_models',
version = '0.0.1',
author = 'mahumt',
author_email = 'mahum.tofiq@outlook.com',
packages = find_packages(), # this function will look for src folder and in there __init__.py file
install_requires = get_requirements('requirements.txt')
)