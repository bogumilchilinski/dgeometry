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

### 2.1. 2D Calling Conventions & Best Practices (Code-Driven Design)

To ensure your sketches are robust, reusable, and easy to modify, follow these essential coding conventions when using `dgeometry`:

* **Parametrization Over Hardcoding:** Avoid entering raw numbers directly into geometric entities. Define all dimensions as variables at the beginning of your script. If a specific dimension (e.g., a tool diameter) needs to be updated from 45 mm to 80 mm, you should only have to change one variable, automatically updating the entire downstream geometry.
* **Standardized Coordinate Origins:** Always anchor your base geometry to the origin `Point(0, 0)`. 
  * For *turned or rotational parts* (e.g., machine shafts, pulleys, or sleeves), standard practice is to place the axis of rotation exactly on the X-axis (where `Y = 0`), modeling only the upper half of the cross-section.
* **Strict Instantiation Order:** Follow this structural hierarchy to build complex shapes cleanly:
  1. **Nodes:** Define all `Point` objects first.
  2. **Edges:** Connect nodes using basic primitives (`Line`, `Circle`, `Arc`).
  3. **Profiles:** Gather your connected edges into a coherent `Profile` or `Sketch` object.
  4. **Transformations/Operations:** Apply operations like fillets, chamfers, intersections, or offsets directly to the profile object, rather than manually calculating new coordinates.
* **Descriptive Naming:** Name variables based on their mechanical function rather than arbitrary letters. Use clear engineering identifiers (e.g., `bearing_journal_line` instead of `line2`, or `d_inner` / `d_outer` for diameters).

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

## 2. 2D Calling Conventions & Workflow

When building custom 2D geometries in `dgeometry`, follow this standard procedural workflow:

1. **Define the Base Points (`Point`):** Always start by anchoring your geometry in the 2D coordinate system. Use these points as your reference nodes.
2. **Build Primitives (`Line`, `Circle`, `Arc`):** Connect your points to create boundaries and centerlines.
3. **Apply Operations:** Use built-in methods (like `.intersect()`, `.offset()`, or `.mirror()`) to manipulate the geometry without hardcoding new coordinates.
4. **Group into Profiles/Sketches:** Gather your connected primitives into a coherent profile representing the mechanical part.
5. **Render/Preview:** Call the `.preview()` or equivalent rendering method to verify the sketch visually before exporting or converting to 3D.

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

# Installation & Setup (Local Development)

## 1. Requirements

Python Version: **Python 3.8+**. All required libraries (including `numpy`, `sympy`, `cadquery`, `matplotlib`, `pylatex`, etc.) are listed in the repository's `requirements.txt` file.

## 2. Manual Installation & VS Code Setup

**CRITICAL NOTE FOR 3D/CADQUERY USERS:** If you plan to use any CadQuery features, **you MUST manually install the `OCP CAD Viewer` extension in Visual Studio Code**. Without this specific extension, your models will not visualize, and the 3D preview windows will simply fail to render.

**Step-by-Step Guide:**

1. Install **Visual Studio Code** (from the Microsoft Store or `code.visualstudio.com`).
2. Install **Python** (from the Microsoft Store or `python.org`).
3. Install **Git**:
   - Windows: `git-scm.com/install/windows`
   - Mac: `git-scm.com/install/mac`
4. Clone the `dgeometry` repository by opening your terminal and running:
   ```bash
   git clone [https://github.com/bogumilchilinski/dgeometry]              (https://github.com/bogumilchilinski/dgeometry)
5. Navigate to the cloned folder and install all required libraries using:
`bash
pip install -r requirements.txt`

(Note: If your terminal returns `"command not found: pip",` try using `pip3 install -r requirements.txt.` If the issue persists, verify that Python is correctly added to your system PATH).

6. Install VS Code Extensions:
   -Python Extension Pack
   -Git Extension Package
   -OCP CAD Viewer (Mandatory for CadQuery visualization!)
7. Environment Setup in VS Code:
   
Create a working folder on your main drive with subfolders (e.g., `output/`, `images/`).

Select the correct Python Interpreter/Kernel for your Jupyter Notebooks in the top right corner.

Go to VS Code Settings and set `Git: Autofetch` to `True`.
   
# Licensing Information

dgeometry is distributed under an open-source license. Refer to the LICENSE file for details.
