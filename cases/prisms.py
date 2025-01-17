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
from .shapes import *

from .basics import LineAndPlaneIntersection


triangle1 = {
              'A':[Point(5, 4, 3)], 

                 'B':[Point(1, 7, 2)],
             'C':[Point(3,9,5)],
              'O':[Point(7,11,2)] ,
             'N':[Point(5, 4, 3) +  0.25*(  Point(3,9,5) - Point(7,11,2)    )] ,
             'shift' : [Point(x, y, z) for x in [0] for y in [0,0.5,1,1.5,2] for z in [2,2.5,3,3.5,4,4.5,5]], # zmin 2 ymin 0
             }

triangle2 = {
              'A':[Point(5, 11, 3)], 

                 'B':[Point(1, 9, 2)],
             'C':[Point(3,4,5)],
              'O':[Point(7,4,0)] ,
             'N':[Point(5, 11, 3) +  0.25*(  Point(3,4,6) - Point(7,4,0)    )] ,
             'shift' : [Point(x, y, z) for x in [0] for y in [0,0.5,1,1.5,2] for z in [3,3.5,4,4.5,5]], # zmin 2 ymin 0
             }

hf_triangle1 = {
              'A':[Point(5, 4, 3)], 

                 'B':[Point(5, 7, 2)],
             'C':[Point(3,11,3)],
              'O':[Point(7,11,2)] ,
             'shift' : [Point(x, y, z) for x in [0] for y in [0,0.5,1,1.5,2] for z in [2,2.5,3,3.5,4,4.5,5]], # zmin 2 ymin 0
             }

hf_triangle2 = {
              'A':[Point(5, 11, 6)], 

                 'B':[Point(3, 9, 2)],
             'C':[Point(3,4,6)],
              'O':[Point(7,4,0)] ,
             'shift' : [Point(x, y, z) for x in [0] for y in [0,0.5,1,1.5,2] for z in [3,3.5,4,4.5,5]], # zmin 2 ymin 0
             }



triangle1_edge = {
              'A':[Point(5, 4, 3)], 
             'B':[Point(4, 7, 4+3)],
             'C':[Point(3,10,6)],
              'O':[Point(7,11,2)] ,
             'shift' : [Point(x, y, z) for x in [0] for y in [-2,-1,0,1,2] for z in [-2,-1,0,1,2]], # zmin 2 ymin 0
             }


triangle1_swapped = {
              'A':[Point(5-12, 4, 3-12)], 

                 'B':[Point(1-12, 7, 2-12)],
             'C':[Point(3-12,11,6-12)],
              'O':[Point(7-12,11,1-12)] ,
             'shift' : [Point(x, y, z) for x in [0] for y in [0,0.5,1,1.5,2] for z in [2,2.5,3,3.5,4,4.5,5]], # zmin 2 ymin 0
             }

triangle2_swapped = {
              'A':[Point(5-12, 11, 3-12)], 

                 'B':[Point(1-12, 9, 2-12)],
             'C':[Point(3-12,4,6-12)],
              'O':[Point(7-12,4,0-12)] ,
             'shift' : [Point(x, y, z) for x in [0] for y in [0,0.5,1,1.5,2] for z in [3,3.5,4,4.5,5]], # zmin 2 ymin 0
             }

class TriangularPrism(GeometricalCase):
    edge_plane = False


    point_packs = [ triangle1,
                    triangle2,
                   #triangle1_edge,
    ]
    #point_packs = None
#### MODE 1  
    
    point_A = [
        Point(x, y, z) for x in [5]
        for y in [4] for z in [3]
    ]

    point_B = [
        Point(x, y, z) for x in [1] for y in [9]
        for z in [2]
    ]

    point_C = [
        Point(x, y, z) for x in [3]
        for y in [11] for z in [6]
    ]

    point_O = [
        Point(x, y, z) for x in [7] for y in [11]
        for z in [2]
    ]

    
    shift = [
        Point(x, y, z) for x in [0] for y in [0,0.5,1,1.5,2]
        for z in [2,2.5,3,3.5,4,4.5,5] # zmin 2 ymin 0
   ]

#### MODE 1    
    
#### MODE 2

#     point_A = [
#         Point(x, y, z) for x in [5]
#         for y in [11] for z in [3]
#     ]

#     point_B = [
#         Point(x, y, z) for x in [1] for y in [9]
#         for z in [2]
#     ]

#     point_C = [
#         Point(x, y, z) for x in [3]
#         for y in [4] for z in [6]
#     ]

#     point_O = [
#         Point(x, y, z) for x in [7] for y in [4]
#         for z in [0]
#     ]

    
#     shift = [
#         Point(x, y, z) for x in [0] for y in [0,1,2]
#         for z in [3,4,5] #zmax 5 ymax 0
#     ]
    
##### MODE 3

#     point_A = [
#         Point(x, y, z) for x in [1, 1.5, 2, 2.5]
#         for y in [2, 2.5, 3, 3.5, 4, 4.5, 5] for z in [2, 2.5, 3, 3.5]
#     ]

#     point_B = [
#         Point(x, y, z) for x in range(4, 6) for y in range(8, 12)
#         for z in [2, 2.5, 3, 3.5]
#     ]

#     point_C = [
#         Point(x, y, z) for x in [1, 1.5, 2, 2.5]
#         for y in [13, 13.5, 14, 14.5, 15] for z in [6, 6.5, 7]
#     ]

#     point_O = [
#         Point(x, y, z) for x in range(7, 10) for y in [6, 6.5, 7, 7.5, 8.5]
#         for z in range(6, 9)
#     ]

    
#     shift = [
#         Point(x, y, z) for x in [0] for y in [0]
#         for z in [0]
#     ]

##### MODE 3

    def __init__(self,
                 point_A=None,
                 point_B=None,
                 point_C=None,
                 point_O=None,
                 point_N=None,
                 **kwargs):

        super().__init__()



        #self._assumptions = DrawingSet(*projections)

        self.point_A = point_A
        self.point_B = point_B
        self.point_C = point_C
        self.point_O = point_O
        self.point_N = point_N

        self._given_data = {
            'A': point_A,
            'B': point_B,
            'C': point_C,
            'O': point_O,
            'N': point_N,
        }


        self.add_solution_step('Assumptions',
                        [point_A, point_B, point_C, point_O, point_N])

        
        
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
        N = current_obj.point_N



        plane_alpha = Plane(A, B, C)('$\\alpha$')



        plane_beta = HorizontalPlane(B)
        plane_eta = VerticalPlane(B)

        line_h = plane_alpha.get_horizontal_line()('h')
        current_obj.line_h=line_h
        current_obj.add_solution_step('horizontal line',[line_h])

        point_P1 = line_h.p2('I')
        current_obj.P1 = point_P1
        current_obj.point_I = point_P1
        current_obj.add_solution_step('Point P1',[point_P1])

        line_f = plane_alpha.get_frontal_line()('f')
        point_P2 = line_f.p2


        beta_p1 = O-(point_P1-A)
        beta_p0 = O
        beta_p2 = O-(point_P2-A)

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

        if self.edge_plane is True:
            
            intersec_case  = D
            current_obj.add_solution_step('Vertices',[D])
            
        else:
            
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

        Q = (plane_alpha & Line(N,O))[0]('Q')
        P = (O@plane_alpha)('P')

        current_obj.point_Q = Q
        current_obj.point_P = P
        
        current_obj.add_solution_step('Vertices',
                        [D,E,F,plane_gamma])

        current_obj.add_solution_step('Prism',
                        [plane_alpha,plane_gamma,line_ad,line_be,line_cf,A,B,C,O])
 
        current_obj.add_solution_step('Prism',
                        [plane_alpha,plane_gamma,line_ad,line_be,line_cf,A,B,C,O,point_P1,N,Q,P])
        
        current_obj.append([plane_alpha,plane_gamma,line_ad,line_be,line_cf,A@HPP,B@HPP,C@HPP,point_P1@HPP,point_P1@VPP])
        current_obj._assumptions=current_obj._solution_step[-1]
        
        return current_obj

    def get_default_data(self):

        if self.__class__.point_packs is not None:
            
            points_dict=random.choice(self.__class__.point_packs)
            
            
            point_A = points_dict['A']
            point_B = points_dict['B']
            point_C = points_dict['C']
            point_O = points_dict['O']
            point_N = points_dict['N']
            shift = points_dict['shift']
        else:
            point_A = self.__class__.point_A
            point_B = self.__class__.point_B
            point_C = self.__class__.point_C
            point_O = self.__class__.point_O
            point_N = self.__class__.point_N
            shift = self.__class__.shift

        default_data_dict = {
            Symbol('A'): point_A,
            Symbol('B'): point_B,
            Symbol('C'): point_C,
            Symbol('O'): point_O,
            Symbol('N'): point_N,
            'shift': shift,
        }
        return default_data_dict
    
    def get_random_parameters(self):

        parameters_dict = super().get_random_parameters()

        point_B = parameters_dict[Symbol('B')]
        point_O = parameters_dict[Symbol('O')]
        point_A = parameters_dict[Symbol('A')]
        point_C = parameters_dict[Symbol('C')]
        point_N = parameters_dict[Symbol('N')]

        shift = parameters_dict['shift']
        parameters_dict.pop('shift')

        for point in symbols('A B C O N'):
            parameters_dict[point] = parameters_dict[point] + shift

        return parameters_dict    


class TriangularPrismHFLines(TriangularPrism):
    

    def get_random_parameters(self):

        parameters_dict=super().get_random_parameters()



        point_A=parameters_dict[Symbol('A')]
        point_B=parameters_dict[Symbol('B')] 
        point_C=parameters_dict[Symbol('C')] 

        
        parameters_dict[Symbol('C')]=Point(point_A.x,point_C.y,point_C.z)
        parameters_dict[Symbol('B')]=Point(point_B.x,point_B.y,point_A.z)

        return parameters_dict
    
class EdgeTriangularPrism(TriangularPrism):
    
    edge_plane=True
    
    shift = [
        Point(x, y, z) for x in [0] for y in [-2,-1,0,1,2] #ymax 2
        for z in [-2,-1,0,1,2] 
    ]
    

    
    def get_random_parameters(self):

        parameters_dict = super().get_random_parameters()

        point_A = parameters_dict[Symbol('A')]
        point_C = parameters_dict[Symbol('C')]

        parameters_dict[Symbol('B')] = (point_A + point_C) * 0.5 + Point(0, 0, 3)

        return parameters_dict

    
