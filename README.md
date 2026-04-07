# DataValues
[![Pypi](https://img.shields.io/pypi/v/datavalues)](https://pypi.org/project/datavalues)
[![MIT licensed](https://img.shields.io/badge/license-MIT-green.svg)](https://raw.githubusercontent.com/bnassif/datavalues/main/LICENSE)
![GitHub Release Date](https://img.shields.io/github/release-date/bnassif/datavalues)

DataValues is a Python package for handling data sizes (bits/bytes) with full support for both SI (decimal) and IEC (binary) prefixes.

## Features

- Supports bits and bytes
- Full range of SI (kilo, mega, giga, …) and IEC (kibi, mebi, gibi, …) units
- Accurate conversions between decimal/binary forms
- Parsing strings to corresponding units
- Intuitive comparisons (>, <, ==, >=, <=)
- Safe arithmetic with unit awareness (+, -, *, /, +=, etc.)
- Simple API that feels natural in Python

## Installation

```bash
# PyPi Installation
pip install datavalues
# GitHub Installation
pip install git+'https://github.com/bnassif/datavalues.git' 
```

## Getting Started

### Coversion
```python
from datavalues import MegaByte, Byte

# Convert using explicit classes
print(MegaByte(1).convert(Byte))
# 1000000.0 B

# Convert using string parsing
print(MegaByte(1).convert('byte'))
# 1000000.0 B
```

### String Parsing
```python
from datavalues import from_string

from_string('16GiB')
# GibiByte(16)
from_string('1000 megabytes')
# MegaByte(1000)

from datavalues import get_unit

get_unit('tebibytes')
# <class 'datavalues.binary.bytes.TebiByte'>
get_unit('GB')
# <class 'datavalues.metric.bytes.GigaByte'>
```

### Comparisons
```python
from datavalues import *

GigaByte(1) > MegaByte(500)
# True
KibiByte(1024) == MebiByte(1)
# True
```

### Arithmetic
```python
from datavalues import *

GigaByte(1) - MegaByte(175)
# GigaByte(0.825)

KibiByte(1024) + MebiByte(14)
# KibiByte(15360.0)

GibiByte(1) / MebiByte(256)
# 4.0

GibiByte(1) / 4
# GibiByte(0.25)

Byte(250) * 4
# Byte(1000)
```

## Why?
This project originally started as a way to reconcile differences in how NetBox reports and stores data sizes for disks and memory, specifically to align its expectations with the reality reported by hosts.

Soon after, many other applications were found, including:
- Computing data transfer times
- Comparing and calculating data & bandwidth units
- Determining storage requirements for backup retention policies

Thus, `datavalues` transitioned to a fully-featured library.

## Supported Units

Below are tables detailing all available units of measurement for data provided by the `datavalues` library.

Additional units will be added to this library as they are officially adopted.

### SI

SI (metric) units are based on powers of 10 (base-1000). These units use standard metric prefixes such as kilo-, mega-, and giga-, and can be applied to both bits and bytes.

For more details on the SI/metric prefixes, visit [the Wikipedia article](https://en.wikipedia.org/wiki/Metric_prefix#List_of_SI_prefixes).

#### Bits

SI/metric bits are most commonly used in network transport measurements (e.g., Mbps, Gbps).

| Unit | Symbol | Bit Conversion | Class |
| ---- | ------ | -------------- | ----- |
| Bit        | b  | 1 bit     | `datavalues.base.core.Bit`         |
| Kilobit    | kb | 10³ bits  | `datavalues.metric.bits.KiloBit`   |
| Megabit    | Mb | 10⁶ bits  | `datavalues.metric.bits.MegaBit`   |
| Gigabit    | Gb | 10⁹ bits  | `datavalues.metric.bits.GigaBit`   |
| Terabit    | Tb | 10¹² bits | `datavalues.metric.bits.TeraBit`   |
| Petabit    | Pb | 10¹⁵ bits | `datavalues.metric.bits.PetaBit`   |
| Exabit     | Eb | 10¹⁸ bits | `datavalues.metric.bits.ExaBit`    |
| Zettabit   | Zb | 10²¹ bits | `datavalues.metric.bits.ZettaBit`  |
| Yottabit   | Yb | 10²⁴ bits | `datavalues.metric.bits.YottaBit`  |
| Ronnabit   | Rb | 10²⁷ bits | `datavalues.metric.bits.RonnaBit`  |
| Quettabit  | Qb | 10³⁰ bits | `datavalues.metric.bits.QuettaBit` |

#### Bytes

SI/metric bytes (e.g., MB, GB) are widely used in marketing and user-facing representations of storage capacity.

Historically, these units were often used ambiguously to represent binary quantities.  
The [IEC 60027-2](https://en.wikipedia.org/wiki/IEC_60027-2) standard introduced IEC/binary units to remove this ambiguity, though SI units are still commonly used.

| Unit | Symbol | Byte Conversion | Class |
| ---- | ------ | --------------- | ----- |
| Byte       | B  | 1 byte     | `datavalues.base.core.Byte`          |
| Kilobyte   | kB | 10³ bytes  | `datavalues.metric.bytes.KiloByte`   |
| Megabyte   | MB | 10⁶ bytes  | `datavalues.metric.bytes.MegaByte`   |
| Gigabyte   | GB | 10⁹ bytes  | `datavalues.metric.bytes.GigaByte`   |
| Terabyte   | TB | 10¹² bytes | `datavalues.metric.bytes.TeraByte`   |
| Petabyte   | PB | 10¹⁵ bytes | `datavalues.metric.bytes.PetaByte`   |
| Exabyte    | EB | 10¹⁸ bytes | `datavalues.metric.bytes.ExaByte`    |
| Zettabyte  | ZB | 10²¹ bytes | `datavalues.metric.bytes.ZettaByte`  |
| Yottabyte  | YB | 10²⁴ bytes | `datavalues.metric.bytes.YottaByte`  |
| Ronnabyte  | RB | 10²⁷ bytes | `datavalues.metric.bytes.RonnaByte`  |
| Quettabyte | QB | 10³⁰ bytes | `datavalues.metric.bytes.QuettaByte` |

### IEC

IEC (binary) units are based on powers of 2 (base-1024). These units use binary prefixes such as kibi-, mebi-, and gibi-, and are most commonly applied to bytes in computing contexts.

For more details on the IEC/binary prefixes, visit [the Wikipedia article](https://en.wikipedia.org/wiki/Binary_prefix).

#### Bits

IEC/binary bits (e.g., Kib, Mib) are defined for consistency with binary prefixes, but are rarely used in practice compared to their byte counterparts.

| Unit | Symbol | Bit Conversion | Class |
| ---- | ------ | -------------- | ----- |
| Bit      | b   | 1 bit     | `datavalues.base.core.Bit`       |
| Kibibit  | Kib | 2¹⁰ bits  | `datavalues.binary.bits.KibiBit`  |
| Mebibit  | Mib | 2²⁰ bits  | `datavalues.binary.bits.MebiBit`  |
| Gibibit  | Gib | 2³⁰ bits  | `datavalues.binary.bits.GibiBit`  |
| Tebibit  | Tib | 2⁴⁰ bits  | `datavalues.binary.bits.TebiBit`  |
| Pebibit  | Pib | 2⁵⁰ bits  | `datavalues.binary.bits.PebiBit`  |
| Exbibit  | Eib | 2⁶⁰ bits  | `datavalues.binary.bits.ExbiBit`  |
| Zebibit  | Zib | 2⁷⁰ bits  | `datavalues.binary.bits.ZebiBit`  |
| Yobibit  | Yib | 2⁸⁰ bits  | `datavalues.binary.bits.YobiBit`  |
| Robibit  | Rib | 2⁹⁰ bits  | `datavalues.binary.bits.RobiBit`  |
| Quebibit | Qib | 2¹⁰⁰ bits | `datavalues.binary.bits.QuebiBit` |

#### Bytes

IEC/binary bytes (e.g., KiB, MiB, GiB) are most commonly used in operating systems and technical contexts to represent storage and memory.

These units were standardized by [IEC 60027-2](https://en.wikipedia.org/wiki/IEC_60027-2) to clearly distinguish binary-based values from SI/metric units.

| Unit      | Symbol | Byte Conversion | Class       |
| --------- | ------ | --------------- | ----------- |
| Byte      | B   | 1 byte     | `datavalues.base.core.Byte`         |
| Kibibyte  | KiB | 2¹⁰ bytes  | `datavalues.binary.bytes.KibiByte`  |
| Mebibyte  | MiB | 2²⁰ bytes  | `datavalues.binary.bytes.MebiByte`  |
| Gibibyte  | GiB | 2³⁰ bytes  | `datavalues.binary.bytes.GibiByte`  |
| Tebibyte  | TiB | 2⁴⁰ bytes  | `datavalues.binary.bytes.TebiByte`  |
| Pebibyte  | PiB | 2⁵⁰ bytes  | `datavalues.binary.bytes.PebiByte`  |
| Exbibyte  | EiB | 2⁶⁰ bytes  | `datavalues.binary.bytes.ExbiByte`  |
| Zebibyte  | ZiB | 2⁷⁰ bytes  | `datavalues.binary.bytes.ZebiByte`  |
| Yobibyte  | YiB | 2⁸⁰ bytes  | `datavalues.binary.bytes.YobiByte`  |
| Robibyte  | RiB | 2⁹⁰ bytes  | `datavalues.binary.bytes.RobiByte`  |
| Quebibyte | QiB | 2¹⁰⁰ bytes | `datavalues.binary.bytes.QuebiByte` |

## License
MIT - Feel free to use, extend, and contribute.