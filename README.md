# dgeometry
## Table of Contents
- [Introduction](#introduction)
  - [1. What is dgeometry?](#1-what-is-dynpi)
  - [2. Key Features](#2-key-features)
  - [3. Getting Started on CoCalc](#3-getting-started-on-cocalc)
- [How to Start / Basic Usage](#how-to-start--basic-usage)
  - [1. Example Script](#1-example-scripts)
  - [2. Usage](#2-usage)
- [Installation \& Setup (Optional, for Local Development)](#installation--setup-optional-for-local-development)
  - [1. Requirements](#1-requirements)
  - [2. Manual Installation](#2-manual-installation)
- [Licensing Information](#licensing-information)

# Introduction

## 1. What is dgeometry?

dgeometry is a Python module designed for generating, manipulating, and visualizing engineering drawings. The library focuses on representing geometric constructions in a clear and extensible way, enabling users to model geometric entities using points, lines, and planes and perform operations on them.
The module is particularly useful in computational geometry, geometric modeling, and educational contexts, where geometric reasoning and visualization are important.
In many mathematical and engineering contexts, geometric constructions are traditionally performed using drawing tools or graphical software. While these approaches are intuitive, they are often difficult to reproduce, automate, or integrate with computational workflows.
dgeometry addresses this limitation by representing geometric objects as Python classes and expressing constructions through code. Each geometric object contains both data describing its geometric properties and methods that define relationships and operations with other objects. This makes it possible to create complex constructions in a transparent, reusable, and extensible way.

## 2. Key Features

- **Representation of Basic Geometric Objects:** Provides classes and structures to represent fundamental geometric elements such as points, lines, and planes.
- **Geometric Transformations and Operations:** Supports creating and manipulating geometric relationships including intersections, projections, and dependencies between objects.
- **Visualization:** Enables generation of diagrams and visual representations of geometric structures to help analyze and present results.
- **Modular and Extensible Design:** Designed as a flexible Python module that can be easily extended with new geometric primitives, algorithms, or visualization features.

## 3. Getting Started on CoCalc

To begin working with dgeometry, you need an account on [CoCalc](https://cocalc.com/).

1. Create an account on CoCalc.
2. Accept the project invitation using this [link](https://cocalc.com/app?project-invite=hXnPFLqokQsoK6TG).
3. It is highly recommended to get familiar with DynPi module first. To do so open the [README](https://cocalc.com/projects/b51ce971-5b39-4911-ad97-ef59f15f0039/files/READme.ipynb) file and follow the instructions in the introductory guide.

---

# How to Start / Basic Usage

## 1. Example Scripts

To view exemplary capabilities of dynpy, run the following example script:

```python
from dgeometry.cases.drawings import SleeveSketch
SleeveSketch.from_random_data().preview()
```

## 2. Usage

After installing the dependencies (refer to Installation & Setup (Optional, for Local Development) section), you can import the module in your Python scripts or notebooks and start creating geometric objects and constructions.
Example:
```python
from dgeometry import *

# Example geometric objects
A = Point(0, 0)
B = Point(4, 3)

# Create a line passing through two points
line_AB = Line(A, B)

print(line_AB)
```

You can extend this by defining additional points, lines, planes, and performing geometric constructions or visualizations depending on your use case.

The module can be used in:

- Python scripts
- Jupyter notebooks
- Educational or computational geometry projects

---

# Installation & Setup (Optional, for Local Development)

## 1. Requirements

Python Version: **Python 3.8+**. Required Libraries:

- **numpy** 
- **pylatex**
- **sympy**
- **pandas**
- **matplotlib**
- **scipy**
- **pint**
- **pypandoc** 
- **pygithub**
- **wand** 
- **pymupdf** 
- **cadquery**

## 2. Manual Installation

1. Install Visual Studio Code (Microsoft Store or code.visualstudio.com/docs/setup/mac for mac)
2. Install Python (Microsoft Store or python.org)
3. Install Git
For Windows users: https://git-scm.com/install/windows
For Mac users: https://git-scm.com/install/mac
4. Install the dgeometry library (https://github.com/bogumilchilinski/dgeometry) by using following command in terminal:
```bash
git clone https://github.com/bogumilchilinski/dgeometry
```
5. Install all required libraries (2 ways):
- If you are just starting coding or your abilities are limited you can install required libraries by using the following code:
```bash
pip install -r requirements.txt
```
 if for some reason the result of above command returns "command not found: pip", then try this code:
```bash
pip3 install -r requirements.txt
```
if the issue still persist verify if step 2 is fulfilled.
6. Install plugins: in VS Code (git extension package)
7. Creating a virtual environment in VSCode
Working folder on the main drive + subfolders (output, images)

Set the kernel and Jupyter Notebook environment

Set Git Autofetch: True in VSCode settings

# Licensing Information

dgeometry is distributed under an open-source license. Refer to the LICENSE file for details.
