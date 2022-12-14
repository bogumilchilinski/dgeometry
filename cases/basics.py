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

class SegmentMidpoint(GeometricalCase):
    
    def __init__(self,point_A=None,point_B=None,**kwargs):
        
        super().__init__()
        
        if point_A and point_B:
            projections=point_A@HPP,point_A@VPP,point_B@HPP,point_B@VPP,
        else:
            projections=[]
        
        self._assumptions=DrawingSet(point_A,point_B,*projections)
        self._assumptions3d = DrawingSet(point_A,point_B)
        self._given_data={'A':point_A,'B':point_B}

        self._point_A=point_A
        self._point_B=point_B
        
        self._solution_step.append(self._assumptions)



    def _solution(self):
        
        current_obj=copy.deepcopy(self)
        
        A=current_obj._point_A
        B=current_obj._point_B
        

        current_set=DrawingSet(*current_obj._solution_step[-1])
        
        midpoint=(A+ (B-A)*0.5)('C')
        current_set += [midpoint]
        
        current_obj._solution_step.append(current_set)
        
        
        current_obj.midpoint = midpoint
        current_obj.point_C = midpoint
        
        return current_obj
    
    def get_default_data(self):

        print('jesteś tu - dziedziczenie')

        default_data_dict = {
            Symbol('A'): [Point(4,5,8),Point(4,6,8),Point(5,10,8),Point(6,10,8),Point(7,10,8),Point(8,10,8),Point(-1,10,8),Point(3,10,8)],
            Symbol('B'): [Point(2,2,4),Point(1,3,3),Point(2,4,-1),Point(4,6,-2),Point(3,8,0)],

        }
        print(default_data_dict)
        return default_data_dict

class PointOnLine(GeometricalCase):
    
    def __init__(self,point_A=None,point_B=None,point_D=None,**kwargs):
        
        super().__init__()
        
        if point_A and point_B and point_D:
            
            point_C=(point_D+Point(0,0,-3))('C')
            projections=point_D,point_A@HPP,point_A@VPP,point_B@HPP,point_B@VPP,point_D@HPP,point_D@VPP,
            self._given_data={'A':point_A,'B':point_B,'D':point_D}
            self._point_C=point_C
            self._point_D=point_D
        else:
            projections=[]
            self._given_data={'A':point_A,'B':point_B}
        
        self._assumptions=DrawingSet(point_A,point_B,*projections)
        self._assumptions3d = DrawingSet(point_A,point_B,point_D)
        #self._given_data={'A':point_A,'B':point_B,'D':point_D}

        self._point_A=point_A
        self._point_B=point_B
        
        print('given_data',self._given_data)
        
        self._solution_step.append(self._assumptions)



    def _solution(self):
        
        current_obj=copy.deepcopy(self)
        
        A=current_obj._point_A
        B=current_obj._point_B
        C=current_obj._point_C
        
        

        current_set=DrawingSet(*current_obj._solution_step[-1])
        

        current_set += [C]
        
        current_obj._solution_step.append(current_set)
        
        

        current_obj.point_C = C
        
        return current_obj
    
    def get_default_data(self):


        
        
        
        
        point_A = [Point(x,y,z) for x in range(1,5) for y in range(1,7) for z in range(1,5) ]
        distance_AB = [Point(2,5,2),Point(2,6,2),Point(2,4,2),Point(3,7,4)]
        
        
        point_B=[pt + dist  for pt,dist   in  it.product(point_A,distance_AB)]
        


        default_data_dict = {
            Symbol('A'): point_A,
            Symbol('B'): point_B,

        }
        
        return default_data_dict

    def get_random_parameters(self):

        parameters_dict=super().get_random_parameters()



        point_A=parameters_dict[Symbol('A')]
        point_B=parameters_dict[Symbol('B')] 
        point_C=((point_A+ (point_B-point_A)*0.3))('C')
        point_D=(point_C+Point(0,0,3))('D')
        
        parameters_dict[Symbol('D')]=point_D

        return parameters_dict
    
    
class PlanesIntersection(GeometricalCase):
    
    def __init__(self,point_A=None,point_B=None,**kwargs):
        
        super().__init__()
        
        self._assumptions=DrawingSet(point_A,point_B)
        self._given_data=None

        self._point_A=point_A
        self._point_B=point_B



    def _solution(self):
        
        A=self._point_A
        B=self._point_B
        
        
        Aprim = A @ HPP
        Abis = A @ VPP
        
        self.append(Aprim)
        self.append(Abis)
        
        self.append(Line(A,B))
        self.append(A^B)

        return copy.deepcopy(self)
    
    def get_default_data(self):

        

        default_data_dict = {
            Symbol('A'): [Point(4,5,8),Point(4,6,8),Point(5,10,8),Point(6,10,8),Point(7,10,8),Point(8,10,8),Point(-1,10,8),Point(3,10,8)],
            Symbol('B'): [Point(2,2,4),Point(1,3,3),Point(2,4,-1),],

        }
        return default_data_dict
    
class VerticalLineOnPlane(GeometricalCase):

    def __init__(self,point_A=None,point_B=None,point_O=None,**kwargs):

        super().__init__()

        if point_A and point_B and point_O:
            projections=Line(point_A@HPP,point_B@HPP),Line(point_A@VPP,point_B@VPP),point_O@HPP,point_O@VPP,point_A@HPP,point_A@VPP,point_B@HPP,point_B@VPP

        else:
            projections=[]

        self._assumptions=DrawingSet(*projections)

        self._point_A=point_A
        self._point_B=point_B
        self._point_O=point_O
        
        self._given_data={'A':point_A,'B':point_B,'O':point_O}
        
        self._solution_step.append(self._assumptions)

    def _solution(self):
        
        current_obj=copy.deepcopy(self)
        
        O=self._point_O
        A=self._point_A
        B=self._point_B
        
        a=Line(A,B)('a')
        
        alpha=Plane(A,B,O)('alpha')
        beta=VerticalPlane(A)('beta')
        
        k=alpha.intersection(beta)[0]
        C=entity_convert(k._coding_points()[0])
        c=Line(C,O)('c')
        
        I=a.intersection(c)[0]('I')
        
        new_set= DrawingSet(self._assumptions)
        
        current_obj._solution_step.append(new_set)
        current_obj.point_P=I

        return current_obj
    
    def get_default_data(self):


        default_data_dict = {
            Symbol('A'): [Point(4,5,8),Point(4,6,8),Point(5,10,8),Point(6,10,8),Point(7,10,8),Point(8,10,8),Point(-1,10,8),Point(3,10,8)],
            Symbol('B'): [Point(2,2,4),Point(1,3,3),Point(2,4,-1),],
            Symbol('O'): [Point(1,6,2),Point(0,7,1),],
        }
        return default_data_dict
class FrontalLineOnPlane(GeometricalCase):
    
    def __init__(self,point_A=None,point_B=None,point_O=None,**kwargs):
        
        super().__init__()
        if point_A and point_B and point_O:
            projections=(point_A@HPP,point_B@HPP,point_A@VPP,point_B@VPP,point_O@HPP,point_O@VPP)
        else:
            projections=[]
        self._assumptions=DrawingSet(*projections)

        self._point_A=point_A
        self._point_B=point_B
        self._point_O=point_O
        self._given_data={'A':point_A,'B':point_B,'O':point_O}

        self._solution_step.append(self._assumptions)
    def _solution(self):
        current_obj=copy.deepcopy(self)
        O=current_obj._point_O
        A=current_obj._point_A
        B=current_obj._point_B
        current_set=DrawingSet(*current_obj._solution_step[-1])
        f=Line(A,B)('a')
        
        alpha=Plane(A,B,O)('alpha')
        beta=VerticalPlane(O)('beta')
        
        k=alpha.intersection(beta)[0] 
        P=entity_convert(k._coding_points()[0])
        p=Line(P,O)('f')
        
        I=f.intersection(p)[0]('I')
        current_obj._point_I=I
        elems=[O,A,B]
        projections=[O@HPP,A@HPP,B@HPP,I@HPP]
        current_set+=[*elems,*projections]
        
        return current_obj
    
    def get_default_data(self):


        default_data_dict = {
            Symbol('A'): [Point(4,5,8),Point(4,6,8),Point(5,10,8),Point(6,10,8),Point(7,10,8),Point(8,10,8),Point(-1,10,8),Point(3,10,8)],
            Symbol('B'): [Point(6,2,3),Point(4,2,5),Point(8,7,1),],
            Symbol('O'): [Point(5,4,7),Point(4,8,2),],
        }
        return default_data_dict
