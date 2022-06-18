from setuptools import find_packages, setup
from typing import List




#Declaring variable fro setup function
PROJECT_NAME = "housing-predictor"
VERSION = '0.0.3'
AUTHER = "Elango"
DESCRIPTION = "This is my first ineuron machine learning project"
PACKAGES = ["housing"]
REQUIREMENTS_FILE_NAME = "requirements.txt"


def get_requirements_list()->List[str]:
    """
    Description: THis function going to return list of requirement mention in the requirements.txt file
    
    return This function is going to return a list which contain  name of library mention in the requirements.txt
    """
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        return requirement_file.readline().remove("-e.")

setup(
name = PROJECT_NAME,
version= VERSION,
auther = AUTHER,
DESCRIPTION =  DESCRIPTION,
packages = find_packages(),
install_requires = get_requirements_list()
)

if __name__ == "__main__":
    print(get_requirements_list())