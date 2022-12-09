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
        

        rot_point = point.rotate_about(axis=axis,plane=plane)(f'{point._label}')
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
        

        rot_point = point.rotate_about(axis=axis,plane=plane)(f'{point._label}_0')
        self._rotated_point = rot_point
        
        axis = rot_point._axis
        plane = rot_point._plane
        
        rot_center=(point@axis)
        
        self.add_solution_step(f'The ${point._label}$ point and axis of rotation ${axis._label}$ are currently highlighted - initial set for rotation process',[point,axis])
        
        if rot_center.coordinates == rot_point.coordinates:

            self.add_solution_step(f'Rotated point ${rot_point._label}$ is the same as {point._label} point.',[rot_point(f'{point._label} = ${point._label}_0$')])
            
        else:    


            point_e1=rot_point+(rot_center-rot_point)*(1+(0.5/rot_center.distance(rot_point)))
            point_e2=(rot_center)+((rot_center)-rot_point)*(-1-(0.5/rot_center.distance(rot_point)))

            self._eps_for_point = (point_e1^point_e2)(f'eps_{point._label}')

            self.add_solution_step(f'A rotation plane of {point._label} point passes {point._label} and is perpendicular to the {point._label} axis. \n \n ${point._label} \in \epsilon_{point._label}$         $\epsilon_{point._label}  \perp$ {axis._label}',[self._eps_for_point(f'eps_{point._label}')])

            self.add_solution_step(f'$S_{point._label}$ point - center of rotation \n \n $S_{point._label}: \epsilon_{point._label} \wedge {axis._label}$',[rot_center])

            


            self.add_solution_step(f'''The position of ${point._label}_0$ point can be determined by utilization of true length of the radius of rotation $({point._label} - S_{point._label}$)
            - the pytagoras theorem has to be applied (auxiliary right triangle)''',[rot_point(f'{point._label}')],caption='$\\square$')
    
    
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
            f'''The ${rot_point._label}$ rotated point, axis of rotation ${axis._label}$ and ${reference._label}$ line are currently highlighted 
            - data needed to find orginal position of the point''',[rot_point,axis,reference])
        
        if rot_center.coordinates == rot_point.coordinates:

            self.add_solution_step(f'$ {rot_point._label} \in {point._label} $   %%%   Rotated point ${rot_point._label}$ is the same as ${point._label}$ point - there is nothing to do',[rot_point(f'${point._label}_0 = {point._label}$')])
            
        else:


            point_e1=rot_point+(rot_center-rot_point)*(1+(0.5/rot_center.distance(rot_point)))
            point_e2=(rot_center)+((rot_center)-rot_point)*(-1-(0.5/rot_center.distance(rot_point)))

            self._eps_for_point = (point_e1^point_e2)(f'$\epsilon_{point._label}$')

            self.add_solution_step(f'A rotation plane of  point ${point._label}$ passes  ${rot_point._label}$  and is perpendicular to ${axis._label}$ axis.',[self._eps_for_point(f'$eps_{point._label}$')])

            self.add_solution_step(f'$S_{point._label}$ point - Center of rotation',[rot_center])

            


            self.add_solution_step(f'''The true position of {point._label} can be found as intersection of plane of rotation {self._eps_for_point._label} and ${reference._label}$ line - 
            {point._label} belongs simultaneously to {self._eps_for_point._label} and ${reference._label}$''',[point(f'{point._label}')])
            
            
            