class HorizontalLineOnPlane(GeometricalCase):
    
    def __init__(self,point_A=None,point_B=None,point_O=None,**kwargs):
        
        super().__init__()
        if point_A and point_B and point_O:
            projections=(point_A@HPP,point_B@HPP,point_A@VPP,point_B@VPP,point_O@HPP,point_O@VPP)
        else:
            projections=[]
        self._assumptions=DrawingSet(*projections)

        self._point_A=point_A
        self._point_B=point_B
        self._point_O=point_O
        self._given_data={'A':point_A,'B':point_B,'O':point_O}

        self._solution_step.append(self._assumptions)
    def _solution(self):
        current_obj=copy.deepcopy(self)
        O=current_obj._point_O
        A=current_obj._point_A
        B=current_obj._point_B
        current_set=DrawingSet(*current_obj._solution_step[-1])
        f=Line(A,B)('a')
        
        alpha=Plane(A,B,O)('alpha')
        beta=HorizontalPlane(O)('beta')
        
        k=alpha.intersection(beta)[0] 
        P=entity_convert(k._coding_points()[0])
        p=Line(P,O)('f')
        
        I=f.intersection(p)[0]('I')
        current_obj._point_I=I
        elems=[O,A,B]
        projections=[O@VPP,A@VPP,B@VPP,I@VPP]
        current_set+=[*elems,*projections]
        
        return current_obj
    
    def get_default_data(self):


        default_data_dict = {
            Symbol('A'): [Point(4,5,8),Point(4,6,8),Point(5,10,8),Point(6,10,8),Point(7,10,8),Point(8,10,8),Point(-1,10,8),Point(3,10,8)],
            Symbol('B'): [Point(6,2,3),Point(4,2,5),Point(8,7,1),],
            Symbol('O'): [Point(5,4,7),Point(4,8,2),],
        }
        return default_data_dict

class LineOnPlane(GeometricalCase):

    point_A = [Point(x,y,z) for x in [2,2.5,3,3.5] for y in range(1,6) for z in [1.5,2,2.5,3,3.5] ]
#     distance_AO = [Point(2,4,2),Point(2,5,2),Point(2,6,2),Point(3,4,4)]

#     point_O = [pt + dist  for pt,dist   in  it.product(point_A,distance_AO)]
    point_O = [Point(x,y,z) for x in range(7,11) for y in range(8,12) for z in range(8,12) ]
    distance_OB = [Point(-4,4,-4),Point(-5,5,-4),Point(-4,5,-6),Point(-5,4,-7)]

    point_B=[Point(x,y,z) for x in [1,1.5,2,2.5,3,3.5] for y in [13,13.5,14,14.5,15] for z in [1,1.5,2,2.5,3,3.5] ]


    distance_AD = [Point(x,y,z) for x in range(1,4) for y in range(0,3) for z in range(1,4) ]
    distance_OE = [Point(x,y,z) for x in range(-4,-1) for y in range(-1,3) for z in range(-4,-1) ]
    distance_BF = [Point(x,y,z) for x in range(1,4) for y in range(-2,2) for z in range(1,4) ]

#     point_D=[pt + dist  for pt,dist   in  it.product(point_A,distance_AD) if (pt+dist).x != 0]
#     point_E = [pt + dist  for pt,dist   in  it.product(point_O,distance_OE) if (pt+dist).x != 0]
#     point_F = [pt + dist  for pt,dist   in  it.product(point_B,distance_BF) if (pt+dist).x != 0]

    point_D=[Point(x,y,z) for x in range(7,11) for y in range(2,6) for z in range(8,12) ]
    point_C = [Point(x,y,z) for x in range(1,5) for y in range(8,12) for z in range(2,5) ]
    point_E = [Point(x,y,z) for x in range(1,5) for y in range(8,12) for z in range(2,5) ]
    point_F = [Point(x,y,z) for x in range(7,11) for y in range(13,16) for z in range(8,12) ]
    
    
    def __init__(self,point_A=None,point_B=None,point_O=None,point_E=None,point_F=None,**kwargs):

        super().__init__()

        if point_A and point_B and point_O and point_E and point_E:
            projections=(point_A@HPP,point_B@HPP,Line(point_A@HPP,point_O@HPP),Line(point_A@VPP,point_O@VPP),
                         Line(point_B@HPP,point_O@HPP),Line(point_B@VPP,point_O@VPP),point_A@VPP,point_B@VPP,
                         point_O@HPP,point_O@VPP,point_E@VPP,point_E@VPP,point_E@HPP,point_F@HPP,point_E@VPP,point_F@VPP
                        )
        else:
            projections=[]

        self._assumptions=DrawingSet(*projections)


        self._point_A=point_A
        self._point_B=point_B
        self._point_O=point_O
        self._point_E=point_E
        self._point_F=point_F


        self._given_data={'A':point_A,'B':point_B,'O':point_O,'E':point_E,'F':point_F}


        
        self._solution_step.append(self._assumptions)
        
#     def solution(self):

        
#         midpoint=(A+ (B-A)*0.5)('C')
#         current_set += [midpoint]
        
#         current_obj._solution_step.append(current_set)
        
        
#         current_obj.midpoint = midpoint
#         current_obj.point_C = midpoint

#         return current_obj
    def _solution(self):

        current_obj=copy.deepcopy(self)
        
        A=current_obj._point_A
        B=current_obj._point_B
        O=current_obj._point_O
        
        E = current_obj._point_E
        F = current_obj._point_F
        

        current_set=DrawingSet(*current_obj._solution_step[-1])

        base_plane=Plane(A,B,O)('base')


        plane_v=base_plane('alpha') #why is the line created? #looks unnecessary
        #plane_h=Plane(n.p1,n.p2,n.p1@HPP)('beta')




        current_obj._solution_step.append(current_set)

        
        
        #tu dodaj
        
        lineE=E^(E+Point(15,0,0))
        lineF=F^(F+Point(15,0,0))

        
        
        current_obj.point_C = plane_v.intersection(lineE)[0]
        current_obj.point_D = plane_v.intersection(lineF)[0]
        
        elems=[lineE,lineF]
        projections=[lineE@HPP,lineF@HPP,lineE@VPP,lineF@VPP]
        current_set+=[*elems,*projections]
        
        
        return current_obj
    
    def get_default_data(self):

        point_A = self.__class__.point_A
        #distance_AO = self.__class__.distance_AO
        
        point_O = self.__class__.point_O 
        #distance_OB = self.__class__.distance_OB
        
        point_B=self.__class__.point_B
        

        #distance_AD = self.__class__.distance_AD
        #distance_OE = self.__class__.distance_OE
        #distance_BF = self.__class__.distance_BF
        
        
        point_D=self.__class__.point_D
        point_E = self.__class__.point_E
        point_F = self.__class__.point_F


        
#         point_A = [Point(x,y,z) for x in range(1,5) for y in range(1,7) for z in range(1,5) ]
#         distance_AO = [Point(2,3,2),Point(2,4,2),Point(2,4,2),Point(3,3,4)]
        
#         point_O = [pt + dist  for pt,dist   in  it.product(point_A,distance_AO)]
#         distance_OB = [Point(-4,2,-4),Point(-5,3,-4),Point(-4,4,-6),Point(-5,3,-7)]
        
#         point_B=[pt + dist  for pt,dist   in  it.product(point_O,distance_OB)]
        
#         distance_AC  = [Point(2,1,1),Point(2,2,1),Point(2,1,2),Point(1,2,3)]
#         distance_AD = [Point(2,5,1),Point(2,6,1),Point(2,6,2),Point(1,5,3)]

        default_data_dict = {
            Symbol('A'): point_A,
            Symbol('B'): point_B,
            Symbol('O'): point_O,

            Symbol('E'): point_E,
            Symbol('F'): point_F,
        }
        return default_data_dict
    
    
    
