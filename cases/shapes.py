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
from .rotations import RotatedPoint, UnrotatedPoint


class ShapeOnPlane(GeometricalCase):

    point_A = [
        Point(x, y, z) for x in [8, 8.5, 9, 7.5, 7] for y in [5, 5.5, 6, 6.5]
        for z in [8, 8.5, 7.5, 7]
    ]

    point_O = [
        Point(x, y, z) for x in [5, 5.5, 6, 6.5] for y in [8, 8.5, 9, 9.5, 10]
        for z in [4, 4.5, 5, 5.5]
    ]

    point_P = [
        Point(x, y, z) for x in [1, 1.5, 2, 2.5] for y in [2, 2.5, 3, 3.5]
        for z in [1, 1.5, 2, 2.5]
    ]
    
    shift = [
        Point(x, y, z) for x in [0] for y in [0]
        for z in [0]
    ]
    

    def __init__(self, point_A=None, point_P=None, point_O=None, **kwargs):

        super().__init__()

        if point_A and point_O and point_P:
            projections = (
                point_A @ HPP,
                point_O @ HPP,
                point_O @ VPP,
                point_P @ VPP,
                point_P @ HPP,
                point_A @ VPP,
            )
        else:
            projections = []

        self._assumptions = DrawingSet(*projections)

        self.point_A = point_A
        self.point_P = point_P
        self.point_O = point_O

        self.add_solution_step(f'''Assumptions''', [point_A, point_P, point_O])

    def _base_shape(self, base_plane=None):

        if base_plane is None:
            A = self._point_A
            O = self._point_O
            P = self._point_P
        else:
            A, O, P = base_plane

        return A, O, P

    def _given_plane(self, base_plane=None):

        if base_plane is None:
            A = self._point_A
            O = self._point_O
            P = self._point_P
        else:
            A, O, P = base_plane

        return A, O, P

    def _rotation_of_given_plane(self, base_plane=None):

        axis = self._axis

        rotated_base = []

        for base_point in self._given_plane():

            base_point_rotation_case = RotatedPoint(base_point, axis=axis)
            self._append_case(base_point_rotation_case)

            rot_base_point = base_point_rotation_case._rotated_point
            rotated_base += [rot_base_point]

        return rotated_base

    def _rotation_of_base(self, base_plane=None):

        if base_plane is None:
            base_plane = self._base_shape()

        return base_plane

    def _shape_points(self):

        A, O, P = self._base_shape()
        self.add_solution_step('Last step - shape outline',
                               [A ^ O, O ^ P, P ^ A])

        return A, O, P

    def _solution(self):

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

        point_P2 = plane_eta.intersection(A ^ O)[0]('2')

        line_f = (P ^ point_P2)('f')

        current_obj.add_solution_step(
            f'''Axis of rotation - it is common part between given plane $\\alpha({A._label},{O._label},{P._label})$  and horizontal plane $\\gamma$ which contains point {P._label}''',
            [point_P2, (P ^ point_P2)('f')])

        point_O = O

        line_k = Line(P, (O @ line_k))('k')
        current_obj._axis = line_k
        current_obj._hor_plane = plane_beta

        A0, O0, P0 = current_obj._rotation_of_given_plane()

        current_obj.A0 = A0
        current_obj.P0 = P0
        current_obj.O0 = O0

        #### Step 4 ####
        ### postion of B0 (based on triangle geometry) #####

        for base_point in current_obj._rotation_of_base():

            shape_unrotation_case = UnrotatedPoint(base_point, (P ^ O)('PO'),
                                                   axis=line_k)
            current_obj._append_case(shape_unrotation_case)

        current_obj._shape_points()

        print(list(current_obj))

        return current_obj

    def get_default_data(self):

        point_A = self.__class__.point_A
        point_O = self.__class__.point_O
        point_P = self.__class__.point_P
        shift = self.__class__.shift

        default_data_dict = {
            Symbol('A'): point_A,
            Symbol('P'): point_P,
            Symbol('O'): point_O,
            'shift': shift,
        }
        return default_data_dict

    
    def get_random_parameters(self):

        parameters_dict = super().get_random_parameters()

        #point_H = parameters_dict[Symbol('H')]
        point_O = parameters_dict[Symbol('O')]
        point_A = parameters_dict[Symbol('A')]
        point_P = parameters_dict[Symbol('P')]

        shift = parameters_dict['shift']
        parameters_dict.pop('shift')

        for point in symbols('A P O'):
            parameters_dict[point] = parameters_dict[point] + shift

        return parameters_dict
    
    