class LineRotation(GeometricalCase):


    point_A = [Point(x,y,z) for x in [1,1.5,2,2.5,3,3.5] for y in [2,2.5,3,3.5,4] for z in [1,1.5,2,2.5,3,3.5] ]

    point_B=[Point(x,y,z) for x in [4,4.5,5,5.5,6,6.5] for y in [6.5,7,7.5,8,8.5,9] for z in [4,4.5,5,5.5,6,6.5] ]

    def __init__(self,point_A=None,point_B=None,**kwargs):

        super().__init__()

        if point_A and point_B:
            projections=(point_A@HPP,point_B@HPP,point_A@VPP,point_B@VPP)
        else:
            projections=[]

        self._assumptions=DrawingSet(*projections)

        self._point_A=point_A
        self._point_B=point_B

        self._given_data={'A':point_A,'B':point_B,}

        self._solution_step.append(self._assumptions)

    def solution(self):
        if self._cached_solution is None:
            
            current_obj = self._solution()
            self._cached_solution = current_obj
        else:
            current_obj = copy.deepcopy(self._cached_solution)
        return current_obj
        
    def _solution(self):
        current_obj=copy.deepcopy(self)

        A=current_obj._point_A
        B=current_obj._point_B

        current_set=DrawingSet(*current_obj._solution_step[-1])

        line_a=Line(A,B)('a')
        S=Point(B.x,B.y,A.z)('S')
        current_obj.add_solution_step('S',[S])
        line_l=Line(B,S)('l')
        epsilon=HorizontalPlane(A)
        A_0=Point(B.x,B.y+(B@HPP).distance(A@HPP),A.z)
        current_obj.add_solution_step('A0',[A_0])
        line_k=Line(B,A_0)

        elems=[line_a,S,line_l,epsilon,A_0,line_k,]

        projections=[line_l@HPP,line_k@HPP,line_l@VPP,line_k@VPP,line_a@HPP,line_a@VPP,S@VPP,S@HPP,A_0@VPP,A_0@HPP]
        current_set+=[*elems,*projections]

        current_obj._solution_step.append(current_set)
        current_obj.point_S=S

        current_obj.point_A_0=A_0
        current_obj._assumptions=DrawingSet(*elems,*projections)
        return current_obj

    def get_default_data(self):

        point_A = self.__class__.point_A
        point_B = self.__class__.point_B
        
        default_data_dict = {
            Symbol('A'): point_A,
            Symbol('B'): point_B,
        }
        return default_data_dict

class PlaneRotation(GeometricalCase):


    point_A=[Point(x,y,z) for x in  [6,7] for y in [11,11.5,12] for z in   [2.5,3,3.5] ]
    
    point_B = [Point(x,y,z) for x in [3,3.5] for y in [8,8.5,9] for z in   [6,7]  ]



    point_C = [Point(x,y,z) for x in [1,1.5,2] for y in [3,3.5]  for z in [1,1.5,2] ]





    def __init__(self,point_A=None,point_B=None,point_C=None,**kwargs):

        super().__init__()

        if point_A and point_B and point_C:
            projections=(point_A@HPP,point_B@HPP,point_A@VPP,point_B@VPP,point_C@HPP,point_C@VPP,)
        else:
            projections=[]

        self._assumptions=DrawingSet(*projections)

        self.point_A=point_A
        self.point_B=point_B
        self.point_C=point_C

        
        self._given_data={'A':point_A,'B':point_B,'C':point_C}
        
        self._solution_step.append(self._assumptions)

        
    def _solution(self):
        current_obj=copy.deepcopy(self)
        
        A=current_obj.point_A
        B=current_obj.point_B
        C=current_obj.point_C


        
        current_set=DrawingSet(*current_obj._solution_step[-1])

        line_a=Line(A,B)('a')
        line_b=Line(C,A)('b')
        plane_alpha=Plane(A,B,C)

        plane_beta=HorizontalPlane(C)

        line_k = plane_alpha.intersection(plane_beta)[0]

        elems=self._assumptions
        projections=[]
        point_0_dict={}
#         for point_I in [A,B]:
        
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
#             #projections+=[I_o@HPP,I_o@VPP]

        current_obj.point_A_0 = A.rotate_about(axis=line_k)('A_0')
        current_obj.point_B_0 = B.rotate_about(axis=line_k)('B_0')
        current_obj.point_C_0 = C.rotate_about(axis=line_k)('C_0')


            
        #line_kk=Line(C,S_I)
        #print(point_0_dict)
        elems+=[line_a,line_b,#,E,F,G,H,line_s1,line_s2,line_s3,line_s4
              ]

        projections+=[line_a@HPP,line_a@VPP,line_b@HPP,line_b@VPP,
                      #line_kk@HPP,line_kk@VPP,#line_s1@HPP,line_s1@VPP,line_s2@HPP,line_s2@VPP,line_s3@HPP,line_s3@VPP,
                     #line_s4@HPP,line_s4@VPP
                    ]
        current_set+=[*elems,*projections]
#         current_obj.point_A_0=point_0_dict['A']
#         current_obj.point_B_0=point_0_dict['B']
        current_obj.point_C_0=C
        current_obj.add_solution_step('A0',[current_obj.point_A,current_obj.point_A_0])
        current_obj.add_solution_step('B0',[current_obj.point_B,current_obj.point_B_0])
        current_obj.add_solution_step('C0',[current_obj.point_C,current_obj.point_C_0])
        current_obj._solution_step.append(current_set)
        current_obj._assumptions=DrawingSet(*elems,*projections)

        return current_obj

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

