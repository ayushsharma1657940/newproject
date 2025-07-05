from typing import List
from setuptools import find_packages,setup

def get_requirements(file_path:str)->List[str]:
    reqirements = []
    with open(file_path) as file_obj:
        requirements= file_obj.readline()
        requirements=[req.replace("\n","")for req in requirements]
setup(
    
name='mlproject',
version='0.0.1',
author='Ayush',
author_email='ayubhai0123@gmail.com',
packages= find_packages(),
install_requires= get_requirements('requirements.txt'),
)