# dgeometry

## Table of Contents
- [Introduction](#introduction)
  - [1. What is dgeometry?](#1-what-is-dgeometry)
  - [2. Key Features](#2-key-features)
  - [3. Getting Started on CoCalc](#3-getting-started-on-cocalc)
- [How to Start / Basic Usage](#how-to-start--basic-usage)
  - [1. Example Scripts (2D Focus)](#1-example-scripts-2d-focus)
  - [2. 2D Calling Conventions & Workflow](#2-2d-calling-conventions--workflow)
- [Installation & Setup (Local Development)](#installation--setup-local-development)
  - [1. Requirements](#1-requirements)
  - [2. Manual Installation & VS Code Setup](#2-manual-installation--vs-code-setup)
- [Licensing Information](#licensing-information)

---

# Introduction

## 1. What is dgeometry?
dgeometry is a Python module designed for generating, manipulating, and visualizing engineering drawings. The library focuses on representing geometric constructions in a clear and extensible way, enabling users to model geometric entities using points, lines, and planes and perform operations on them.

The module is particularly useful in computational geometry, geometric modeling, and educational contexts (e.g., parametric design of machine parts), where geometric reasoning and visualization are important. By representing geometric objects as Python classes and expressing constructions through code, it makes it possible to create complex, repeatable constructions in a transparent and fully automated way.

## 2. Key Features
- **Representation of Basic Geometric Objects:** Provides classes and structures to represent fundamental geometric elements such as points, lines, and profiles.
- **Geometric Transformations and Operations:** Supports creating and manipulating geometric relationships including intersections, projections, and parametric dependencies between objects.
- **2D Drafting & Visualization:** Enables generation of detailed 2D diagrams and technical profiles.
- **Integration with CadQuery:** Ready for advanced boundary representation (B-rep) modeling and programmatic CAD generation.

## 3. Getting Started on CoCalc
To begin working with dgeometry without local installation, you need an account on [CoCalc](https://cocalc.com/).
1. Create an account on CoCalc.
2. Accept the project invitation using this [link](https://cocalc.com/app?project-invite=hXnPFLqokQsoK6TG).
3. Open the repository files and explore the provided notebooks.

---

# How to Start / Basic Usage

## 1. Example Scripts (2D Focus)
You can find a massive collection of diverse examples and use cases in the **`cases/models/test.ipynb`** notebook. 

Here are three distinct examples demonstrating different 2D capabilities of the library:

**Example A: Simple Parametric Profile (Sleeve)**
```python
from dgeometry.cases.drawings import SleeveSketch

# Generates a basic sleeve profile using randomized/default parametric data
sleeve = SleeveSketch.from_random_data()
sleeve.preview()
```
**Example B: Drive Shaft Geometry Construction**
```python
from dgeometry import Point, Line, Profile

# Defining base nodes for a stepped shaft
p1 = Point(0, 0)
p2 = Point(50, 0)
p3 = Point(50, 20)
p4 = Point(0, 20)

# Creating boundary lines
shaft_axis = Line(p1, p2)
step_edge = Line(p2, p3)

print("Shaft axis length:", shaft_axis.length)
```

**Example C: Intersections and Constraints**
```python
from dgeometry import Point, Circle, Line

# Creating a reference circle (e.g., for a bolt pattern on a flange)
center = Point(0, 0)
pitch_circle = Circle(center, radius=80)

# Finding intersections with a specific axis
horizontal_axis = Line(Point(-100, 0), Point(100, 0))
intersections = pitch_circle.intersect(horizontal_axis)

print("Bolt hole locations:", intersections)
```

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
