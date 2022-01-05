from typing import List
import numpy as np
import sympy as sym
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


class GivenHeightIsoscelesRightTrianglePrism(GeometricalCase):

    point_A = [Point(x,y,z) for x in [6,6.5] for y in [7,7.5,8] for z in   [8,8.5]  ]
    point_O = [Point(x,y,z) for x in [3,3.5,4,4.5] for y in [2,2.5,3] for z in  [2,2.5,3,4,5]]
    point_P = [Point(x,y,z) for x in [2,2.5] for y in [10,10.5,11]  for z in [4,5,6] ]
    point_H = [Point(x,y,z) for x in [9,9.5,10] for y in [2,2.5,3] for z in range(6,8) ]
    
    shift = [Point(x,y,z) for x in [-3,-2.5,-2,-1,-0.5,0,0.5,1] for y in [2,2.5,3] for z in [-2,-1.5,-1,-0.5,0] ]
    


    

    def __init__(self, point_A=None, point_P=None, point_O=None, point_H=None, *args, **kwargs):

        super().__init__()


        if point_A and point_O and point_P:  ### and point_H
            projections=(point_A@HPP,point_O@HPP,point_O@VPP,point_P@VPP,point_P@HPP,point_A@VPP,point_H@VPP,point_H@HPP)  
            
        else:
            projections=[]


            
        # First step
        self.add_solution_step('Assumptions',[point_A,point_O,point_P,point_H])
        self._assumptions3d=DrawingSet(point_A,point_O,point_P,point_H)('Assumptions')
        self._assumptions=DrawingSet(*projections)
        #self._assumptions3d=DrawingSet(point_A,point_O,point_P,point_H)('Assumptions')
        
        #self += [point_A,point_O,point_P,point_H]

        self._point_A=point_A
        self._point_P=point_P
        self._point_O=point_O
        self._point_H=point_H
        self._given_data={'A':point_A,'P':point_P,'O':point_O,'H':point_H}
        


    def solution(self):
        if self._cached_solution is None:
            current_obj=copy.deepcopy(self)

            A=current_obj._point_A
            O=current_obj._point_O
            P=current_obj._point_P
            H=current_obj._point_H


            S = (A @ (O^P))('S') # Middle of the base, of the triangle.

            dirPS = P-S
            dirOS = O-S
            triangle_height = A.distance(S).n(5)
            triangle_side =  triangle_height / ((3**(1/2))/2)

            B = (S + dirPS/(P.distance(S))*(triangle_height))('B')
            C = (S - dirPS/(P.distance(S))*(triangle_height))('C')
            triangle_plane=Plane(A,B,C)

            current_set=DrawingSet(*current_obj._solution_step[-1])

            line_a=Line(A,B)('a')
            line_b=Line(C,A)('b')
            plane_alpha=Plane(A,O,P)

            plane_beta=HorizontalPlane(P)
            plane_eta=VerticalPlane(P)



            line_k = plane_alpha.intersection(plane_beta)[0]('a')


            point_P1 = plane_beta.intersection(A^O)[0]('1')
            point_P2 = plane_eta.intersection(A^O)[0]('2')
            current_obj.P1=point_P1
            line_kk = (P^point_P1)('a')
            line_f = (P^point_P2)('f')


            # it creates next step of solution - lines are presented
            current_step3d=copy.deepcopy(current_obj._solution3d_step[-1])+[(A^point_P1)('AO'),point_P1,(P^point_P1)('a')]

            #it sets the step elements
            current_obj.add_solution_step('Axis of rotation',[(A^point_P1)('AO'),point_P1,(P^point_P1)('a'),point_P2,line_f])



            elems=self._assumptions
            projections=[]
            point_0_dict={}
            eps_dict={}


            point_B=B
            point_C=C
            point_O=O


            ##################   plane rotation

            line_kk=Line(P, (O@line_k)  )('k')

            A0=A.rotate_about(axis=line_k)('A_0')
            current_obj.A0=A0

            ### Step 2 #####
            ###  plane of rotation of A ####

            current_obj.add_solution_step('Point A rotation',[A0])

            #### Step 3 ####
            ### rotated point A0 of A #####




            B0=B.rotate_about(axis=line_k)('B_0')
            current_obj.B0=B0

            current_obj.add_solution_step('Point B rotation',[B0])

            #### Step 4 ####
            ### postion of B0 (based on triangle geometry) #####       




            C0=C.rotate_about(axis=line_k)('C_0')
            current_obj.C0=C0
            current_obj.add_solution_step('Point C rotation',[C0])

            #### Step 5 ####
            ### postion of C0 (based on triangle geometry) #####      

            #current_obj.D0=D.rotate_about(axis=line_k)('D_0')
            current_obj.O0=O.rotate_about(axis=line_k)('O_0')
            line_ab=Line(A,B)('|AB|')
            line_bc=Line(B,C)('|BC|')
            line_ca=Line(C,A)('|CA|')
            
            current_obj.add_solution_step('Base ABC',[A,B,C,line_ab,line_bc,line_ca])



            G = (H@plane_alpha)('G')


            ############  upper  base

            dirHG = H-G
            distance_HG = (H.distance(G)).n(5)



            #D = (A + dirHG/distance_HG*triangle_height)('D')
            #E = (B + dirHG/distance_HG*triangle_height)('E')
            #F = (C + dirHG/distance_HG*triangle_height)('F')

            A,B,C,D,E,F = Prism(triangle_plane, dirHG/distance_HG*triangle_height)



            line_de=Line(D,E)('|DE|')
            line_ef=Line(E,F)('|EF|', color='g')
            line_fd=Line(F,D)('|FD|')
            
            current_obj.add_solution_step('Prism',[D,E,F,line_de,line_ef,line_fd])
            
            line_eb=Line(E,B)('|EB|')
            line_da=Line(D,A)('|DA|')
            line_fc=Line(F,C)('|FC|')
            
            current_obj.add_solution_step('Vertices D,E,F',[D,E,F,line_de,line_fd,line_ab,line_bc,line_ca,line_eb,line_da,line_fc])
            
            current_obj._assumptions=DrawingSet(*current_obj.get_projections())('Solution')
            current_obj._assumptions3d=DrawingSet(*current_obj)

            current_obj._point_B=B
            current_obj._point_C=C
            current_obj.point_D=D
            current_obj.point_E=E
            current_obj.point_F=F
           

            self._cached_solution = current_obj
        else:
            current_obj = copy.deepcopy(self._cached_solution)
        return current_obj

        return current_obj

    def present_solution(self):
        
        doc_model = Document(f'{self.__class__.__name__} solution')

        doc_model.packages.append(Package('booktabs'))
        doc_model.packages.append(Package('float'))
        doc_model.packages.append(Package('standalone'))
        doc_model.packages.append(Package('siunitx'))


        #ReportText.set_container(doc_model)
        #ReportText.set_directory('./SDAresults')

        for no,step3d in enumerate(self._solution3d_step):
            GeometryScene()
            
            for elem in range(no):
                self._solution3d_step[elem].plot(color='k')
                self._solution_step[elem].plot_vp( ='k').plot_hp(color='k')
                
            
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
        point_P=self.__class__.point_P
        point_H=self.__class__.point_H

        
        shift = self.__class__.shift


        
        default_data_dict = {
            Symbol('A'): point_A,
            Symbol('P'): point_P,
            Symbol('O'): point_O,
            Symbol('H'): point_H,
            'shift':shift



        }
        return default_data_dict

    
    def get_random_parameters(self):
        


        parameters_dict=super().get_random_parameters()

        point_H=parameters_dict[Symbol('H')] 
        point_O=parameters_dict[Symbol('O')] 
        point_A=parameters_dict[Symbol('A')] 
        point_P=parameters_dict[Symbol('P')]
        
        shift = parameters_dict['shift']
        parameters_dict.pop('shift')
      

        for point in symbols('A P O H'): 
            parameters_dict[point]=parameters_dict[point] + shift

        

        return parameters_dict
    


