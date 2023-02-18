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
from ...dgeometry import *
from ..shapes import *

from ..basics import LineAndPlaneIntersection




class TriangularPrism(GeometricalCase):

    point_A = [
        Point(x, y, z) for x in [1, 1.5, 2, 2.5]
        for y in [2, 2.5, 3, 3.5, 4, 4.5, 5] for z in [2, 2.5, 3, 3.5]
    ]

    point_B = [
        Point(x, y, z) for x in range(4, 6) for y in range(8, 12)
        for z in [2, 2.5, 3, 3.5]
    ]

    point_C = [
        Point(x, y, z) for x in [1, 1.5, 2, 2.5]
        for y in [13, 13.5, 14, 14.5, 15] for z in [6, 6.5, 7]
    ]

    point_O = [
        Point(x, y, z) for x in range(7, 10) for y in [6, 6.5, 7, 7.5, 8.5]
        for z in range(6, 9)
    ]

    
    shift = [
        Point(x, y, z) for x in [0] for y in [0]
        for z in [0]
    ]
    
    
    def __init__(self,
                 point_A=None,
                 point_B=None,
                 point_C=None,
                 point_O=None,
                 **kwargs):

        super().__init__()



        #self._assumptions = DrawingSet(*projections)

        self.point_A = point_A
        self.point_B = point_B
        self.point_C = point_C
        self.point_O = point_O

        self._given_data = {
            'A': point_A,
            'B': point_B,
            'C': point_C,
            'O': point_O,
        }


        self.add_solution_step('Assumptions',
                        [point_A, point_B, point_C, point_O])

        
        
    def solution(self):
        if self._cached_solution is None:
            
            current_obj = self._solution()
            self._cached_solution = current_obj
        else:
            current_obj = copy.deepcopy(self._cached_solution)
        return current_obj
        
    def _solution(self):
        current_obj = copy.deepcopy(self)

        A = current_obj.point_A
        B = current_obj.point_B
        C = current_obj.point_C
        O = current_obj.point_O



        plane_alpha = Plane(A, B, C)



        plane_beta = HorizontalPlane(B)
        plane_eta = VerticalPlane(B)


        point_P1 = plane_beta.intersection(A ^ C)[0]('1')
        current_obj.P1 = point_P1
        line_h = (B ^ point_P1)('h')

        point_P2 = plane_eta.intersection(A ^ C)[0]('2')

        line_f = (B ^ point_P2)('f')

        beta_p1 = O-(point_P1-B)
        beta_p0 = O
        beta_p2 = O-(point_P2-B)

        plane_beta=Plane(beta_p0,beta_p1,beta_p2)
        
        
        #minus controls position (side) of parallel plane
        current_obj.add_solution_step('Parallel plane',[Line(beta_p0,beta_p1)('e') , Line(beta_p0,beta_p2)('f') ])
        
        D=(A@plane_beta)('D')
        E=(B@plane_beta)('E')
        F=(C@plane_beta)('F')
        
        #aux_point = A+(D-A)*2
        
        aux_point = D
        
        
        height_A = Line(A,aux_point)('hA')
        current_obj.add_solution_step('Perpendicular line - height',[height_A])
        
        plane_gamma=Plane(D,E,F)

        
        intersec_case  = LineAndPlaneIntersection(beta_p1,beta_p0,beta_p2 , A,aux_point ).solution()
        current_obj._append_case(intersec_case)
        
        # triangle_plane = Plane(A, B, C)
        # A, B, C, D, E, F = Prism.right_from_parallel_plane(triangle_plane, O)
        # plane_gamma=Plane(D,E,F)

        line_ad = Line(A, D)('a')
        line_be = Line(B, E)('b')
        line_cf = Line(C, F)('c')





        current_obj.point_D = D
        current_obj.point_E = E
        current_obj.point_F = F

        
        current_obj.add_solution_step('Vertices',
                        [D,E,F,plane_gamma])

        current_obj.add_solution_step('Prism',
                        [plane_alpha,plane_gamma,line_ad,line_be,line_cf])
        
        return current_obj

    def get_default_data(self):

        point_A = self.__class__.point_A
        point_B = self.__class__.point_B
        point_C = self.__class__.point_C
        point_O = self.__class__.point_O

        default_data_dict = {
            Symbol('A'): point_A,
            Symbol('B'): point_B,
            Symbol('C'): point_C,
            Symbol('O'): point_O,
        }
        return default_data_dict


    


