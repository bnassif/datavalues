# Data Values
[![Pypi](https://img.shields.io/pypi/v/datavalues)](https://pypi.org/project/datavalues)
[![MIT licensed](https://img.shields.io/badge/license-MIT-green.svg)](https://raw.githubusercontent.com/Scraps23/datavalues/main/LICENSE)
![GitHub Release Date](https://img.shields.io/github/release-date/Scraps23/datavalues)

Simple package for managing data units including conversions and operations

## Installation

```python
# PyPi Installation
pip install datavalues
# GitHub Installation
pip install git+'https://github.com/Scraps23/datavalues.git' 
```

## Getting Started

The package is a collection of sub-classed object classes for each data unit.
To import all the object classes, use the import below in your code:
```python
from data.units import *
```
This is the import method used for all examples below.
### Object Classes
There are nine 9 object classes, each named for the unit they represent.
- Byte
- KiloByte
- MegaByte
- GigaByte
- TeraByte
- PetaByte
- ExaByte
- YottaByte
- ZettaByte
## Usage
Each of the object classes sub-classes the BaseDataModel which allows for arithmetic and comparison operators, and a shared `convert` method.
### Conversion
The conversion method is non-destructive and relies upon the class name of the data object. Changing the names of the class(es) on import will break functionality.
```python
# Converting the object does not alter it, it returns a new object
as_mb = MegaByte(100)
as_gb = as_mb.convert('gb')
print(as_mb, as_gb)
## RETURNS:
100 MB 0.1 GB
```
```python
import os
# Conversion can be done in-line to reduce memory usage
as_gb = MegaByte(100).convert('gb')
# This is especially useful for bytes-based systems and human-readable input being merged
selected_size = GigaByte(float(input('How many gigabytes? : ')))
os.environ['disk_size_var'] = selected_size.convert('b')
```
### Operators
Data objects can have math applied against them, and be compared to each other and int/float objects to simplify operations like calculating total disk usage, RAID viability, and more.

#### Arithmetic Operators
The mathematical operators allow objects of different classes to interact; if another data object is supplied as the other value, both values are converted to bytes, evaluated, and converted back to the original unit.
Otherwise, if an integer or float is supplied, it is assumed that value is in the same unit as the original unit.

```python
current_disk = GigaByte(1270)
end_goal = TeraByte(2)
# Will return in Terabytes (0.73 TB)
print(end_goal - current_disk)
# Will return in Gigabytes (730.0 GB)
print((end_goal - current_disk).convert('gb'))
```

#### Comparison Operators

The data objects can also be compared to each other using the comparison operators (i.e. >, <, >=, etc). In this case, they similarly convert both values to bytes and compare that float object.
Otherwise, if a float or int is supplied as the comparator, then it is assumed the number is in the same unit as the object being compared.
```python
current_disk = GigaByte(1270)

if current_disk > 1000:
    print(current_disk.convert('tb'))
else:
    print(current_disk)
```

### Returning Values
The `__str__` method returns the value in a human-readable format which allows for clean output in code.  
The `__repr__` method returns the creation string for the object.
```python
disk1 = Byte(150000000000).convert('gb')
disk2 = MegaByte(328000).convert('gb')

# Printing the disks returns the human-readable value
print(','.join([disk1, disk2]))
## RETURNS:
150.0 GB 328.0 GB

# The object itself returns its creation string
disk1
## RETURNS:
GigaByte(150.0)
```