class HorizontalLineOnPlane(LineOnPlane):


    def get_random_parameters(self):

        parameters_dict=super().get_random_parameters()



        point_E=parameters_dict[Symbol('E')]
        point_F=parameters_dict[Symbol('F')] 

        
        parameters_dict[Symbol('F')]=Point(point_F.x,point_F.y,point_E.z)

        return parameters_dict

class FrontalLineOnPlane(LineOnPlane):


    def get_random_parameters(self):

        parameters_dict=super().get_random_parameters()

        point_E=parameters_dict[Symbol('E')]
        point_F=parameters_dict[Symbol('F')] 

        
        parameters_dict[Symbol('F')]=Point(point_E.x,point_F.y,point_F.z)

        return parameters_dict
    
class PointOnPlane(GeometricalCase):

    point_A = [Point(x,y,z) for x in [1,1.5,2,2.5,3,3.5] for y in range(2,6) for z in [1,1.5,2,2.5,3,3.5] ]
#     distance_AO = [Point(2,4,2),Point(2,5,2),Point(2,6,2),Point(3,4,4)]

#     point_O = [pt + dist  for pt,dist   in  it.product(point_A,distance_AO)]
    point_O = [Point(x,y,z) for x in range(7,11) for y in range(8,12) for z in range(8,12) ]
    distance_OB = [Point(-4,4,-4),Point(-5,5,-4),Point(-4,5,-6),Point(-5,4,-7)]

    point_B=[Point(x,y,z) for x in [4,4.5,5,5.5,6] for y in [12,12.5,13,13.5] for z in [1,1.5,2,2.5,3,3.5] ]


    distance_AD = [Point(x,y,z) for x in range(1,5) for y in range(0,4) for z in range(1,5) ]
    distance_OE = [Point(x,y,z) for x in range(-5,-1) for y in range(-1,4) for z in range(-5,-1) ]
    distance_BF = [Point(x,y,z) for x in range(1,5) for y in range(-2,3) for z in range(1,5) ]

#     point_D=[pt + dist  for pt,dist   in  it.product(point_A,distance_AD) if (pt+dist).x != 0]
#     point_E = [pt + dist  for pt,dist   in  it.product(point_O,distance_OE) if (pt+dist).x != 0]
#     point_F = [pt + dist  for pt,dist   in  it.product(point_B,distance_BF) if (pt+dist).x != 0]

    point_D=[Point(x,y,z) for x in range(7,11) for y in range(2,6) for z in range(8,12) ]
    point_E = [Point(x,y,z) for x in range(1,5) for y in range(8,12) for z in range(5,7) ]
    point_F = [Point(x,y,z) for x in range(7,11) for y in range(13,16) for z in range(8,12) ]
    
    
    def __init__(self,point_A=None,point_B=None,point_O=None,point_D=None,**kwargs):

        super().__init__()

        if point_A and point_B and point_O and point_D:
            projections=(point_A@HPP,point_B@HPP,Line(point_A@HPP,point_O@HPP),Line(point_A@VPP,point_O@VPP),
                         Line(point_B@HPP,point_O@HPP),Line(point_B@VPP,point_O@VPP),point_A@VPP,point_B@VPP,
                         point_O@HPP,point_O@VPP,point_D@HPP,point_D@VPP)
        else:
            projections=[]

        self._assumptions=DrawingSet(*projections)


        self._point_A=point_A
        self._point_B=point_B
        self._point_O=point_O
        self._point_D=point_D



        self._given_data={'A':point_A,'B':point_B,'O':point_A,'D':point_D}


        
        self._solution_step.append(self._assumptions)

        
    def _solution(self):
#         self._line=Line(self._point_N1,self._point_N2)
        current_obj=copy.deepcopy(self)
        
        A=current_obj._point_A
        B=current_obj._point_B
        O=current_obj._point_O
        D=current_obj._point_D
        current_set=DrawingSet(*current_obj._solution_step[-1])

        base_plane=Plane(A,B,O)('base')
        line_a=Line(A,O)('a')
        line_b=Line(B,O)('b')

        line_D=Line(D,D@VPP)
        intersection_ABO_D=base_plane.intersection(line_D)[0]('C')
        C=intersection_ABO_D
        elems=[line_a,line_b,line_D]
        projections=[line_a@HPP,line_b@HPP,line_a@VPP,line_b@VPP,C@HPP,C@VPP]
        current_set+=[*elems,*projections]

        current_obj._solution_step.append(current_set)
        current_obj.point_C = C

        return current_obj
    
    def get_default_data(self):

#         point_A = [Point(x,y,z) for x in range(1,5) for y in range(1,7) for z in range(1,5) ]
#         distance_AO = [Point(2,3,2),Point(2,4,2),Point(2,4,2),Point(3,3,4)]
        
#         point_O = [pt + dist  for pt,dist   in  it.product(point_A,distance_AO)]
#         distance_OB = [Point(-4,2,-4),Point(-5,3,-4),Point(-4,4,-6),Point(-5,3,-7)]
        
#         point_B=[pt + dist  for pt,dist   in  it.product(point_O,distance_OB)]
        


#         distance_AD = [Point(x,y,z) for x in range(3,5) for y in range(0,5) for z in range(1,4) ]

        point_A = self.__class__.point_A
        #distance_AO = self.__class__.distance_AO
        
        point_O = self.__class__.point_O 
        #distance_OB = self.__class__.distance_OB
        
        point_B=self.__class__.point_B
        

        #distance_AD = self.__class__.distance_AD
        #distance_OE = self.__class__.distance_OE
        #distance_BF = self.__class__.distance_BF
        
        
        point_D=self.__class__.point_D
        point_E = self.__class__.point_E
        point_F = self.__class__.point_F


        default_data_dict = {
            Symbol('A'): point_A,
            Symbol('B'): point_B,
            Symbol('O'): point_O,

            Symbol('D'): point_E, #it's not a mistake - selected due to convenient position
        }
        return default_data_dict

    
    
class TriangleOnPlane(GeometricalCase):
    
    point_A = [Point(x,y,z) for x in [1,1.5,2,2.5,3,3.5] for y in range(2,6) for z in [1,1.5,2,2.5,3,3.5] ]
#     distance_AO = [Point(2,4,2),Point(2,5,2),Point(2,6,2),Point(3,4,4)]

#     point_O = [pt + dist  for pt,dist   in  it.product(point_A,distance_AO)]
    point_O = [Point(x,y,z) for x in range(7,11) for y in range(8,12) for z in range(8,12) ]
    distance_OB = [Point(-4,4,-4),Point(-5,5,-4),Point(-4,5,-6),Point(-5,4,-7)]

    point_B=[Point(x,y,z) for x in [1,1.5,2,2.5,3,3.5] for y in [13,13.5,14,14.5,15] for z in [1,1.5,2,2.5,3,3.5] ]


    distance_AD = [Point(x,y,z) for x in range(1,4) for y in range(0,3) for z in range(1,4) ]
    distance_OE = [Point(x,y,z) for x in range(-4,-1) for y in range(-1,3) for z in range(-4,-1) ]
    distance_BF = [Point(x,y,z) for x in range(1,4) for y in range(-2,2) for z in range(1,4) ]