class EquilateralTrianglePrism(GeometricalCase):
    """"
    #quite good data
    #point_A = [Point(x,y,z) for x in [4,5.5,5] for y in [5,5.5,6] for z in   [5.5,6,6.5]  ]

    #point_O=[Point(x,y,z) for x in [3,3.5] for y in [8,8.5,9] for z in   [3,3.5,4] ]

    #point_P = [Point(x,y,z) for x in [6,6.5,7] for y in [3,3.5]  for z in [1,1.5,2] ]

    #point_H = [Point(x,y,z) for x in range(9,11) for y in [3,3.5] for z in range(9,11) ]
    """
    # new set
    point_A = [
        Point(x, y, z) for x in [3, 3.5] for y in [8, 8.5, 9] for z in [6, 7]
    ]

    point_O = [
        Point(x, y, z) for x in [6, 7] for y in [11, 11.5, 12]
        for z in [2.5, 3, 3.5]
    ]

    point_P = [
        Point(x, y, z) for x in [1, 1.5, 2] for y in [3, 3.5]
        for z in [1, 1.5, 2]
    ]

    point_H = [
        Point(x, y, z) for x in range(7, 9) for y in [3, 3.5]
        for z in range(9, 11)
    ]
    
    shift = [
        Point(x, y, z) for x in [0] for y in [0]
        for z in [0]
    ]

    def __init__(self,
                 point_A=None,
                 point_P=None,
                 point_O=None,
                 point_H=None,
                 **kwargs):

        super().__init__()

        if point_A and point_O and point_P and point_H:
            projections = (point_A @ HPP, point_O @ HPP, point_O @ VPP,
                           point_P @ VPP, point_P @ HPP, point_A @ VPP,
                           point_H @ VPP, point_H @ HPP)
        else:
            projections = []

        # it creates first step of solution
        self.add_solution_step('Assumptions',
                               [point_A, point_O, point_P, point_H])

        self._assumptions3d = DrawingSet(point_A, point_O, point_P,
                                         point_H)('Assumptions')
        self._assumptions = DrawingSet(*projections)
        #self._assumptions3d=DrawingSet(point_A,point_O,point_P,point_H)('Assumptions')

        #self += [point_A,point_O,point_P,point_H]

        self.point_A = point_A
        self.point_P = point_P
        self.point_O = point_O
        self.point_H = point_H

        self._given_data = {
            'A': point_A,
            'P': point_P,
            'O': point_O,
            'H': point_H
        }

    def _solution(self):
        current_obj = copy.deepcopy(self)

        A = current_obj.point_A
        O = current_obj.point_O
        P = current_obj.point_P

        H = current_obj.point_H

        S = (A @ (O ^ P))('S')  #'Srodek' podstawy

        dirPS = P - S
        dirOS = O - S
        triangle_height = A.distance(S)
        triangle_side = triangle_height / ((3**(1 / 2)) / 2)

        B = (S + dirPS / (P.distance(S)) * (triangle_side / 2))('B')
        C = (S - dirPS / (P.distance(S)) * (triangle_side / 2))('C')

        triangle_plane = Plane(A, B, C)

        current_set = DrawingSet(*current_obj._solution_step[-1])

        line_a = Line(A, B)('a')
        line_b = Line(C, A)('b')
        plane_alpha = Plane(A, O, P)

        plane_beta = HorizontalPlane(P)
        plane_eta = VerticalPlane(P)

        line_k = plane_alpha.intersection(plane_beta)[0]('a')

        point_P1 = plane_beta.intersection(A ^ O)[0]('1')
        point_P2 = plane_eta.intersection(A ^ O)[0]('2')
        current_obj.P1 = point_P1
        line_kk = (P ^ point_P1)('a')
        line_f = (P ^ point_P2)('f')

        # it creates next step of solution - lines are presented
        #current_step3d=copy.deepcopy(current_obj._solution3d_step[-1])+[(A^point_P1)('AO'),point_P1,(P^point_P1)('a')]

        #it sets the step elements
        current_obj.add_solution_step(
            'Axis of rotation', [(A ^ point_P1)('AO'), point_P1,
                                 (P ^ point_P1)('a'), point_P2, line_f])

        elems = self._assumptions
        projections = []
        point_0_dict = {}
        eps_dict = {}

        point_B = B
        point_C = C
        point_O = O

        ##################   plane rotation

        line_kk = Line(P, (O @ line_k))('k')

        A0 = A.rotate_about(axis=line_k)('A_0')
        current_obj.point_A_0 = A0
        current_obj.add_solution_step('Point A rotation', [A0])
        elems=[current_obj.point_A_0]
        projections=[current_obj.point_A_0@HPP,current_obj.point_A_0@VPP]
        current_set+=[*elems,*projections]
        ### Step 2 #####
        ###  plane of rotation of A ####

        

        #### Step 3 ####
        ### rotated point A0 of A #####

        B0 = B.rotate_about(axis=line_k)('B_0')
        current_obj.point_B_0 = B0

        current_obj.add_solution_step('Point B rotation', [B0])

        #### Step 4 ####
        ### postion of B0 (based on triangle geometry) #####

        C0 = C.rotate_about(axis=line_k)('C_0')
        current_obj.point_C_0 = C0
        current_obj.add_solution_step('Point C rotation', [C0])

        #### Step 5 ####
        ### postion of C0 (based on triangle geometry) #####

        #current_obj.D0=D.rotate_about(axis=line_k)('D_0')
        current_obj.O0 = O.rotate_about(axis=line_k)('O_0')

        current_obj.add_solution_step('Base ABC', [A, B, C])

        G = (H @ plane_alpha)('G')

        ############  upper  base

        dirHG = H - G
        distance_HG = (H.distance(G)).n(5)

        #D = (A + dirHG/distance_HG*triangle_height)('D')
        #E = (B + dirHG/distance_HG*triangle_height)('E')
        #F = (C + dirHG/distance_HG*triangle_height)('F')

        A, B, C, D, E, F = Prism(triangle_plane,
                                 dirHG)

        current_obj.add_solution_step('Vertices D,E,F', [D, E, F])

        elems += [D, E, F, G]

        projections += [
            G @ HPP, G @ VPP, D @ HPP, D @ VPP, E @ HPP, E @ VPP, F @ HPP,
            F @ VPP
        ]

        current_obj._assumptions = DrawingSet(
            *current_obj.get_projections())('Solution')
        current_obj._assumptions3d = DrawingSet(*current_obj)

        current_obj.point_B = B
        current_obj.point_C = C
        current_obj.point_D = D
        current_obj.point_E = E
        current_obj.point_F = F


        return current_obj

    def get_default_data(self):

        point_A = self.__class__.point_A
        point_O = self.__class__.point_O
        point_P = self.__class__.point_P
        point_H = self.__class__.point_H
        shift = self.__class__.shift

        default_data_dict = {
            Symbol('A'): point_A,
            Symbol('P'): point_P,
            Symbol('O'): point_O,
            Symbol('H'): point_H,
            'shift':shift,
        }
        return default_data_dict

    
    def get_random_parameters(self):

        parameters_dict = super().get_random_parameters()

        point_H = parameters_dict[Symbol('H')]
        point_O = parameters_dict[Symbol('O')]
        point_A = parameters_dict[Symbol('A')]
        point_P = parameters_dict[Symbol('P')]

        shift = parameters_dict['shift']
        parameters_dict.pop('shift')

        for point in symbols('A P O H'):
            parameters_dict[point] = parameters_dict[point] + shift

        return parameters_dict