class Shape(GeometricalCase):

    point_A = [
        Point(x, y, z) for x in [8, 8.5, 9, 7.5, 7] for y in [5, 5.5, 6, 6.5]
        for z in [8, 8.5, 7.5, 7]
    ]

    point_B = [
        Point(x, y, z) for x in [5, 5.5, 6, 6.5] for y in [8, 8.5, 9, 9.5, 10]
        for z in [4, 4.5, 5, 5.5]
    ]

    point_C = [
        Point(x, y, z) for x in [1, 1.5, 2, 2.5] for y in [2, 2.5, 3, 3.5]
        for z in [1, 1.5, 2, 2.5]
    ]
    
    point_Z = [
        Point(x, y, z) for x in [1, 1.5, 2, 2.5] for y in [2, 2.5, 3, 3.5]
        for z in [1, 1.5, 2, 2.5]
    ]

    def __init__(self, point_A=None, point_B=None, point_C=None, point_Z=None, **kwargs):

        super().__init__()

        if point_A and point_B and point_C:
            projections = [
                point_A @ HPP,
                point_B @ HPP,
                point_B @ VPP,
                point_C @ VPP,
                point_C @ HPP,
                point_A @ VPP,
            ]
        else:
            projections = []
        
        if point_Z:
            projections += [
                point_Z @ HPP,
                point_Z @ VPP,
            ]
        else:
            projections += []

        self._assumptions = DrawingSet(*projections)

        self._point_A = point_A
        self._point_B = point_B
        self._point_C = point_C
        self._point_Z = point_Z

        self.add_solution_step(f'''Assumptions''', [point_A, point_B, point_C, point_Z])

    def _base_shape(self, base_plane=None):

        if base_plane is None:
            A = self._point_A
            B = self._point_B
            C = self._point_C
            Z = self._point_Z
        else:
            A, B, C, Z = base_plane

        return A, B, C, Z

    def _given_plane(self, base_plane=None):

        if base_plane is None:
            A = self._point_A
            B = self._point_B
            C = self._point_C
            Z = self._point_Z
        else:
            A, B, C, Z = base_plane

        return A, B, C, Z

    def _rotation_of_given_plane(self, base_plane=None):

        axis = self._axis

        rotated_base = []

        for base_point in self._given_plane():

            base_point_rotation_case = RotatedPoint(base_point, axis=axis)
            self._append_case(base_point_rotation_case)

            rot_base_point = base_point_rotation_case._rotated_point
            rotated_base += [rot_base_point]

        return rotated_base

    def _rotation_of_base(self, base_plane=None):

        if base_plane is None:
            base_plane = self._base_shape()

        return base_plane

    def _shape_points(self):

        A, B, C, Z = self._base_shape()
        if Z == None:
            self.add_solution_step('Last step - shape outline',
                               [A ^ B, B ^ C, C ^ A])
        else:
            self.add_solution_step('Last step - shape outline',
                               [A ^ B, B ^ C, C ^ Z, Z ^ A])

        return A, B, C, Z


    def get_default_data(self):

        point_A = self.__class__.point_A
        point_B = self.__class__.point_B
        point_C = self.__class__.point_C

        default_data_dict = {
            Symbol('A'): point_A,
            Symbol('B'): point_B,
            Symbol('C'): point_C,
        }
        return default_data_dict

# class SquareOnPlane(ShapeOnPlane):

#     point_A = [
#         Point(x, y, z) for x in [8, 8.5, 9, 7.5, 7] for y in [5, 5.5, 6, 6.5]
#         for z in [8, 8.5, 7.5, 7]
#     ]

#     point_O = [
#         Point(x, y, z) for x in [5, 5.5, 6, 6.5] for y in [8, 8.5, 9, 9.5, 10]
#         for z in [4, 4.5, 5, 5.5]
#     ]

#     point_P = [
#         Point(x, y, z) for x in [1, 1.5, 2, 2.5] for y in [2, 2.5, 3, 3.5]
#         for z in [1, 1.5, 2, 2.5]
#     ]

#     def _base_shape(self, base_plane=None):

#         if base_plane is None:
#             A = self._point_A
#             O = self._point_O
#             P = self._point_P
#         else:
#             A, O, P = base_plane

