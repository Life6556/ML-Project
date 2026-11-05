from setuptools import find_packages,setup
from typing import List

HYPEN_E_dot="-e ."
def get_requirments(file_path:str)->List[str]:
    '''
    this function will return the requirement.txt
    '''
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_dot in requirements:
            requirements.remove(HYPEN_E_dot)
    return requirements
setup(
    name='MLproject',
    version='0.0.1',
    author='Al Hafij',
    author_email='lifealhafij@gmail.com',
    packages=find_packages(),
    install_requires=get_requirments('requirements.txt')

)