## START –> odtąd KOPIOWAĆ
class EquilateralTrianglePrismNew(EquilateralTrianglePrism):

    point_A = [
        Point(x, y, z) for x in [8] for y in [6, 6.5]
        for z in [8]
    ]

    point_O = [
        Point(x, y, z) for x in [5.5, 6, 6.5] for y in [9, 9.5, 10]
        for z in [4, 4.5, 5, 5.5]
    ]

    point_P = [
        Point(x, y, z) for x in [2, 2.5] for y in [4,4.5]
        for z in [2, 2.5]]
    
    point_H = [
        Point(x, y, z) for x in range(7, 9) for y in [3, 3.5]
        for z in range(9, 11)
    ]
    
    shift = [
        Point(x, y, z) for x in [0] for y in [0]
        for z in [0]
    ]
    
    @property
    def base_generating_class(self):
        return EquilateralTriangleOnPlane
    
    def _solution(self):
        current_obj = copy.deepcopy(self)

        A = current_obj.point_A
        O = current_obj.point_O
        P = current_obj.point_P

        H = current_obj.point_H

        # PASTE –> odtąd KOPIOWAĆ
        # ALWAYS (A,O,P)
        plane_alpha = Plane(A,O,P)
        base = self.base_generating_class(A,O,P).solution()
        
        current_obj._append_case(base)

        current_obj.point_A_0 = base.point_A_0
        current_obj.point_B_0 = base.point_B_0
        current_obj.point_C_0 = base.point_C_0

        current_obj.point_A = base.point_A
        current_obj.point_B = base.point_B
        current_obj.point_C = base.point_C


        B = base.point_B
        C = base.point_C
        

        G = (H @ plane_alpha)('G')

        ############  upper  base

        dirHG = H - G
        distance_HG = (H.distance(G)).n(5)

        base_plane = Plane(A,B,C)

        prism=TriangularPrism(A,B,C,H).solution()
        current_obj._append_case(prism)

        current_obj.point_B = prism.point_B
        current_obj.point_C = prism.point_C
        current_obj.point_D = prism.point_D
        current_obj.point_E = prism.point_E
        current_obj.point_F = prism.point_F


        return current_obj
    
## KONIEC –> dotąd KOPIOWAĆ



## START –> odtąd KOPIOWAĆ
class SquarePrismNew(EquilateralTrianglePrism):

    @property
    def base_generating_class(self):
        return SquareOnPlane
    
    
class IsoscelesRightTrianglePrismNew(EquilateralTrianglePrism):

    @property
    def base_generating_class(self):
        return IsoscelesRightTriangleOnPlane
    