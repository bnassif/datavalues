#!/usr/bin/env python

from setuptools import setup

def read(filename):
    with open(filename, encoding='utf8', errors='ignore') as file:
        return file.read()

    
def get_version():
    # type: () -> str
    """Get the version string from the module's __init__ file."""
    with open("data/__init__.py") as init:
        for line in init.readlines():
            if '__version__' in line:
                return line.split('"')[1]

setup(
    name="datavalues",
    version=get_version(),
    description="Python package for handling data sizes",
    long_description=read("README.md"),
    author="Ben Nassif",
    author_email="bennassif@gmail.com",
    maintainer="Ben Nassif",
    maintainer_email="bennassif@gmail.com",
    url="https://github.com/Scraps23",
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Topic :: Software Development",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    license=read("LICENSE"),
    packages=['data'],
)
