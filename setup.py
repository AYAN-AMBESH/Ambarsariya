from setuptools import setup
from setuptools import find_packages

with open('requirements.txt') as f:
    requirements = f.readlines()

setup(
    name='ambarsariya',
    version='1.1',
    author='ayan ambesh',
    url='https://github.com/AYAN-AMBESH/Ambarsariya',
    author_email='ambesh12k@gmai.com',
    description='steganography tool',
    license='MIT',
    install_requires = requirements,
    packages=find_packages(),
    entry_point={
        'console_scripts': [
            'ambarsariya-cli = src.main:main'
        ]
    }
)