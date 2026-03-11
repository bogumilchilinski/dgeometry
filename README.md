# dgeometry
## Table of Contents
- [Introduction](#introduction)
  - [1. What is dgeometry?](#1-what-is-dynpi)
  - [2. Key Features](#2-key-features)
  - [3. Getting Started on CoCalc](#3-getting-started-on-cocalc)
- [How to Start / Basic Usage](#how-to-start--basic-usage)
  - [1. Example Script](#1-example-scripts)
    to-do: expand
- [Installation \& Setup (Optional, for Local Development)](#installation--setup-optional-for-local-development)
  - [Requirements](#requirements)
  - [Manual Installation](#manual-installation)
- [Licensing Information](#licensing-information)

# Introduction

## 1. What is dgeometry?

dgeometry is a Python module designed for generating, manipulating, and visualizing engineering drawings. The library focuses on representing geometric constructions in a clear and extensible way, enabling users to model geometric entities using points, lines, and planes and perform operations on them.
The module is particularly useful in computational geometry, geometric modeling, and educational contexts, where geometric reasoning and visualization are important.
In many mathematical and engineering contexts, geometric constructions are traditionally performed using drawing tools or graphical software. While these approaches are intuitive, they are often difficult to reproduce, automate, or integrate with computational workflows.
dgeometry addresses this limitation by representing geometric objects as Python classes and expressing constructions through code. Each geometric object contains both data describing its geometric properties and methods that define relationships and operations with other objects. This makes it possible to create complex constructions in a transparent, reusable, and extensible way.

## 2. Key Features

- **Dynamics Module:** Tools for modeling mechanical systems and their dynamics.
- **Mechanical Models:** A collection of predefined mechanical models developed by experts.
- **Symbolic and Numeric Solvers:** Tools for solving Ordinary Differential Equations (ODEs) using symbolic and numerical methods.
- **Reporting Module:** A structured reporting system for generating and exporting reports.

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


# Installation & Setup (Optional, for Local Development)

## Requirements

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


## Manual Installation

```bash
pip install numpy pylatex sympy pandas matplotlib scipy pint pypandoc wand pymupdf

pip install dgeometry
```

Installing the Development Environment for Engineering Analysis

1. Install Visual Studio Code (Microsoft Store)
2. Install Python (Microsoft Store)
3. Install Git
For Windows users: https://git-scm.com/install/windows
For Mac users: https://git-scm.com/install/mac
4. Install the dgeometry library (https://github.com/bogumilchilinski/dgeometry) by using following command in terminal:
```bash
git clone https://github.com/bogumilchilinski/dgeometry
```
5. Install required libraries (code to be used in terminal available above)
5.1. Installing the plugin in VS Code (git extension package + latex workshop)
5.2. #to-do: create requirements.txt and add pip install -r requirements.txt
6. Creating a virtual environment in VSCode
Working folder on the main drive + subfolders (output, images)
Set the kernel and Jupyter Notebook environment
Set Git Autofetch: True in VSCode settings


# Licensing Information

dgeometry is distributed under an open-source license. Refer to the LICENSE file for details.