#         S = (A @ (O ^ P))('S')  #'Srodek' podstawy

#         dirPS = P - S
#         dirOS = O - S
#         square_diagonal = 2 * A.distance(S).n(5)
#         #triangle_side =  triangle_height / ((3**(1/2))/2)

#         B = (S + dirPS / (P.distance(S)) * (square_diagonal / 2))('B')
#         D = (S - dirPS / (P.distance(S)) * (square_diagonal / 2))('D')
#         C = (S + (S - A))('C')

#         self.add_solution_step(
#             'Creating a point $C_0$ based on triangle geometry ',
#             [A ^ B, B ^ C])

#         #self.add_solution_step('Creating a point $\\C_0$ based on triangle geometry ', [A^B,B^C]) #<- to źle źle niedobrze połowa kroków się w ogóle nie wyświetla

#         self.A = A
#         self.B = B
#         self.D = D

#         return A, B, D

#     def _rotation_of_base(self, base_plane=None):

#         self._base_shape()

#         A = self.A
#         B = self.B
#         D = self.D

#         A0 = self.A0('A_0')
#         B0 = B.rotate_about(self._axis)('B_0')
#         D0 = D.rotate_about(self._axis)()('D_0')
#         C0 = (B0 + (D0 - A0))('C_0')

#         #\u25A1  #symbole \square, \Box ani \triangle nie działają, a by się tu przydały
#         #przy {A0._label}{B0}{0} powinno być ABO, a nie AB0 (zero), ale w jupyterze wyświetla że O nie zostało zdefiniowane, mimo że zostało w 146 linijce

#         self.add_solution_step(
#             f'Rotated Base (  $ {A0._label}{B0}{0} $ triangle - half of  $\u25A1$ ${A0}{B0}{C0}{D0}$ square )',
#             [A0 ^ B0, A0 ^ D0],
#             caption=
#             'Rotated Base (  ${A0._label}{B0}{0} $ triangle - half of  $ \\square {A0}{B0}{C0}{D0}$ square )'
#         )

#         return B, D

#     def _shape_points(self):

#         A, B, D = self._given_plane()

#         C = B + (D - A)

#         self.add_solution_step('Obtained shape - $ {A}{B}{C}{D}$ square ',
#                                [(A ^ B)('_'), (B ^ C)('_'), (C ^ D)('_'),
#                                 (D ^ A)('_')])

#         return A, B, C, D


class EquilateralTriangleOnPlane(ShapeOnPlane):

    point_A = [
        Point(x, y, z) for x in [8] for y in [5, 5.5, 6, 6.5]
        for z in [8]
    ]

    point_O = [
        Point(x, y, z) for x in [5, 5.5, 6, 6.5] for y in [8, 8.5, 9, 9.5, 10]
        for z in [4, 4.5, 5, 5.5]
    ]

    point_P = [
        Point(x, y, z) for x in [1, 1.5, 2, 2.5] for y in [2, 2.5, 3, 3.5]
        for z in [1, 1.5, 2, 2.5]]
    
    
    def _solution(self):
        current_obj = copy.deepcopy(self)

        A = current_obj.point_A
        O = current_obj.point_O
        P = current_obj.point_P

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
        current_obj.add_solution_step('Axis of rotation',
                                      [(A ^ point_P1)('AO'), point_P1,
                                       (P ^ point_P1)('a'), 
                                       point_P2,
                                       #line_f,
                                      ])

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
        O0 =current_obj.O0 = O.rotate_about(axis=line_k)('O_0')
        current_obj.point_A_0 = A0
        current_obj.add_solution_step('Point A rotation', [A0])
        current_obj.add_solution_step('Point O rotation', [O0])
        elems = [current_obj.point_A_0]
        projections = [
            current_obj.point_A_0 @ HPP, current_obj.point_A_0 @ VPP
        ]
        current_set += [*elems, *projections]
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


        current_obj.add_solution_step('Base ABC', [A, B, C])

        current_obj.point_B = B
        current_obj.point_C = C

        return current_obj



