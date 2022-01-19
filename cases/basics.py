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
        self._given_data={'A':point_A,'B':point_B}

        self._point_A=point_A
        self._point_B=point_B
        
        self._solution_step.append(self._assumptions)



    def solution(self):
        
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
        #self._given_data={'A':point_A,'B':point_B,'D':point_D}

        self._point_A=point_A
        self._point_B=point_B
        
        print('given_data',self._given_data)
        
        self._solution_step.append(self._assumptions)



    def solution(self):
        
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



    def solution(self):
        
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

    def solution(self):
        
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
    def solution(self):
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
    def solution(self):
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
    point_E = [Point(x,y,z) for x in range(1,5) for y in range(8,12) for z in range(2,5) ]
    point_F = [Point(x,y,z) for x in range(7,11) for y in range(13,16) for z in range(8,12) ]
    
    
    def __init__(self,point_A=None,point_B=None,point_O=None,point_C=None,point_D=None,**kwargs):

        super().__init__()

        if point_A and point_B and point_O and point_C and point_D:
            projections=(point_A@HPP,point_B@HPP,Line(point_A@HPP,point_O@HPP),Line(point_A@VPP,point_O@VPP),
                         Line(point_B@HPP,point_O@HPP),Line(point_B@VPP,point_O@VPP),point_A@VPP,point_B@VPP,
                         point_O@HPP,point_O@VPP,point_C@VPP,point_D@VPP,point_C@HPP,point_D@HPP,point_C@VPP,point_D@VPP
                        )
        else:
            projections=[]

        self._assumptions=DrawingSet(*projections)


        self._point_A=point_A
        self._point_B=point_B
        self._point_O=point_O
        self._point_C=point_C
        self._point_D=point_D


        self._given_data={'A':point_A,'B':point_B,'O':point_A,'C':point_C,'D':point_D}


        
        self._solution_step.append(self._assumptions)
#     def solution(self):

        
#         midpoint=(A+ (B-A)*0.5)('C')
#         current_set += [midpoint]
        
#         current_obj._solution_step.append(current_set)
        
        
#         current_obj.midpoint = midpoint
#         current_obj.point_C = midpoint
        
#         return current_obj
    def solution(self):
        self._line=Line(self._point_C,self._point_D)
        current_obj=copy.deepcopy(self)
        
        A=current_obj._point_A
        B=current_obj._point_B
        O=current_obj._point_O
        n=current_obj._line
        current_set=DrawingSet(*current_obj._solution_step[-1])

        base_plane=Plane(A,B,O)('base')
        line_a=Line(self._point_C,self._point_C+Point(15,0,0))('a')
        line_b=Line(self._point_D,self._point_D+Point(15,0,0))('b')

        plane_v=base_plane('alpha') #why is the line created? #looks unnecessary
        #plane_h=Plane(n.p1,n.p2,n.p1@HPP)('beta')
        #int_line_h=Line(plane_h.intersection(line_a)[0],plane_h.intersection(line_b)[0])('n')
        int_line_v=Line(plane_v.intersection(line_a)[0],plane_v.intersection(line_b)[0])('n') 

        elems=[line_a,line_b,int_line_v]
        projections=[line_a@HPP,line_b@HPP,line_a@VPP,line_b@VPP]
        current_set+=[*elems,*projections]

        current_obj._solution_step.append(current_set)
        current_obj.int_line_v_p1=(int_line_v).p1 #names
        current_obj.int_line_v_p2=(int_line_v).p2 #names
        
        current_obj.point_P=(int_line_v).p1 #names
        current_obj.point_Q=(int_line_v).p2 #names
        
        
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

            Symbol('C'): point_D,
            Symbol('D'): point_F,
        }
        return default_data_dict
    
    
    
class PointOnPlane(GeometricalCase):

    point_A = [Point(x,y,z) for x in [1,1.5,2,2.5,3,3.5] for y in range(2,6) for z in [1,1.5,2,2.5,3,3.5] ]
#     distance_AO = [Point(2,4,2),Point(2,5,2),Point(2,6,2),Point(3,4,4)]

