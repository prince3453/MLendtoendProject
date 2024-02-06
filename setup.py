from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    This function will read the requirements.txt file and return the list of requirements
    '''
    requirements=[]

    with open(file_path) as fileobj:
        requirements=fileobj.readlines()
        requirements = [req.replace('\n',"") for req in requirements]
    return requirements


setup(
    name='MLENDTOENDPROJECT',
    version='0.0.1',
    author='Prince',
    author_email='princeghoghari3453@gmail.com',
    packages= find_packages(),
    install_requires=get_requirements('requirements.txt')
)