class SquareOnPlane(ShapeOnPlane):

    def _solution(self):
        current_obj = copy.deepcopy(self)

        A = current_obj.point_A
        O = current_obj.point_O
        P = current_obj.point_P

        S = (A @ (O ^ P))('S')  #'Srodek' podstawy

        dirPS = P - S
        dirOS = O - S
        dirAS = S - A
        square_diagonal = 2 * A.distance(S)

        ########################   it's base (square) definition ################

        print(square_diagonal)
        B = (S + dirPS / (P.distance(S)) * (square_diagonal / 2))('B')
        D = (S - dirPS / (P.distance(S)) * (square_diagonal / 2))('D')
        C = (A + 2 * dirAS)('C')

        #         line_AD=A^D
        #         line_AB=A^B
        #         line_BC=line_AD.parallel_line(P)
        #         line_AS=Line(A,S)
        #         C=line_BC.intersection(line_AS)[0]

        ########################   it's base (square) definition ################

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

        line_kk = Line(P, S_I)('k')

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

        square_plane = Plane(A, B, C)

        elems += [
            line_a,
        ]

        current_obj.point_B = B
        current_obj.point_C = C
        current_obj.point_D = D
        current_obj.add_solution_step('', [
            current_obj.point_B, current_obj.point_C, current_obj.point_D,
            current_obj.A0, current_obj.B0, current_obj.C0, current_obj.D0
        ])

        return current_obj


class IsoscelesRightTriangleOnPlane(ShapeOnPlane):

    point_A = [
        Point(x, y, z) for x in [8] for y in [5, 5.5, 6, 6.5]
        for z in [8]
    ]

    point_O = [
        Point(x, y, z) for x in [5, 5.5, 6, 6.5] for y in [8, 8.5, 9, 9.5, 10]
        for z in [4, 4.5, 5, 5.5]
    ]

    point_P = [
        Point(x, y, z) for x in [1, 1.5, 2, 2.5] for y in [2, 2.5, 3, 3.5]
        for z in [1, 1.5, 2, 2.5]]
    
    
    def _solution(self):
        current_obj = copy.deepcopy(self)

        A = current_obj.point_A
        O = current_obj.point_O
        P = current_obj.point_P

        S = (A @ (O ^ P))('S')  #'Srodek' podstawy

        dirPS = P - S
        dirOS = O - S
        triangle_height = A.distance(S)
        #triangle_side = triangle_height / ((3**(1 / 2)) / 2)

        B = S('B')
        C = (S - dirPS / (P.distance(S)) * (triangle_height))('C')

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
        current_obj.add_solution_step('Axis of rotation',
                                      [(A ^ point_P1)('AO'), point_P1,
                                       (P ^ point_P1)('a'), 
                                       point_P2,
                                       #line_f,
                                      ])

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
        O0 =current_obj.O0 = O.rotate_about(axis=line_k)('O_0')
        current_obj.point_A_0 = A0
        current_obj.add_solution_step('Point A rotation', [A0])
        current_obj.add_solution_step('Point O rotation', [O0])
        elems = [current_obj.point_A_0]
        projections = [
            current_obj.point_A_0 @ HPP, current_obj.point_A_0 @ VPP
        ]
        current_set += [*elems, *projections]
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


        current_obj.add_solution_step('Base ABC', [A, B, C])

        current_obj.point_B = B
        current_obj.point_C = C

        return current_obj
    

class Triangular(Shape):


    def _solution(self):
        current_obj = copy.deepcopy(self)

        A = current_obj.point_A
        B = current_obj.point_B
        C = current_obj.point_C

        current_obj.add_solution_step('Assumptions', [A, B, C])
        current_set = DrawingSet(*current_obj._solution_step[-1])

        plane_alpha = Plane(A, B, C)


        elems = [plane_alpha]

        projections = [
            plane_alpha @ HPP,
            plane_alpha @ VPP,
        ]

        current_set += [*elems, *projections]

        current_obj._solution_step.append(current_set)
#        current_obj._assumptions += [DrawingSet(*elems, *projections)]

        return current_obj


class Tetragonal(Shape):

    def _solution(self):
        current_obj = copy.deepcopy(self)

        A = current_obj.point_A
        B = current_obj.point_B
        C = current_obj.point_C
        Z = current_obj.point_Z


        current_set = DrawingSet(*current_obj._solution_step[-1])

        plane_alpha = Plane(A, B, C)
        line_z = Line(Z, Z @ HPP)


        elems = [A, B, C, plane_alpha]

        projections = [
            plane_alpha @ HPP, plane_alpha @ VPP
        ]

        current_set += [*elems, *projections]
