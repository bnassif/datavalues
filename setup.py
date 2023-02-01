#!/usr/bin/env python

from setuptools import setup
import re
import pypandoc

long_description = pypandoc.convert_file('README.md', 'rst')


def read(filename):
    with open(filename, encoding='utf8', errors='ignore') as file:
        return "\n" + file.read()


def get_version():
    # type: () -> str
    """Get the version string from the module's __init__ file."""
    with open("data/__init__.py") as init:
        version = re.search(r'[\'"]\S\d*.\d*.\d*\S*[\'"]', init.read())
        return version.group().strip('"').strip("'")


setup(
    name="datavalues",
    version=get_version(),
    description="Package for converting data units",
    long_description_content_type='text/x-rst',
    long_description=long_description,
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
