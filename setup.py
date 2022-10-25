#!/usr/bin/env python

from setuptools import setup

def read(filename):
    with open(filename, encoding='utf8', errors='ignore') as file:
        return file.read()

setup(
    name="datavalues",
    version=read('VERSION'),
    description="Python package for handling data sizes",
    long_description=read("README.md"),
    author="Ben Nassif",
    author_email="bennassif@gmail.com",
    maintainer="Ben Nassif",
    maintainer_email="bennassif@gmail.com",
    url="https://github.com/Scraps23",
    classifiers=(
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Topic :: Software Development",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ),
    license=read("LICENSE"),
    packages=['data'],
)
