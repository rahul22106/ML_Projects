from setuptools import find_packages,setup
from typing import List

Hyphen_E_DOT = '-e .'
def get_requirements(file_path)->list[str]:
    ''' this function will return the list of requirements '''
    requirements =[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if Hyphen_E_DOT in requirements:
            requirements.remove(Hyphen_E_DOT)

    return requirements        
setup(
    name='ML_Projects',
    version='0.1.0',
    author='Rahul',
    author_email = "rahulkrmishra2004@gmail.com",
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt')
)