#     point_D=[pt + dist  for pt,dist   in  it.product(point_A,distance_AD) if (pt+dist).x != 0]
#     point_E = [pt + dist  for pt,dist   in  it.product(point_O,distance_OE) if (pt+dist).x != 0]
#     point_F = [pt + dist  for pt,dist   in  it.product(point_B,distance_BF) if (pt+dist).x != 0]

    point_D=[Point(x,y,z) for x in range(7,11) for y in range(2,6) for z in range(8,12) ]
    point_E = [Point(x,y,z) for x in range(1,5) for y in range(8,12) for z in range(2,5) ]
    point_F = [Point(x,y,z) for x in range(7,11) for y in range(13,16) for z in range(8,12) ]


    def __init__(self,point_A=None,point_B=None,point_O=None,point_D=None,point_E=None,point_F=None,**kwargs):

        super().__init__()

        if point_A and point_B and point_O and point_D and point_E and point_F:
            projections=(point_A@HPP,point_B@HPP,Line(point_A@HPP,point_O@HPP),Line(point_A@VPP,point_O@VPP),
                         Line(point_B@HPP,point_O@HPP),Line(point_B@VPP,point_O@VPP),point_A@VPP,point_B@VPP,
                         point_O@HPP,point_O@VPP,point_D@HPP,point_D@VPP,point_E@HPP,point_E@VPP,point_F@HPP,point_F@VPP)
        else:
            projections=[]

        self._assumptions=DrawingSet(*projections)




        self._point_A=point_A
        self._point_B=point_B
        self._point_O=point_O
        self._point_D=point_D
        self._point_E=point_E
        self._point_F=point_F

        self._given_data={'A':point_A,'B':point_B,'O':point_A,'D':point_D,'E':point_E,'F':point_F}
        
        self._solution_step.append(self._assumptions)

        
    def _solution(self):
#         self._line=Line(self._point_N1,self._point_N2)
        current_obj=copy.deepcopy(self)
        
        A=current_obj._point_A
        B=current_obj._point_B
        O=current_obj._point_O
        D=current_obj._point_D
        E=current_obj._point_E
        F=current_obj._point_F
        
        current_set=DrawingSet(*current_obj._solution_step[-1])

        base_plane=Plane(A,B,O)('base')
        line_a=Line(A,O)('a')
        line_b=Line(B,O)('b')

        line_D=Line(D,D@VPP)
        intersection_ABO_D=base_plane.intersection(line_D)[0]('K')
        K=intersection_ABO_D
        
        line_E=Line(E,E@VPP)
        intersection_ABO_E=base_plane.intersection(line_E)[0]('L')
        L=intersection_ABO_E

        line_F=Line(F,F@VPP)
        intersection_ABO_F=base_plane.intersection(line_F)[0]('M')
        M=intersection_ABO_F
        
        elems=[line_a,line_b,line_D]
        
        #to remove
        C=K
        
        projections=[line_a@HPP,line_b@HPP,line_a@VPP,line_b@VPP,C@HPP,C@VPP]
        current_set+=[*elems,*projections]

        current_obj._solution_step.append(current_set)
        # to remove
        current_obj.point_C=C
        current_obj.point_K = K
        current_obj.point_L = L
        current_obj.point_M = M

        return current_obj
    
    def get_default_data(self):

        point_A = self.__class__.point_A
        #distance_AO = self.__class__.distance_AO
        
        point_O = self.__class__.point_O 
        #distance_OB = self.__class__.distance_OB
        
        point_B=self.__class__.point_B
        

        #distance_AD = self.__class__.distance_AD
        #distance_OE = self.__class__.distance_OE
        #distance_BF = self.__class__.distance_BF
        
        
        point_D=self.__class__.point_D
        point_E = self.__class__.point_E
        point_F = self.__class__.point_F

        
        default_data_dict = {
            Symbol('A'): point_A,
            Symbol('B'): point_B,
            Symbol('O'): point_O,

            Symbol('D'): point_D,
            Symbol('E'): point_E,
            Symbol('F'): point_F,
        }
        return default_data_dict

    
class LineAndPlaneIntersection(GeometricalCase):
    
    point_A = [Point(x,y,z) for x in [1,1.5,2,2.5,3,3.5] for y in [2,2.5,3,3.5,4,4.5,5] for z in [1,1.5,2,2.5,3,3.5] ]

    point_O = [Point(x,y,z) for x in range(7,11) for y in range(8,12) for z in range(8,12) ]


    point_B=[Point(x,y,z) for x in [1,1.5,2,2.5,3,3.5] for y in [13,13.5,14,14.5,15] for z in [1,1.5,2,2.5,3,3.5] ]


    point_D=[Point(x,y,z) for x in [1,1.5,2,2.5,3,3.5] for y in [7,7.5,8.5,9,9.5] for z in range(8,12) ]
    point_E = [Point(x,y,z) for x in [7,7.5,8,8.5,9] for y in [10,10.5,11,11.5,12] for z in range(2,5) ]


    

    def __init__(self,point_A=None,point_B=None,point_O=None,point_D=None,point_E=None,**kwargs):

        super().__init__()

        if point_A and point_B and point_O and point_D and point_E:
            projections=(point_A@HPP,point_B@HPP,Line(point_A@HPP,point_O@HPP),Line(point_A@VPP,point_O@VPP),
                         Line(point_B@HPP,point_O@HPP),Line(point_B@VPP,point_O@VPP),point_A@VPP,point_B@VPP,
                         point_O@HPP,point_O@VPP,point_D@HPP,point_D@VPP,point_E@HPP,point_E@VPP)
        else:
            projections=[]

        self._assumptions=DrawingSet(*projections)




        self._point_A=point_A
        self._point_B=point_B
        self._point_O=point_O
        self._point_D=point_D
        self._point_E=point_E


        self._given_data={'A':point_A,'B':point_B,'O':point_A,'D':point_D,'E':point_E}
        
        self._solution_step.append(self._assumptions)

        
    def _solution(self):
#         self._line=Line(self._point_N1,self._point_N2)
        current_obj=copy.deepcopy(self)
        
        A=current_obj._point_A
        B=current_obj._point_B
        O=current_obj._point_O
        D=current_obj._point_D
        E=current_obj._point_E

        
        current_set=DrawingSet(*current_obj._solution_step[-1])

        base_plane=Plane(A,B,O)('base')
        line_a=Line(A,O)('a')
        line_b=Line(B,O)('b')

        line_d=Line(D,E)
        intersection_ABO_DE=base_plane.intersection(line_d)[0]('P')
        P=intersection_ABO_DE
        

        
        elems=[line_a,line_b,line_d,intersection_ABO_DE]

        
        projections=[line_a@HPP,line_b@HPP,line_a@VPP,line_b@VPP,intersection_ABO_DE@HPP,intersection_ABO_DE@VPP,line_d@HPP,line_d@VPP]
        current_set+=[*elems,*projections]

        current_obj._solution_step.append(current_set)
        # to remove
        current_obj.point_P=P
        current_obj._assumptions=DrawingSet(*elems,*projections)

        return current_obj

    def get_default_data(self):

        point_A = self.__class__.point_A
        #distance_AO = self.__class__.distance_AO
        
        point_O = self.__class__.point_O 
        #distance_OB = self.__class__.distance_OB
        
        point_B=self.__class__.point_B
        

        #distance_AD = self.__class__.distance_AD
        #distance_OE = self.__class__.distance_OE
        #distance_BF = self.__class__.distance_BF
        
        
        point_D=self.__class__.point_D
        point_E = self.__class__.point_E


        
        default_data_dict = {
            Symbol('A'): point_A,
            Symbol('B'): point_B,
            Symbol('O'): point_O,

            Symbol('D'): point_D,
            Symbol('E'): point_E,

        }
        return default_data_dict
    
class LineAndHorizontalEdgePlaneIntersection(LineAndPlaneIntersection):
    
    def get_random_parameters(self):

        parameters_dict=super().get_random_parameters()



        point_A=parameters_dict[Symbol('A')]
        print(point_A.coordinates)
        point_B=parameters_dict[Symbol('B')] 
        print(point_B.coordinates)
        
        parameters_dict[Symbol('O')]=(point_A+point_B)*0.5+Point(0,0,5)
        print(parameters_dict[Symbol('O')].coordinates)

        return parameters_dict
    
class LineAndFrontalEdgePlaneIntersection(LineAndPlaneIntersection):
    
    def get_random_parameters(self):

        parameters_dict=super().get_random_parameters()



        point_A=parameters_dict[Symbol('A')]
        print(point_A.coordinates)
        point_B=parameters_dict[Symbol('B')] 
        print(point_B.coordinates)
        
        parameters_dict[Symbol('O')]=(point_A+point_B)*0.5+Point(5,0,0)
        print(parameters_dict[Symbol('O')].coordinates)

        return parameters_dict
    
    
