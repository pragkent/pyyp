#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
setup.py
~~~~~~~~

This module provides the setup script for pyyp.
"""

from setuptools import setup
from codecs import open

import pyyp

with open('README.rst', encoding='utf-8') as f:
    readme = f.read()

setup(
    name='pyyp',

    version=pyyp.__version__,

    description='Yunpian API wrapper.',
    long_description=readme,

    url='https://github.com/pragkent/pyyp',

    author='Kent Wang',
    author_email='pragkent@gmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    packages=['pyyp'],

    install_requires=['requests>=2.0.0'],

    package_data={'': ['LICENSE']},
    include_package_data=True,
)
