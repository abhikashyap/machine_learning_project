from setuptools import setup,find_packages
from typing import List

REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirements_list()->List[str]:
  """
  Description: this will return list of requirement in requirements.txt  as a list
  """
  with open(REQUIREMENT_FILE_NAME) as requirements_file:
    return requirements_file.readlines()


setup(
  name="housing-predictor",
  version="0.0.6",
  author="abhishek",
  description="this is first ml project",
  packages=find_packages(),
  install_requires=get_requirements_list()
)

 