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
from .rotations import RotatedPoint,UnrotatedPoint
    
class ShapeOnPlane(GeometricalCase):


    point_A = [Point(x,y,z) for x in [8,8.5,9,7.5,7] for y in [5,5.5,6,6.5] for z in   [8,8.5,7.5,7]  ]

    point_O=[Point(x,y,z) for x in [5,5.5,6,6.5] for y in [8,8.5,9,9.5,10] for z in   [4,4.5,5,5.5] ]

    point_P = [Point(x,y,z) for x in [1,1.5,2,2.5] for y in [2,2.5,3,3.5]  for z in [1,1.5,2,2.5] ]





    def __init__(self,point_A=None,point_P=None,point_O=None,**kwargs):

        super().__init__()

        if point_A and point_O and point_P:
            projections=(point_A@HPP,point_O@HPP,point_O@VPP,point_P@VPP,point_P@HPP,point_A@VPP,)
        else:
            projections=[]

        self._assumptions=DrawingSet(*projections)

        self._point_A=point_A
        self._point_P=point_P
        self._point_O=point_O

        
        self.add_solution_step(
                f'''Assumptions''', [point_A,point_P,point_O])



    def _base_shape(self,base_plane=None):
        
        if base_plane is None:
            A = self._point_A
            O = self._point_O
            P = self._point_P
        else:
            A,O,P = base_plane
        
        return A,O,P
        
        
        
    def _given_plane(self,base_plane=None):
        
        if base_plane is None:
            A = self._point_A
            O = self._point_O
            P = self._point_P
        else:
            A,O,P = base_plane
        
        return A,O,P
        
    def _rotation_of_given_plane(self,base_plane=None):
        
        axis = self._axis
        
        
        rotated_base=[]
        
        
        for base_point  in self._given_plane():

            base_point_rotation_case = RotatedPoint(base_point,axis=axis)
            self._append_case(base_point_rotation_case)

            rot_base_point = base_point_rotation_case._rotated_point
            rotated_base += [rot_base_point]
            
        return rotated_base
        
    def _rotation_of_base(self,base_plane=None):
        
        if base_plane is None:
            base_plane = self._base_shape()

        return base_plane
        
        
    def solution(self):
        if self._cached_solution is None:
            current_obj = copy.deepcopy(self)

            A = current_obj._point_A
            O = current_obj._point_O
            P = current_obj._point_P

            plane_alpha = Plane(A, O, P)

            plane_beta = HorizontalPlane(P)
            plane_eta = VerticalPlane(P)

            line_k = plane_alpha.intersection(plane_beta)[0]('a')

            point_P1 = plane_beta.intersection(A ^ O)[0]('1')
            current_obj.P1 = point_P1
            line_kk = (P ^ point_P1)('a')            

            
            current_obj.add_solution_step(
                f'''Axis of rotation - it is common part between given plane and horizontal plane which contains point {P._label}. 
                The {point_P1._label} point has to be found, in order to determine axis position''', [point_P1,
                                     (P ^ point_P1)('a')])
            point_P2 = plane_eta.intersection(A ^ O)[0]('2')

            line_f = (P ^ point_P2)('f') 

            current_obj.add_solution_step(
                f'''Axis of rotation - it is common part between given plane and horizontal plane which contains point {P._label}''', [point_P2,
                                     (P ^ point_P2)('f')])


            point_O = O

            line_k = Line(P, (O @ line_k))('k')
            current_obj._axis = line_k

            A0,O0,P0 = current_obj._rotation_of_given_plane()
                
            current_obj.A0 = A0
            current_obj.P0 = P0
            current_obj.O0 = O0
                
            #### Step 4 ####
            ### postion of B0 (based on triangle geometry) #####

            for base_point  in current_obj._rotation_of_base():
            
                shape_unrotation_case = UnrotatedPoint(base_point,(P^O)('PO'),axis=line_k)
                current_obj._append_case(shape_unrotation_case)


            current_obj._cached_solution = current_obj
        else:
            current_obj = copy.deepcopy(self._cached_solution)
            
        print(list(current_obj))
            
        return current_obj


    def get_default_data(self):

        point_A = self.__class__.point_A
        point_O = self.__class__.point_O
        point_P = self.__class__.point_P


        
        default_data_dict = {
            Symbol('A'): point_A,
            Symbol('P'): point_P,
            Symbol('O'): point_O,



        }
        return default_data_dict
        
        
    
class SquareOnPlane(ShapeOnPlane):


    point_A = [Point(x,y,z) for x in [8,8.5,9,7.5,7] for y in [5,5.5,6,6.5] for z in   [8,8.5,7.5,7]  ]

    point_O=[Point(x,y,z) for x in [5,5.5,6,6.5] for y in [8,8.5,9,9.5,10] for z in   [4,4.5,5,5.5] ]

    point_P = [Point(x,y,z) for x in [1,1.5,2,2.5] for y in [2,2.5,3,3.5]  for z in [1,1.5,2,2.5] ]




    def _base_shape(self,base_plane=None):
        
        if base_plane is None:
            A = self._point_A
            O = self._point_O
            P = self._point_P
        else:
            A,O,P = base_plane
            
        S = (A @ (O ^ P))('S')  #'Srodek' podstawy

        dirPS = P - S
        dirOS = O - S
        square_diagonal = 2 * A.distance(S).n(5)
        #triangle_side =  triangle_height / ((3**(1/2))/2)

        B = (S + dirPS / (P.distance(S)) * (square_diagonal / 2))('B')
        D = (S - dirPS / (P.distance(S)) * (square_diagonal / 2))('D')
        C = (S + (S - A))('C')

        self.add_solution_step('Dawid Creating a point $C_0$ based on triangle geometry ', [A^B,B^C])
        
        self.A = A
        self.B = B
        self.D = D
        
        return A,B, D

    def _rotation_of_base(self,base_plane=None):

        self._base_shape()
        
        
        A = self.A
        B= self.B 
        D = self.D
        
        self.add_solution_step('Dawid - Rotated Base (triangle BAD - half of square $ABCD$)', [A^B,A^D])
        
        return  B,D
    