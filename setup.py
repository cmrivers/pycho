import os
from distutils.core import setup

setup(
    name = "pycho",
    version = "0.1",
    description = 'Python wrapper for Project Tycho',
    author = "Caitlin Rivers",
    author_email = "caitlin.rivers@gmail.com",
    url = 'http://github.com/cmrivers/pycho',
    #install_requires = ['Numpy >= 1.6.2',
    #                    'Matplotlib >=1.2.0',
    #                    'Networkx >=1.6.0',
    #                    'Pandas >= 0.12.0',
    #                    'Scipy >= 0.13'],
    license = "MIT",
    keywords = "epidemiology",
    packages = ['pycho'],
    include_package_data=True,
    scripts = ['pycho/pycho.py'],
    long_description='README.md',
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 2.7",
        "Natural Language :: English",
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Mathematics'],
)