class TwoPlanesIntersection(GeometricalCase):
    
    point_A = [Point(x,y,z) for x in [1,1.5,2,2.5,3,3.5] for y in [2,2.5,3,3.5,4,4.5,5] for z in [1,1.5,2,2.5,3,3.5] ]

    point_O = [Point(x,y,z) for x in range(7,11) for y in range(8,12) for z in range(8,12) ]


    point_B=[Point(x,y,z) for x in [1,1.5,2,2.5,3,3.5] for y in [13,13.5,14,14.5,15] for z in [1,1.5,2,2.5,3,3.5] ]



    point_D=[Point(x,y,z) for x in [1,1.5,2,2.5,3,3.5] for y in [7,7.5,8.5,9,9.5] for z in range(8,12) ]
    point_E = [Point(x,y,z) for x in [7,7.5,8,8.5,9] for y in [10,10.5,11,11.5,12] for z in range(2,5) ]

    point_F = [Point(x,y,z) for x in  [1,1.5,2,2.5,3,3.5] for y in [13,13.5,14,14.5,15] for z in range(8,12) ]


    def __init__(self,point_A=None,point_B=None,point_O=None,point_D=None,point_E=None,point_F=None,**kwargs):

        super().__init__()

        if point_A and point_B and point_O and point_D and point_E and point_F:
            projections=(point_A@HPP,point_B@HPP,Line(point_A@HPP,point_O@HPP),Line(point_A@VPP,point_O@VPP),
                         Line(point_B@HPP,point_O@HPP),Line(point_B@VPP,point_O@VPP),point_A@VPP,point_B@VPP,
                         point_O@HPP,point_O@VPP,point_D@HPP,point_D@VPP,point_E@HPP,point_E@VPP,point_F@HPP,point_F@VPP)
        else:
            projections=[]

        self._assumptions=DrawingSet(*projections)




        self._point_A=point_A
        self._point_B=point_B
        self._point_O=point_O
        self._point_D=point_D
        self._point_E=point_E
        self._point_F=point_F

        self._given_data={'A':point_A,'B':point_B,'O':point_A,'D':point_D,'E':point_E,'F':point_F}
        
        self._solution_step.append(self._assumptions)

        
    def _solution(self):

        current_obj = self._solve()

        return current_obj

    def _solve(self):
    
#         self._line=Line(self._point_N1,self._point_N2)
        current_obj=copy.deepcopy(self)
        
        A=current_obj._point_A
        B=current_obj._point_B
        O=current_obj._point_O
        D=current_obj._point_D
        E=current_obj._point_E
        F=current_obj._point_F
        
        current_set=DrawingSet(*current_obj._solution_step[-1])

        base_plane=Plane(A,B,O)('base')
        line_a=Line(A,O)('a')
        line_b=Line(B,O)('b')
        line_d=Line(D,E)('d')
        line_f=Line(F,E)('f')
        cutting_plane=Plane(D,E,F)('cutting')
#         intersection_line=base_plane.intersection(cutting_plane)[0]('k')
        P=base_plane.intersection(line_d)[0]('P')
        Q=base_plane.intersection(line_f)[0]('Q')
        intersection_line=Line(P,Q)('k')

        
        elems=[line_a,line_b,line_d,line_f,intersection_line,P,Q]

        
        projections=[line_d@HPP,line_f@HPP,line_d@VPP,line_f@VPP,line_a@HPP,line_b@HPP,line_a@VPP,line_b@VPP,P@VPP,P@HPP,Q@VPP,Q@HPP,intersection_line@HPP,intersection_line@VPP]
        current_set+=[*elems,*projections]

        current_obj._solution_step.append(current_set)
        # to remove
        current_obj.point_P=P
        current_obj.point_Q=Q
        current_obj._assumptions=DrawingSet(*elems,*projections)

        return current_obj

    def get_default_data(self):

        point_A = self.__class__.point_A
        #distance_AO = self.__class__.distance_AO
        
        point_O = self.__class__.point_O 
        #distance_OB = self.__class__.distance_OB
        
        point_B=self.__class__.point_B
        

        #distance_AD = self.__class__.distance_AD
        #distance_OE = self.__class__.distance_OE
        #distance_BF = self.__class__.distance_BF
        
        
        point_D=self.__class__.point_D
        point_E = self.__class__.point_E
        point_F = self.__class__.point_F

        
        default_data_dict = {
            Symbol('A'): point_A,
            Symbol('B'): point_B,
            Symbol('O'): point_O,

            Symbol('D'): point_D,
            Symbol('E'): point_E,
            Symbol('F'): point_F,
        }
        return default_data_dict
        
class HorizontalEgdePlaneAndPlaneIntersection(TwoPlanesIntersection):
    
    point_A = [Point(x,y,z) for x in [4,4.5,5,5.5,6,6.5] for y in [2,2.5,3,3.5,4,4.5,5] for z in [1,1.5,2,2.5,3,3.5] ]

    point_O = [Point(x,y,z) for x in range(7,11) for y in range(8,12) for z in range(8,12) ]


    point_B=[Point(x,y,z) for x in [1,1.5,2,2.5,3,3.5] for y in [13,13.5,14,14.5,15] for z in [1,1.5,2,2.5,3,3.5] ]

    point_D=[Point(x,y,z) for x in [1,1.5,2,2.5,3,3.5] for y in [1,1.5,2,2.5,3,3.5] for z in range(8,12) ]
    point_E = [Point(x,y,z) for x in [7,7.5,8,8.5,9] for y in [7,7.5,8.5,9,9.5] for z in range(2,5) ]

    point_F = [Point(x,y,z) for x in  [1,1.5,2,2.5,3,3.5] for y in [10,10.5,11,11.5,12] for z in range(8,12) ]


    def get_default_data(self):

        point_A = self.__class__.point_A
        
        point_O = self.__class__.point_O 
        
        point_B=self.__class__.point_B
        
        point_D=self.__class__.point_D
        point_E = self.__class__.point_E
        point_F = self.__class__.point_F
        
        default_data_dict = {
            Symbol('A'): point_A,
            Symbol('B'): point_B,
            Symbol('O'): point_O,

            Symbol('D'): point_D,
            Symbol('E'): point_E,
            Symbol('F'): point_F,
        }
        return default_data_dict

    def get_random_parameters(self):

        parameters_dict=super().get_random_parameters()



        point_A=parameters_dict[Symbol('A')]
        point_B=parameters_dict[Symbol('B')] 

        
        parameters_dict[Symbol('O')]=(point_A+point_B)*0.5+Point(0,0,5)

        return parameters_dict

class FrontalEgdePlaneAndPlaneIntersection(TwoPlanesIntersection):
    
    point_A = [Point(x,y,z) for x in [4,4.5,5,5.5,6,6.5] for y in [2,2.5,3,3.5,4,4.5,5] for z in [1,1.5,2,2.5,3,3.5] ]

    point_O = [Point(x,y,z) for x in range(7,11) for y in range(8,12) for z in range(8,12) ]


    point_B=[Point(x,y,z) for x in [1,1.5,2,2.5,3,3.5] for y in [13,13.5,14,14.5,15] for z in [1,1.5,2,2.5,3,3.5] ]

    point_D=[Point(x,y,z) for x in [1,1.5,2,2.5,3,3.5] for y in [1,1.5,2,2.5,3,3.5] for z in range(8,12) ]
    point_E = [Point(x,y,z) for x in [7,7.5,8,8.5,9] for y in [7,7.5,8.5,9,9.5] for z in range(2,5) ]

    point_F = [Point(x,y,z) for x in  [1,1.5,2,2.5,3,3.5] for y in [10,10.5,11,11.5,12] for z in range(8,12) ]


    def get_default_data(self):

        point_A = self.__class__.point_A
        
        point_O = self.__class__.point_O 
        
        point_B=self.__class__.point_B
        
        point_D=self.__class__.point_D
        point_E = self.__class__.point_E
        point_F = self.__class__.point_F
        
        default_data_dict = {
            Symbol('A'): point_A,
            Symbol('B'): point_B,
            Symbol('O'): point_O,

            Symbol('D'): point_D,
            Symbol('E'): point_E,
            Symbol('F'): point_F,
        }
        return default_data_dict

    def get_random_parameters(self):

        parameters_dict=super().get_random_parameters()



        point_A=parameters_dict[Symbol('A')]
        print(point_A.coordinates)
        point_B=parameters_dict[Symbol('B')] 
        print(point_B.coordinates)
        
        parameters_dict[Symbol('O')]=(point_A+point_B)*0.5+Point(1,0,0)
        print(parameters_dict[Symbol('O')].coordinates)

        return parameters_dict
    
