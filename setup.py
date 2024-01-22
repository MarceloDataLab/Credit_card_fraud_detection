# setup.py
from setuptools import setup
from setuptools import find_packages

# list dependencies from file
with open('requirements.txt') as f:
    content = f.readlines()
requirements = [x.strip() for x in content]

setup(name='Credit_card_fraud_detection',
      description="Python package designed to detect fraudulent transactions in credit card data. Utilizing machine learning algorithms",
      packages=find_packages(),
      install_requires=requirements)