class EdgePlaneRotation(PlaneRotation):
    def get_random_parameters(self):

        parameters_dict = super().get_random_parameters()

        point_A = parameters_dict[Symbol('A')]
        point_C = parameters_dict[Symbol('C')]

        parameters_dict[Symbol('B')] = (point_A + point_C) * 0.5 + Point(0, 0, 3)

        return parameters_dict
    
class IsoscelesRightTriangleRotation(GeometricalCase):


    point_A = [Point(x,y,z) for x in [3,3.5] for y in [8,8.5,9] for z in   [6,7]  ]

    point_O=[Point(x,y,z) for x in  [6,7] for y in [11,11.5,12] for z in   [2.5,3,3.5] ]

    point_P = [Point(x,y,z) for x in [1,1.5,2] for y in [3,3.5]  for z in [1,1.5,2] ]


    

    def __init__(self,point_A=None,point_P=None,point_O=None,**kwargs):

        super().__init__()

        if point_A and point_O and point_P:
            projections=(point_A@HPP,point_O@HPP,point_O@VPP,point_P@VPP,point_P@HPP,point_A@VPP)
        else:
            projections=[]

        self._assumptions=DrawingSet(*projections)

        self.point_A=point_A
        self.point_P=point_P
        self.point_O=point_O


        
        self._given_data={'A':point_A,'P':point_P,'O':point_O}
        
        self._solution_step.append(self._assumptions)
        self.add_solution_step('Assumptions',
                               [point_A, point_P, point_O])
        

#     def solution(self):
#         if self._cached_solution is None:
            
#             current_obj = self._solution()
#             self._cached_solution = current_obj
#         else:
#             current_obj = copy.deepcopy(self._cached_solution)
#         return current_obj
        
    def _solution(self):
        current_obj=copy.deepcopy(self)
        
        A=current_obj.point_A
        O=current_obj.point_O
        P=current_obj.point_P

        
        S = (A @ (O^P))('S') #'Srodek' podstawy
        
        dirPS = P-S
        dirOS = O-S
        triangle_height = A.distance(S)
        #triangle_side =  triangle_height / ((3**(1/2))/2)
        
        B = (S + dirPS/(P.distance(S))*(triangle_height))('B')
        C = (S - dirPS/(P.distance(S))*(triangle_height))('C')


        
        current_set=DrawingSet(*current_obj._solution_step[-1])

        line_a=Line(A,B)('a')
        line_b=Line(C,A)('b')
        plane_alpha=Plane(A,O,P)

        plane_beta=HorizontalPlane(P)

        line_k = plane_alpha.intersection(plane_beta)[0]

        elems=self._assumptions
        projections=[]
        point_0_dict={}
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
#             elems += [I_o]
#             #projections+=[I_o@HPP,I_o@VPP]

            
#         line_kk=Line(P,S_I)('k')

        current_obj.point_A_0 = A.rotate_about(axis=line_k)('A_0')
        current_obj.point_B_0 = B.rotate_about(axis=line_k)('B_0')
        current_obj.point_C_0 = C.rotate_about(axis=line_k)('C_0')

#         current_obj.point_A_0=point_0_dict['A']
#         current_obj.point_B_0=point_0_dict['B']
#         current_obj.point_C_0=point_0_dict['C']

        
        #print(point_0_dict)
        elems+=[line_a,line_b,#,E,F,G,H,line_s1,line_s2,line_s3,line_s4
              ]

        projections+=[
            #current_obj.point_A_0@HPP,current_obj.point_A_0@VPP,current_obj.point_B_0@HPP,current_obj.point_B_0@VPP,
            #          current_obj.point_C_0@HPP,current_obj.point_C_0@VPP,
            B@HPP,B@VPP,C@HPP,C@VPP,line_a@HPP,line_a@VPP,line_b@HPP,line_b@VPP,
                    #  line_kk@HPP,line_kk@VPP,#line_s1@HPP,line_s1@VPP,line_s2@HPP,line_s2@VPP,line_s3@HPP,line_s3@VPP,
                     #line_s4@HPP,line_s4@VPP
                    ]
        current_set+=[*elems,*projections]

        current_obj._solution_step.append(current_set)
        current_obj._assumptions=DrawingSet(*elems,*projections)