# Probably intersection - do usunięcia?
        current_obj.horizontal_line_cross_BC = (HorizontalPlane(A) &
                                                (B ^ C))[0]
        current_obj.frontal_line_cross_BC = (VerticalPlane(A) & (B ^ C))[0]

#        current_obj._assumptions += [DrawingSet(*elems, *projections)]

        return current_obj




class Parallelogram(GeometricalCase):

    point_A = [Point(x,y,z) for x in [1,1.5,2,2.5] for y in [2,2.5,3,3.5,4,4.5,5] for z in [2,2.5,3,3.5]  ]

    point_B=  [Point(x,y,z) for x in range(4,6) for y in range(8,12) for z in [2,2.5,3,3.5] ]
    
    point_C = [Point(x,y,z) for x in [1,1.5,2,2.5] for y in [13,13.5,14,14.5,15] for z in [6,6.5,7] ]
    
    point_O = [Point(x,y,z) for x in range(7,10) for y in [6,6.5,7,7.5,8.5] for z in range(6,9) ]
    
    shift = [
        Point(x, y, z) for x in [-1, -0.5, 0, 0.5, 1]
        for y in [ -1.5, -1, -0.5]
        for z in [-1, -0.5, 0, 0.5, 1]
    ]
    
    def __init__(self,
                 point_A=None,
                 point_B=None,
                 point_C=None,
                 point_O=None,
                 **kwargs):

        super().__init__()

        if point_A and point_B and point_C and point_O:
            projections = (
                point_A @ HPP,
                point_B @ HPP,
                point_C @ HPP,
                #point_O @ HPP,
                point_A @ VPP,
                point_B @ VPP,
                point_C @ VPP,
                #point_O @ VPP,
                #Plane(point_A@HPP,point_B@HPP,point_C@HPP),Plane(point_A@VPP,point_B@VPP,point_C@VPP),
            )
        else:
            projections = []

        self._assumptions = DrawingSet(*projections)

        self._point_A = point_A
        self._point_B = point_B
        self._point_C = point_C
        self._point_O = point_O

        self._given_data = {
            'A': point_A,
            'B': point_B,
            'C': point_C,
            'O': point_O,
        }

        self.add_solution_step('Assumptions',
                               [point_A, point_B, point_C])
        self._assumptions3d = DrawingSet(point_A, point_B, point_C)('Assumptions')
        self._assumptions = DrawingSet(*projections)

    @property
    def _shape_plane(self):
        
        current_obj = self
        
        A = current_obj._point_A
        B = current_obj._point_B
        C = current_obj._point_C
        O = current_obj._point_O
        
        return Plane(A, B, C)
        
    def _solution(self):
        current_obj = copy.deepcopy(self)

        A = current_obj._point_A
        B = current_obj._point_B
        C = current_obj._point_C
        O = current_obj._point_O

        current_set = DrawingSet(*current_obj._solution_step[-1])

        plane_alpha = Plane(A, B, C)

        point_P1 = (HorizontalPlane(A) & (B ^ C))[0]('1')
        point_P2 = (VerticalPlane(A) & (B ^ C))[0]('2')

        current_obj.horizontal_line_cross_BC = point_P1
        current_obj.frontal_line_cross_BC = point_P2

        current_obj.add_solution_step('Horizontal and forntal lines',
                               [point_P1, point_P2,point_P1^A, point_P2^A])
        
        #         plane_beta=Plane(O,O+(B-A),O-(C-A))
        #         D=(A@plane_beta)('D')
        #         E=(B@plane_beta)('E')
        #         F=(C@plane_beta)('F')
        #         plane_gamma=Plane(D,E,F)

        triangle_plane = Plane(A, B, C)
        
        
        D = Point((A + (C - B)).coordinates)('D')
        
        #A, B, C, E, F, G = Prism.right_from_parallel_plane(triangle_plane, O)

        #plane_gamma = Plane(D,E,F)
        
        line_ad = Line(A, D)('a')
