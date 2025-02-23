#!/usr/bin/env python
from setuptools import setup, find_packages
#from distutils.core import setup

#import pychebfun


setup(
    name         = 'pychebfun',
    version      = '1.0.0', #pychebfun.__version__,
    maintainer = 'Olivier Verdier',
    maintainer_email = 'olivier.verdier@gmail.com',
    description  = 'Python Chebyshev Functions',
    author = 'Olivier Verdier',
    author_email = 'olivier.verdier@gmail.com',
    url = "https://github.com/pychebfun/pychebfun",
    license      = 'BSD',
    keywords = ['Math', 'Chebyshev', 'chebfun',],
    #packages=['pychebfun',],
    packages=find_packages(),
    install_requires=['typing_extensions','scipy','numpy','matplotlib'],
    
    classifiers = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Scientific/Engineering :: Mathematics',
    ],
    )
