#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = [ ]

setup(
    author="Combiz Khozoie",
    author_email='c.khozoie@imperial.ac.uk',
    python_requires='>=3.6',
    description="Python helper functions for scFlow",
    entry_points={
        'console_scripts': [
            'scflowpy=scflowpy.cli:main',
        ],
    },
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='scflowpy',
    name='scflowpy',
    packages=find_packages(include=['scflowpy', 'scflowpy.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/combiz/scflowpy',
    version='0.7.1',
    zip_safe=False,
)