class LinePerpendicularToPlaneIntersection(GeometricalCase):
    
    point_A = [Point(x,y,z) for x in [1,1.5,2,2.5] for y in [2,2.5,3,3.5,4,4.5,5] for z in [3,3.5,4,4.5]  ]

    point_O = [Point(x,y,z) for x in range(7,11) for y in range(8,12) for z in range(8,12) ]


    point_B=[Point(x,y,z) for x in [3,3.5,4,4.5] for y in [13,13.5,14,14.5,15] for z in [1,1.5,2,2.5] ]


    point_D=[Point(x,y,z) for x in [1,1.5,2,2.5,3,3.5] for y in [7,7.5,8.5,9,9.5] for z in range(8,12) ]



    

    def __init__(self,point_A=None,point_B=None,point_O=None,point_D=None,**kwargs):

        super().__init__()

        if point_A and point_B and point_O and point_D:
            projections=(point_A@HPP,point_B@HPP,Line(point_A@HPP,point_O@HPP),Line(point_A@VPP,point_O@VPP),
                         Line(point_B@HPP,point_O@HPP),Line(point_B@VPP,point_O@VPP),point_A@VPP,point_B@VPP,
                         point_O@HPP,point_O@VPP,point_D@HPP,point_D@VPP)
        else:
            projections=[]

        self._assumptions=DrawingSet(*projections)




        self._point_A=point_A
        self._point_B=point_B
        self._point_O=point_O
        self._point_D=point_D



        self._given_data={'A':point_A,'B':point_B,'O':point_A,'D':point_D}
        
        self._solution_step.append(self._assumptions)

        
    def _solution(self):
#         self._line=Line(self._point_N1,self._point_N2)
        current_obj=copy.deepcopy(self)
        
        A=current_obj._point_A
        B=current_obj._point_B
        O=current_obj._point_O
        D=current_obj._point_D


        
        current_set=DrawingSet(*current_obj._solution_step[-1])

        base_plane=Plane(A,B,O)('base')
        line_a=Line(A,O)('a')
        line_b=Line(B,O)('b')

        #line_d=Line(D,D@base_plane  )
        intersection_ABO_DE=(D@base_plane)('P')
        P=intersection_ABO_DE
        

        
        elems=[line_a,line_b,intersection_ABO_DE]

        
        projections=[line_a@HPP,line_b@HPP,line_a@VPP,line_b@VPP,intersection_ABO_DE@HPP,intersection_ABO_DE@VPP]
        current_set+=[*elems,*projections]

        current_obj._solution_step.append(current_set)
        # to remove
        current_obj.point_P=P
        current_obj._assumptions=DrawingSet(*elems,*projections)

        return current_obj

    def get_default_data(self):

        point_A = self.__class__.point_A
        #distance_AO = self.__class__.distance_AO
        
        point_O = self.__class__.point_O 
        #distance_OB = self.__class__.distance_OB
        
        point_B=self.__class__.point_B
        

        #distance_AD = self.__class__.distance_AD
        #distance_OE = self.__class__.distance_OE
        #distance_BF = self.__class__.distance_BF
        
        
        point_D=self.__class__.point_D



        
        default_data_dict = {
            Symbol('A'): point_A,
            Symbol('B'): point_B,
            Symbol('O'): point_O,

            Symbol('D'): point_D,


        }
        return default_data_dict

    
class LinePerpendicularToEdgePlaneIntersection(LinePerpendicularToPlaneIntersection):
    
    def get_random_parameters(self):

        parameters_dict=super().get_random_parameters()



        point_A=parameters_dict[Symbol('A')]
        point_B=parameters_dict[Symbol('B')] 

        
        parameters_dict[Symbol('O')]=(point_A+point_B)*0.5+Point(0,0,5)

        return parameters_dict

class LinePerpendicularToHFLinesIntersection(LinePerpendicularToPlaneIntersection):
    
    point_A = [Point(x,y,z) for x in [1,1.5,2,2.5] for y in [2,2.5,3,3.5,4,4.5,5] for z in [2,2.5,3,3.5]  ]

    point_O = [Point(x,y,z) for x in range(7,11) for y in range(8,12) for z in [5,5.5,6,6.5,7] ]


    point_B=[Point(x,y,z) for x in [4,4.5,5,5.5,6] for y in [13,13.5,14,14.5,15] for z in [1,1.5,2,2.5] ]


    point_D=[Point(x,y,z) for x in range(7,10) for y in [6,6.5,7,7.5,8.5] for z in range(9,12) ]


    def get_random_parameters(self):

        parameters_dict=super().get_random_parameters()



        point_A=parameters_dict[Symbol('A')]
        point_B=parameters_dict[Symbol('B')] 
        point_O=parameters_dict[Symbol('O')] 

        
        parameters_dict[Symbol('O')]=Point(point_A.x,point_O.y,point_O.z)
        parameters_dict[Symbol('B')]=Point(point_B.x,point_B.y,point_A.z)

        return parameters_dict
    
    
class PlanePerpendicularToLineIntersection(GeometricalCase):
    
    point_A = [Point(x,y,z) for x in [1,1.5,2,2.5,3,3.5] for y in [2,2.5,3,3.5,4,4.5,5] for z in [1,1.5,2,2.5,3,3.5] ]




    point_D=[Point(x,y,z) for x in [1,1.5,2,2.5,3,3.5] for y in [6,6.5,7,7.5] for z in range(8,12) ]

    point_E = [Point(x,y,z) for x in [7,7.5,8,8.5,9] for y in [8,8.5,9,9.5] for z in range(2,5) ]
    

    def __init__(self,point_A=None,point_D=None,point_E=None,**kwargs):

        super().__init__()

        if point_A and point_D and point_E:
            
            line_DE=Line(point_D,point_E)('n')
            projections=(point_A@HPP,point_A@VPP,point_D@HPP,point_D@VPP,point_E@HPP,point_E@VPP,line_DE@HPP,line_DE@VPP)
        else:
            projections=[]

        self._assumptions=DrawingSet(*projections)




        self._point_A=point_A
        self._point_E=point_E
        self._point_D=point_D



        self._given_data={'A':point_A,'E':point_E,'D':point_D}
        
        self._solution_step.append(self._assumptions)

        
    def _solution(self):
#         self._line=Line(self._point_N1,self._point_N2)
        current_obj=copy.deepcopy(self)
        
        A=current_obj._point_A
        E=current_obj._point_E
        D=current_obj._point_D


        
        current_set=DrawingSet(*current_obj._solution_step[-1])

        base_plane=Plane(A,normal_vector=(D-E)('d').coordinates)('base')


        #line_d=Line(D,D@base_plane  )
        intersection_ABO_DE=(D@base_plane)('P')
        P=intersection_ABO_DE
        

        
        elems=[intersection_ABO_DE]

        
        projections=[intersection_ABO_DE@HPP,intersection_ABO_DE@VPP]
        current_set+=[*elems,*projections]

        current_obj._solution_step.append(current_set)
        # to remove
        current_obj.point_P=P
        current_obj._assumptions=DrawingSet(*elems,*projections)

        return current_obj

    def get_default_data(self):

        point_A = self.__class__.point_A
        
        point_D=self.__class__.point_D
        point_E=self.__class__.point_E


        
        default_data_dict = {
            Symbol('A'): point_A,

            Symbol('D'): point_D,
            Symbol('E'): point_E,

        }
        return default_data_dict
    
    
    
