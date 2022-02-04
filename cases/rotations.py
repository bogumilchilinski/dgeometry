from typing import List
import numpy as np
import sympy as sym
#from sympy.geometry import *
import sympy.geometry as geo
import matplotlib.pyplot as plt
from sympy.plotting import plot_parametric
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

import random
import base64
import random
import IPython as IP
import numpy as np
from sympy import Symbol, symbols
import copy


import itertools as it
from ..dgeometry import *
from .basics import *
    
class PointRotation(GeometricalCase):
        
    def __init__(self,point=Point(1,2,3),axis=None,plane=None,**kwargs):

        super().__init__()


        self._axis=axis
        self._plane = plane
        self._point = point
        

        rot_point = point.rotate_about(axis=axis,plane=plane)(f'{point._label}0')
        self._rotated_point = rot_point
        
        axis = rot_point._axis
        plane = rot_point._plane
        
        rot_center=(point@axis)
        

        
    def solution(self):
        
        
        current_obj=copy.deepcopy(self)

        return current_obj
        
    def get_default_data(self):




        
        default_data_dict = {
            Symbol('point'): [Point(x,y,z) for x in [8,8.5,9,7.5,7] for y in [5,5.5,6,6.5] for z in   [8,8.5,7.5,7]  ],
            Symbol('axis'): [(Point(1,2,3)^Point(5,11,3))],



        }
        return default_data_dict
    
    
class RotatedPoint(PointRotation):
        
    def __init__(self,point=Point(1,2,3),axis=None,plane=None,**kwargs):

        super().__init__(point=point,axis=axis,plane=plane,**kwargs)


        self._axis=axis
        self._plane = plane
        self._point = point
        

        rot_point = point.rotate_about(axis=axis,plane=plane)(f'{point._label}0')
        self._rotated_point = rot_point
        
        axis = rot_point._axis
        plane = rot_point._plane
        
        rot_center=(point@axis)
        
        self.add_solution_step(f'The ${point._label}$ point and axis of rotation ${axis._label}$ are currently highlighted - initial set for rotation process',[point,axis])
        
        if rot_center.coordinates == rot_point.coordinates:

            self.add_solution_step(f'Rotated point {rot_point._label} is the same as {point._label} point.',[rot_point(f'{point._label} = {point._label}0')])
            
        else:    


            point_e1=rot_point+(rot_center-rot_point)*(1+(0.5/rot_center.distance(rot_point)))
            point_e2=(rot_center)+((rot_center)-rot_point)*(-1-(0.5/rot_center.distance(rot_point)))

            self._eps_for_point = (point_e1^point_e2)(f'eps_{point._label}')

            self.add_solution_step(f'A rotation plane of {point._label} point passes {point._label} and is perpendicular to {axis._label} axis.',[self._eps_for_point(f'eps_{point._label}')])

            self.add_solution_step(f'S_{point._label} point - center of rotation',[rot_center])

            


            self.add_solution_step(f'''The position of {point._label}0 point can be determined by utilization of true length of the radius of rotation ({point._label} - S_{point._label})
            - the pytagoras theorem has to be applied (auxiliary right triangle)''',[rot_point(f'{point._label}')])
    
    
class UnrotatedPoint(PointRotation):
        
    def __init__(self,point=Point(1,2,3),reference=Line(Point(4,2,5),Point(7,11,5)),axis=None,plane=None,**kwargs):

        super().__init__(point=point,axis=axis,plane=plane,**kwargs)


        self._axis=axis
        self._plane = plane
        self._point = point
        self._reference = reference
        

        rot_point = point.rotate_about(axis=axis,plane=plane)(f'{point._label}0')
        self._rotated_point = rot_point
        
        axis = rot_point._axis
        plane = rot_point._plane
        
        rot_center=(point@axis)
        
        self.add_solution_step(
            f'''The {rot_point._label} rotated point, axis of rotation {axis._label} and {reference._label} line are currently highlighted 
            - data needed to find orginal position of the point''',[rot_point,axis,reference])
        
        if rot_center.coordinates == rot_point.coordinates:

            self.add_solution_step(f'Rotated point {rot_point._label} is the same as {point._label} point - there is nothing to do',[rot_point(f'{point._label}0 = {point._label}')])
            
        else:


            point_e1=rot_point+(rot_center-rot_point)*(1+(0.5/rot_center.distance(rot_point)))
            point_e2=(rot_center)+((rot_center)-rot_point)*(-1-(0.5/rot_center.distance(rot_point)))

            self._eps_for_point = (point_e1^point_e2)(f'eps_{point._label}')

            self.add_solution_step(f'A rotation plane of  point {point._label} passes  {rot_point._label}  and is perpendicular to {axis._label} axis.',[self._eps_for_point(f'eps_{point._label}')])

            self.add_solution_step(f'S_{point._label} point - Center of rotation',[rot_center])

            


            self.add_solution_step(f'''=== The true position of {point._label} can be found as intersection of plane of rotation {self._eps_for_point._label} and {reference._label} line - 
            {point._label} belongs simultaneously to {self._eps_for_point._label} and {reference._label}''',[point(f'{point._label}')])