#         line_be = Line(B, E)('b')
#         line_cf = Line(C, F)('c')

        plane_aux = Plane(A, D, A + Point(5, 0, 0))

        #point_P3 = (((O - (point_P1 - A)) ^ O)('h_H') & plane_aux)[0]('3')
        #point_P4 = (((O - (point_P2 - A)) ^ O)('f_H') & plane_aux)[0]('4')

        #current_obj.add_solution_step('Piercing point',
        #                              [point_P3, point_P4])


        #elems = [ plane_alpha, plane_gamma, line_ad,# line_be, line_cf
                #]
        elems = [ plane_alpha, line_ad,# line_be, line_cf
                ]

        projections = [
            line_ad @ HPP,
            line_ad @ VPP,
            #line_be @ HPP,
            #line_be @ VPP,
            #line_cf @ HPP,
            #line_cf @ VPP,
            D @ HPP,
            D @ VPP,
#             E @ HPP,
#             E @ VPP,
#             F @ HPP,
#             F @ VPP,
        ]

        current_set += [*elems, *projections]

        current_obj._solution_step.append(current_set)
        current_obj.point_D = D
        #current_obj.point_E = E
        #current_obj.point_F = F
        current_obj._assumptions = DrawingSet(
            *current_obj.get_projections())('Solution')
        current_obj._assumptions3d = DrawingSet(*current_obj)

        current_obj.add_solution_step('D vertex', [D])
        
        return current_obj


    def get_default_data(self):

        point_A = self.__class__.point_A
        point_B = self.__class__.point_B
        point_C = self.__class__.point_C
        point_O = self.__class__.point_O
        shift = self.shift

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
    
    
class ParallelogramHFLines(Parallelogram):
    

    def get_random_parameters(self):

        parameters_dict=super().get_random_parameters()



        point_A=parameters_dict[Symbol('A')]
        point_B=parameters_dict[Symbol('B')] 
        point_C=parameters_dict[Symbol('C')] 

        
        parameters_dict[Symbol('C')]=Point(point_A.x,point_C.y,point_C.z)
        parameters_dict[Symbol('B')]=Point(point_B.x,point_B.y,point_A.z)

        return parameters_dict
    
class EdgeParallelogram(Parallelogram):
    
    def get_random_parameters(self):

        parameters_dict = super().get_random_parameters()

        point_A = parameters_dict[Symbol('A')]
        point_C = parameters_dict[Symbol('C')]

        parameters_dict[Symbol('B')] = (point_A + point_C) * 0.5 + Point(0, 0, 3)

        return parameters_dict
    
    
    
class TiltedTetragonalOnPlane(ShapeOnPlane):

    def _solution(self):

        current_obj = copy.deepcopy(self)

        A = current_obj.point_A
        B = current_obj.point_B
        C = current_obj.point_C
        Z = current_obj.point_Z
        O = current_obj.point_O

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
    
class TruncatedParallelogramOnPlane(ShapeOnPlane):

    def _solution(self):
        current_obj = copy.deepcopy(self)

        A = current_obj.point_A
        B = current_obj.point_B
        C = current_obj.point_C

        M = current_obj.point_M
        N = current_obj.point_N
        O = current_obj.point_O

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
    
class VerticalTiltedTetragonalOnPlane(ShapeOnPlane):

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

class HorizontalTiltedTetragonalOnPlane(ShapeOnPlane):

    def _solution(self):


        current_obj = copy.deepcopy(self)

        A = current_obj.point_A
        B = current_obj.point_B
        C = current_obj.point_C
        Z = current_obj.point_Z
        O = current_obj.point_O

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
    
class GivenHeightEquilateralTriangleOnPlane(ShapeOnPlane):

    def _solution(self):
        current_obj = copy.deepcopy(self)

        A = current_obj.point_A
        O = current_obj.point_O
        P = current_obj.point_P

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

        current_obj.point_B = B
        current_obj.point_C = C
        current_obj.point_D = D

        return current_obj
    
class GivenHeightIsoscelesRightTriangleOnPlane(ShapeOnPlane):

    def _solution(self):
        current_obj = copy.deepcopy(self)

        A = current_obj.point_A
        O = current_obj.point_O
        P = current_obj.point_P

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

        current_obj.point_B = B
        current_obj.point_C = C
        current_obj.point_D = D

        #current_obj._assumptions = DrawingSet(*projections)("Solution")
        
        return current_obj
    
class GivenHeightSquareOnPlane(ShapeOnPlane):

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
        
        current_obj.point_B = B
        current_obj.point_C = C
        current_obj.point_D = D

        return current_obj
    
class GivenHeightRhomboidOnPlane(ShapeOnPlane):

    def _solution(self):

        current_obj = copy.deepcopy(self)

        A = current_obj.point_A
        O = current_obj.point_O
        P = current_obj.point_P

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


        current_obj.point_B = B
        current_obj.point_C = C
        current_obj.point_D = D

        return current_obj