#         current_obj._point_B=B
#         current_obj._point_C=C
        current_obj.point_B=B
        current_obj.point_C=C


        
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

class EdgeIsoscelesRightTriangleRotation(IsoscelesRightTriangleRotation):
    def get_random_parameters(self):

        parameters_dict = super().get_random_parameters()

        point_P = parameters_dict[Symbol('P')]
        point_O = parameters_dict[Symbol('O')]

        parameters_dict[Symbol('A')] = (point_P + point_O) * 0.5 + Point(0, 0, 5)

        return parameters_dict
    
class SquareRotation(GeometricalCase):


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

        self.point_A=point_A
        self.point_P=point_P
        self.point_O=point_O

        
        self._given_data={'A':point_A,'P':point_P,'O':point_O}
        
        self._solution_step.append(self._assumptions)

    def _solution(self):
        current_obj=copy.deepcopy(self)
        
        A=current_obj.point_A
        O=current_obj.point_O
        P=current_obj.point_P

        
        S = (A @ (O^P))('S') #'Srodek' podstawy
        
        dirPS = P-S
        dirOS = O-S
        dirAS = S-A
        square_diagonal = 2*A.distance(S)
        #square_side =  square_diagonal / (((3)**(1/2))/2)
        print(square_diagonal)
        B = (S + dirPS/(P.distance(S))*(square_diagonal/2))('B')
        D = (S - dirPS/(P.distance(S))*(square_diagonal/2))('D')
        C = (A + 2*dirAS)('C')
#         line_AD=A^D
#         line_AB=A^B
#         line_BC=line_AD.parallel_line(P)
#         line_AS=Line(A,S)
#         C=line_BC.intersection(line_AS)[0]


        
        current_set=DrawingSet(*current_obj._solution_step[-1])

        line_a=Line(A,B)('a')
        line_b=Line(B,C)('b')
        line_c=Line(C,D)('c')
        line_d=Line(D,A)('d')
        plane_alpha=Plane(A,O,P)

        plane_beta=HorizontalPlane(P)

        line_k = plane_alpha.intersection(plane_beta)[0]

        elems=self._assumptions
        projections=[]
        point_0_dict={}

        S_I = (A @ line_k)('k')
        
        current_obj.point_A_0 = A.rotate_about(axis=line_k)('A_0')
        current_obj.point_B_0 = B.rotate_about(axis=line_k)('B_0')
        current_obj.point_C_0 = C.rotate_about(axis=line_k)('C_0')
        current_obj.point_D_0 = D.rotate_about(axis=line_k)('D_0')            
        line_kk=Line(P,S_I)('k')
        

        current_obj.add_solution_step('A0',[current_obj.point_A_0])
        current_obj.add_solution_step('B0',[current_obj.point_B_0])
        current_obj.add_solution_step('C0',[current_obj.point_C_0])
        current_obj.add_solution_step('D0',[current_obj.point_D_0])
        #print(point_0_dict)
        elems+=[line_a,line_b,#,E,F,G,H,line_s1,line_s2,line_s3,line_s4
              ]

        projections+=[current_obj.point_D_0@HPP,current_obj.point_D_0@VPP,D@HPP,D@VPP,
            current_obj.point_A_0@HPP,current_obj.point_A_0@VPP,current_obj.point_B_0@HPP,current_obj.point_B_0@VPP,
                      current_obj.point_C_0@HPP,current_obj.point_C_0@VPP,B@HPP,B@VPP,C@HPP,C@VPP,line_a@HPP,line_a@VPP,line_b@HPP,line_b@VPP,
                      line_kk@HPP,line_kk@VPP,#line_s1@HPP,line_s1@VPP,line_s2@HPP,line_s2@VPP,line_s3@HPP,line_s3@VPP,
                     #line_s4@HPP,line_s4@VPP
                    ]
        current_set+=[*elems,*projections]

        current_obj._solution_step.append(current_set)
        current_obj._assumptions=DrawingSet(*elems,*projections)
        current_obj.point_B=B
        current_obj.point_C=C
        current_obj.point_D=D
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

    
class EdgeSquareRotation(SquareRotation):
    def get_random_parameters(self):

        parameters_dict = super().get_random_parameters()

        point_P = parameters_dict[Symbol('P')]
        point_O = parameters_dict[Symbol('O')]

        parameters_dict[Symbol('A')] = (point_P + point_O) * 0.5 + Point(0, 0, 5)

        return parameters_dict
    
    
