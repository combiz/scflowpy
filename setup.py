#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    "anndata",
    "rich",
    "pip",
    "bump2version",
    "wheel",
    "watchdog",
    "flake8",
    "tox",
    "coverage",
    "Sphinx",
    "sphinx_rtd_theme",
    "readthedocs-sphinx-search",
    "twine",
    "PyHamcrest",
    "pathlib",
    "pandas",
    "black",
    "isort",
    "flake8",
    "MarkupSafe"
]

test_requirements = [ ]

setup(
    author="Combiz Khozoie",
    author_email='c.khozoie@imperial.ac.uk',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    description="Python helper functions for scFlow",
    entry_points={
        'console_scripts': [
            'scflowpy=scflowpy.cli:main',
        ],
    },
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description_content_type='text/x-rst',
    long_description=readme,
    include_package_data=True,
    keywords='scflowpy',
    name='scflowpy',
    packages=find_packages(include=['scflowpy', 'scflowpy.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/combiz/scflowpy',
    setup_requires=['flake8'],
    version='0.7.4',
    zip_safe=False,
)