class PlanePerpendicularToPlaneIntersection(GeometricalCase):
    
    point_A = [Point(x,y,z) for x in [1,1.5,2,2.5] for y in [2,2.5,3,3.5,4,4.5,5] for z in [3,3.5,4,4.5]  ]

    point_O = [Point(x,y,z) for x in range(7,11) for y in range(8,12) for z in range(8,12) ]


    point_B=[Point(x,y,z) for x in [3,3.5,4,4.5] for y in [13,13.5,14,14.5,15] for z in [1,1.5,2,2.5] ]



    point_D=[Point(x,y,z) for x in [1,1.5,2,2.5,3,3.5] for y in [7,7.5,8.5,9,9.5] for z in range(8,12) ]
    point_E = [Point(x,y,z) for x in  [1,1.5,2,2.5,3,3.5] for y in [13,13.5,14,14.5,15] for z in range(8,12) ]


    def __init__(self,point_A=None,point_B=None,point_O=None,point_D=None,point_E=None,**kwargs):

        super().__init__()

        if point_A and point_B and point_O and point_D and point_E:
            projections=(point_A@HPP,point_B@HPP,Line(point_A@HPP,point_O@HPP),Line(point_A@VPP,point_O@VPP),
                         Line(point_B@HPP,point_O@HPP),Line(point_B@VPP,point_O@VPP),point_A@VPP,point_B@VPP,
                         point_O@HPP,point_O@VPP,point_D@HPP,point_D@VPP,point_E@HPP,point_E@VPP)
        else:
            projections=[]

        self._assumptions=DrawingSet(*projections)




        self._point_A=point_A
        self._point_B=point_B
        self._point_O=point_O
        self._point_D=point_D
        self._point_E=point_E


        self._given_data={'A':point_A,'B':point_B,'O':point_A,'D':point_D,'E':point_E}
        
        self._solution_step.append(self._assumptions)

        
    def _solution(self):
#         self._line=Line(self._point_N1,self._point_N2)
        current_obj=copy.deepcopy(self)
        
        A=current_obj._point_A
        B=current_obj._point_B
        O=current_obj._point_O
        D=current_obj._point_D
        E=current_obj._point_E

        
        current_set=DrawingSet(*current_obj._solution_step[-1])

        base_plane=Plane(A,B,O)('base')
        line_a=Line(A,O)('a')
        line_b=Line(B,O)('b')
        line_d=Line(D,E)('d')


#         intersection_line=base_plane.intersection(cutting_plane)[0]('k')
        P=(D@base_plane)('P')
        Q=(E@base_plane)('Q')
        intersection_line=Line(P,Q)('k')

        
        elems=[line_a,line_b,line_d,intersection_line,P,Q]

        
        projections=[line_d@HPP,line_d@VPP,line_a@HPP,line_b@HPP,line_a@VPP,line_b@VPP,P@VPP,P@HPP,Q@VPP,Q@HPP,intersection_line@HPP,intersection_line@VPP]
        current_set+=[*elems,*projections]

        current_obj._solution_step.append(current_set)
        # to remove
        current_obj.point_P=P
        current_obj.point_Q=Q
        current_obj._assumptions=DrawingSet(*elems,*projections)

        return current_obj

    def get_default_data(self):

        point_A = self.__class__.point_A
        #distance_AO = self.__class__.distance_AO
        
        point_O = self.__class__.point_O 
        #distance_OB = self.__class__.distance_OB
        
        point_B=self.__class__.point_B
        

        #distance_AD = self.__class__.distance_AD
        #distance_OE = self.__class__.distance_OE
        #distance_BF = self.__class__.distance_BF
        
        
        point_D=self.__class__.point_D
        point_E = self.__class__.point_E


        
        default_data_dict = {
            Symbol('A'): point_A,
            Symbol('B'): point_B,
            Symbol('O'): point_O,

            Symbol('D'): point_D,
            Symbol('E'): point_E,

        }
        return default_data_dict
class LineParallelToPlane(TwoPlanesIntersection):
    
    point_A = [Point(x,y,z) for x in [4,4.5,5,5.5,6,6.5] for y in [2,2.5,3,3.5,4,4.5,5] for z in [1,1.5,2,2.5,3,3.5] ]

    point_O = [Point(x,y,z) for x in range(7,11) for y in range(8,12) for z in range(8,12) ]


    point_B=[Point(x,y,z) for x in [1,1.5,2,2.5,3,3.5] for y in [13,13.5,14,14.5,15] for z in [1,1.5,2,2.5,3,3.5] ]

    point_D=[Point(x,y,z) for x in [1,1.5,2,2.5,3,3.5] for y in [1,1.5,2,2.5,3,3.5] for z in range(8,12) ]
    point_E = [Point(x,y,z) for x in [7,7.5,8,8.5,9] for y in [7,7.5,8.5,9,9.5] for z in range(2,5) ]

    point_F = [Point(x,y,z) for x in  [1,1.5,2,2.5,3,3.5] for y in [10,10.5,11,11.5,12] for z in range(8,12) ]

    def _solution(self):
#         self._line=Line(self._point_N1,self._point_N2)
        current_obj=copy.deepcopy(self)
        
        A=current_obj._point_A
        B=current_obj._point_B
        O=current_obj._point_O
        D=current_obj._point_D
        E=current_obj._point_E
        F=current_obj._point_F
        
        current_set=DrawingSet(*current_obj._solution_step[-1])

        base_plane=Plane(A,B,O)('base')
        line_a=Line(A,O)('a')
        line_b=Line(B,O)('b')
        line_d=Line(D,E)('d')
        line_f=line_d.parallel_line(F)('f')
        edge_plane=Plane(line_f.p1,line_f.p2,line_f.p1@VPP)
        line_q=edge_plane.intersection(base_plane)[0]('q')
#         point_G=line_f_on_AOB.intersection(line_a)[0]
#         point_H=line_f_on_AOB.intersection(line_b)[0]
# #         intersection_line=base_plane.intersection(cutting_plane)[0]('k')
#         P=base_plane.intersection(line_d)[0]('P')
#         Q=base_plane.intersection(line_f)[0]('Q')
#         intersection_line=Line(P,Q)('k')
        
        
        elems=[line_a,line_b,line_d,line_f,line_q]

        
        projections=[line_d@HPP,line_f@HPP,line_d@VPP,line_f@VPP,line_a@HPP,line_b@HPP,line_a@VPP,line_b@VPP,line_q@VPP,line_q@HPP]
        current_set+=[*elems,*projections]

        current_obj._solution_step.append(current_set)

        current_obj._assumptions=DrawingSet(*elems,*projections)

        return current_obj

    def get_default_data(self):

        point_A = self.__class__.point_A
        
        point_O = self.__class__.point_O 
        
        point_B=self.__class__.point_B
        
        point_D=self.__class__.point_D
        point_E = self.__class__.point_E
        point_F = self.__class__.point_F
        
        default_data_dict = {
            Symbol('A'): point_A,
            Symbol('B'): point_B,
            Symbol('O'): point_O,

            Symbol('D'): point_D,
            Symbol('E'): point_E,
            Symbol('F'): point_F,
        }
        return default_data_dict


class PerpendicularLineAndParallelPlaneIntersection(GeometricalCase):

    point_A = [Point(x,y,z) for x in [1,1.5,2,2.5] for y in [2,2.5,3,3.5,4,4.5,5] for z in [2,2.5,3,3.5]  ]

    point_B=  [Point(x,y,z) for x in range(4,6) for y in range(8,12) for z in [2,2.5,3,3.5] ]
    
    point_C = [Point(x,y,z) for x in [1,1.5,2,2.5] for y in [13,13.5,14,14.5,15] for z in [6,6.5,7] ]
    
    point_O = [Point(x,y,z) for x in range(7,10) for y in [6,6.5,7,7.5,8.5] for z in range(6,9) ]
    
    shift = [
        Point(x, y, z) for x in [-1, -0.5, 0, 0.5, 1]
        for y in [-2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2]
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
                point_O @ HPP,
                point_A @ VPP,
                point_B @ VPP,
                point_C @ VPP,
                point_O @ VPP,
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
                               [point_A, point_B, point_C, point_O])
        self._assumptions3d = DrawingSet(point_A, point_B, point_C,
                                         point_O)('Assumptions')
        self._assumptions = DrawingSet(*projections)

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
        A, B, C, D, E, F = Prism.right_from_parallel_plane(triangle_plane, O)

        plane_gamma = Plane(D,E,F)
        
        line_ad = Line(A, D)('a')