class EquilateralTriangleRotation(GeometricalCase):


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

        self.point_A=point_A
        self.point_P=point_P
        self.point_O=point_O

        
        self._given_data={'A':point_A,'P':point_P,'O':point_O}
        
        self._solution_step.append(self._assumptions)

    def _solution(self):
        current_obj=copy.deepcopy(self)
        
        A=current_obj.point_A
        O=current_obj.point_O
        P=current_obj.point_P
        
        S = (A @ (O^P))('S') #'Srodek' podstawy
        
        dirPS = P-S
        dirOS = O-S
        triangle_height = A.distance(S)
        triangle_side =  triangle_height / ((3**(1/2))/2)
        
        B = (S + dirPS/(P.distance(S))*(triangle_side/2))('B')
        C = (S - dirPS/(P.distance(S))*(triangle_side/2))('C')


        current_set=DrawingSet(*current_obj._solution_step[-1])

        line_a=Line(A,B)('a')
        line_b=Line(B,C)('b')
        line_c=Line(C,D)('c')
        line_d=Line(D,A)('d')
        plane_alpha=Plane(A,O,P)

        plane_beta=HorizontalPlane(P)

        line_k = plane_alpha.intersection(plane_beta)[0]

        elems=self._assumptions
        projections=[]
        point_0_dict={}

        S_I = (A @ line_k)('k')
        
        current_obj.point_A_0 = A.rotate_about(axis=line_k)('A_0')
        current_obj.point_B_0 = B.rotate_about(axis=line_k)('B_0')
        current_obj.point_C_0 = C.rotate_about(axis=line_k)('C_0')
     
        line_kk=Line(P,S_I)('k')
        

        current_obj.add_solution_step('A0',[current_obj.point_A_0])
        current_obj.add_solution_step('B0',[current_obj.point_B_0])
        current_obj.add_solution_step('C0',[current_obj.point_C_0])
        current_obj.add_solution_step('D0',[current_obj.point_D_0])
        #print(point_0_dict)
        elems+=[line_a,line_b,#,E,F,G,H,line_s1,line_s2,line_s3,line_s4
              ]

        projections+=[current_obj.point_D_0@HPP,current_obj.point_D_0@VPP,D@HPP,D@VPP,
            current_obj.point_A_0@HPP,current_obj.point_A_0@VPP,current_obj.point_B_0@HPP,current_obj.point_B_0@VPP,
                      current_obj.point_C_0@HPP,current_obj.point_C_0@VPP,B@HPP,B@VPP,C@HPP,C@VPP,line_a@HPP,line_a@VPP,line_b@HPP,line_b@VPP,
                      line_kk@HPP,line_kk@VPP,#line_s1@HPP,line_s1@VPP,line_s2@HPP,line_s2@VPP,line_s3@HPP,line_s3@VPP,
                     #line_s4@HPP,line_s4@VPP
                    ]
        current_set+=[*elems,*projections]

        current_obj._solution_step.append(current_set)
        current_obj._assumptions=DrawingSet(*elems,*projections)
        current_obj.point_B=B
        current_obj.point_C=C

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

    
class EdgeEquilateralTriangleRotation(EquilateralTriangleRotation):
    def get_random_parameters(self):

        parameters_dict = super().get_random_parameters()

        point_P = parameters_dict[Symbol('P')]
        point_O = parameters_dict[Symbol('O')]

        parameters_dict[Symbol('A')] = (point_P + point_O) * 0.5 + Point(0, 0, 5)

        return parameters_dict
    
    
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
        
        self.add_solution_step(
                f'''Assumptions''', [A,P,O])


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
            
            line_kk = Line(P, (O @ line_k))('k')

            A0 = A.rotate_about(axis=line_k)('A_0')
            current_obj.A0 = A0
            
            A0_e1=A0+((A0@line_k)-A0)/((A0@line_k).distance(A0))*(1.2*((A0@line_k).distance(A0)))
            A0_e2=(A0@line_k)+((A0@line_k)-A0)/((A0@line_k).distance(A0))*(-1.2*((A0@line_k).distance(A0)))
            
            current_obj.add_solution_step(f'''Plane rotation - it is creating projection of {O._label} on the planes intersection''', [((A0_e1)^A0_e2)('e_A')])

            #### Step 3 ####
            ### rotated point A0 of A #####
            
            current_obj.add_solution_step('Point A rotation by using a rotation plane', [A0])

            
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
    
    
            