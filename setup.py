# Setup.py is responsible in creating the machine learning application as a package which can be installed in your projects to use
# We can then deploy our ML model on PyPI and anybody can install and use from there
# In a crux it is building our application as a package

from setuptools import find_packages, setup
# find_package: automatically finds out all the packages that are available in the entire ML application in the directory we have created
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:  # Takes a file path of string type and return a list of string
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","")for req in requirements] # or use req.strip()

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
name = 'mlproject',
version = '0.0.1',
author = 'Ridhi',
author_email = 'ridhi.kulshreshtha@gmail.com',
packages = find_packages(),
install_requires = get_requirements('requirements.txt')
)
# Metadata information about the entire projecct

'''If we want src (source) to be found as a package, we will create a init file 
When find_packages runs it will go to see how many folders have __init__.py. 
So it directly considers the source as a package itself.
We can import the package anywhere we want like seaborn, numpy, etc. 
But for that we need to put it in a PyPI package.

The entire project development will happen inside src folder so that it can later on be imported by anyone
'''

'''
We can either directly install setup.py 
OR
Whenever we try to install all the requirements at that time setup.py should also run to build packages
-e . automatically triggers setup.py
'''