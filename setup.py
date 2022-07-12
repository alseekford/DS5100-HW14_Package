from setuptools import setup

setup(
    name='DS5100-HW14_Package',
    version='1.0',
    author='Anne Louise Seekford',
    author_email='bng3be@virginia.edu',
    packages=['bookluver/booklover.py', 'bookluver/booklover_test.py'],
    url = 'https://github.com/alseekford/DS5100-HW14_Package',
    license='LICENSE.txt',
    description='Package created for UVA MSDS DS5100 Module 14 Homework.',
    long_description=open('README.md').read(),
    install_requires=[
       "pandas",
       "numpy",
       "matplotlib.pyplot", 
       "unittest"
   ],
)