#     point_O = [pt + dist  for pt,dist   in  it.product(point_A,distance_AO)]
    point_O = [Point(x,y,z) for x in range(7,11) for y in range(8,12) for z in range(8,12) ]
    distance_OB = [Point(-4,4,-4),Point(-5,5,-4),Point(-4,5,-6),Point(-5,4,-7)]

    point_B=[Point(x,y,z) for x in [1,1.5,2,2.5,3,3.5] for y in [13,13.5,14,14.5,15] for z in [1,1.5,2,2.5,3,3.5] ]


    distance_AD = [Point(x,y,z) for x in range(1,5) for y in range(0,4) for z in range(1,5) ]
    distance_OE = [Point(x,y,z) for x in range(-5,-1) for y in range(-1,4) for z in range(-5,-1) ]
    distance_BF = [Point(x,y,z) for x in range(1,5) for y in range(-2,3) for z in range(1,5) ]

#     point_D=[pt + dist  for pt,dist   in  it.product(point_A,distance_AD) if (pt+dist).x != 0]
#     point_E = [pt + dist  for pt,dist   in  it.product(point_O,distance_OE) if (pt+dist).x != 0]
#     point_F = [pt + dist  for pt,dist   in  it.product(point_B,distance_BF) if (pt+dist).x != 0]

    point_D=[Point(x,y,z) for x in range(7,11) for y in range(2,6) for z in range(8,12) ]
    point_E = [Point(x,y,z) for x in range(1,5) for y in range(8,12) for z in range(2,5) ]
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

        
    def solution(self):
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

        
    def solution(self):
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

        
    def solution(self):
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

        
    def solution(self):
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

        
    def solution(self):
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

        
    def solution(self):
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

        
    def solution(self):
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

    def solution(self):
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
        current_obj=copy.deepcopy(self)

        A=current_obj._point_A
        B=current_obj._point_B

        current_set=DrawingSet(*current_obj._solution_step[-1])

        line_a=Line(A,B)('a')
        S=Point(B.x,B.y,A.z)('S')
        line_l=Line(B,S)('l')
        epsilon=HorizontalPlane(A)
        A_0=Point(B.x,B.y+(B@HPP).distance(A@HPP),A.z)
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


    point_A = [Point(x,y,z) for x in [8,8.5,9,7.5,7] for y in [5,5.5,6,6.5] for z in   [8,8.5,7.5,7]  ]

    point_B=[Point(x,y,z) for x in [5,5.5,6,6.5] for y in [8,8.5,9,9.5,10] for z in   [4,4.5,5,5.5] ]

    point_C = [Point(x,y,z) for x in [1,1.5,2,2.5] for y in [2,2.5,3,3.5]  for z in [1,1.5,2,2.5] ]





    def __init__(self,point_A=None,point_B=None,point_C=None,**kwargs):

        super().__init__()

        if point_A and point_B and point_C:
            projections=(point_A@HPP,point_B@HPP,point_A@VPP,point_B@VPP,point_C@HPP,point_C@VPP,)
        else:
            projections=[]

        self._assumptions=DrawingSet(*projections)

        self._point_A=point_A
        self._point_B=point_B
        self._point_C=point_C

        
        self._given_data={'A':point_A,'B':point_B,'C':point_C}
        
        self._solution_step.append(self._assumptions)

    def solution(self):
        current_obj=copy.deepcopy(self)
        
        A=current_obj._point_A
        B=current_obj._point_B
        C=current_obj._point_C


        
        current_set=DrawingSet(*current_obj._solution_step[-1])

        line_a=Line(A,B)('a')
        line_b=Line(C,A)('b')
        plane_alpha=Plane(A,B,C)

        plane_beta=HorizontalPlane(C)

        line_k = plane_alpha.intersection(plane_beta)[0]

        elems=self._assumptions
        projections=[]
        point_0_dict={}
        for point_I in [A,B]:
        
            S_I = (point_I @ line_k)('k')



            # zaimplementować w metode dla punktu 
            dir_I_on_HPP =(point_I @ plane_beta) - S_I
            
            #display(dir_I_on_HPP.coordinates)
            #display((point_I @ plane_beta).distance( S_I ))
            #display(point_I.distance( S_I ))
            
            ratio = (point_I.distance( S_I )) /(point_I @ plane_beta).distance( S_I )
            
            I_o =(S_I+(dir_I_on_HPP)*ratio)(point_I._label+'_0')
            
            point_0_dict[str(point_I)]=I_o
            elems += [I_o]
            projections+=[I_o@HPP,I_o@VPP]

            
        line_kk=Line(C,S_I)
        #print(point_0_dict)
        elems+=[line_a,line_b,#,E,F,G,H,line_s1,line_s2,line_s3,line_s4
              ]

        projections+=[line_a@HPP,line_a@VPP,line_b@HPP,line_b@VPP,line_kk@HPP,line_kk@VPP,#line_s1@HPP,line_s1@VPP,line_s2@HPP,line_s2@VPP,line_s3@HPP,line_s3@VPP,
                     #line_s4@HPP,line_s4@VPP
                    ]
        current_set+=[*elems,*projections]
        current_obj.A0=point_0_dict['A']
        current_obj.B0=point_0_dict['B']
        current_obj.C0=C
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

        self._point_A=point_A
        self._point_P=point_P
        self._point_O=point_O


        
        self._given_data={'A':point_A,'P':point_P,'O':point_O}
        
        self._solution_step.append(self._assumptions)

    def solution(self):
        current_obj=copy.deepcopy(self)
        
        A=current_obj._point_A
        O=current_obj._point_O
        P=current_obj._point_P

        
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
        for point_I in [A,B,C,O]:
        
            S_I = (point_I @ line_k)('k')



            # zaimplementować w metode dla punktu 
            dir_I_on_HPP =(point_I @ plane_beta) - S_I
            
            #display(dir_I_on_HPP.coordinates)
            #display((point_I @ plane_beta).distance( S_I ))
            #display(point_I.distance( S_I ))
            
            ratio = (point_I.distance( S_I )) /(point_I @ plane_beta).distance( S_I )
            
            I_o =(S_I+(dir_I_on_HPP)*ratio)(point_I._label+'_0')
            
            point_0_dict[str(point_I)]=I_o
            elems += [I_o]
            projections+=[I_o@HPP,I_o@VPP]

            
        line_kk=Line(P,S_I)('k')
        
        current_obj.A0=point_0_dict['A']
        current_obj.B0=point_0_dict['B']
        current_obj.C0=point_0_dict['C']
        
        
     
        
        #print(point_0_dict)
        elems+=[line_a,line_b,#,E,F,G,H,line_s1,line_s2,line_s3,line_s4
              ]

        projections+=[current_obj.A0@HPP,current_obj.A0@VPP,current_obj.B0@HPP,current_obj.B0@VPP,
                      current_obj.C0@HPP,current_obj.C0@VPP,B@HPP,B@VPP,C@HPP,C@VPP,line_a@HPP,line_a@VPP,line_b@HPP,line_b@VPP,
                      line_kk@HPP,line_kk@VPP,#line_s1@HPP,line_s1@VPP,line_s2@HPP,line_s2@VPP,line_s3@HPP,line_s3@VPP,
                     #line_s4@HPP,line_s4@VPP
                    ]
        current_set+=[*elems,*projections]

        current_obj._solution_step.append(current_set)
        current_obj._assumptions=DrawingSet(*elems,*projections)
        current_obj._point_B=B
        current_obj._point_C=C

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

        self._point_A=point_A
        self._point_P=point_P
        self._point_O=point_O

        
        self._given_data={'A':point_A,'P':point_P,'O':point_O}
        
        self._solution_step.append(self._assumptions)

    def solution(self):
        current_obj=copy.deepcopy(self)
        
        A=current_obj._point_A
        O=current_obj._point_O
        P=current_obj._point_P
        
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
        for point_I in [A,B,C,D,O]:
        
            S_I = (point_I @ line_k)('k')



            # zaimplementować w metode dla punktu 
            dir_I_on_HPP =(point_I @ plane_beta) - S_I
            
            #display(dir_I_on_HPP.coordinates)
            #display((point_I @ plane_beta).distance( S_I ))
            #display(point_I.distance( S_I ))
            
            ratio = (point_I.distance( S_I )) /(point_I @ plane_beta).distance( S_I )
            
            I_o =(S_I+(dir_I_on_HPP)*ratio)(point_I._label+'_0')
            
            point_0_dict[str(point_I)]=I_o
            elems += [I_o]
            projections+=[I_o@HPP,I_o@VPP]

            
        line_kk=Line(P,S_I)('k')
        
        current_obj.A0=point_0_dict['A']
        current_obj.B0=point_0_dict['B']
        current_obj.C0=point_0_dict['C']
        current_obj.D0=point_0_dict['D']
        
        #print(point_0_dict)
        elems+=[line_a,line_b,#,E,F,G,H,line_s1,line_s2,line_s3,line_s4
              ]

        projections+=[current_obj.D0@HPP,current_obj.D0@VPP,D@HPP,D@VPP,
            current_obj.A0@HPP,current_obj.A0@VPP,current_obj.B0@HPP,current_obj.B0@VPP,
                      current_obj.C0@HPP,current_obj.C0@VPP,B@HPP,B@VPP,C@HPP,C@VPP,line_a@HPP,line_a@VPP,line_b@HPP,line_b@VPP,
                      line_kk@HPP,line_kk@VPP,#line_s1@HPP,line_s1@VPP,line_s2@HPP,line_s2@VPP,line_s3@HPP,line_s3@VPP,
                     #line_s4@HPP,line_s4@VPP
                    ]
        current_set+=[*elems,*projections]

        current_obj._solution_step.append(current_set)
        current_obj._assumptions=DrawingSet(*elems,*projections)
        current_obj._point_B=B
        current_obj._point_C=C
        current_obj._point_D=D
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

        self._point_A=point_A
        self._point_P=point_P
        self._point_O=point_O

        
        self._given_data={'A':point_A,'P':point_P,'O':point_O}
        
        self._solution_step.append(self._assumptions)

    def solution(self):
        current_obj=copy.deepcopy(self)
        
        A=current_obj._point_A
        O=current_obj._point_O
        P=current_obj._point_P
        
        S = (A @ (O^P))('S') #'Srodek' podstawy
        
        dirPS = P-S
        dirOS = O-S
        triangle_height = A.distance(S)
        triangle_side =  triangle_height / ((3**(1/2))/2)
        
        B = (S + dirPS/(P.distance(S))*(triangle_side/2))('B')
        C = (S - dirPS/(P.distance(S))*(triangle_side/2))('C')


        
        current_set=DrawingSet(*current_obj._solution_step[-1])

        line_a=Line(A,B)('a')
        line_b=Line(C,A)('b')
        plane_alpha=Plane(A,O,P)

        plane_beta=HorizontalPlane(P)

        line_k = plane_alpha.intersection(plane_beta)[0]

        elems=self._assumptions
        projections=[]
        point_0_dict={}
        for point_I in [A,B,C,O]:
        
            S_I = (point_I @ line_k)('k')



            # zaimplementować w metode dla punktu 
            dir_I_on_HPP =(point_I @ plane_beta) - S_I
            
            #display(dir_I_on_HPP.coordinates)
            #display((point_I @ plane_beta).distance( S_I ))
            #display(point_I.distance( S_I ))
            
            ratio = (point_I.distance( S_I )) /(point_I @ plane_beta).distance( S_I )
            
            I_o =(S_I+(dir_I_on_HPP)*ratio)(point_I._label+'_0')
            
            point_0_dict[str(point_I)]=I_o
            elems += [I_o]
            projections+=[I_o@HPP,I_o@VPP]

            
        line_kk=Line(P,S_I)('k')
        
        current_obj.A0=point_0_dict['A']
        current_obj.B0=point_0_dict['B']
        current_obj.C0=point_0_dict['C']
        
        
        #print(point_0_dict)
        elems+=[line_a,line_b,#,E,F,G,H,line_s1,line_s2,line_s3,line_s4
              ]

        projections+=[current_obj.A0@HPP,current_obj.A0@VPP,current_obj.B0@HPP,current_obj.B0@VPP,
                      current_obj.C0@HPP,current_obj.C0@VPP,B@HPP,B@VPP,C@HPP,C@VPP,line_a@HPP,line_a@VPP,line_b@HPP,line_b@VPP,
                      line_kk@HPP,line_kk@VPP,#line_s1@HPP,line_s1@VPP,line_s2@HPP,line_s2@VPP,line_s3@HPP,line_s3@VPP,
                     #line_s4@HPP,line_s4@VPP
                    ]
        current_set+=[*elems,*projections]

        current_obj._solution_step.append(current_set)
        current_obj._assumptions=DrawingSet(*elems,*projections)
        current_obj._point_B=B
        current_obj._point_C=C
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

            # it creates next step of solution - lines are presented
            #current_step3d=copy.deepcopy(current_obj._solution3d_step[-1])+[(A^point_P1)('AO'),point_P1,(P^point_P1)('a')]

            #it sets the step elements


            
            current_obj.add_solution_step(
                f'Axis of rotation - it is common part between given plane and horizontal plane which contains point {P._label}', [point_P2, line_f])
            
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
    