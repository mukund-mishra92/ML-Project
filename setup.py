from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(path:str)->List[str]:
    ''' 
    this function will returns the list of requirements
    '''
    requirements = []
    with open(path) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)
    return requirements



setup(
    name = "ml-project",
    version = "0.0.1",
    author = "Balmukund",
    author_email="balmukud.mishra92@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements("requirements.txt")

)