#         line_be = Line(B, E)('b')
#         line_cf = Line(C, F)('c')

#         plane_aux = Plane(A, D, A + Point(5, 0, 0))

#         point_P3 = (((O - (point_P1 - A)) ^ O)('h_H') & plane_aux)[0]('3')
#         point_P4 = (((O - (point_P2 - A)) ^ O)('f_H') & plane_aux)[0]('4')

#         current_obj.add_solution_step('Piercing point',
#                                       [point_P3, point_P4])


        elems = [D, E, F, plane_alpha, plane_gamma, line_ad,# line_be, line_cf
                ]

        print(D,D.n().coordinates)
    
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
        
        
        current_obj.point_P = D('P')
        
        #current_obj.point_E = E
        #current_obj.point_F = F
        
        current_obj.add_solution_step('D vertex', [D])
        #current_obj.add_solution_step('P vertex', [D])
        
        current_obj._assumptions = DrawingSet(
            *current_obj.get_projections())('Solution')
        current_obj._assumptions3d = DrawingSet(*current_obj)


        
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
    
    
class PerpendicularLineAndParallelPlaneIntersectionSwappedProjections(PerpendicularLineAndParallelPlaneIntersection):

    shift = [
        Point(x, y, z) for x in [-11, -10.5, -10, -9.5, -9, -8.5, -8]
        for y in [0] for z in [-13, -12, -11, -10.5, -10, -9.5, -9]
    ]

    
    
    
class PerpendicularLineAndParallelHFLinesPlaneIntersection(PerpendicularLineAndParallelPlaneIntersection):
    point_A = [Point(x,y,z) for x in [1,1.5,2,2.5] for y in [2,2.5,3,3.5,4,4.5,5] for z in [2,2.5,3,3.5]  ]

    point_B = [Point(x,y,z) for x in range(7,11) for y in range(8,12) for z in [5,5.5,6,6.5,7] ]


    point_C=[Point(x,y,z) for x in [4,4.5,5,5.5,6] for y in [13,13.5,14,14.5,15] for z in [1,1.5,2,2.5] ]


    point_O=[Point(x,y,z) for x in range(9,12) for y in [6,6.5,7,7.5,8.5] for z in range(9,12) ]


    def get_random_parameters(self):

        parameters_dict=super().get_random_parameters()



        point_A=parameters_dict[Symbol('A')]
        point_B=parameters_dict[Symbol('B')] 
        point_C=parameters_dict[Symbol('C')] 

        
        parameters_dict[Symbol('B')]=Point(point_A.x,point_C.y,point_C.z)
        parameters_dict[Symbol('C')]=Point(point_B.x,point_B.y,point_A.z)

        return parameters_dict
    
class PerpendicularLineAndParallelEdgePlaneIntersection(PerpendicularLineAndParallelPlaneIntersection):
    point_A = [Point(x,y,z) for x in [1,1.5,2,2.5] for y in [2,2.5,3,3.5,4,4.5,5] for z in [2,2.5,3,3.5]  ]

    point_B = [Point(x,y,z) for x in range(7,11) for y in range(8,12) for z in [5,5.5,6,6.5,7] ]


    point_C=[Point(x,y,z) for x in [4,4.5,5,5.5,6] for y in [13,13.5,14,14.5,15] for z in [1,1.5,2,2.5] ]


    point_O=[Point(x,y,z) for x in range(9,12) for y in [6,6.5,7,7.5,8.5] for z in range(9,12) ]


    def get_random_parameters(self):

        parameters_dict=super().get_random_parameters()

        point_A=parameters_dict[Symbol('A')]
        point_B=parameters_dict[Symbol('B')] 
        point_C=parameters_dict[Symbol('C')] 

        
        parameters_dict[Symbol('C')]=(point_A+point_B)*0.5+Point(0,0,5)
        #parameters_dict[Symbol('C')]=Point(point_B.x,point_B.y,point_A.z)

        return parameters_dict
    
class IntersectionOfLineAndParallelPlane(GeometricalCase):

    point_A = [
        Point(x, y, z) for x in [1, 1.5, 2, 2.5]
        for y in [2, 2.5, 3, 3.5, 4, 4.5, 5] for z in range(0, 1)
    ]

    point_B = [
        Point(x, y, z) for x in range(0, 2) for y in range(7, 10)
        for z in range(2, 3)
    ]

    point_C = [
        Point(x, y, z) for x in range(4, 6) for y in [11.5, 12, 12.5, 13]
        for z in range(7, 8)
    ]

    point_O = [
        Point(x, y, z) for x in range(5, 7) for y in [1, 1.5, 2, 2.5]
        for z in range(5, 7)
    ]

    point_M = [
        Point(x, y, z) for x in [4, 5, 6] for y in [7, 7.5, 8.5, 9, 9.5]
        for z in [6, 7, 8]
    ]

    point_N = [
        Point(x, y, z) for x in [7, 7.5, 8, 8.5, 9]
        for y in [9, 10, 19.5, 11, 11.5] for z in range(2, 5)
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
            projections = (point_A @ HPP, point_A @ VPP,
                           point_B @ HPP, point_B @ VPP,
                           Line(point_A @ HPP, point_B @ HPP),
                           Line(point_A @ VPP, point_B @ VPP),
                           Line(point_B @ HPP, point_C @ HPP),
                           Line(point_B @ VPP, point_C @ VPP),
                           Line(point_C @ HPP, point_A @ HPP),
                           Line(point_C @ VPP, point_A @ VPP),
                           Line(point_M @ HPP, point_N @ HPP),
                           Line(point_M @ VPP, point_N @ VPP),
                           point_C @ HPP, point_C @ VPP,
                           point_M @ HPP, point_M @ VPP,
                           point_N @ HPP, point_N @ VPP,
                           point_O @ HPP, point_O @ VPP)
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


        self._assumptions3d = DrawingSet(point_A, point_B, point_C,
                                         point_O)('Assumptions')
        self._assumptions = DrawingSet(*projections)

        self.add_solution_step('Assumptions',
                               [point_A, point_B, point_C, point_O])

    def _solution(self):

        current_obj = copy.deepcopy(self)
        current_set = DrawingSet(*current_obj._solution_step[-1])
        A = current_obj._point_A
        B = current_obj._point_B
        C = current_obj._point_C

        M = current_obj._point_M
        N = current_obj._point_N
        O = current_obj._point_O

        plane_alpha = Plane(A, B, C)

        dAO = O - A

        D = O('D')
        E = (B + dAO)('E')
        F = (C + dAO)('F')

        current_obj.add_solution_step('Points D, E, F, O', [D, E, F, O], [D, E, F, O])

        line_mn=Line(M, N)('m')
        line_de=Line(D, E)('d')
        line_ef=Line(E, F)('e')
        line_df=Line(D, F)('f')

        current_obj.add_solution_step('Lines', [line_mn, line_de, line_ef, line_df], [line_mn, line_de, line_ef, line_df])

        plane_beta = Plane(D, E, F)

        G = (plane_beta & line_mn)[0]('G')

        current_obj.add_solution_step('Piercing point G', [G], [G])

        elems = [D, E, F, G, line_mn, line_de, line_ef, line_df]

        projections = [
            line_mn @ HPP, line_mn @ VPP, line_de @ HPP, line_de @ VPP,
            line_ef @ HPP, line_ef @ VPP, line_df @ HPP, line_df @ VPP,
            D @ HPP, D @ VPP, E @ HPP, E @ VPP, G @ HPP, G @ VPP, F @ HPP,
            F @ VPP
        ]

        current_set += [*elems, *projections]
        current_obj._solution_step.append(current_set)
        current_obj.point_D = D
        current_obj.point_E = E
        current_obj.point_F = F
        current_obj.point_G = G

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

