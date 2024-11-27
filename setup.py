from setuptools import find_packages,setup
from typing import List
#just updates
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]
        return requirements

setup(
    name='Fault detection',
    version='0.0.1',
    author='Sanskriti',
    author_main='thatenigmatic003@gmail.com',
    install_requirements=get_requirements('requirements.txt'),
    packages=find_packages()

)