#!/usr/bin/env python
# :WORKAROUND: http://bugs.python.org/issue15881#msg170215
import multiprocessing
from setuptools import setup

setup(
    name='mangopi',
    author='Jiawei Li',
    version='0.2.0',
    description='A manga API with a pluggable site architecture.',
    keywords='manga api',
    install_requires=['underscore.py==0.1.6'],
    test_suite='nose.collector',
    tests_require=['nose'],
    url='https://github.com/jiaweihli/mangopi/',
    author_email='jiawei.h.li@gmail.com',
    license='MIT',
    packages=['mangopi', 'mangopi.site']
)
