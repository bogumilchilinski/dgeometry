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

        
        self._given_data={'A':point_A,'P':point_P,'O':point_O}
        
        self._solution_step.append(self._assumptions)


    def _rotation_of_base(self,base_plane):
        
        return base_plane

    def _base_shape(self,base_plane):
        
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
            
            
            

            ##################   plane rotation

            ### Step 2 #####
            ###  plane of rotation of A ####
            
            line_k = Line(P, (O @ line_k))('k')

            A0_rotation_case = RotatedPoint(A,axis=line_k)
            current_obj._append_case(A0_rotation_case)
            
            A0 = A0_rotation_case._rotated_point('A_0')
            current_obj.A0 = A0
            
            O0_rotation_case = RotatedPoint(O,axis=line_k)
            current_obj._append_case(O0_rotation_case)
            
            O0 = O0_rotation_case._rotated_point('O_0')
            current_obj.O0 = O0

            
            points_of_base=current_obj._base_shape([A,P,O])
            
            
            rotated_base = []
            
            for base_point  in points_of_base:
                
            
                point0 = base_point.rotate_about(axis=line_k)(f'{base_point._label}_0')
                rotated_base += [point0]

                current_obj.add_solution_step(f'Creating a point {point0._label} based on triangle geometry', [point0])

            #### Step 4 ####
            ### postion of B0 (based on triangle geometry) #####

            for rotated_point,base_point  in zip(rotated_base,points_of_base):
            
                rotP = rotated_point
                
                
                if ((rotP@line_k).distance(rotP)) != 0:
                    rotP_e1=rotP+((rotP@line_k)-rotP)/((rotP@line_k).distance(rotP))*(1.2*((rotP@line_k).distance(rotP)))
                    rotP_e2=(rotP@line_k)+((rotP@line_k)-rotP)/((rotP@line_k).distance(rotP))*(-1.2*((rotP@line_k).distance(rotP)))

                    current_obj.add_solution_step('Reverse point B0 rotation - plane of rotation of B0 point', [((rotP_e1)^rotP_e2)('e_B')])
                    current_obj.add_solution_step('Reverse point B0 rotation - getting a point B in the space', [base_point])



            self._cached_solution = current_obj
            current_obj._cached_solution = current_obj
        else:
            current_obj = copy.deepcopy(self._cached_solution)
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


        
        default_data_dict = {
            Symbol('A'): point_A,
            Symbol('P'): point_P,
            Symbol('O'): point_O,



        }
        return default_data_dict
        
        
    
class SquareOnPlane(GeometricalCase):


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

        
        self._given_data={'A':point_A,'P':point_P,'O':point_O}
        
        self._solution_step.append(self._assumptions)


    

    def solution(self):
        if self._cached_solution is None:
            current_obj = copy.deepcopy(self)

            A = current_obj._point_A
            O = current_obj._point_O
            P = current_obj._point_P



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

            # it creates next step of solution - lines are presented
            #current_step3d=copy.deepcopy(current_obj._solution3d_step[-1])+[(A^point_P1)('AO'),point_P1,(P^point_P1)('a')]

            #it sets the step elements

            elems = self._assumptions
            projections = []
            point_0_dict = {}
            eps_dict = {}

            point_B = B
            point_C = C
            point_O = O

            ##################   plane rotation

            ### Step 2 #####
            ###  plane of rotation of A ####
            
            line_kk = Line(P, (O @ line_k))('k')

            A0 = A.rotate_about(axis=line_k)('A_0')
            current_obj.A0 = A0
            
            A0_e1=A0+((A0@line_k)-A0)/((A0@line_k).distance(A0))*(1.2*((A0@line_k).distance(A0)))
            A0_e2=(A0@line_k)+((A0@line_k)-A0)/((A0@line_k).distance(A0))*(-1.2*((A0@line_k).distance(A0)))
            
            current_obj.add_solution_step('''Plane rotation - it is creating projection of {O._label} on the planes intersection''', [((A0_e1)^A0_e2)('e_A')])

            #### Step 3 ####
            ### rotated point A0 of A #####
            
            current_obj.add_solution_step('Point A rotation by using a rotation plane', [A0])

            B0 = B.rotate_about(axis=line_k)('B_0')
            current_obj.B0 = B0
            
            current_obj.add_solution_step('Creating a point B0 based on triangle geometry', [B0])

            #### Step 4 ####
            ### postion of B0 (based on triangle geometry) #####

            C0 = C.rotate_about(axis=line_k)('C_0')
            current_obj.C0 = C0
            current_obj.add_solution_step('Creating a point C0 based on triangle geometry', [C0])

            #### Step 5 ####
            ### postion of C0 (based on triangle geometry) #####

            D0 = D.rotate_about(axis=line_k)('D_0')
            current_obj.D0 = D0
            current_obj.add_solution_step('Creating a point D0 based on triangle geometry', [D0])

            #current_obj.D0=D.rotate_about(axis=line_k)('D_0')
            current_obj.O0 = O.rotate_about(axis=line_k)('O_0')
            
            B0_e1=B0+((B0@line_k)-B0)/((B0@line_k).distance(B0))*(1.2*((B0@line_k).distance(B0)))
            B0_e2=(B0@line_k)+((B0@line_k)-B0)/((B0@line_k).distance(B0))*(-1.2*((B0@line_k).distance(B0)))
            
            current_obj.add_solution_step('Reverse point B0 rotation - getting a point B in the space', [B,((B0_e1)^B0_e2)('e_B')])
            
            C0_e1=C0+((C0@line_k)-C0)/((C0@line_k).distance(C0))*(1.2*((C0@line_k).distance(C0)))
            C0_e2=(C0@line_k)+((C0@line_k)-C0)/((C0@line_k).distance(C0))*(-1.2*((C0@line_k).distance(C0)))
            
            current_obj.add_solution_step('Reverse point C0 rotation - getting a point C in the space', [C,((C0_e1)^C0_e2)('e_C')])
            
            D0_e1=D0+((D0@line_k)-D0)/((D0@line_k).distance(D0))*(1.2*((D0@line_k).distance(D0)))
            D0_e2=(D0@line_k)+((D0@line_k)-D0)/((D0@line_k).distance(D0))*(-1.2*((D0@line_k).distance(D0)))
            
            current_obj.add_solution_step('Reverse point D0 rotation - getting a point D in the space', [D,((D0_e1)^D0_e2)('e_D')])
            
            line_AB=(A^B)('AB')
            line_BC=(B^C)('BC')
            line_CD=(C^D)('CD')
            line_DA=(D^A)('DA')
            
            current_obj.add_solution_step('Creating a square', [line_AB,line_BC,line_CD,line_DA])
            
            current_obj.add_solution_step('Drawn square', [A,B,C,D])

            self._cached_solution = current_obj
            current_obj._cached_solution = current_obj
        else:
            current_obj = copy.deepcopy(self._cached_solution)
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
    