class ParallelogramPrism(GeometricalCase):
    edge_plane = False

    point_packs = [ triangle1,
                    triangle2,
                   #triangle1_edge,
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



        plane_alpha = Plane(A, B, C)('$\\alpha$')
        D = Point((A + (C - B)).coordinates)('D')



        plane_beta = HorizontalPlane(B)
        plane_eta = VerticalPlane(B)

        line_h = plane_alpha.get_horizontal_line()('h')
        current_obj.line_h=line_h
        current_obj.add_solution_step('horizontal line',[line_h])

        point_P1 = line_h.p2('I')
        current_obj.P1 = point_P1
        current_obj.add_solution_step('Point P1',[point_P1])

        current_obj.point_I = point_P1
        current_obj.add_solution_step('Point P1',[point_P1])


        line_f = plane_alpha.get_frontal_line()('f')
        point_P2 = line_f.p2


        beta_p1 = O-(point_P1-A)
        beta_p0 = O
        beta_p2 = O-(point_P2-A)

        plane_beta=Plane(beta_p0,beta_p1,beta_p2)
        
        
        #minus controls position (side) of parallel plane
        current_obj.add_solution_step('Parallel plane',[Line(beta_p0,beta_p1)('e') , Line(beta_p0,beta_p2)('f') ])
        
        E=(A@plane_beta)('E')
        F=(B@plane_beta)('F')
        G=(C@plane_beta)('G')
        H=(D@plane_beta)('H')
        
        #aux_point = A+(D-A)*2
        
        aux_point = E
        
        
        
        height_A = Line(A,aux_point)('hA')
        current_obj.add_solution_step('Perpendicular line - height',[height_A])
        
        plane_gamma=Plane(E,F,G)

        if self.edge_plane is True:
            
            intersec_case  = E
            current_obj.add_solution_step('Vertices',[E])
            
        else:
            
            intersec_case  = LineAndPlaneIntersection(beta_p1,beta_p0,beta_p2 , A,aux_point ).solution()
            current_obj._append_case(intersec_case)
        
        
        P = (O@plane_alpha)('P')

        current_obj.point_P = P
        
        # triangle_plane = Plane(A, B, C)
        # A, B, C, D, E, F = Prism.right_from_parallel_plane(triangle_plane, O)
        # plane_gamma=Plane(D,E,F)

        line_ad = Line(A, D)('a')
        line_be = Line(B, E)('b')
        line_cf = Line(C, F)('c')
        line_dh = Line(D, H)('c')

        line_ab = Line(A, B)('a')
        line_bc = Line(B, C)('b')
        line_cd = Line(C, D)('c')
        line_ad = Line(A, D)('c')



        current_obj.point_D = D
        current_obj.point_E = E
        current_obj.point_F = F
        current_obj.point_G = G
        current_obj.point_H = H

        

        
        
        current_obj.add_solution_step('Vertices',
                        [D,E,F,G,H,plane_gamma])

        current_obj.add_solution_step('Prism',
                        [plane_alpha,plane_gamma,
                         line_ad,line_be,line_cf,line_dh,A,B,C,D,E,F,G,H,line_ab,line_bc,line_cd,line_ad,point_P1,P])
        
        current_obj.append([Tetragon(A,B,C,D),plane_alpha,plane_gamma,line_ad,line_be,line_cf,A@HPP,B@HPP,C@HPP,point_P1@HPP,point_P1@VPP])
        current_obj._assumptions=current_obj._solution_step[-1]
        
        return current_obj

    def get_default_data(self):

        if self.__class__.point_packs is not None:
            
            points_dict=random.choice(self.__class__.point_packs)
            
            
            point_A = points_dict['A']
            point_B = points_dict['B']
            point_C = points_dict['C']
            point_O = points_dict['O']
            shift = points_dict['shift']
        else:
            point_A = self.__class__.point_A
            point_B = self.__class__.point_B
            point_C = self.__class__.point_C
            point_O = self.__class__.point_O
            shift = self.__class__.shift

        default_data_dict = {
            Symbol('A'): point_A,
            Symbol('B'): point_B,
            Symbol('C'): point_C,
            Symbol('O'): point_O,
            'shift': shift,
        }
        return default_data_dict
    
    def get_random_parameters(self):

        parameters_dict = super().get_random_parameters()

        point_B = parameters_dict[Symbol('B')]
        point_O = parameters_dict[Symbol('O')]
        point_A = parameters_dict[Symbol('A')]
        point_C = parameters_dict[Symbol('C')]

        shift = parameters_dict['shift']
        parameters_dict.pop('shift')

        for point in symbols('A B C O'):
            parameters_dict[point] = parameters_dict[point] + shift

        return parameters_dict    


class ParallelogramPrismHFLines(ParallelogramPrism):
    edge_plane = False


    point_packs = [ triangle1,
                    triangle2,
                   #triangle1_edge,
    ]
    

    def get_random_parameters(self):

        parameters_dict=super().get_random_parameters()



        point_A=parameters_dict[Symbol('A')]
        point_B=parameters_dict[Symbol('B')] 
        point_C=parameters_dict[Symbol('C')] 

        
        parameters_dict[Symbol('C')]=Point(point_A.x,point_C.y,point_C.z)
        parameters_dict[Symbol('B')]=Point(point_B.x,point_B.y,point_A.z)

        return parameters_dict

hf_triangle_AOP_1 = {
              'P':[Point(6, 4, 3)], 

                 'A':[Point(6, 10, -1)],
             'O':[Point(3,11,3)],
              'H':[Point(7,11,2)] ,
             'shift' : [Point(x, y, z) for x in [0] for y in [0,0.5,1,1.5,2] for z in [2,2.5,3,3.5,4,4.5,5]], # zmin 2 ymin 0
             }

hf_triangle_AOP_2 = {
              'P':[Point(5, 11, 6)], 

                 'A':[Point(3, 9, 2)],
             'O':[Point(3,4,6)],
              'H':[Point(7,4,0)] ,
             'shift' : [Point(x, y, z) for x in [0] for y in [0,0.5,1,1.5,2] for z in [3,3.5,4,4.5,5]], # zmin 2 ymin 0
             }

 
swapped_hf_triangle_AOP_1 = {
              'P':[Point(6-12, 4, 3-12)], 

                 'A':[Point(6-12, 10, -1-12)],
             'O':[Point(3-12,11,3-12)],
              'H':[Point(7-12,11,2-12)] ,
             'shift' : [Point(x, y, z) for x in [0] for y in [0,0.5,1,1.5,2] for z in [2,2.5,3,3.5,4,4.5,5]], # zmin 2 ymin 0
             }

swapped_hf_triangle_AOP_2 = {
              'P':[Point(5-12, 11, 6-12)], 

                 'A':[Point(3-12, 9, 2-12)],
             'O':[Point(3-12,4,6-12)],
              'H':[Point(7-12,4,0-12)] ,
             'shift' : [Point(x, y, z) for x in [1,2] for y in [0,0.5,1,1.5,2] for z in [2,3,3.5,4]], # zmin 2 ymin 0
             }
    
    
swapped_h_triangle_AOP_1 = {
              'P':[Point(6-12, 4, 3-12)], 

                 'A':[Point(2-12, 10, -1-12)],
             'O':[Point(3-12,11,3-12)],
              'H':[Point(7-12,11,2-12)] ,
             'shift' : [Point(x, y, z) for x in [0] for y in [-3,-2,-1
                                                              #-0.5,0,0.5,1
                                                             ] for z in [3,3.5,4,4.5,5]], # zmin 2 ymin 0
             }

swapped_h_triangle_AOP_2 = {
              'P':[Point(5-12, 11, 6-12)], 

                 'A':[Point(2-12, 10, 2-12)],
             'O':[Point(3-12,4,6-12)],
              'H':[Point(7-12,4,0-12)] ,
             'shift' : [Point(x, y, z) for x in [1,2] for y in [0,0.5,1,1.5,2] for z in [2,3,3.5,4]], # zmin 2 ymin 0
             }
    
    
class EquilateralTrianglePrism(GeometricalCase):
    """"
    #quite good data
    #point_A = [Point(x,y,z) for x in [4,5.5,5] for y in [5,5.5,6] for z in   [5.5,6,6.5]  ]

    #point_O=[Point(x,y,z) for x in [3,3.5] for y in [8,8.5,9] for z in   [3,3.5,4] ]

    #point_P = [Point(x,y,z) for x in [6,6.5,7] for y in [3,3.5]  for z in [1,1.5,2] ]

    #point_H = [Point(x,y,z) for x in range(9,11) for y in [3,3.5] for z in range(9,11) ]
    """
    
    edge_plane = False
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

    point_packs = None
    
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

        triangle_plane = Plane(A, B, C)('$\\alpha$')

        current_set = DrawingSet(*current_obj._solution_step[-1])

        line_a = Line(A, B)('a')
        line_b = Line(C, A)('b')
        #plane_alpha = Plane(A, O, P)('$\\alpha$')
        plane_alpha = Plane(P,A, O)('$\\alpha$')        

        plane_beta = HorizontalPlane(P)
        plane_eta = VerticalPlane(P)

        line_k = plane_alpha.intersection(plane_beta)[0]('a')


        line_h = plane_alpha.get_horizontal_line()('h')
        current_obj.line_h=line_h
        current_obj.add_solution_step('horizontal line',[line_h])

        point_P1 = line_h.p2('I')
        current_obj.P1 = point_P1
        current_obj.add_solution_step('Point P1',[point_P1])

        line_f = plane_alpha.get_frontal_line()('f')
        point_P2 = line_f.p2
        
        
        current_obj.P1 = point_P1
        current_obj.point_I = point_P1
        
        
        current_obj.P1 = point_P1
        line_kk = line_h('a')
        line_f = line_f

        # it creates next step of solution - lines are presented
        #current_step3d=copy.deepcopy(current_obj._solution3d_step[-1])+[(A^point_P1)('AO'),point_P1,(P^point_P1)('a')]

        #it sets the step elements
        current_obj.add_solution_step(
            'Axis of rotation', [(A ^ point_P1)('AO'), point_P1,
                                 (line_kk)('a'), point_P2, line_f])

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

        
        beta_p0 = H
        alpha_p0 = P
        
        beta_p1 = beta_p0-(O-alpha_p0)
        beta_p0 = beta_p0
        beta_p2 = beta_p0-(A-alpha_p0)

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

        if self.edge_plane is True:
            
            intersec_case  = D
            current_obj.add_solution_step('Vertices',[D])
            
        else:
            
            intersec_case  = LineAndPlaneIntersection(beta_p1,beta_p0,beta_p2 , A,aux_point ).solution()
            current_obj._append_case(intersec_case)
        
        current_obj.add_solution_step('Vertices D,E,F', [D, E, F])

        elems += [D, E, F, G]

        
        
        
        
        projections += [
            G @ HPP, G @ VPP, D @ HPP, D @ VPP, E @ HPP, E @ VPP, F @ HPP,
            F @ VPP
        ]

        line_ad = Line(A, D)('a')
        line_be = Line(B, E)('b')
        line_cf = Line(C, F)('c')
        
        
        plane_gamma = Plane(D,E,F)('$\\gamma$')
        current_obj.add_solution_step('Prism',
                        [plane_alpha,plane_gamma,line_ad,line_be,line_cf,A,B,C,O])
        
        
        
        #current_obj.append([plane_alpha,plane_gamma,line_ad,line_be,line_cf,A@HPP,B@HPP,C@HPP])
        
        current_obj._assumptions = DrawingSet(
            *current_obj.get_projections())('Solution')
        current_obj._assumptions3d = DrawingSet(*current_obj)

        current_obj.point_B = B
        current_obj.point_C = C
        current_obj.point_D = D
        current_obj.point_E = E
        current_obj.point_F = F


        return current_obj

#     def get_default_data(self):

#         point_A = self.__class__.point_A
#         point_O = self.__class__.point_O
#         point_P = self.__class__.point_P
#         point_H = self.__class__.point_H
#         shift = self.__class__.shift

#         default_data_dict = {
#             Symbol('A'): point_A,
#             Symbol('P'): point_P,
#             Symbol('O'): point_O,
#             Symbol('H'): point_H,
#             'shift':shift,
#         }
#         return default_data_dict

    
    
    
    def get_default_data(self):

        if self.__class__.point_packs is not None:
            
            points_dict=random.choice(self.__class__.point_packs)
            
            
            point_A = points_dict['A']
            point_O = points_dict['O']
            point_P = points_dict['P']
            point_H = points_dict['H']
            shift = points_dict['shift']
        else:
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

    
class EquilateralTrianglePrismHFLines(EquilateralTrianglePrism):
    point_packs = [ hf_triangle_AOP_1,
                   hf_triangle_AOP_2,
                   #triangle1_edge, 
                  ]
    
    
class EquilateralTrianglePrismHFLinesSwappedProjections(EquilateralTrianglePrism):
    point_packs = [ swapped_hf_triangle_AOP_1,
                   swapped_hf_triangle_AOP_2,
                   #triangle1_edge, 
                  ]

    
class EquilateralTrianglePrismHLineSwappedProjections(EquilateralTrianglePrism):
    point_packs = [ swapped_h_triangle_AOP_1,
                   swapped_h_triangle_AOP_2,
                   #triangle1_edge, 
                  ]

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
    
    
class IsoscelesRightTrianglePrismNew(EquilateralTrianglePrismNew):

    @property
    def base_generating_class(self):
        return IsoscelesRightTriangleOnPlane
    

    
## KONIEC –> dotąd KOPIOWAĆ


## PONIZEJ KOPIE





#_____________________

class SquarePrism(GeometricalCase):

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

    point_K = [
        Point(x, y, z) for x in range(7, 9) for y in [3, 3.5]
        for z in range(9, 11)
    ]

    def __init__(self,
                 point_A=None,
                 point_P=None,
                 point_O=None,
                 point_K=None,
                 **kwargs):

        super().__init__()

        if point_A and point_P and point_O and point_K:
            elems=[point_A, point_P, point_O, point_K]
            
            self._given_data={'A':point_A,'P':point_P,'O':point_O,'K':point_K}
        else:
            elems=[]
            self._given_data={}

#         self._assumptions = DrawingSet(*projections)

        self.point_A = point_A
        self.point_P = point_P
        self.point_O = point_O
        self.point_K = point_K

        self._given_data = {
            'A': point_A,
            'P': point_P,
            'O': point_O,
            'K': point_K
        }

        self.add_solution_step('Assumptions',elems)
    def _solution(self):
        current_obj = copy.deepcopy(self)

        A = current_obj.point_A
        O = current_obj.point_O
        P = current_obj.point_P
        K = current_obj.point_K
        S = (A @ (O ^ P))('S')  #'Srodek' podstawy

        dirPS = P - S
        dirOS = O - S
        dirAS = S - A
        square_diagonal = 2 * A.distance(S)
        #square_side =  square_diagonal / (((3)**(1/2))/2)
        print(square_diagonal)
        B = (S + dirPS / (P.distance(S)) * (square_diagonal / 2))('B')
        D = (S - dirPS / (P.distance(S)) * (square_diagonal / 2))('D')
        C = (A + 2 * dirAS)('C')

        #         line_AD=A^D
        #         line_AB=A^B
        #         line_BC=line_AD.parallel_line(P)
        #         line_AS=Line(A,S)
        #         C=line_BC.intersection(line_AS)[0]

        current_set = DrawingSet(*current_obj._solution_step[-1])

        line_a = Line(A, B)('a')
        line_b = Line(B, C)('b')
        line_c = Line(C, D)('c')
        line_d = Line(D, A)('d')
        plane_alpha = Plane(A, O, P)

        plane_beta = HorizontalPlane(P)

        line_k = plane_alpha.intersection(plane_beta)[0]

        elems = self._assumptions
        projections = []
        point_0_dict = {}
        
        S_I = (B @ line_k)('k')
        #         for point_I in [A,B,C,D,O]:

        #             S_I = (point_I @ line_k)('k')

        #             # zaimplementować w metode dla punktu
        #             dir_I_on_HPP =(point_I @ plane_beta) - S_I

        #             #display(dir_I_on_HPP.coordinates)
        #             #display((point_I @ plane_beta).distance( S_I ))
        #             #display(point_I.distance( S_I ))

        #             ratio = (point_I.distance( S_I )) /(point_I @ plane_beta).distance( S_I )

        #             I_o =(S_I+(dir_I_on_HPP)*ratio)(point_I._label+'_0')

        #             point_0_dict[str(point_I)]=I_o
        #             elems += [I_o]
        #             projections+=[I_o@HPP,I_o@VPP]



        line_kk = Line(P, S_I)('k')

#         current_obj.A0 = point_0_dict['A']
#         current_obj.B0 = point_0_dict['B']
#         current_obj.C0 = point_0_dict['C']
#         current_obj.D0 = point_0_dict['D']

        current_obj.point_A_0 = A.rotate_about(axis=line_k)('A_0')
        current_obj.point_B_0 = B.rotate_about(axis=line_k)('B_0')
        current_obj.point_C_0 = C.rotate_about(axis=line_k)('C_0')
        current_obj.point_D_0 = D.rotate_about(axis=line_k)('D_0')        
        current_obj.point_O_0 = O.rotate_about(axis=line_k)('O_0')    

        current_obj.A0 = current_obj.point_A_0
        current_obj.B0 = current_obj.point_B_0
        current_obj.C0 = current_obj.point_C_0
        current_obj.D0 = current_obj.point_D_0
        current_obj.O0 = current_obj.point_O_0
        
        #plane_beta=Plane(H,H+(B-A),H-(C-A))
        #         plane_beta=Plane(K,K+(A-P),K-(O-P))
        #         E=(A@plane_beta)('E')
        #         F=(B@plane_beta)('F')
        #         G=(C@plane_beta)('G')
        #         H=(D@plane_beta)('H')

        square_plane = Plane(A, B, C)
        A, B, C, E, F, G = Prism.right_from_parallel_plane(square_plane, K)
        
        H=(D+(E-A))('H')

        line_ae = Line(A, E)('a')
        line_bf = Line(B, F)('b')
        line_cg = Line(C, G)('c')
        line_dh = Line(D, H)('d')
        elems += [E, F, G, H, plane_alpha, line_ae, line_bf, line_cg, line_dh]

        projections += [
            line_ae @ HPP, line_ae @ VPP, line_bf @ HPP, line_bf @ VPP,
            line_cg @ HPP, line_cg @ VPP, line_dh @ HPP, line_dh @ VPP,
            E @ HPP, E @ VPP, F @ HPP, F @ VPP, G @ HPP, G @ VPP, H @ HPP,
            H @ VPP
        ]

        #print(point_0_dict)
        elems += [
            line_a,
            line_b,  #,E,F,G,H,line_s1,line_s2,line_s3,line_s4
        ]

        projections += [
            current_obj.A0 @ HPP,
            current_obj.A0 @ VPP,
            current_obj.B0 @ HPP,
            current_obj.B0 @ VPP,
            current_obj.C0 @ HPP,
            current_obj.C0 @ VPP,
            current_obj.D0 @ HPP,
            current_obj.D0 @ VPP,
            B @ HPP,
            B @ VPP,
            C @ HPP,
            C @ VPP,
            D @ HPP,
            D @ VPP,
            line_a @ HPP,
            line_a @ VPP,
            line_b @ HPP,
            line_b @ VPP,
            line_c @ HPP,
            line_c @ VPP,
            line_d @ HPP,
            line_d @ VPP,
            line_kk @ HPP,
            line_kk
            @ VPP,  #line_s1@HPP,line_s1@VPP,line_s2@HPP,line_s2@VPP,line_s3@HPP,line_s3@VPP,
            #line_s4@HPP,line_s4@VPP
        ]
        current_set += [*elems, *projections]

        current_obj._solution_step.append(current_set)
        current_obj._assumptions = DrawingSet(*elems, *projections)
        
        
        
        current_obj.point_B = B
        current_obj.point_C = C
        current_obj.point_D = D
        current_obj.point_E = E
        current_obj.point_F = F
        current_obj.point_G = G
        current_obj.point_H = H
        current_obj.add_solution_step('', [current_obj.point_B,current_obj.point_C,current_obj.point_D,current_obj.A0,current_obj.B0,current_obj.C0,current_obj.D0,current_obj.point_E,current_obj.point_F,current_obj.point_G])
        return current_obj

    def get_default_data(self):

        point_A = self.__class__.point_A
        point_O = self.__class__.point_O
        point_P = self.__class__.point_P
        point_K = self.__class__.point_K

        default_data_dict = {
            Symbol('A'): point_A,
            Symbol('P'): point_P,
            Symbol('O'): point_O,
            Symbol('K'): point_K,
        }
        return default_data_dict


class IsoscelesRightTrianglePrism(GeometricalCase):

    #quite good data
    #point_A = [Point(x,y,z) for x in [4,5.5,5] for y in [5,5.5,6] for z in   [5.5,6,6.5]  ]

    #point_O=[Point(x,y,z) for x in [3,3.5] for y in [8,8.5,9] for z in   [3,3.5,4] ]

    #point_P = [Point(x,y,z) for x in [6,6.5,7] for y in [3,3.5]  for z in [1,1.5,2] ]

    #point_H = [Point(x,y,z) for x in range(9,11) for y in [3,3.5] for z in range(9,11) ]

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

    def __init__(self,
                 point_A=None,
                 point_P=None,
                 point_O=None,
                 point_H=None,
                 **kwargs):

        super().__init__()
        self._solution_step = []
        self._solution3d_step = []

        if point_A and point_O and point_P and point_H:
            projections = (point_A @ HPP, point_O @ HPP, point_O @ VPP,
                           point_P @ VPP, point_P @ HPP, point_A @ VPP,
                           point_H @ VPP, point_H @ HPP)

        else:
            projections = []

        self._assumptions = DrawingSet(*projections)('Assumptions')
        self._assumptions3d = DrawingSet(point_A, point_O, point_P,
                                         point_H)('Assumptions')

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

        self._solution_step.append(self._assumptions)
        self._solution3d_step.append(self._assumptions3d)

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
        #triangle_side =  triangle_height / ((3**(1/2))/2)

        B = (S + dirPS / (P.distance(S)) * (triangle_height))('B')
        C = (S - dirPS / (P.distance(S)) * (triangle_height))('C')

        current_set = DrawingSet(*current_obj._solution_step[-1])

        line_a = Line(A, B)('a')
        line_b = Line(C, A)('b')
        plane_alpha = Plane(A, O, P)

        plane_beta = HorizontalPlane(P)

        line_k = plane_alpha.intersection(plane_beta)[0]('a')

        point_P1 = plane_beta.intersection(A ^ O)[0]('1')
        line_kk = (P ^ point_P1)('a')

        #current_step3d=copy.deepcopy(current_obj._solution3d_step[-1])+[(A^point_P1)('AO'),point_P1,(P^point_P1)('a')]
        current_step3d = [(A ^ point_P1)('AO'), point_P1, (P ^ point_P1)('a')]

        current_obj._solution3d_step.append(
            DrawingSet(*current_step3d)('Step 1 - axis of rotation'))
        current_obj._solution_step.append(
            DrawingSet(
                *([obj @ HPP for obj in current_step3d] +
                  [obj @ VPP
                   for obj in current_step3d]))('Step 1 - axis of rotation'))

        elems = self._assumptions
        projections = []
        point_0_dict = {}
        eps_dict = {}

        #         for point_I in [A,B,C,O]:

        #             S_I = (point_I @ line_k)('k')

        #             # zaimplementować w metode dla punktu
        #             dir_I_on_HPP =(point_I @ plane_beta) - S_I

        #             #display(dir_I_on_HPP.coordinates)
        #             #display((point_I @ plane_beta).distance( S_I ))
        #             #display(point_I.distance( S_I ))

        #             ratio = (point_I.distance( S_I )) /(point_I @ plane_beta).distance( S_I )

        #             I_o =(S_I+(dir_I_on_HPP)*ratio)(point_I._label+'_0')

        #             point_0_dict[str(point_I)]=I_o
        #             eps_dict[str(point_I)]=(I_o^(S_I-(dir_I_on_HPP)*ratio))('eps'+point_I._label)

        #             elems += [I_o]
        #             projections+=[I_o@HPP,I_o@VPP]

        #         line_kk=Line(P,S_I)('k')

        current_obj.A0 = A.rotate_about(axis=line_k)('A_0')
        current_obj.B0 = B.rotate_about(axis=line_k)('B_0')
        current_obj.C0 = C.rotate_about(axis=line_k)('C_0')
        #current_obj.D0=D.rotate_about(axis=line_k)('D_0')
        current_obj.O0 = O.rotate_about(axis=line_k)('O_0')

        #         current_obj.A0=point_0_dict['A']
        #         current_obj.B0=point_0_dict['B']
        #         current_obj.C0=point_0_dict['C']
        #         current_obj.O0=point_0_dict['O']

        A0 = current_obj.A0
        O0 = current_obj.O0

        current_obj.point_A_0 = A.rotate_about(axis=line_k)('A_0')
        current_obj.point_B_0 = B.rotate_about(axis=line_k)('B_0')
        current_obj.point_C_0 = C.rotate_about(axis=line_k)('C_0')
   
        current_obj.point_O_0 = O.rotate_about(axis=line_k)('O_0')   
        
        #current_step3d=copy.deepcopy(current_obj._solution3d_step[-1])+[eps_dict['A'],eps_dict['O']]
        
        eps_dict['A']=A
        eps_dict['O']=O
        print(eps_dict)
        current_step3d = [eps_dict['A'], eps_dict['O']]

        current_obj._solution3d_step.append(
            DrawingSet(
                *current_step3d)('Step 2 - planes of rotation for A and O'))
        current_obj._solution_step.append(
            DrawingSet(*([obj @ HPP for obj in current_step3d] +
                         [obj @ VPP for obj in current_step3d]
                         ))('Step 2 - planes of rotation for A and O'))

        #current_step3d=copy.deepcopy(current_obj._solution3d_step[-1])+[A0,O0]
        current_step3d = [A0, O0]

        current_obj._solution3d_step.append(
            DrawingSet(*current_step3d)('Step 3 - rotated A0 and O0'))
        current_obj._solution_step.append(
            DrawingSet(
                *([obj @ HPP for obj in current_step3d] +
                  [obj @ VPP
                   for obj in current_step3d]))('Step 3 - rotated A0 and O0'))

        current_step3d = [(P ^ O0)('PO0')]
        #current_step3d=copy.deepcopy(current_obj._solution3d_step[-1])+[(P^O0)('PO0')]

        current_obj._solution3d_step.append(
            DrawingSet(*current_step3d)('Step 4 - P0O0 line'))
        current_obj._solution_step.append(
            DrawingSet(*([obj @ HPP for obj in current_step3d] +
                         [obj @ VPP
                          for obj in current_step3d]))('Step 4 - P0O0 line'))

        B0 = current_obj.B0
        C0 = current_obj.C0

        #current_step3d=copy.deepcopy(current_obj._solution3d_step[-1])+[B0,C0]
        current_step3d = [B0, C0]

        current_obj._solution3d_step.append(
            DrawingSet(
                *current_step3d)('Step 5 - triangle vertices B0 and C0'))
        current_obj._solution_step.append(
            DrawingSet(*([obj @ HPP for obj in current_step3d] +
                         [obj @ VPP for obj in current_step3d]
                         ))('Step 5 - triangle vertices B0 and C0'))

        #current_step3d=copy.deepcopy(current_obj._solution3d_step[-1])+[eps_dict['B'],eps_dict['C']]
        eps_dict['B']=B
        eps_dict['C']=C
        current_step3d = [eps_dict['B'], eps_dict['C']]

        current_obj._solution3d_step.append(
            DrawingSet(
                *current_step3d)('Step 6 - planes of rotation for B and C'))
        current_obj._solution_step.append(
            DrawingSet(*([obj @ HPP for obj in current_step3d] +
                         [obj @ VPP for obj in current_step3d]
                         ))('Step 6 - planes of rotation for B and C'))

        #current_step3d=copy.deepcopy(current_obj._solution3d_step[-1])+[C,B]
        current_step3d = [C, B]

        current_obj._solution3d_step.append(
            DrawingSet(*current_step3d)('Step 7 - triangle vertices B and C'))
        current_obj._solution_step.append(
            DrawingSet(*([obj @ HPP for obj in current_step3d] +
                         [obj @ VPP for obj in current_step3d]
                         ))('Step 7 - triangle vertices B and C'))

        plane_beta = Plane(H, H + (A - P), H - (O - P))

        #current_step3d=copy.deepcopy(current_obj._solution3d_step[-1])+[((H+(A-P))^H)('e'),(H+(O-P)^H)('f')]
        current_step3d = [((H + (A - P)) ^ H)('e'), (H + (O - P) ^ H)('f')]

        current_obj._solution3d_step.append(
            DrawingSet(*current_step3d)('Step 8 - parallel plane'))
        current_obj._solution_step.append(
            DrawingSet(
                *([obj @ HPP for obj in current_step3d] +
                  [obj @ VPP
                   for obj in current_step3d]))('Step 8 - parallel plane'))

        #         D=(A@plane_beta)('D')
        #         E=(B@plane_beta)('E')
        #         F=(C@plane_beta)('F')

        triangle_plane = Plane(A, B, C)
        
        A, B, C, D, E, F = Prism.right_from_parallel_plane(triangle_plane, H)

        #current_step3d=copy.deepcopy(current_obj._solution3d_step[-1])+[(B^E)('n')]
        current_step3d = [(B ^ E)('n')]

        current_obj._solution3d_step.append(
            DrawingSet(
                *current_step3d)('Step 9 - perpendicular line (prism height)'))
        current_obj._solution_step.append(
            DrawingSet(*([obj @ HPP for obj in current_step3d] +
                         [obj @ VPP for obj in current_step3d]
                         ))('Step 9 - perpendicular line (prism height)'))

        #current_step3d=copy.deepcopy(current_obj._solution3d_step[-1])+[D,E,F]
        current_step3d = [D, E, F]

        current_obj._solution3d_step.append(
            DrawingSet(*current_step3d)('Step 10 - prims vertices'))
        current_obj._solution_step.append(
            DrawingSet(
                *([obj @ HPP for obj in current_step3d] +
                  [obj @ VPP
                   for obj in current_step3d]))('Step 10 - prims vertices'))

        line_ad = Line(A, D)('a')
        line_be = Line(B, E)('b')
        line_cf = Line(C, F)('c')

        #current_step3d=copy.deepcopy(current_obj._solution3d_step[-1])+[line_ad,line_be,line_cf,(A^B)('_'),(B^C)('_'),(A^C)('_'), (D^E)('_'),(E^F)('_'),(F^D)('_')]
        current_step3d = [
            line_ad, line_be, line_cf, (A ^ B)('_'), (B ^ C)('_'),
            (A ^ C)('_'), (D ^ E)('_'), (E ^ F)('_'), (F ^ D)('_')
        ]

        current_obj._solution3d_step.append(
            DrawingSet(*current_step3d)('Step 11 - solid'))
        current_obj._solution_step.append(
            DrawingSet(*([obj @ HPP for obj in current_step3d] +
                         [obj @ VPP
                          for obj in current_step3d]))('Step 11 - solid'))

        elems += [D, E, F, plane_alpha, line_ad, line_be, line_cf]

        projections += [
            line_ad @ HPP,
            line_ad @ VPP,
            line_be @ HPP,
            line_be @ VPP,
            line_cf @ HPP,
            line_cf @ VPP,
            D @ HPP,
            D @ VPP,
            E @ HPP,
            E @ VPP,
            F @ HPP,
            F @ VPP,
        ]

        #print(point_0_dict)
        elems += [
            line_a,
            line_b,  #,E,F,G,H,line_s1,line_s2,line_s3,line_s4
        ]

        projections += [
            current_obj.A0 @ HPP,
            current_obj.A0 @ VPP,
            current_obj.B0 @ HPP,
            current_obj.B0 @ VPP,
            current_obj.C0 @ HPP,
            current_obj.C0 @ VPP,
            B @ HPP,
            B @ VPP,
            C @ HPP,
            C @ VPP,
            line_a @ HPP,
            line_a @ VPP,
            line_b @ HPP,
            line_b @ VPP,
            line_kk @ HPP,
            line_kk
            @ VPP,  #line_s1@HPP,line_s1@VPP,line_s2@HPP,line_s2@VPP,line_s3@HPP,line_s3@VPP,
            #line_s4@HPP,line_s4@VPP
        ]
        current_set += [*elems, *projections]

        current_obj._solution_step.append(current_set)
        current_obj._assumptions = DrawingSet(*elems, *projections)
        current_obj.point_B = B
        current_obj.point_C = C
        current_obj.point_D = D
        current_obj.point_E = E
        current_obj.point_F = F

        current_obj.add_solution_step('', [current_obj.point_B,current_obj.point_D,current_obj.point_E,current_obj.point_F])
        
        return current_obj

    def present_solution(self):

        doc_model = Document(f'{self.__class__.__name__} solution')

        doc_model.packages.append(Package('booktabs'))
        doc_model.packages.append(Package('float'))
        doc_model.packages.append(Package('standalone'))
        doc_model.packages.append(Package('siunitx'))

        ReportText.set_container(doc_model)
        ReportText.set_directory('./SDAresults')

        for no, step3d in enumerate(self._solution3d_step):
            GeometryScene()

            for elem in range(no):
                self._solution3d_step[elem].plot(color='k')
                self._solution_step[elem].plot_vp(color='k').plot_hp(color='k')

            self._solution3d_step[no].plot(color='r')
            self._solution_step[no].plot_vp(color='r').plot_hp(color='r')

            with doc_model.create(Figure(position='H')) as fig:
                #path=f'./images/image{no}.png'
                #plt.savefig(path)
                #fig.add_image(path)
                fig.add_plot(width=NoEscape(r'1.4\textwidth'))

                if step3d._label is not None:
                    fig.add_caption(step3d._label)

            plt.show()

        return doc_model

    def get_default_data(self):

        point_A = self.__class__.point_A
        point_O = self.__class__.point_O
        point_P = self.__class__.point_P
        point_H = self.__class__.point_H

        default_data_dict = {
            Symbol('A'): point_A,
            Symbol('P'): point_P,
            Symbol('O'): point_O,
            Symbol('H'): point_H,
        }
        return default_data_dict

    
    
class IsoscelesRightTrianglePrism(GeometricalCase):
    """"
    #quite good data
    #point_A = [Point(x,y,z) for x in [4,5.5,5] for y in [5,5.5,6] for z in   [5.5,6,6.5]  ]

    #point_O=[Point(x,y,z) for x in [3,3.5] for y in [8,8.5,9] for z in   [3,3.5,4] ]

    #point_P = [Point(x,y,z) for x in [6,6.5,7] for y in [3,3.5]  for z in [1,1.5,2] ]

    #point_H = [Point(x,y,z) for x in range(9,11) for y in [3,3.5] for z in range(9,11) ]
    """
    
    edge_plane = False
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

    point_packs = None
    
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
        #triangle_side =  triangle_height / ((3**(1/2))/2)

        B = (S + dirPS / (P.distance(S)) * (triangle_height))('B')
        C = (S - dirPS / (P.distance(S)) * (triangle_height))('C')
        
        
        triangle_plane = Plane(A, B, C)('$\\alpha$')

        current_set = DrawingSet(*current_obj._solution_step[-1])

        line_a = Line(A, B)('a')
        line_b = Line(C, A)('b')
        plane_alpha = Plane(P,A, O)('$\\alpha$')

        plane_beta = HorizontalPlane(P)
        plane_eta = VerticalPlane(P)

        line_k = plane_alpha.intersection(plane_beta)[0]('a')


        line_h = plane_alpha.get_horizontal_line()('h')
        current_obj.line_h=line_h
        current_obj.add_solution_step('horizontal line',[line_h])

        point_P1 = line_h.p2('I')
        current_obj.P1 = point_P1
        current_obj.add_solution_step('Point P1',[point_P1])

        line_f = plane_alpha.get_frontal_line()('f')
        point_P2 = line_f.p2
        
        
        
        current_obj.P1 = point_P1
        current_obj.point_I = point_P1
        

        
        line_kk = line_h('a')
        line_f = line_f

        # it creates next step of solution - lines are presented
        #current_step3d=copy.deepcopy(current_obj._solution3d_step[-1])+[(A^point_P1)('AO'),point_P1,(P^point_P1)('a')]

        #it sets the step elements
        current_obj.add_solution_step(
            'Axis of rotation', [(A ^ point_P1)('AO'), point_P1,
                                 (line_kk)('a'), point_P2, line_f])

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
        current_obj.point_G = G

        ############  upper  base

        dirHG = H - G
        distance_HG = (H.distance(G)).n(5)

        #D = (A + dirHG/distance_HG*triangle_height)('D')
        #E = (B + dirHG/distance_HG*triangle_height)('E')
        #F = (C + dirHG/distance_HG*triangle_height)('F')

        A, B, C, D, E, F = Prism(triangle_plane,
                                 dirHG)

        
        beta_p0 = H
        alpha_p0 = P
        
        beta_p1 = beta_p0-(O-alpha_p0)
        beta_p0 = beta_p0
        beta_p2 = beta_p0-(A-alpha_p0)

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

        if self.edge_plane is True:
            
            intersec_case  = D
            current_obj.add_solution_step('Vertices',[D])
            
        else:
            
            intersec_case  = LineAndPlaneIntersection(beta_p1,beta_p0,beta_p2 , A,aux_point ).solution()
            current_obj._append_case(intersec_case)
        
        current_obj.add_solution_step('Vertices D,E,F', [D, E, F])

        elems += [D, E, F, G]

        
        
        
        
        projections += [
            G @ HPP, G @ VPP, D @ HPP, D @ VPP, E @ HPP, E @ VPP, F @ HPP,
            F @ VPP,point_P1@ HPP, point_P1 @ VPP,
        ]

        line_ad = Line(A, D)('a')
        line_be = Line(B, E)('b')
        line_cf = Line(C, F)('c')
        
        
        plane_gamma = Plane(D,E,F)('$\\gamma$')
        current_obj.add_solution_step('Prism',
                        [plane_alpha,plane_gamma,line_ad,line_be,line_cf,A,B,C,O,point_P1])
        
        
        
        #current_obj.append([plane_alpha,plane_gamma,line_ad,line_be,line_cf,A@HPP,B@HPP,C@HPP])
        
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

        if self.__class__.point_packs is not None:
            
            points_dict=random.choice(self.__class__.point_packs)
            
            
            point_A = points_dict['A']
            point_O = points_dict['O']
            point_P = points_dict['P']
            point_H = points_dict['H']
            shift = points_dict['shift']
        else:
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

    
class IsoscelesRightTrianglePrismHFLines(IsoscelesRightTrianglePrism):
    point_packs = [ hf_triangle_AOP_1,
                   hf_triangle_AOP_2,
                   #triangle1_edge, 
                  ]
    
    


class IsoscelesRightTrianglePrismHFLinesSwappedProjections(IsoscelesRightTrianglePrism):
    point_packs = [ swapped_hf_triangle_AOP_1,
                   swapped_hf_triangle_AOP_2,
                   #triangle1_edge, 
                  ]
    
    
class IsoscelesRightTrianglePrismHLineSwappedProjections(IsoscelesRightTrianglePrism):
    point_packs = [ swapped_h_triangle_AOP_1,
                   swapped_h_triangle_AOP_2,
                   #triangle1_edge, 
                  ]

    
    
class EdgeIsoscelesRightTrianglePrism(IsoscelesRightTrianglePrism):
  
    def get_random_parameters(self):

        parameters_dict = super().get_random_parameters()

        point_P = parameters_dict[Symbol('P')]
        point_O = parameters_dict[Symbol('O')]

        parameters_dict[Symbol('A')] = (point_P + point_O) * 0.5 + Point(0, 0, 5)

        return parameters_dict
    

class TruncatedTriangularPrism(GeometricalCase):

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

    point_M = [
        Point(x, y, z) for x in [1, 1.5, 2, 2.5, 3, 3.5]
        for y in [7, 7.5, 8.5, 9, 9.5] for z in range(8, 12)
    ]
    point_N = [
        Point(x, y, z) for x in [7, 7.5, 8, 8.5, 9]
        for y in [10, 10.5, 11, 11.5, 12] for z in range(2, 5)
    ]

    point_O = [
        Point(x, y, z) for x in [1, 1.5, 2, 2.5, 3, 3.5]
        for y in [13, 13.5, 14, 14.5, 15] for z in range(8, 12)
    ]

    def __init__(self,
                 point_A=None,
                 point_B=None,
                 point_C=None,
                 point_M=None,
                 point_N=None,
                 point_O=None,
                 **kwargs):

        super().__init__()

        if point_A and point_B and point_O and point_C and point_M and point_N:
            projections = (point_A @ HPP, point_B @ HPP,
                           Line(point_A @ HPP, point_B @ HPP),
                           Line(point_A @ VPP, point_B @ VPP),
                           Line(point_B @ HPP, point_C @ HPP),
                           Line(point_B @ VPP, point_C @ VPP), point_A @ VPP,
                           point_B @ VPP, point_C @ HPP, point_C @ VPP,
                           point_M @ HPP, point_M @ VPP, point_N @ HPP,
                           point_N @ VPP, point_O @ HPP, point_O @ VPP)
        else:
            projections = []

        self._assumptions = DrawingSet(*projections)

        self._point_A = point_A
        self._point_B = point_B
        self._point_C = point_C
        self._point_M = point_M
        self._point_N = point_N
        self._point_O = point_O

        self._given_data = {
            'A': point_A,
            'B': point_B,
            'C': point_C,
            'M': point_M,
            'N': point_N,
            'O': point_O
        }

        self._solution_step.append(self._assumptions)
        self.add_solution_step('Assumptions',
                               self._assumptions)
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

        A = current_obj._point_A
        B = current_obj._point_B
        C = current_obj._point_C

        M = current_obj._point_M
        N = current_obj._point_N
        O = current_obj._point_O
        current_obj.add_solution_step('Assumptions',[A,B,C,M,N,O])
        current_set = DrawingSet(*current_obj._solution_step[-1])

        plane_alpha = Plane(A, B, C)

        plane_beta = Plane(M, N, O)
        D = (plane_alpha.perpendicular_line(A) & plane_beta)[0]('D')
        E = (plane_alpha.perpendicular_line(B) & plane_beta)[0]('E')
        F = (plane_alpha.perpendicular_line(C) & plane_beta)[0]('F')
        plane_gamma = Plane(D, E, F)
        current_obj.add_solution_step('D',[D])
        current_obj.add_solution_step('E',[E])
        current_obj.add_solution_step('F',[F])
        
        line_ad = Line(A, D)('a')
        line_be = Line(B, E)('b')
        line_cf = Line(C, F)('c')

        elems = [D, E, F, plane_alpha, plane_gamma, line_ad, line_be, line_cf]

        projections = [
            line_ad @ HPP,
            line_ad @ VPP,
            line_be @ HPP,
            line_be @ VPP,
            line_cf @ HPP,
            line_cf @ VPP,
            D @ HPP,
            D @ VPP,
            E @ HPP,
            E @ VPP,
            F @ HPP,
            F @ VPP,
        ]

        current_set += [*elems, *projections]

        current_obj._solution_step.append(current_set)
        current_obj.point_D = D
        current_obj.point_E = E
        current_obj.point_F = F
        current_obj._assumptions += [DrawingSet(*elems, *projections)]

        return current_obj

    def get_default_data(self):

        point_A = self.__class__.point_A
        point_B = self.__class__.point_B
        point_C = self.__class__.point_C
        point_O = self.__class__.point_O
        point_M = self.__class__.point_M
        point_N = self.__class__.point_N

        default_data_dict = {
            Symbol('A'): point_A,
            Symbol('B'): point_B,
            Symbol('C'): point_C,
            Symbol('M'): point_M,
            Symbol('N'): point_N,
            Symbol('O'): point_O,
        }
        return default_data_dict


class TruncatedTriangularPrismByEdgePlane(TruncatedTriangularPrism):

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

    point_M = [
        Point(x, y, z) for x in [7, 7.5, 8, 8.5, 9]
        for y in [7, 7.5, 8.5, 9, 9.5] for z in range(7, 10)
    ]
    point_N = [
        Point(x, y, z) for x in [7, 7.5, 8, 8.5, 9]
        for y in [10, 10.5, 11, 11.5, 12] for z in range(2, 5)
    ]

    point_O = [
        Point(x, y, z) for x in [7, 7.5, 8, 8.5, 9]
        for y in [13, 13.5, 14, 14.5, 15] for z in range(9, 12)
    ]

    def get_random_parameters(self):

        parameters_dict = super().get_random_parameters()

        point_M = parameters_dict[Symbol('M')]
        point_O = parameters_dict[Symbol('O')]

        parameters_dict[Symbol('N')] = (point_M + point_O) * 0.5 + Point(
            3, 0, 0)

        return parameters_dict


class TruncatedTetragonalPrism(GeometricalCase):

    point_A = [
        Point(x, y, z) for x in [1, 1.5, 2, 2.5]
        for y in [2, 2.5, 3, 3.5, 4, 4.5, 5] for z in [2.5, 3, 3.5]
    ]

    point_B = [
        Point(x, y, z) for x in range(0, 2) for y in range(7, 10)
        for z in range(4, 6)
    ]

    point_C = [
        Point(x, y, z) for x in [2, 2.5, 3, 3.5]
        for y in [13.5, 14, 14.5, 15.5] for z in [6.5, 7, 7.5]
    ]

    point_Z = [
        Point(x, y, z) for x in range(4, 8) for y in range(11, 13)
        for z in [2, 2.5, 3, 3.5]
    ]

    #     point_O = [Point(x,y,z) for x in range(7,10) for y in [6,6.5,7,7.5,8.5] for z in range(6,9) ]

    point_M = [
        Point(x, y, z) for x in [1, 1.5, 2, 2.5, 3, 3.5]
        for y in [7, 7.5, 8.5, 9, 9.5] for z in range(8, 12)
    ]
    point_N = [
        Point(x, y, z) for x in [7, 7.5, 8, 8.5, 9]
        for y in [10, 10.5, 11, 11.5, 12] for z in range(2, 5)
    ]

    point_O = [
        Point(x, y, z) for x in [1, 1.5, 2, 2.5, 3, 3.5]
        for y in [13, 13.5, 14, 14.5, 15] for z in range(8, 12)
    ]

    def __init__(self,
                 point_A=None,
                 point_B=None,
                 point_C=None,
                 point_Z=None,
                 point_M=None,
                 point_N=None,
                 point_O=None,
                 **kwargs):

        super().__init__()

        if point_A and point_B and point_O and point_C and point_Z and point_M and point_N:
            projections = (point_A @ HPP, point_B @ HPP,
                           Line(point_A @ HPP, point_B @ HPP),
                           Line(point_A @ VPP, point_B @ VPP),
                           Line(point_B @ HPP, point_C @ HPP),
                           Line(point_B @ VPP, point_C @ VPP), point_A @ VPP,
                           point_B @ VPP, point_C @ HPP, point_C @ VPP,
                           point_M @ HPP, point_M @ VPP, point_N @ HPP,
                           point_N @ VPP, point_O @ HPP, point_O @ VPP,
                           point_Z @ VPP, point_Z @ HPP)
        else:
            projections = []

        self._assumptions = DrawingSet(*projections)

        self._point_A = point_A
        self._point_B = point_B
        self._point_C = point_C
        self._point_Z = point_Z
        self._point_M = point_M
        self._point_N = point_N
        self._point_O = point_O

        self._given_data = {
            'A': point_A,
            'B': point_B,
            'C': point_C,
            'M': point_M,
            'N': point_N,
            'O': point_O,
            'Z': point_Z
        }

        self._solution_step.append(self._assumptions)
        self.add_solution_step('Assumptions',[point_A, point_B, point_C, point_O])

    def _solution(self):
        current_obj = copy.deepcopy(self)

        A = current_obj._point_A
        B = current_obj._point_B
        C = current_obj._point_C
        Z = current_obj._point_Z
        M = current_obj._point_M
        N = current_obj._point_N
        O = current_obj._point_O

        current_set = DrawingSet(*current_obj._solution_step[-1])

        plane_alpha = Plane(A, B, C)
        line_z = Line(Z, Z @ HPP)
        D = line_z.intersection(plane_alpha)[0]('D')

        plane_beta = Plane(M, N, O)

        E = (plane_alpha.perpendicular_line(A) & plane_beta)[0]('E')
        F = (plane_alpha.perpendicular_line(B) & plane_beta)[0]('F')
        G = (plane_alpha.perpendicular_line(C) & plane_beta)[0]('G')
        H = (plane_alpha.perpendicular_line(D) & plane_beta)[0]('H')

        plane_gamma = Plane(E, F, G)

        line_ae = Line(A, E)('a')
        line_bf = Line(B, F)('b')
        line_cg = Line(C, G)('c')
        line_dh = Line(D, H)('d')
        plane_gamma = Plane(D, E, F)

        current_obj.point_P = (O @ plane_alpha)('P')

        elems = [E, F, G, H, line_ae, line_bf, line_cg, line_dh]

        projections = [
            line_ae @ HPP, line_ae @ VPP, line_bf @ HPP, line_bf @ VPP,
            line_cg @ HPP, line_cg @ VPP, line_dh @ HPP, line_dh @ VPP,
            E @ HPP, E @ VPP, F @ HPP, F @ VPP, G @ HPP, G @ VPP, H @ HPP,
            H @ VPP, D @ HPP, D @ VPP
        ]

        current_set += [*elems, *projections]

        current_obj.horizontal_line_cross_BC = (HorizontalPlane(A) &
                                                (B ^ C))[0]
        current_obj.frontal_line_cross_BC = (VerticalPlane(A) & (B ^ C))[0]

        current_obj.point_D = D
        current_obj.point_E = E
        current_obj.point_F = F
        current_obj.point_G = G
        current_obj.point_H = H
        current_obj._assumptions += [DrawingSet(*elems, *projections)]

        return current_obj

    def get_default_data(self):

        point_A = self.__class__.point_A
        point_B = self.__class__.point_B
        point_C = self.__class__.point_C
        point_Z = self.__class__.point_Z
        point_O = self.__class__.point_O
        point_M = self.__class__.point_M
        point_N = self.__class__.point_N

        default_data_dict = {
            Symbol('A'): point_A,
            Symbol('B'): point_B,
            Symbol('C'): point_C,
            Symbol('Z'): point_Z,
            Symbol('M'): point_M,
            Symbol('N'): point_N,
            Symbol('O'): point_O,
        }
        return default_data_dict


class TruncatedTetragonalPrismByEdgePlane(TruncatedTetragonalPrism):

    point_A = [
        Point(x, y, z) for x in [1, 1.5, 2, 2.5]
        for y in [2, 2.5, 3, 3.5, 4, 4.5, 5] for z in [2.5, 3, 3.5]
    ]

    point_B = [
        Point(x, y, z) for x in range(0, 2) for y in range(7, 10)
        for z in range(4, 6)
    ]

    point_C = [
        Point(x, y, z) for x in [2, 2.5, 3, 3.5]
        for y in [13.5, 14, 14.5, 15.5] for z in [6.5, 7, 7.5]
    ]

    point_Z = [
        Point(x, y, z) for x in range(4, 8) for y in range(11, 13)
        for z in [2, 2.5, 3, 3.5]
    ]

    point_M = [
        Point(x, y, z) for x in [7, 7.5, 8, 8.5, 9]
        for y in [7, 7.5, 8.5, 9, 9.5] for z in range(7, 10)
    ]
    point_N = [
        Point(x, y, z) for x in [7, 7.5, 8, 8.5, 9]
        for y in [10, 10.5, 11, 11.5, 12] for z in range(2, 5)
    ]

    point_O = [
        Point(x, y, z) for x in [7, 7.5, 8, 8.5, 9]
        for y in [13, 13.5, 14, 14.5, 15] for z in range(9, 12)
    ]

    def get_random_parameters(self):

        parameters_dict = super().get_random_parameters()

        point_M = parameters_dict[Symbol('M')]
        point_O = parameters_dict[Symbol('O')]

        parameters_dict[Symbol('N')] = (point_M + point_O) * 0.5 + Point(
            3, 0, 0)

        return parameters_dict


class TetragonalPrism(GeometricalCase):

    point_A = [
        Point(x, y, z) for x in [1, 1.5, 2, 2.5]
        for y in [2, 2.5, 3, 3.5, 4, 4.5, 5] for z in [2.5, 3, 3.5]
    ]

    point_B = [
        Point(x, y, z) for x in range(0, 2) for y in range(7, 10)
        for z in range(4, 6)
    ]

    point_C = [
        Point(x, y, z) for x in [2, 2.5, 3, 3.5]
        for y in [13.5, 14, 14.5, 15.5] for z in [6.5, 7, 7.5]
    ]

    point_Z = [
        Point(x, y, z) for x in [4,7] for y in [11,12]
        for z in [2, 2.5, 3, 3.5]
    ]

    point_O = [
        Point(x, y, z) for x in range(7, 10) for y in [6, 6.5, 7, 7.5, 8.5]
        for z in range(6, 9)
    ]

    def __init__(self,
                 point_A=None,
                 point_B=None,
                 point_C=None,
                 point_Z=None,
                 point_O=None,
                 **kwargs):

        super().__init__()

        if point_A and point_B and point_C and point_Z and point_O:
            projections = (
                point_A @ HPP, point_B @ HPP, point_C @ HPP, point_O @ HPP,
                point_Z @ HPP, point_A @ VPP, point_B @ VPP, point_C @ VPP,
                point_O @ VPP, point_Z @ VPP
                #Plane(point_A@HPP,point_B@HPP,point_C@HPP),Plane(point_A@VPP,point_B@VPP,point_C@VPP),
            )
        else:
            projections = []

        self._assumptions = DrawingSet(*projections)

        self._point_A = point_A
        self._point_B = point_B
        self._point_C = point_C
        self._point_Z = point_Z
        self._point_O = point_O

        self._given_data = {
            'A': point_A,
            'B': point_B,
            'C': point_C,
            'Z': point_Z,
            'O': point_O,
        }

        self._solution_step.append(self._assumptions)
        self.add_solution_step('Assumptions',
                               [point_A, point_B, point_C, point_O])

    def _solution(self):
        current_obj = copy.deepcopy(self)

        A = current_obj._point_A
        B = current_obj._point_B
        C = current_obj._point_C
        Z = current_obj._point_Z
        O = current_obj._point_O

        current_set = DrawingSet(*current_obj._solution_step[-1])

        plane_alpha = Plane(A, B, C)
        line_z = Line(Z, Z @ HPP)
        D = line_z.intersection(plane_alpha)[0]('D')

        #         plane_beta=Plane(O,O+(B-A),O+(C-A))
        #         E=(A@plane_beta)('E')
        #         F=(B@plane_beta)('F')
        #         G=(C@plane_beta)('G')
        #         H=(D@plane_beta)('H')
        #         plane_gamma=Plane(E,F,G)

        tetragonal_plane = Tetragon(A, B, C, D)
        A, B, C, D, E, F, G, H = Prism.right_from_parallel_plane(
            tetragonal_plane, O)

        line_ae = Line(A, E)('a')
        line_bf = Line(B, F)('b')
        line_cg = Line(C, G)('c')
        line_dh = Line(D, H)('d')
        elems = [E, F, G, H, line_ae, line_bf, line_cg, line_dh]

        projections = [
            line_ae @ HPP, line_ae @ VPP, line_bf @ HPP, line_bf @ VPP,
            line_cg @ HPP, line_cg @ VPP, line_dh @ HPP, line_dh @ VPP,
            E @ HPP, E @ VPP, F @ HPP, F @ VPP, G @ HPP, G @ VPP, H @ HPP,
            H @ VPP, D @ HPP, D @ VPP
        ]

        current_set += [*elems, *projections]

        current_obj._solution_step.append(current_set)

        current_obj.horizontal_line_cross_BC = (HorizontalPlane(A) &
                                                (B ^ C))[0]
        current_obj.frontal_line_cross_BC = (VerticalPlane(A) & (B ^ C))[0]

        current_obj.point_P = (O @ plane_alpha)('P')
        current_obj.point_D = D
        current_obj.point_E = E
        current_obj.point_F = F
        current_obj.point_G = G
        current_obj.point_H = H
        current_obj._assumptions += [DrawingSet(*elems, *projections)]

        return current_obj

    def get_default_data(self):

        point_A = self.__class__.point_A
        point_B = self.__class__.point_B
        point_C = self.__class__.point_C
        point_Z = self.__class__.point_Z
        point_O = self.__class__.point_O

        default_data_dict = {
            Symbol('A'): point_A,
            Symbol('B'): point_B,
            Symbol('C'): point_C,
            Symbol('Z'): point_Z,
            Symbol('O'): point_O,
        }
        return default_data_dict



    
#     def present_solution(self):

#         doc_model = Document(f'{self.__class__.__name__} solution')

#         doc_model.packages.append(Package('booktabs'))
#         doc_model.packages.append(Package('float'))
#         doc_model.packages.append(Package('standalone'))
#         doc_model.packages.append(Package('siunitx'))

#         #ReportText.set_container(doc_model)
#         #ReportText.set_directory('./SDAresults')

#         for no, step3d in enumerate(self._solution3d_step):
#             GeometryScene()

#             for elem in range(no):
#                 self._solution3d_step[elem].plot(color='k')
#                 self._solution_step[elem].plot_vp(color='k').plot_hp(color='k')

#             self._solution3d_step[no].plot(color='r')
#             self._solution_step[no].plot_vp(color='r').plot_hp(color='r')

#             with doc_model.create(Figure(position='H')) as fig:
#                 #path=f'./images/image{no}.png'
#                 #plt.savefig(path)
#                 #fig.add_image(path)
#                 fig.add_plot(width=NoEscape(r'1.4\textwidth'))

#                 if step3d._label is not None:
#                     fig.add_caption(step3d._label)

#             plt.show()

#         return doc_model
    
#     def get_default_data(self):

#         point_A = self.__class__.point_A
#         point_B = self.__class__.point_B
#         point_C = self.__class__.point_C
#         point_O = self.__class__.point_O

#         default_data_dict = {
#             Symbol('A'): point_A,
#             Symbol('B'): point_B,
#             Symbol('C'): point_C,
#             Symbol('O'): point_O,
#         }
#         return default_data_dict


class TiltedTetragonalPrism(TetragonalPrism):

    point_A = [
        Point(x, y, z) for x in range(2, 4) for y in range(7, 12)
        for z in [2.5, 3, 3.5]
    ]

    point_B = [
        Point(x, y, z) for x in range(0, 2) for y in range(13, 15)
        for z in range(6, 8)
    ]

    point_C = [
        Point(x, y, z) for x in [2, 2.5, 3, 3.5]
        for y in [13.5, 14, 14.5, 15.5] for z in [6.5, 7, 7.5]
    ]

    point_Z = [
        Point(x, y, z) for x in range(4, 8) for y in range(11, 13)
        for z in [2, 2.5, 3, 3.5]
    ]

    point_O = [
        Point(x, y, z) for x in range(7, 10) for y in [6, 6.5, 7, 7.5, 8.5]
        for z in range(9, 12)
    ]
    shift = [
        Point(x, y, z) for x in [-1, -0.5, 0, 0.5, 1]
        for y in [-2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2]
        for z in [-1, -0.5, 0, 0.5, 1]
    ]

    def __init__(self,
                 point_A=None,
                 point_B=None,
                 point_C=None,
                 point_Z=None,
                 point_O=None,
                 *args,
                 **kwargs):

        super().__init__()

        if point_A and point_B and point_C and point_Z and point_O:
            projections = (point_A @ HPP, point_B @ HPP, point_B @ VPP,
                           point_C @ VPP, point_C @ HPP, point_A @ VPP,
                           point_Z @ VPP, point_Z @ HPP, point_O @ VPP,
                           point_O @ HPP)
        else:
            projections = []

        self._point_A = point_A
        self._point_B = point_B
        self._point_C = point_C
        self._point_Z = point_Z
        self._point_O = point_O

        self._given_data = {
            'A': point_A,
            'B': point_B,
            'C': point_C,
            'Z': point_Z,
            'O': point_O
        }

        self.add_solution_step('Assumptions',
                               [point_A, point_B, point_C, point_Z, point_O])
        self._assumptions3d = DrawingSet(point_A, point_B, point_C, point_Z,
                                         point_O)('Assumptions')
        self._assumptions = DrawingSet(*projections)

    def _solution(self):

        current_obj = copy.deepcopy(self)

        A = current_obj._point_A
        B = current_obj._point_B
        C = current_obj._point_C
        Z = current_obj._point_Z
        O = current_obj._point_O

        current_set = DrawingSet(*current_obj._solution_step[-1])

        plane_alpha = Plane(A, B, C)
        line_z = Line(Z, Z @ HPP)
        D = line_z.intersection(plane_alpha)[0]('D')

        #         plane_beta=Plane(O,O+(B-A),O+(C-A))
        #         E=(A@plane_beta)('E')
        #         F=(B@plane_beta)('F')
        #         G=(C@plane_beta)('G')
        #         H=(D@plane_beta)('H')
        #         plane_gamma=Plane(E,F,G)

        tetragonal_plane = Tetragon(A, B, C, D)
        A, B, C, D, E, F, G, H = TetraPrism.right_from_parallel_plane(
            tetragonal_plane, O)
        self.add_solution_step('Prism', [A, B, C, Z, O, E, F, G, H])
        line_ae = Line(A, E)('a')
        line_bf = Line(B, F)('b')
        line_cg = Line(C, G)('c')
        line_dh = Line(D, H)('d')
        elems = [E, F, G, H, line_ae, line_bf, line_cg, line_dh]

        projections = [
            line_ae @ HPP, line_ae @ VPP, line_bf @ HPP, line_bf @ VPP,
            line_cg @ HPP, line_cg @ VPP, line_dh @ HPP, line_dh @ VPP,
            E @ HPP, E @ VPP, F @ HPP, F @ VPP, G @ HPP, G @ VPP, H @ HPP,
            H @ VPP, D @ HPP, D @ VPP
        ]

        current_set += [*elems, *projections]

        current_obj._solution_step.append(current_set)

        current_obj.horizontal_line_cross_BC = (HorizontalPlane(A) &
                                                (B ^ C))[0]
        current_obj.frontal_line_cross_BC = (VerticalPlane(A) & (B ^ C))[0]

        current_obj.point_P = (O @ plane_alpha)('P')
        current_obj.point_D = D
        current_obj.point_E = E
        current_obj.point_F = F
        current_obj.point_G = G
        current_obj.point_H = H
        current_obj._assumptions += [DrawingSet(*elems, *projections)]

        return current_obj

    def get_random_parameters(self):

        parameters_dict = super().get_random_parameters()

        point_A = parameters_dict[Symbol('A')]
        point_B = parameters_dict[Symbol('B')]

        parameters_dict[Symbol('Z')] = (point_A + point_B) * 0.5 + Point(
            5, 0, 0)
        point_Z = parameters_dict[Symbol('Z')]
        parameters_dict[Symbol('C')] = (point_B + point_Z) * 0.5 + Point(
            -1, 0, 0)
        return parameters_dict




# class TriangularPrismHFLines(TriangularPrism):
#     point_A = [Point(x,y,z) for x in [1,1.5,2,2.5] for y in [4,4.5,5] for z in [2,2.5,3,3.5]  ]

#     point_B = [Point(x,y,z) for x in [3,3.5,4,4.5,5] for y in range(9,12) for z in [5,5.5,6,6.5,7] ]


#     point_C=[Point(x,y,z) for x in [4,4.5,5,5.5,6] for y in [13,13.5,14,14.5,15] for z in [1,1.5,2,2.5] ]


#     point_O=[Point(x,y,z) for x in range(9,12) for y in [6,6.5,7,7.5,8.5] for z in range(9,12) ]

#     shift = [
#         Point(x, y, z) for x in [-1, -0.5, 0, 0.5, 1]
#         for y in [0, 0.5]
#         for z in [-1, -0.5, 0, 0.5, 1]
#     ]
    

#     def get_random_parameters(self):

#         parameters_dict=super().get_random_parameters()



#         point_A=parameters_dict[Symbol('A')]
#         point_B=parameters_dict[Symbol('B')] 
#         point_C=parameters_dict[Symbol('C')] 

        
#         parameters_dict[Symbol('C')]=Point(point_A.x,point_C.y,point_C.z)
#         parameters_dict[Symbol('B')]=Point(point_B.x,point_B.y,point_A.z)

#         return parameters_dict
    
class TriangularPrismSwappedProjections(TriangularPrism):
    shift = [
        Point(x, y, z) for x in [-11, -10.5, -10, -9.5, -9, -8.5, -8]
        for y in [0] for z in [-13, -12, -11, -10.5, -10, -9.5, -9]
    ]

class ParallelogramPrismSwappedProjections(ParallelogramPrism):
    point_packs = [ triangle1_swapped,
                    triangle2_swapped,

    ]



class TruncatedParallelogramPrism(GeometricalCase):

    point_A = [
        Point(x, y, z) for x in [3, 3.5, 4, 4.5]
        for y in [2, 2.5, 3, 3.5, 4, 4.5, 5] for z in range(0, 1)
    ]

    point_B = [
        Point(x, y, z) for x in range(0, 2) for y in range(7, 10)
        for z in range(2, 3)
    ]

    point_C = [
        Point(x, y, z) for x in range(4, 6) for y in [11.5, 12, 12.5, 13.5]
        for z in range(5, 6)
    ]

    point_O = [
        Point(x, y, z) for x in range(4, 7) for y in [1, 1.5, 2, 2.5]
        for z in range(2, 4)
    ]

    point_M = [
        Point(x, y, z) for x in [4, 5, 6] for y in [7, 7.5, 8.5, 9, 9.5]
        for z in [4, 5, 6, 7]
    ]

    point_N = [
        Point(x, y, z) for x in [7, 7.5, 8, 8.5, 9]
        for y in [10, 10.5, 11, 11.5, 12] for z in range(2, 4)
    ]

    shift = [
        Point(x, y, z) for x in [-1, -0.5, 0, 0.5, 1]
        for y in [-2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2]
        for z in [-1, -0.5, 0, 0.5, 1]
    ]

    def __init__(self,
                 point_A=None,
                 point_B=None,
                 point_C=None,
                 point_M=None,
                 point_N=None,
                 point_O=None,
                 *args,
                 **kwargs):

        super().__init__()

        if point_A and point_B and point_O and point_C and point_M and point_N:
            projections = (point_A @ HPP, point_B @ HPP,
                           Line(point_A @ HPP, point_B @ HPP),
                           Line(point_A @ VPP, point_B @ VPP),
                           Line(point_B @ HPP, point_C @ HPP),
                           Line(point_B @ VPP, point_C @ VPP), point_A @ VPP,
                           point_B @ VPP, point_C @ HPP, point_C @ VPP,
                           point_M @ HPP, point_M @ VPP, point_N @ HPP,
                           point_N @ VPP, point_O @ HPP, point_O @ VPP)
        else:
            projections = []

        self._assumptions = DrawingSet(*projections)

        self._point_A = point_A
        self._point_B = point_B
        self._point_C = point_C
        self._point_M = point_M
        self._point_N = point_N
        self._point_O = point_O

        self._given_data = {
            'A': point_A,
            'B': point_B,
            'C': point_C,
            'M': point_M,
            'N': point_N,
            'O': point_O
        }

        self.add_solution_step('Assumptions',
                               [point_A, point_B, point_C, point_O])
        self._assumptions3d = DrawingSet(point_A, point_B, point_C,
                                         point_O)('Assumptions')
        self._assumptions = DrawingSet(*projections)

    def _solution(self):
        current_obj = copy.deepcopy(self)

        A = current_obj._point_A
        B = current_obj._point_B
        C = current_obj._point_C

        M = current_obj._point_M
        N = current_obj._point_N
        O = current_obj._point_O

        plane_alpha = Plane(A, B, C)

        point_P1 = (HorizontalPlane(A) & (B ^ C))[0]('1')
        point_P2 = (VerticalPlane(A) & (B ^ C))[0]('2')

        current_obj.horizontal_line_cross_BC = point_P1
        current_obj.frontal_line_cross_BC = point_P2

#         self.add_solution_step('Horizontal and forntal lines',
#                                [point_P1, point_P2])

        D = (A + (C - B))('D')

        current_obj.add_solution_step('Vertices A,B,C,D', [A, B, C, D])

        plane_beta = Plane(M, N, O)

        E = (plane_alpha.perpendicular_line(A) & plane_beta)[0]('E')
        F = (plane_alpha.perpendicular_line(B) & plane_beta)[0]('F')
        G = (plane_alpha.perpendicular_line(C) & plane_beta)[0]('G')
        H = (plane_alpha.perpendicular_line(D) & plane_beta)[0]('H')

        plane_gamma = Plane(E, F, G)

        #plane_aux = Plane(A,F,A+Point(5,0,0))

        #point_P3 = (   ((O-(point_P1-A))^O)('h_H') & plane_aux  )[0]('3')
        #point_P4 = (   ((O-(point_P2-A))^O)('f_H') & plane_aux  )[0]('4')

        current_obj.add_solution_step('Piercing points', [E, F, G])

        line_ae = Line(A, E)('a')
        line_bf = Line(B, F)('b')
        line_cg = Line(C, G)('c')
        line_dh = Line(D, H)('d')
        elems = [E, F, G, H, line_ae, line_bf, line_cg, line_dh]

        current_obj.add_solution_step('Verticices E,F,G,H', [E, F, G, H])

        projections = [
            line_ae @ HPP, line_ae @ VPP, line_bf @ HPP, line_bf @ VPP,
            line_cg @ HPP, line_cg @ VPP, line_dh @ HPP, line_dh @ VPP,
            E @ HPP, E @ VPP, F @ HPP, F @ VPP, G @ HPP, G @ VPP, H @ HPP,
            H @ VPP, D @ HPP, D @ VPP
        ]

        current_obj.point_P = (O @ plane_alpha)('P')
        current_obj.point_D = D
        current_obj.point_E = E
        current_obj.point_F = F
        current_obj.point_G = G
        current_obj.point_H = H
        current_obj._assumptions += [DrawingSet(*elems, *projections)]

        return current_obj

    def get_default_data(self):

        point_A = self.__class__.point_A
        point_B = self.__class__.point_B
        point_C = self.__class__.point_C
        point_M = self.__class__.point_M
        point_N = self.__class__.point_N
        point_O = self.__class__.point_O
        shift = self.shift

        default_data_dict = {
            Symbol('A'): point_A,
            Symbol('B'): point_B,
            Symbol('C'): point_C,
            Symbol('M'): point_M,
            Symbol('N'): point_N,
            Symbol('O'): point_O,
            'shift': shift,
        }
        return default_data_dict




class TruncatedParallelogramPrismByEdgePlane(TruncatedParallelogramPrism):
    def get_random_parameters(self):

        parameters_dict = super().get_random_parameters()

        #point_B=parameters_dict[Symbol('B')]
        point_M = parameters_dict[Symbol('M')]
        point_N = parameters_dict[Symbol('N')]
        point_O = parameters_dict[Symbol('O')]
        #point_A=parameters_dict[Symbol('A')]
        #point_C=parameters_dict[Symbol('C')]

        parameters_dict[Symbol('N')] = 0.5 * (point_M + point_O) + Point(
            3, 0, 0)

        return parameters_dict


class TruncatedParallelogramPrismByEdgePlaneSwappedProjections(
        TruncatedParallelogramPrismByEdgePlane):
    shift = [
        Point(x, y, z) for x in [-11, -10.5, -10, -9.5, -9, -8.5, -8]
        for y in [0] for z in [-13, -12, -11, -10.5, -10, -9.5, -9]
    ]


class VerticalTiltedTetragonalPrism(TetragonalPrism):

    point_A = [
        Point(x, y, z) for x in range(2, 4) for y in range(7, 12)
        for z in [2.5, 3, 3.5]
    ]

    point_B = [
        Point(x, y, z) for x in range(0, 2) for y in range(13, 15)
        for z in range(6, 8)
    ]

    point_C = [
        Point(x, y, z) for x in [2, 2.5, 3, 3.5]
        for y in [13.5, 14, 14.5, 15.5] for z in [6.5, 7, 7.5]
    ]

    point_Z = [
        Point(x, y, z) for x in range(4, 8) for y in range(11, 13)
        for z in [2, 2.5, 3, 3.5]
    ]

    point_O = [
        Point(x, y, z) for x in range(7, 10) for y in [6, 6.5, 7, 7.5, 8.5]
        for z in range(9, 12)
    ]
    shift = [
        Point(x, y, z) for x in [-1, -0.5, 0, 0.5, 1]
        for y in [-2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2]
        for z in [-1, -0.5, 0, 0.5, 1]
    ]

    def __init__(self,
                 point_A=None,
                 point_B=None,
                 point_C=None,
                 point_Z=None,
                 point_O=None,
                 *args,
                 **kwargs):

        super().__init__()

        if point_A and point_B and point_C and point_Z and point_O:
            projections = (point_A @ HPP, point_B @ HPP, point_B @ VPP,
                           point_C @ VPP, point_C @ HPP, point_A @ VPP,
                           point_Z @ VPP, point_Z @ HPP, point_O @ VPP,
                           point_O @ HPP)
        else:
            projections = []

        self._point_A = point_A
        self._point_B = point_B
        self._point_C = point_C
        self._point_Z = point_Z
        self._point_O = point_O

        self._given_data = {
            'A': point_A,
            'B': point_B,
            'C': point_C,
            'Z': point_Z,
            'O': point_O
        }

        self.add_solution_step('Assumptions',
                               [point_A, point_B, point_C, point_Z, point_O])
        self._assumptions3d = DrawingSet(point_A, point_B, point_C, point_Z,
                                         point_O)('Assumptions')
        self._assumptions = DrawingSet(*projections)

    def _solution(self):

        current_obj = copy.deepcopy(self)

        A = current_obj._point_A
        B = current_obj._point_B
        C = current_obj._point_C
        Z = current_obj._point_Z
        O = current_obj._point_O

        current_set = DrawingSet(*current_obj._solution_step[-1])

        plane_alpha = Plane(A, B, C)
        line_z = Line(Z, Z @ HPP)
        D = (A + (C-B)) ('D')

        #         plane_beta=Plane(O,O+(B-A),O+(C-A))
        #         E=(A@plane_beta)('E')
        #         F=(B@plane_beta)('F')
        #         G=(C@plane_beta)('G')
        #         H=(D@plane_beta)('H')
        #         plane_gamma=Plane(E,F,G)

        tetragonal_plane = Tetragon(A, B, C, D)
        A, B, C, D, E, F, G, H = TetraPrism.right_from_parallel_plane(
            tetragonal_plane, O)
        current_obj.add_solution_step('Prism', [A, B, C, D, O, E, F, G, H])
        line_ae = Line(A, E)('a')
        line_bf = Line(B, F)('b')
        line_cg = Line(C, G)('c')
        line_dh = Line(D, H)('d')
        elems = [E, F, G, H, line_ae, line_bf, line_cg, line_dh]

        projections = [
            line_ae @ HPP, line_ae @ VPP, line_bf @ HPP, line_bf @ VPP,
            line_cg @ HPP, line_cg @ VPP, line_dh @ HPP, line_dh @ VPP,
            E @ HPP, E @ VPP, F @ HPP, F @ VPP, G @ HPP, G @ VPP, H @ HPP,
            H @ VPP, D @ HPP, D @ VPP
        ]

        current_set += [*elems, *projections]

        current_obj._solution_step.append(current_set)

        current_obj.horizontal_line_cross_BC = (HorizontalPlane(A) &
                                                (B ^ C))[0]('I')
        current_obj.frontal_line_cross_BC = (VerticalPlane(A) & (B ^ C))[0]('J')
        I = current_obj.horizontal_line_cross_BC
        J = current_obj.frontal_line_cross_BC
        current_obj.add_solution_step('Frontal & Horizontal', [I, J])
        current_obj.point_P = (O @ plane_alpha)('P')
        current_obj.point_D = D
        current_obj.point_E = E
        current_obj.point_F = F
        current_obj.point_G = G
        current_obj.point_H = H

        current_obj._assumptions = DrawingSet(
            *current_obj.get_projections())('Solution')
        current_obj._assumptions3d = DrawingSet(*current_obj)

        return current_obj

    def get_random_parameters(self):

        parameters_dict = super().get_random_parameters()

        point_A = parameters_dict[Symbol('A')]
        point_B = parameters_dict[Symbol('B')]

        parameters_dict[Symbol('Z')] = (point_A + point_B) * 0.5 + Point(
            5, 0, 0)
        point_Z = parameters_dict[Symbol('Z')]
        parameters_dict[Symbol('C')] = (point_B + point_Z) * 0.5 + Point(
            -1, 0, 0)
        return parameters_dict


class HorizontalTiltedTetragonalPrism(TetragonalPrism):

    point_A = [
        Point(x, y, z) for x in range(2, 4) for y in range(13, 15)
        for z in [2.5, 3, 3.5]
    ]

    point_B = [
        Point(x, y, z) for x in range(0, 2) for y in range(7, 12)
        for z in range(4, 6)
    ]

    point_C = [
        Point(x, y, z) for x in [2, 2.5, 3, 3.5]
        for y in [13.5, 14, 14.5, 15.5] for z in [6.5, 7, 7.5]
    ]

    point_Z = [
        Point(x, y, z) for x in range(4, 8) for y in range(11, 13)
        for z in [2, 2.5, 3, 3.5]
    ]

    point_O = [
        Point(x, y, z) for x in range(7, 10) for y in [6, 6.5, 7, 7.5, 8.5]
        for z in range(9, 12)
    ]
    shift = [
        Point(x, y, z) for x in [-1, -0.5, 0, 0.5, 1]
        for y in [-2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2]
        for z in [-1, -0.5, 0, 0.5, 1]
    ]

    def __init__(self,
                 point_A=None,
                 point_B=None,
                 point_C=None,
                 point_Z=None,
                 point_O=None,
                 *args,
                 **kwargs):

        super().__init__()

        if point_A and point_B and point_C and point_Z and point_O:
            projections = (point_A @ HPP, point_B @ HPP, point_B @ VPP,
                           point_C @ VPP, point_C @ HPP, point_A @ VPP,
                           point_Z @ VPP, point_Z @ HPP, point_O @ VPP,
                           point_O @ HPP)
        else:
            projections = []

        self._point_A = point_A
        self._point_B = point_B
        self._point_C = point_C
        self._point_Z = point_Z
        self._point_O = point_O

        self._given_data = {
            'A': point_A,
            'B': point_B,
            'C': point_C,
            'Z': point_Z,
            'O': point_O
        }

        self.add_solution_step('Assumptions',
                               [point_A, point_B, point_C, point_Z, point_O])
        self._assumptions3d = DrawingSet(point_A, point_B, point_C, point_Z,
                                         point_O)('Assumptions')
        self._assumptions = DrawingSet(*projections)

    def _solution(self):


        current_obj = copy.deepcopy(self)

        A = current_obj._point_A
        B = current_obj._point_B
        C = current_obj._point_C
        Z = current_obj._point_Z
        O = current_obj._point_O

        current_set = DrawingSet(*current_obj._solution_step[-1])

        plane_alpha = Plane(A, B, C)
        line_z = Line(Z, Z @ HPP)
        #D=line_z.intersection(plane_alpha)[0]('D')
        D = Z('D')

        #         plane_beta=Plane(O,O+(B-A),O+(C-A))
        #         E=(A@plane_beta)('E')
        #         F=(B@plane_beta)('F')
        #         G=(C@plane_beta)('G')
        #         H=(D@plane_beta)('H')
        #         plane_gamma=Plane(E,F,G)

        tetragonal_plane = Plane(A, B, C)
        #GeometryScene()
        #current_set.plot_hp().plot_vp()
        #A,B,C,D,E,F,G,H = TetraPrism.right_from_parallel_plane(tetragonal_plane, O)

        T = (O @ tetragonal_plane)('T')

        ############  upper  base

        dirRT = O - T

        #D = (A + dirHG/distance_HG*triangle_height)('D')
        #E = (B + dirHG/distance_HG*triangle_height)('E')
        #F = (C + dirHG/distance_HG*triangle_height)('F')

        A, B, C, E, F, G = Prism(tetragonal_plane, dirRT)

        E = E('E')
        F = F('F')
        G = G('G')
        H = (D + (E - A))('H')

        current_obj.add_solution_step('Prism', [A, B, C, Z, O, E, F, G, H])
        line_ae = Line(A, E)('a')
        line_bf = Line(B, F)('b')
        line_cg = Line(C, G)('c')
        line_dh = Line(D, H)('d')
        elems = [E, F, G, H, line_ae, line_bf, line_cg, line_dh]

        projections = [
            line_ae @ HPP, line_ae @ VPP, line_bf @ HPP, line_bf @ VPP,
            line_cg @ HPP, line_cg @ VPP, line_dh @ HPP, line_dh @ VPP,
            E @ HPP, E @ VPP, F @ HPP, F @ VPP, G @ HPP, G @ VPP, H @ HPP,
            H @ VPP, D @ HPP, D @ VPP
        ]

        current_set += [*elems, *projections]

        current_obj._solution_step.append(current_set)

        current_obj.horizontal_line_cross_BC = (HorizontalPlane(A) &
                                                (B ^ C))[0]
        current_obj.frontal_line_cross_BC = (VerticalPlane(A) & (B ^ C))[0]
        I = current_obj.horizontal_line_cross_BC
        J = current_obj.frontal_line_cross_BC
        current_obj.add_solution_step('Frontal & Horizontal', [I, J])
        current_obj.point_P = (O @ plane_alpha)('P')
        current_obj.point_D = D
        current_obj.point_E = E
        current_obj.point_F = F
        current_obj.point_G = G
        current_obj.point_H = H

        current_obj._assumptions = DrawingSet(
            *current_obj.get_projections())('Solution')
        current_obj._assumptions3d = DrawingSet(*current_obj)


        return current_obj

    def get_random_parameters(self):

        parameters_dict = super().get_random_parameters()

        point_A = parameters_dict[Symbol('A')]
        point_B = parameters_dict[Symbol('B')]

        parameters_dict[Symbol('Z')] = (point_A + point_B) * 0.5 + Point(
            0, 0, 5)
        point_Z = parameters_dict[Symbol('Z')]
        parameters_dict[Symbol('C')] = (point_B + point_Z) * 0.5 + Point(
            0, 0, -1)
        return parameters_dict



class GivenHeightEquilateralTrianglePrism(GeometricalCase):

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
        Point(x, y, z) for x in [-1, 0, 0.5, 1, 1.5, 2] for y in [-1, -.5, 0]
        for z in [-2, -1.5, -1, -0.5, 0]
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

        self._point_A = point_A
        self._point_P = point_P
        self._point_O = point_O
        self._point_H = point_H

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

        H = current_obj._point_H

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

        A0 = A.rotate_about(axis=line_kk)('A_0')
        current_obj.A0 = A0

        ### Step 2 #####
        ###  plane of rotation of A ####

        current_obj.add_solution_step('Point A rotation', [A0])

        #### Step 3 ####
        ### rotated point A0 of A #####

        B0 = B.rotate_about(axis=line_kk)('B_0')
        current_obj.B0 = B0

        current_obj.add_solution_step('Point B rotation', [B0])

        #### Step 4 ####
        ### postion of B0 (based on triangle geometry) #####

        C0 = C.rotate_about(axis=line_kk)('C_0')
        current_obj.C0 = C0
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

        #D = (A + dirHG/distance_HG*triangle_height)('D')S
        #E = (B + dirHG/distance_HG*triangle_height)('E')
        #F = (C + dirHG/distance_HG*triangle_height)('F')

        A, B, C, D, E, F = Prism(triangle_plane,
                                 dirHG / distance_HG * triangle_height)

        current_obj.add_solution_step('Vertices D,E,F', [D, E, F])

        elems += [D, E, F, G]

        projections += [
            G @ HPP, G @ VPP, D @ HPP, D @ VPP, E @ HPP, E @ VPP, F @ HPP,
            F @ VPP
        ]

        line_ab=Line(A,B)('|AB|')
        line_bc=Line(B,C)('|BC|')
        line_ca=Line(C,A)('|CA|')
        line_eb=Line(E,B)('|EB|')
        line_da=Line(D,A)('|DA|')
        line_fc=Line(F,C)('|FC|')
        line_de=Line(D,E)('|DE|')
        line_ef=Line(E,F)('|EF|')
        line_fd=Line(F,D)('|FD|')
        current_obj.add_solution_step('Lines implementation', [line_ab, line_bc, line_ca, like_eb, line_da, line_fc])
        
        
        current_obj._assumptions = DrawingSet(
            *current_obj.get_projections())('Solution')
        current_obj._assumptions3d = DrawingSet(*current_obj)

        current_obj._point_B = B
        current_obj._point_C = C
        current_obj.point_D = D
        current_obj.point_E = E
        current_obj.point_F = F

        return current_obj

    def present_solution(self):

        doc_model = Document(f'{self.__class__.__name__} solution')

        doc_model.packages.append(Package('booktabs'))
        doc_model.packages.append(Package('float'))
        doc_model.packages.append(Package('standalone'))
        doc_model.packages.append(Package('siunitx'))

        #ReportText.set_container(doc_model)
        #ReportText.set_directory('./SDAresults')

        for no, step3d in enumerate(self._solution3d_step):
            GeometryScene()

            for elem in range(no):
                self._solution3d_step[elem].plot(color='k')
                self._solution_step[elem].plot_vp(color='k').plot_hp(color='k')

            self._solution3d_step[no].plot(color='r')
            self._solution_step[no].plot_vp(color='r').plot_hp(color='r')

            with doc_model.create(Figure(position='H')) as fig:
                #path=f'./images/image{no}.png'
                #plt.savefig(path)
                #fig.add_image(path)
                fig.add_plot(width=NoEscape(r'1.4\textwidth'))

                if step3d._label is not None:
                    fig.add_caption(step3d._label)

            plt.show()

        return doc_model

    def get_default_data(self):

        point_A = self.__class__.point_A
        point_O = self.__class__.point_O
        point_P = self.__class__.point_P
        point_H = self.__class__.point_H

        shift = self.shift

        default_data_dict = {
            Symbol('A'): point_A,
            Symbol('P'): point_P,
            Symbol('O'): point_O,
            Symbol('H'): point_H,
            'shift': shift
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


    
class GivenHeightIsoscelesRightTrianglePrism(GeometricalCase):

    point_A = [
        Point(x, y, z) for x in [6, 6.5] for y in [7, 7.5, 8]
        for z in [8, 8.5]
    ]

    point_O = [
        Point(x, y, z) for x in [3, 3.5, 4, 4.5] for y in [2, 2.5, 3]
        for z in [2, 2.5, 3, 4, 5]
    ]

    point_P = [
        Point(x, y, z) for x in [2, 2.5] for y in [10, 10.5, 11]
        for z in [4, 5, 6]
    ]

    point_H = [
        Point(x, y, z) for x in [9, 9.5, 10] for y in [2, 2.5, 3]
        for z in range(6, 8)
    ]

    shift = [
        Point(x, y, z) for x in [-3, -2.5, -2, -1, -0.5, 0, 0.5, 1]
        for y in [-1,-0.5,0,0.5] for z in [-2, -1.5, -1, -0.5, 0]
    ]

    def __init__(self,
                 point_A=None,
                 point_P=None,
                 point_O=None,
                 point_H=None,
                 *args,
                 **kwargs):

        super().__init__()

        if point_A and point_O and point_P and point_H:
            projections = (point_A @ HPP, point_O @ HPP, point_O @ VPP,
                           point_P @ VPP, point_P @ HPP, point_A @ VPP,
                           point_H @ VPP, point_H @ HPP)

        else:
            projections = []

        # it creates first step of solution
#         self.add_solution_step('',
#                                [point_A, point_O, point_P, point_H])
#         self._assumptions3d = DrawingSet(point_A, point_O, point_P,
#                                          point_H)('')
#         self._assumptions = DrawingSet(*projections)
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

        self.add_solution_step('Assumptions',
                               [point_A, point_P, point_H, point_O])
        self._assumptions3d = DrawingSet(point_A,point_P, point_H, point_O,
                                         point_H)('Assumptions')
        self._assumptions = DrawingSet(*projections)
        
        self.add_solution_step("Assumptions", [point_A, point_P, point_O,point_H])
        
    def _solution(self):
        current_obj = copy.deepcopy(self)

        A = current_obj.point_A
        O = current_obj.point_O
        P = current_obj.point_P

        H = current_obj.point_H

        S = (A @ (O ^ P))('S')  #'Srodek' podstawy

        dirPS = P - S
        dirOS = O - S
        triangle_height = A.distance(S).n(5)
        #triangle_side =  triangle_height / ((3**(1/2))/2)

        B = (S + dirPS / (P.distance(S)) * (triangle_height))('B')
        C = (S - dirPS / (P.distance(S)) * (triangle_height))('C')
        triangle_plane = Plane(A, B, C)

        current_set = DrawingSet(*current_obj._solution_step[-1])

        line_a = Line(A, B)('AB')
        line_b = Line(C, A)('BC')
        plane_alpha = Plane(A, O, P)

        plane_beta = HorizontalPlane(P)
        plane_eta = VerticalPlane(P)


        line_a = plane_alpha.intersection(plane_beta)[0]('a')

        point_P1 = plane_beta.intersection(A ^ O)[0]('P1')
        point_P2 = plane_eta.intersection(A ^ O)[0]('P2')
        current_obj.P1 = point_P1
        line_p = (P ^ point_P1)('p')
        line_l = (P ^ point_P2)('l')
        line_k = (P ^ point_P1)('k')

        
        current_obj.add_solution_step("", [A, B, C])
        #current_obj.add_solution_step('Base ABC', [A, B, C])
        
        # it creates next step of solution - lines are presented
        #current_step3d=copy.deepcopy(current_obj._solution3d_step[-1])+[(A^point_P1)('AO'),point_P1,(P^point_P1)('a')]

        #it sets the step elements
#         current_obj.add_solution_step(
#             '', [point_P2, point_P1,
#                                  line_k, line_p, line_l])

        
        elems = self._assumptions
        projections = []
        point_0_dict = {}
        eps_dict = {}

        point_B = B
        point_C = C
        point_O = O
        
        ##################   plane rotation

        #line_kk = Line(P, (O @ line_k))('k')

        A0 = A.rotate_about(axis=line_a)('A_0')
        current_obj.A0 = A0

        ### Step 2 #####
        ###  plane of rotation of A ####

        current_obj.add_solution_step('', [A0])

        #### Step 3 ####
        ### rotated point A0 of A #####

        B0 = B.rotate_about(axis=line_a)('B_0')
        current_obj.B0 = B0

        current_obj.add_solution_step('', [B0])

        #### Step 4 ####
        ### postion of B0 (based on triangle geometry) #####

        #current_obj.add_solution_step(
            #'Point B rotation - plane of rotation',
            #[(B0 ^ (B0 @ line_k))('eps_B')])

        C0 = C.rotate_about(axis=line_a)('C_0')
        current_obj.C0 = C0
        current_obj.add_solution_step('', [C0])

        #### Step 5 ####
        ### postion of C0 (based on triangle geometry) #####

        #current_obj.D0=D.rotate_about(axis=line_k)('D_0')
        current_obj.O0 = O.rotate_about(axis=line_a)('O_0')

        current_obj.point_A_0 = A.rotate_about(axis=line_k)('A_0')
        current_obj.point_B_0 = B.rotate_about(axis=line_k)('B_0')
        current_obj.point_C_0 = C.rotate_about(axis=line_k)('C_0')

        current_obj.point_O_0 = O.rotate_about(axis=line_k)('O_0')   

        G = (H @ plane_alpha)('G')

        ############  upper  base

        dirHG = H - G
        distance_HG = (H.distance(G)).n(5)

        #D = (A + dirHG/distance_HG*triangle_height)('D')
        #E = (B + dirHG/distance_HG*triangle_height)('E')
        #F = (C + dirHG/distance_HG*triangle_height)('F')

        A, B, C, D, E, F = Prism(triangle_plane,
                                 dirHG / distance_HG * triangle_height)

        current_obj.add_solution_step('', [D, E, F])

        line_ab=Line(A,B)('|AB|')
        line_bc=Line(B,C)('|BC|')
        line_ca=Line(C,A)('|CA|')
        line_eb=Line(E,B)('|EB|')
        line_da=Line(D,A)('|DA|')
        line_fc=Line(F,C)('|FC|')
        line_de=Line(D,E)('|DE|')
        line_ef=Line(E,F)('|EF|')
        #line_fd=Line(F,D)('|FD|')
        line_fd = (F ^ D)('|FD|')
        current_obj.add_solution_step('', [line_ab, line_bc, line_ca, line_eb, line_da, line_fc, line_de, line_ef, line_fd])
        
        elems += [D, E, F, G]

        projections += [
            G @ HPP, G @ VPP, D @ HPP, D @ VPP, E @ HPP, E @ VPP, F @ HPP,
            F @ VPP
        ]



        current_obj.point_B = B
        current_obj.point_C = C
        current_obj.point_D = D
        current_obj.point_E = E
        current_obj.point_F = F


        current_obj.add_solution_step("Solution", [A, B, C, D, E, F])
        

        #current_obj._assumptions = DrawingSet(*projections)("Solution")
        
        return current_obj

    def present_solution(self):

        doc_model = Document(f'{self.__class__.__name__} solution')

        doc_model.packages.append(Package('booktabs'))
        doc_model.packages.append(Package('float'))
        doc_model.packages.append(Package('standalone'))
        doc_model.packages.append(Package('siunitx'))

        #ReportText.set_container(doc_model)
        #ReportText.set_directory('./SDAresults')

        for no, step3d in enumerate(self._solution3d_step):
            GeometrySceneDG()

            for elem in range(no):
                self._solution3d_step[elem].plot(color='k')
                self._solution_step[elem].plot_vp(color='k').plot_hp(color='k')

            self._solution3d_step[no].plot(color='r')
            self._solution_step[no].plot_vp(color='r').plot_hp(color='g')

            with doc_model.create(Figure(position='H')) as fig:
                #path=f'./images/image{no}.png'
                #plt.savefig(path)
                #fig.add_image(path)
                fig.add_plot(width=NoEscape(r'1.4\textwidth'))

                if step3d._label is not None:
                    fig.add_caption(step3d._label)

            plt.show()

        return doc_model

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
            'shift': shift
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

class GivenHeightEdgeIsoscelesRightTrianglePrism(GivenHeightIsoscelesRightTrianglePrism):
    def get_random_parameters(self):

        parameters_dict = super().get_random_parameters()

        point_P = parameters_dict[Symbol('P')]
        point_O = parameters_dict[Symbol('O')]

        parameters_dict[Symbol('A')] = (point_P + point_O) * 0.5 + Point(0, 0, 5)

        return parameters_dict
    
    
class GivenHeightIsoscelesRightTrianglePrismSwappedProjections(GivenHeightIsoscelesRightTrianglePrism):

    shift = [
        Point(x, y, z) for x in [ -8.5, -8,-7]
        for y in [-1,-0.5,0,0.5] for z in [-11,-10,-9]
    ]

class GivenHeightEdgeIsoscelesRightTrianglePrismSwappedProjections(GivenHeightEdgeIsoscelesRightTrianglePrism):

    shift = [
        Point(x, y, z) for x in [ -9.5, -9, -8.5, -8,-7]
        for y in [-1,-0.5,0,0.5] for z in [-13, -12, -11, -10.5, -10, -9.5, -9]
    ]
    
    

class GivenHeightHFLinesIsoscelesRightTrianglePrism(
        GivenHeightIsoscelesRightTrianglePrism):

    #quite good data
    #point_A = [Point(x,y,z) for x in [4,5.5,5] for y in [5,5.5,6] for z in   [5.5,6,6.5]  ]

    #point_O=[Point(x,y,z) for x in [3,3.5] for y in [8,8.5,9] for z in   [3,3.5,4] ]

    #point_P = [Point(x,y,z) for x in [6,6.5,7] for y in [3,3.5]  for z in [1,1.5,2] ]

    #point_H = [Point(x,y,z) for x in range(9,11) for y in [3,3.5] for z in range(9,11) ]

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
        Point(x, y, z) for x in [7, 7.5, 8] for y in [1, 1.5, 2]
        for z in [5.5, 6, 6.5]
    ]
    shift = [
        Point(x, y, z) for x in [-3, -2.5, -2, -1, -0.5, 0, 0.5, 1]
        for y in [2, 2.5, 3] for z in [-2, -1.5, -1, -0.5, 0]
    ]

    #point_H = [Point(x,y,z) for x in [1,1.5] for y in [1,1.5,2] for z in [5.5,6,6.5] ]

    def get_random_parameters(self):

        parameters_dict = super().get_random_parameters()

        point_H = parameters_dict[Symbol('H')]
        point_O = parameters_dict[Symbol('O')]
        point_A = parameters_dict[Symbol('A')]
        point_P = parameters_dict[Symbol('P')]

        parameters_dict[Symbol('A')] = Point(point_O.x, point_A.y, point_A.z)
        parameters_dict[Symbol('P')] = Point(point_P.x, point_P.y, point_O.z)

        return parameters_dict


class GivenHeightHFLinesIsoscelesRightTrianglePrism2(
        GivenHeightHFLinesIsoscelesRightTrianglePrism):

    point_A = [
        Point(x, y, z) for x in [6, 6.5] for y in [7, 7.5, 8]
        for z in [8, 8.5]
    ]

    point_C = [
        Point(x, y, z) for x in [3, 3.5, 4, 4.5] for y in [2, 2.5, 3]
        for z in [2, 2.5, 3, 4, 5]
    ]

    def get_random_parameters(self):

        parameters_dict = super().get_random_parameters()

        point_B = parameters_dict[Symbol('B')]
        point_M = parameters_dict[Symbol('M')]
        point_N = parameters_dict[Symbol('N')]
        point_O = parameters_dict[Symbol('O')]
        point_A = parameters_dict[Symbol('A')]
        point_C = parameters_dict[Symbol('C')]

        shift = parameters_dict['shift']
        parameters_dict.pop('shift')

        for point in symbols('A B C M N O'):
            parameters_dict[point] = parameters_dict[point] + shift

        return parameters_dict

    
    
class GivenHeightSquarePrism(GeometricalCase):

    point_A = [
        Point(x, y, z) for x in [6, 6.5] for y in [6.5,7, 7.5]
        for z in [8, 8.5]
    ]

    point_O = [
        Point(x, y, z) for x in [3, 3.5, 4, 4.5] for y in [4.5, 5, 5.5]
        for z in [2, 2.5, 3, 4, 5]
    ]

    point_P = [
        Point(x, y, z) for x in [2, 2.5] for y in [8.5,9,9.5]
        for z in [4, 5, 6]
    ]

    point_R = [
        Point(x, y, z) for x in [9, 9.5, 10] for y in [2, 2.5, 3]
        for z in range(0, 2)
    ]

    shift = [
        Point(x, y, z) for x in [-3,-2,-1] for y in [-1,-1.5, -2,]
        for z in [-2, -1.5, -1, -0.5, 0]
    ]

    def __init__(self,
                 point_A=None,
                 point_P=None,
                 point_O=None,
                 point_R=None,
                 **kwargs):

        super().__init__()

        if point_A and point_O and point_P and point_R:
            projections = (point_A @ HPP, point_O @ HPP, point_O @ VPP,
                           point_P @ VPP, point_P @ HPP, point_A @ VPP,
                           point_R @ VPP, point_R @ HPP)

        else:
            projections = []

        # it creates first step of solution
        self.add_solution_step('',
                               [point_A, point_O, point_P, point_R])

        self._assumptions3d = DrawingSet(point_A, point_O, point_P,
                                         point_R)('')
        self._assumptions = DrawingSet(*projections)
        self._assumptions3d=DrawingSet(point_A,point_O,point_P,point_R)('Assumptions')

        #self += [point_A,point_O,point_P,point_H]

        self.point_A = point_A
        self.point_P = point_P
        self.point_O = point_O
        self.point_R = point_R

        self._given_data = {
            'A': point_A,
            'P': point_P,
            'O': point_O,
            'R': point_R
        }

    def _solution(self):
        current_obj = copy.deepcopy(self)

        A = current_obj.point_A
        O = current_obj.point_O
        P = current_obj.point_P

        R = current_obj.point_R

        S = (A @ (O ^ P))('S')  #'Srodek' podstawy

        dirPS = P - S
        dirOS = O - S
        square_diagonal = 2 * A.distance(S).n(5)
        #triangle_side =  triangle_height / ((3**(1/2))/2)

        B = (S + dirPS / (P.distance(S)) * (square_diagonal / 2))('B')
        D = (S - dirPS / (P.distance(S)) * (square_diagonal / 2))('D')
        C = (S + (S - A))('C')
        triangle_plane = Plane(A, B, C)

        current_set = DrawingSet(*current_obj._solution_step[-1])

        line_a = Line(A, B)('a')
        line_b = Line(C, A)('b')
        plane_alpha = Plane(A, O, P)

        plane_beta = HorizontalPlane(P)
        plane_eta = VerticalPlane(P)

        line_a = plane_alpha.intersection(plane_beta)[0]('a')

        point_P1 = plane_beta.intersection(A ^ O)[0]('P1')
        point_P2 = plane_eta.intersection(A ^ O)[0]('P2')
#         current_obj.P1 = point_P1
#         #line_kk = (P ^ point_P1)('a')
#         #line_f = (P ^ point_P2)('f')
#         line_p = (P ^ point_P1)('p')
#         line_l = (P ^ point_P2)('l')
        line_k = (P ^ point_P1)('k')

        current_obj.add_solution_step("", [A, B, C, D])
        # it creates next step of solution - lines are presented
        #current_step3d=copy.deepcopy(current_obj._solution3d_step[-1])+[(A^point_P1)('AO'),point_P1,(P^point_P1)('a')]

        #it sets the step elements
#         current_obj.add_solution_step(
#             '', [point_P1, point_P2,
#                                  line_k, line_p, line_l])

        elems = current_obj._assumptions
        projections = []
        point_0_dict = {}
        eps_dict = {}

        point_B = B
        point_C = C
        point_O = O

        ##################   plane rotation

        #line_kk = Line(P, (O @ line_k))('k')

        A0 = A.rotate_about(axis=line_a)('A_0')
        current_obj.A0 = A0

        ### Step 2 #####
        ###  plane of rotation of A ####

        current_obj.add_solution_step('', [A0])

        #### Step 3 ####
        ### rotated point A0 of A #####

        B0 = B.rotate_about(axis=line_a)('B_0')
        current_obj.B0 = B0

        current_obj.add_solution_step('', [B0])

        #### Step 4 ####
        ### postion of B0 (based on triangle geometry) #####

        C0 = C.rotate_about(axis=line_a)('C_0')
        current_obj.C0 = C0
        current_obj.add_solution_step('', [C0])

        #### Step 5 ####
        ### postion of C0 (based on triangle geometry) #####

        D0 = D.rotate_about(axis=line_a)('D_0')
        current_obj.D0 = D0
        current_obj.add_solution_step('', [D0])

        #current_obj.D0=D.rotate_about(axis=line_k)('D_0')
        current_obj.O0 = O.rotate_about(axis=line_a)('O_0')

        current_obj.add_solution_step('', [A, B, C, D])

        current_obj.point_A_0 = A.rotate_about(axis=line_k)('A_0')
        current_obj.point_B_0 = B.rotate_about(axis=line_k)('B_0')
        current_obj.point_C_0 = C.rotate_about(axis=line_k)('C_0')
        current_obj.point_D_0 = D.rotate_about(axis=line_k)('D_0')        
        current_obj.point_O_0 = O.rotate_about(axis=line_k)('O_0')   
        
        T = (R @ plane_alpha)('T')

        ############  upper  base

        dirRT = R - T
        distance_RT = (R.distance(T)).n(5)

        #D = (A + dirHG/distance_HG*triangle_height)('D')
        #E = (B + dirHG/distance_HG*triangle_height)('E')
        #F = (C + dirHG/distance_HG*triangle_height)('F')

        A, B, C, E, F, G = Prism(triangle_plane,
                                 dirRT / distance_RT * B.distance(C))

        E = E('E')
        F = F('F')
        G = G('G')
        H = (D + (E - A))('H')

        current_obj.add_solution_step('', [E, F, G, H])

        elems += [D, E, F, G]

        projections += [
            G @ HPP, G @ VPP, D @ HPP, D @ VPP, E @ HPP, E @ VPP, F @ HPP,
            F @ VPP
        ]

        
        
        line_ab=Line(A,B)('|AB|')
        line_bc=Line(B,C)('|BC|')
        line_cd=Line(C,D)('|CD|')
        line_da=Line(D,A)('|DA|')
        line_ae=Line(A,E)('|AE|')
        line_bf=Line(B,F)('|BF|')
        line_cg=Line(C,G)('|CG|')
        line_di=Line(D,H)('|DH|')
        line_ef=Line(E,F)('|EF|')
        line_fg=Line(F,G)('|FG|')
        line_gi=Line(G,H)('|GH|')
        line_ie=Line(H,E)('|HE|')
        current_obj.add_solution_step('', [line_ab, line_bc, line_cd, line_da, line_ae, line_bf, line_cg, line_di, line_ef, line_fg, line_gi, line_ie])
        
        current_obj._assumptions = DrawingSet(
            *current_obj.get_projections())('Solution')
        current_obj._assumptions3d = DrawingSet(*current_obj)

        current_obj.point_B = B
        current_obj.point_C = C
        current_obj.point_D = D
        current_obj.point_E = E
        current_obj.point_F = F
        current_obj.point_G = G
        current_obj.point_H = H

        return current_obj

#     def present_solution(self):

#         doc_model = Document(f'{self.__class__.__name__} solution')

#         doc_model.packages.append(Package('booktabs'))
#         doc_model.packages.append(Package('float'))
#         doc_model.packages.append(Package('standalone'))
#         doc_model.packages.append(Package('siunitx'))

#         #ReportText.set_container(doc_model)
#         #ReportText.set_directory('./SDAresults')

#         for no, step3d in enumerate(self._solution3d_step):
#             GeometrySceneDG()

#             for elem in range(no):
#                 self._solution3d_step[elem].plot(color='k')
#                 self._solution_step[elem].plot_vp(color='k').plot_hp(color='k')

#             self._solution3d_step[no].plot(color='r')
#             self._solution_step[no].plot_vp(color='r').plot_hp(color='g')

#             with doc_model.create(Figure(position='H')) as fig:
#                 #path=f'./images/image{no}.png'
#                 #plt.savefig(path)
#                 #fig.add_image(path)
#                 fig.add_plot(width=NoEscape(r'1.4\textwidth'))

#                 if step3d._label is not None:
#                     fig.add_caption(step3d._label)

#             plt.show()

#         return doc_model

    def get_default_data(self):

        point_A = self.__class__.point_A
        point_O = self.__class__.point_O
        point_P = self.__class__.point_P
        point_R = self.__class__.point_R

        shift = self.shift

        default_data_dict = {
            Symbol('A'): point_A,
            Symbol('P'): point_P,
            Symbol('O'): point_O,
            Symbol('R'): point_R,
            'shift': shift
        }
        return default_data_dict

    def get_random_parameters(self):

        parameters_dict = super().get_random_parameters()

        point_R = parameters_dict[Symbol('R')]
        point_O = parameters_dict[Symbol('O')]
        point_A = parameters_dict[Symbol('A')]
        point_P = parameters_dict[Symbol('P')]

        shift = parameters_dict['shift']
        parameters_dict.pop('shift')

        for point in symbols('A P O R'):
            parameters_dict[point] = parameters_dict[point] + shift

        return parameters_dict

    
class GivenHeightEdgeSquarePrism(GivenHeightSquarePrism):
  
    def get_random_parameters(self):

        parameters_dict = super().get_random_parameters()

        point_P = parameters_dict[Symbol('P')]
        point_O = parameters_dict[Symbol('O')]

        parameters_dict[Symbol('A')] = (point_P + point_O) * 0.5 + Point(0, 0, 5)

        return parameters_dict

class GivenHeightHorizontalSquarePrism(GivenHeightSquarePrism):
  
    shift = [
        Point(x, y, z) for x in [-3,-2,-1, 0] for y in [-2,-1.5,-1,0,0.5,1]
        for z in [-1,-.5,0,0.5,1]
    ]



    def get_random_parameters(self):

        parameters_dict = super().get_random_parameters()

        point_P = parameters_dict[Symbol('P')]
        point_O = parameters_dict[Symbol('O')]

        
        parameters_dict[Symbol('O')] = Point(point_P.x,point_O.y,point_O.z   )('O')
        point_O = parameters_dict[Symbol('O')]
        parameters_dict[Symbol('A')] = (point_P + point_O) * 0.5 + Point(0, 0, 5)
        

        return parameters_dict
    
    
    
class GivenHeightSquarePrismSwappedProjections(GivenHeightSquarePrism):
    shift = [
        Point(x, y, z) for x in [ -8,-7]
        for y in [0] for z in [ -6,-5]
    ]

    
class GivenHeightRhomboidPrism(GeometricalCase):

    point_A = [
        Point(x, y, z) for x in [6, 6.5] for y in [7, 7.5, 8]
        for z in [8, 8.5]
    ]

    point_O = [
        Point(x, y, z) for x in [3, 3.5, 4, 4.5] for y in [3, 4, 5]
        for z in [2, 2.5, 3, 4, 5]
    ]

    point_P = [
        Point(x, y, z) for x in [2, 2.5] for y in [10, 10.5, 11]
        for z in [4, 5, 6]
    ]

    point_R = [
        Point(x, y, z) for x in [9, 9.5, 10] for y in [2, 2.5, 3]
        for z in range(0, 2)
    ]

    shift = [
        Point(x, y, z) for x in [-3, -2, -1, 0] for y in [1, 2, 3]
        for z in [-2, -1.5, -1, -0.5, 0]
    ]

    def __init__(self,
                 point_A=None,
                 point_P=None,
                 point_O=None,
                 point_R=None,
                 **kwargs):

        super().__init__()

        if point_A and point_O and point_P and point_R:
            projections = (point_A @ HPP, point_O @ HPP, point_O @ VPP,
                           point_P @ VPP, point_P @ HPP, point_A @ VPP,
                           point_R @ VPP, point_R @ HPP)

        else:
            projections = []

        # it creates first step of solution
        self.add_solution_step('Assumptions',
                               [point_A, point_O, point_P, point_R])

        self._assumptions3d = DrawingSet(point_A, point_O, point_P,
                                         point_R)('Assumptions')
        self._assumptions = DrawingSet(*projections)
        #self._assumptions3d=DrawingSet(point_A,point_O,point_P,point_R)('Assumptions')

        #self += [point_A,point_O,point_P,point_R]

        self._point_A = point_A
        self._point_P = point_P
        self._point_O = point_O
        self._point_R = point_R

        self._given_data = {
            'A': point_A,
            'P': point_P,
            'O': point_O,
            'R': point_R
        }

    def _solution(self):

        current_obj = copy.deepcopy(self)

        A = current_obj._point_A
        O = current_obj._point_O
        P = current_obj._point_P

        R = current_obj._point_R

        S = (A @ (O ^ P))('S')  #'Srodek' podstawy

        dirPS = P - S
        dirOS = O - S
        square_diagonal = 2 * A.distance(S).n(5)
        #triangle_side =  triangle_height / ((3**(1/2))/2)

        B = (S + dirPS / (P.distance(S)) * (square_diagonal / 4))('B')
        D = (S - dirPS / (P.distance(S)) * (square_diagonal / 4))('D')
        C = (S + (S - A))('C')
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
        current_obj.A0 = A0

        ### Step 2 #####
        ###  plane of rotation of A ####

        current_obj.add_solution_step('Point A rotation', [A0])

        #### Step 3 ####
        ### rotated point A0 of A #####

        B0 = B.rotate_about(axis=line_k)('B_0')
        current_obj.B0 = B0

        current_obj.add_solution_step('Point B rotation', [B0])

        #### Step 4 ####
        ### postion of B0 (based on triangle geometry) #####

        C0 = C.rotate_about(axis=line_k)('C_0')
        current_obj.C0 = C0
        current_obj.add_solution_step('Point C rotation', [C0])

        #### Step 5 ####
        ### postion of C0 (based on triangle geometry) #####

        D0 = D.rotate_about(axis=line_k)('D_0')
        current_obj.D0 = D0
        current_obj.add_solution_step('Point D rotation', [D0])

        #current_obj.D0=D.rotate_about(axis=line_k)('D_0')
        current_obj.O0 = O.rotate_about(axis=line_k)('O_0')

        current_obj.add_solution_step('Base ABCD', [A, B, C, D])

        T = (R @ plane_alpha)('T')

        ############  upper  base

        dirRT = R - T
        distance_RT = (T.distance(R)).n(5)

        #D = (A + dirHG/distance_HG*triangle_height)('D')
        #E = (B + dirHG/distance_HG*triangle_height)('E')
        #F = (C + dirHG/distance_HG*triangle_height)('F')

        A, B, C, E, F, G = Prism(triangle_plane,
                                 dirRT / distance_RT * B.distance(C))

        E = E('E')
        F = F('F')
        G = G('G')
        H = (D + (E - A))('H')

        current_obj.add_solution_step('Vertices E,F,G,H', [E, F, G, H])

        elems += [D, E, F, G]

        projections += [
            G @ HPP, G @ VPP, D @ HPP, D @ VPP, E @ HPP, E @ VPP, F @ HPP,
            F @ VPP
        ]

        current_obj._assumptions = DrawingSet(
            *current_obj.get_projections())('Solution')
        current_obj._assumptions3d = DrawingSet(*current_obj)

        current_obj._point_B = B
        current_obj._point_C = C
        current_obj._point_D = D
        current_obj.point_E = E
        current_obj.point_F = F
        current_obj.point_G = G
        current_obj.point_H = H

        return current_obj

    def present_solution(self):

        doc_model = Document(f'{self.__class__.__name__} solution')

        doc_model.packages.append(Package('booktabs'))
        doc_model.packages.append(Package('float'))
        doc_model.packages.append(Package('standalone'))
        doc_model.packages.append(Package('siunitx'))

        #ReportText.set_container(doc_model)
        #ReportText.set_directory('./SDAresults')

        for no, step3d in enumerate(self._solution3d_step):
            GeometryScene()

            for elem in range(no):
                self._solution3d_step[elem].plot(color='k')
                self._solution_step[elem].plot_vp(color='k').plot_hp(color='k')

            self._solution3d_step[no].plot(color='r')
            self._solution_step[no].plot_vp(color='r').plot_hp(color='r')

            with doc_model.create(Figure(position='H')) as fig:
                #path=f'./images/image{no}.png'
                #plt.savefig(path)
                #fig.add_image(path)
                fig.add_plot(width=NoEscape(r'1.4\textwidth'))

                if step3d._label is not None:
                    fig.add_caption(step3d._label)

            plt.show()

        return doc_model

    def get_default_data(self):

        point_A = self.__class__.point_A
        point_O = self.__class__.point_O
        point_P = self.__class__.point_P
        point_R = self.__class__.point_R

        shift = self.shift

        default_data_dict = {
            Symbol('A'): point_A,
            Symbol('P'): point_P,
            Symbol('O'): point_O,
            Symbol('R'): point_R,
            'shift': shift
        }
        return default_data_dict

    def get_random_parameters(self):

        parameters_dict = super().get_random_parameters()

        point_R = parameters_dict[Symbol('R')]
        point_O = parameters_dict[Symbol('O')]
        point_A = parameters_dict[Symbol('A')]
        point_P = parameters_dict[Symbol('P')]

        shift = parameters_dict['shift']
        parameters_dict.pop('shift')

        for point in symbols('A P O R'):
            parameters_dict[point] = parameters_dict[point] + shift

        return parameters_dict


class EquilateralTrianglePrismNew2(EquilateralTrianglePrismNew):

    point_A = [
        Point(x, y, z) for x in [8] for y in [6, 6.5]
        for z in [8]
    ]

    point_O = [
        Point(x, y, z) for x in [5.5, 6] for y in [9.5, 10]
        for z in [5, 5.5]
    ]

    point_P = [
        Point(x, y, z) for x in [3, 3.5] for y in [4,4.5]
        for z in [2, 2.5]]
    
    point_H = [
        Point(x, y, z) for x in [3] for y in [3]
        for z in [9]
    ]
    
    shift = [
        Point(x, y, z) for x in [0,0.5,1,1.5,2] for y in [-1,0,1,2]
        for z in [0,-0.5,-1,-1.5,-2]
    ]

class EquilateralTrianglePrismNew2SwappedProjections(EquilateralTrianglePrismNew2):


    shift = [
        Point(x, y, z) for x in [-9,-9.5,-10,-10.5,-11] for y in [-1,0,1,2]
        for z in [-9,-9.5,-10,-10.5,-11]
    ]