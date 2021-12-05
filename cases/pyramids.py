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

class HFLinesIsoscelesRightTrianglePyramid(GeometricalCase):

    #quite good data
    #point_A = [Point(x,y,z) for x in [4,5.5,5] for y in [5,5.5,6] for z in   [5.5,6,6.5]  ]

    #point_O=[Point(x,y,z) for x in [3,3.5] for y in [8,8.5,9] for z in   [3,3.5,4] ]

    #point_P = [Point(x,y,z) for x in [6,6.5,7] for y in [3,3.5]  for z in [1,1.5,2] ]

    #point_H = [Point(x,y,z) for x in range(9,11) for y in [3,3.5] for z in range(9,11) ]

    # new set
    point_A = [Point(x,y,z) for x in [3,3.5] for y in [8,8.5,9] for z in   [6,7]  ]

    point_O=[Point(x,y,z) for x in  [6,7] for y in [11,11.5,12] for z in   [2.5,3,3.5] ]

    point_P = [Point(x,y,z) for x in [1,1.5,2] for y in [3,3.5]  for z in [1,1.5,2] ]

    point_H = [Point(x,y,z) for x in [7,7.5,8] for y in [1,1.5,2] for z in [5.5,6,6.5] ]
    #point_H = [Point(x,y,z) for x in [1,1.5] for y in [1,1.5,2] for z in [5.5,6,6.5] ]
    

    def __init__(self,point_A=None,point_P=None,point_O=None,point_H=None,**kwargs):

        super().__init__()
        self._solution_step=[]
        self._solution3d_step=[]

        if point_A and point_O and point_P and point_H:
            projections=(point_A@HPP,point_O@HPP,point_O@VPP,point_P@VPP,point_P@HPP,point_A@VPP,point_H@VPP,point_H@HPP)
            
        else:
            projections=[]

        self._assumptions=DrawingSet(*projections)('Assumptions')
        self._assumptions3d=DrawingSet(point_A,point_O,point_P,point_H)('Assumptions')
        

        self._point_A=point_A
        self._point_P=point_P
        self._point_O=point_O
        self._point_H=point_H

        
        self._given_data={'A':point_A,'P':point_P,'O':point_O,'H':point_H}
        
        self._solution_step.append(self._assumptions)
        self._solution3d_step.append(self._assumptions3d)

    def solution(self):
        current_obj=copy.deepcopy(self)
        
        A=current_obj._point_A
        O=current_obj._point_O
        P=current_obj._point_P
        H=current_obj._point_H
        
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
        
        

        line_k = plane_alpha.intersection(plane_beta)[0]('a')
        
        
        point_P1 = plane_beta.intersection(A^O)[0]('1')
        line_kk = (P^point_P1)('a')
        
        
        #current_step3d=copy.deepcopy(current_obj._solution3d_step[-1])+[(A^point_P1)('AO'),point_P1,(P^point_P1)('a')]
        current_step3d=[(A^point_P1)('AO'),point_P1,(P^point_P1)('a')]
        
        
        
        current_obj._solution3d_step.append(DrawingSet(*current_step3d)('Step 1 - axis of rotation'))
        current_obj._solution_step.append(DrawingSet(*([obj@HPP for obj  in current_step3d] + [obj@VPP for obj  in current_step3d])   )('Step 1 - axis of rotation'))


        elems=self._assumptions
        projections=[]
        point_0_dict={}
        eps_dict={}
        
        #for point_I in [A]:
        
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

        current_obj.A0=A.rotate_about(axis=line_k)('A_0')
        current_obj.B0=B.rotate_about(axis=line_k)('B_0')
        current_obj.C0=C.rotate_about(axis=line_k)('C_0')
        #current_obj.D0=D.rotate_about(axis=line_k)('D_0')
        current_obj.O0=O.rotate_about(axis=line_k)('O_0')
        
        
        point_B=B
        point_C=C
        point_O=O
        current_obj.A0=point_0_dict['A']
        current_obj.B0=point_B
        current_obj.C0=point_C
        current_obj.O0=point_O

#         plane_beta=Plane(H,H+(A-P),H-(O-P))
#         D=(C@plane_beta)('D')

        triangle_plane=Plane(A,B,C)

        A,B,C,D = [*Pyramid].right_from_parallel_plane(triangle_plane, H)

        

        elems+=[D]

        projections+=[
                     D@HPP,D@VPP]
        
        
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
        current_obj.point_D=D


        return current_obj

    def present_solution(self):
        
        doc_model = Document(f'{self.__class__.__name__} solution')

        doc_model.packages.append(Package('booktabs'))
        doc_model.packages.append(Package('float'))
        doc_model.packages.append(Package('standalone'))
        doc_model.packages.append(Package('siunitx'))


        ReportText.set_container(doc_model)
        ReportText.set_directory('./SDAresults')

        for no,step3d in enumerate(self._solution3d_step):
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
        point_P=self.__class__.point_P
        point_H=self.__class__.point_H




        
        default_data_dict = {
            Symbol('A'): point_A,
            Symbol('P'): point_P,
            Symbol('O'): point_O,
            

            Symbol('H'): point_H,


        }
        return default_data_dict
    def get_random_parameters(self):
        


        parameters_dict=super().get_random_parameters()

        point_H=parameters_dict[Symbol('H')] 
        point_O=parameters_dict[Symbol('O')] 
        point_A=parameters_dict[Symbol('A')] 
        point_P=parameters_dict[Symbol('P')] 

        parameters_dict[Symbol('A')]=Point(point_O.x,point_A.y,point_A.z)
        parameters_dict[Symbol('P')]=Point(point_P.x,point_P.y,point_O.z)
        

        return parameters_dict
    
class RectangleLongSideAtPOPyramid(GeometricalCase):


    point_A = [Point(x,y,z) for x in [3,3.5] for y in [8,8.5,9] for z in   [6,7]  ]

    point_O=[Point(x,y,z) for x in  [6,7] for y in [11,11.5,12] for z in   [2.5,3,3.5] ]

    point_P = [Point(x,y,z) for x in [1,1.5,2] for y in [3,3.5]  for z in [1,1.5,2] ]

    point_H = [Point(x,y,z) for x in range(7,9) for y in [3,3.5] for z in range(9,11) ]
    

    def __init__(self,point_A=None,point_P=None,point_O=None,point_H=None,**kwargs):

        super().__init__()

        if point_A and point_O and point_P and point_H:
            projections=(point_A@HPP,point_O@HPP,point_O@VPP,point_P@VPP,point_P@HPP,point_A@VPP,point_H@VPP,point_H@HPP)
        else:
            projections=[]

        self._assumptions=DrawingSet(*projections)

        self._point_A=point_A
        self._point_P=point_P
        self._point_O=point_O
        self._point_H=point_H

        
        self._given_data={'A':point_A,'P':point_P,'O':point_O,'H':point_H}
        
        self._solution_step.append(self._assumptions)

    def solution(self):
        current_obj=copy.deepcopy(self)
        
        A=current_obj._point_A
        O=current_obj._point_O
        P=current_obj._point_P
        H=current_obj._point_H
        
        S = (A @ (O^P))('S') #'Srodek' podstawy
        
        dirPS = P-S
        dirOS = O-S
        dirAS = S-A
        longer_leg = 2*A.distance(S)
        
        #square_side =  square_diagonal / (((3)**(1/2))/2)
#         print(square_diagonal)
        C = (S + dirPS/(P.distance(S))*(longer_leg))('C')

        B = (A @ (O^P))('B')
        
        D = (A + (C-B) )('D')
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

            
#         line_kk=Line(P,S_I)('k')

        current_obj.A0=A.rotate_about(axis=line_k)('A_0')
        current_obj.B0=B.rotate_about(axis=line_k)('B_0')
        current_obj.C0=C.rotate_about(axis=line_k)('C_0')
        current_obj.D0=D.rotate_about(axis=line_k)('D_0')
        current_obj.O0=O.rotate_about(axis=line_k)('O_0')
        
#         current_obj.A0=point_0_dict['A']
#         current_obj.B0=point_0_dict['B']
#         current_obj.C0=point_0_dict['C']
#         current_obj.D0=point_0_dict['D']
        
        
#         #plane_beta=Plane(H,H+(B-A),H-(C-A))
#         plane_beta=Plane(H,H+(A-P),H-(O-P))
#         E=(A@plane_beta)('E')

        rectangle_plane=Plane(A,B,C)

        A,B,C,D,E = [*Pyramid].right_from_parallel_plane(rectangle_plane, H)

        line_ae=Line(S,E)('a')

        elems+=[E,plane_alpha,line_ae]

        projections+=[line_ae@HPP,line_ae@VPP,
                     E@HPP,E@VPP]
        
        
        #print(point_0_dict)
        elems+=[line_a,line_b,#,E,F,G,H,line_s1,line_s2,line_s3,line_s4
              ]

        projections+=[current_obj.A0@HPP,current_obj.A0@VPP,current_obj.B0@HPP,current_obj.B0@VPP,
                      current_obj.C0@HPP,current_obj.C0@VPP,
                      #current_obj.D0@HPP,current_obj.D0@VPP,
                      B@HPP,B@VPP,C@HPP,C@VPP,
                      D@HPP,D@VPP,
                      line_a@HPP,line_a@VPP,
                      line_kk@HPP,line_kk@VPP,#line_s1@HPP,line_s1@VPP,line_s2@HPP,line_s2@VPP,line_s3@HPP,line_s3@VPP,
                     #line_s4@HPP,line_s4@VPP
                    ]
        current_set+=[*elems,*projections]

        current_obj._solution_step.append(current_set)
        current_obj._assumptions=DrawingSet(*elems,*projections)
        current_obj._point_B=B
        current_obj._point_C=C
        current_obj._point_D=D
        current_obj.point_E=E
        return current_obj


    
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
    
class RightTriangleShortLegAtPOPyramid(GeometricalCase):


    point_A = [Point(x,y,z) for x in [6,6.5] for y in [7,7.5] for z in   [8,8.5]  ]

    point_O=[Point(x,y,z) for x in  [4,5] for y in [4.5,5] for z in   [7,7.5] ]

    point_P = [Point(x,y,z) for x in [2,2.5] for y in [13,13.5]  for z in [2,2.5] ]

    point_H = [Point(x,y,z) for x in [9,9.5,10] for y in [6,7] for z in range(9,11) ]
    
    shift = [Point(x,y,z) for x in [-1,-0.5,0,0.5,1] for y in [1,1.5,2] for z in [-1,-0.5,0,0.5,1] ]
    

    def __init__(self,point_A=None,point_P=None,point_O=None,point_H=None,*args,**kwargs):

        super().__init__()

        if point_A and point_O and point_P and point_H:
            projections=(point_A@HPP,point_O@HPP,point_O@VPP,point_P@VPP,point_P@HPP,point_A@VPP,point_H@VPP,point_H@HPP)
        else:
            projections=[]

        self._assumptions=DrawingSet(*projections)

        self._point_A=point_A
        self._point_P=point_P
        self._point_O=point_O
        self._point_H=point_H

        
        self._given_data={'A':point_A,'P':point_P,'O':point_O,'H':point_H}
        
        self._solution_step.append(self._assumptions)

    def solution(self):
            

        
        if self._cached_solution is None:
            
            current_obj = copy.deepcopy(self)
        
            A=current_obj._point_A
            O=current_obj._point_O
            P=current_obj._point_P
            H=current_obj._point_H

            S = (A @ (O^P))('S') #'Srodek' podstawy

            dirPS = P-S
            dirOS = O-S
            dirAS = S-A
            shorter_leg = 1.5*A.distance(S)

            #square_side =  square_diagonal / (((3)**(1/2))/2)
    #         print(square_diagonal)
            C = (S + dirOS/(O.distance(S))*(shorter_leg))('C')
    #         D = (S - dirPS/(P.distance(S))*(diamond_diagonal))('D')
            B = (A @ (O^P))('B')
    #         line_AD=A^D
    #         line_AB=A^B
    #         line_BC=line_AD.parallel_line(P)
    #         line_AS=Line(A,S)
    #         C=line_BC.intersection(line_AS)[0]



            current_set=DrawingSet(*current_obj._solution_step[-1])

            line_a=Line(A,B)('a')
            line_b=Line(B,C)('b')
            line_c=Line(C,A)('c')
            #line_d=Line(D,A)('d')
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
            #current_obj.D0=point_0_dict['D']

            #plane_beta=Plane(H,H+(B-A),H-(C-A))
            plane_beta=Plane(H,H+(A-P),H-(O-P))
            E=(A@plane_beta)('E')


            line_ae=Line(S,E)('a')

            elems+=[E,plane_alpha,line_ae]

            projections+=[line_ae@HPP,line_ae@VPP,
                         E@HPP,E@VPP]


            #print(point_0_dict)
            elems+=[line_a,line_b,#,E,F,G,H,line_s1,line_s2,line_s3,line_s4
                  ]

            projections+=[current_obj.A0@HPP,current_obj.A0@VPP,current_obj.B0@HPP,current_obj.B0@VPP,
                          current_obj.C0@HPP,current_obj.C0@VPP,
                          #current_obj.D0@HPP,current_obj.D0@VPP,
                          B@HPP,B@VPP,C@HPP,C@VPP,
                          #D@HPP,D@VPP,
                          line_a@HPP,line_a@VPP,
                          line_kk@HPP,line_kk@VPP,#line_s1@HPP,line_s1@VPP,line_s2@HPP,line_s2@VPP,line_s3@HPP,line_s3@VPP,
                         #line_s4@HPP,line_s4@VPP
                        ]
            current_set+=[*elems,*projections]

            current_obj._solution_step.append(current_set)
            current_obj._assumptions=DrawingSet(*elems,*projections)
            current_obj._point_B=B
            current_obj._point_C=C
            #current_obj._point_D=D
            current_obj.point_E=E
            
            self._cached_solution = current_obj
            
        else:
            current_obj = copy.deepcopy(self._cached_solution)
            
        return current_obj

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

        for point in symbols('H O A P'): 
            parameters_dict[point]=parameters_dict[point] + shift

        

        return parameters_dict
    
class RightTriangleLongLegAtPOPyramid(GeometricalCase):


    point_A = [Point(x,y,z) for x in [6,6.5] for y in [7,7.5] for z in   [8,8.5]  ]

    point_O=[Point(x,y,z) for x in  [4,5] for y in [4.5,5] for z in   [4.5,5,5.5] ]

    point_P = [Point(x,y,z) for x in [2,2.5] for y in [13,13.5]  for z in [2,2.5] ]

    point_H = [Point(x,y,z) for x in [9,9.5,10] for y in [6,7] for z in range(9,11) ]
    
    shift = [Point(x,y,z) for x in [-1,-0.5,0,0.5,1] for y in [-1,-0.5,0,1,1.5,2] for z in [-1,-0.5,0,0.5,1] ]
    

    
    
    
    def __init__(self,point_A=None,point_P=None,point_O=None,point_H=None,*args,**kwargs):

        super().__init__()

        if point_A and point_O and point_P and point_H:
            projections=(point_A@HPP,point_O@HPP,point_O@VPP,point_P@VPP,point_P@HPP,point_A@VPP,point_H@VPP,point_H@HPP)
        else:
            projections=[]

        # it creates first step of solution
        self.add_solution_step('Assumptions',[point_A,point_O,point_P,point_H])
        #self._assumptions3d=DrawingSet(point_A,point_O,point_P,point_H)('Assumptions')
        
        #self += [point_A,point_O,point_P,point_H]

        self._point_A=point_A
        self._point_P=point_P
        self._point_O=point_O
        self._point_H=point_H

        
        self._given_data={'A':point_A,'P':point_P,'O':point_O,'H':point_H}
        


    def solution(self):
        

        
        if self._cached_solution is None:
            
            current_obj = copy.deepcopy(self)
        
            A=current_obj._point_A
            O=current_obj._point_O
            P=current_obj._point_P
            H=current_obj._point_H

            S = (A @ (O^P))('S') #'Srodek' podstawy

            dirPS = P-S
            dirOS = O-S
            dirAS = S-A
            longer_leg = 2*A.distance(S)

            C = (S + dirPS/(P.distance(S))*(longer_leg))('C')
            B = (A @ (O^P))('B')

            triangle_plane=Plane(A,B,C)


            line_a=Line(A,B)('a')
            line_b=Line(C,A)('b')
            plane_alpha=Plane(A,O,P)

            plane_beta=HorizontalPlane(P)



            line_k = plane_alpha.intersection(plane_beta)[0]('a')


            point_P1 = plane_beta.intersection(A^O)[0]('1')
            current_obj.P1=point_P1
            line_kk = (P^point_P1)('a')



            # it creates next step of solution - lines are presented
            #current_step3d=copy.deepcopy(current_obj._solution3d_step[-1])+[(A^point_P1)('AO'),point_P1,(P^point_P1)('a')]

            #it sets the step elements
            current_obj.add_solution_step('Step 1 - axis of rotation',[(A^point_P1)('AO'),point_P1,(P^point_P1)('a')])



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




            current_obj.C0=C.rotate_about(axis=line_k)('C_0')

            #### Step 5 ####
            ### postion of C0 (based on triangle geometry) #####      

            #current_obj.D0=D.rotate_about(axis=line_k)('D_0')
            current_obj.O0=O.rotate_about(axis=line_k)('O_0')



            G = (H@plane_alpha)('G')


            ############  upper  base



            
            plane_beta=Plane(H,H+(A-P),H-(O-P))
            E=(A@plane_beta)('E')

            current_obj.add_solution_step('Vertex E',[E])
            
            
            line_ae=Line(S,E)('a')

            elems+=[E,plane_alpha,line_ae]

            projections+=[line_ae@HPP,line_ae@VPP,
                         E@HPP,E@VPP]


            #print(point_0_dict)
            elems+=[point_P1,line_a,line_b,#,E,F,G,H,line_s1,line_s2,line_s3,line_s4
                   ]

            projections+=[point_P1@HPP,point_P1@VPP,
                          current_obj.A0@HPP,current_obj.A0@VPP,current_obj.B0@HPP,current_obj.B0@VPP,
                          current_obj.C0@HPP,current_obj.C0@VPP,
                          #current_obj.D0@HPP,current_obj.D0@VPP,
                          B@HPP,B@VPP,C@HPP,C@VPP,
                          #D@HPP,D@VPP,
                          line_a@HPP,line_a@VPP,
                          line_kk@HPP,line_kk@VPP,#line_s1@HPP,line_s1@VPP,line_s2@HPP,line_s2@VPP,line_s3@HPP,line_s3@VPP,
                         #line_s4@HPP,line_s4@VPP
                        ]
            #current_set+=[*elems,*projections]

            #current_obj._solution_step.append(current_set)
            current_obj._assumptions=DrawingSet(*elems,*projections)
            current_obj._point_B=B
            current_obj._point_C=C
            #current_obj._point_D=D
            current_obj.point_E=E
            
            current_obj._assumptions=DrawingSet(*current_obj.get_projections())('Solution')
            current_obj._assumptions3d=DrawingSet(*current_obj)
            
            self._cached_solution = current_obj
            
        else:
            current_obj = copy.deepcopy(self._cached_solution)
            
            
        return current_obj

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
        

        for point in symbols('H O A P'): 
            parameters_dict[point]=parameters_dict[point] + shift
            
            

        

        return parameters_dict
    
class SquarePyramid(GeometricalCase):


    point_A = [Point(x,y,z) for x in [3,3.5] for y in [8,8.5,9] for z in   [6,7]  ]

    point_O=[Point(x,y,z) for x in  [6,7] for y in [11,11.5,12] for z in   [2.5,3,3.5] ]

    point_P = [Point(x,y,z) for x in [1,1.5,2] for y in [3,3.5]  for z in [1,1.5,2] ]

    point_H = [Point(x,y,z) for x in range(7,9) for y in [3,3.5] for z in range(9,11) ]
    

    def __init__(self,point_A=None,point_P=None,point_O=None,point_H=None,**kwargs):

        super().__init__()

        if point_A and point_O and point_P and point_H:
            projections=(point_A@HPP,point_O@HPP,point_O@VPP,point_P@VPP,point_P@HPP,point_A@VPP,point_H@VPP,point_H@HPP)
        else:
            projections=[]

        self._assumptions=DrawingSet(*projections)

        self._point_A=point_A
        self._point_P=point_P
        self._point_O=point_O
        self._point_H=point_H

        
        self._given_data={'A':point_A,'P':point_P,'O':point_O,'H':point_H}
        
        self._solution_step.append(self._assumptions)

    def solution(self):
        current_obj=copy.deepcopy(self)
        
        A=current_obj._point_A
        O=current_obj._point_O
        P=current_obj._point_P
        H=current_obj._point_H
        
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

        current_obj.A0=A.rotate_about(axis=line_k)('A_0')
        current_obj.B0=B.rotate_about(axis=line_k)('B_0')
        current_obj.C0=C.rotate_about(axis=line_k)('C_0')
        current_obj.D0=D.rotate_about(axis=line_k)('D_0')
        current_obj.O0=O.rotate_about(axis=line_k)('O_0')
    
#        line_kk=Line(P,S_I)('k')
        
#         current_obj.A0=point_0_dict['A']
#         current_obj.B0=point_0_dict['B']
#         current_obj.C0=point_0_dict['C']
#         current_obj.D0=point_0_dict['D']
        
        
        #plane_beta=Plane(H,H+(B-A),H-(C-A))
        plane_beta=Plane(H,H+(A-P),H-(O-P))
        E=(S@plane_beta)('E')


        line_ae=Line(S,E)('a')

        elems+=[E,plane_alpha,line_ae]

        projections+=[line_ae@HPP,line_ae@VPP,
                     E@HPP,E@VPP]
        
        
        #print(point_0_dict)
        elems+=[line_a,line_b,#,E,F,G,H,line_s1,line_s2,line_s3,line_s4
              ]

        projections+=[current_obj.A0@HPP,current_obj.A0@VPP,current_obj.B0@HPP,current_obj.B0@VPP,
                      current_obj.C0@HPP,current_obj.C0@VPP,current_obj.D0@HPP,current_obj.D0@VPP,B@HPP,B@VPP,C@HPP,C@VPP,D@HPP,D@VPP,line_a@HPP,line_a@VPP,
                      line_kk@HPP,line_kk@VPP,#line_s1@HPP,line_s1@VPP,line_s2@HPP,line_s2@VPP,line_s3@HPP,line_s3@VPP,
                     #line_s4@HPP,line_s4@VPP
                    ]
        current_set+=[*elems,*projections]

        current_obj._solution_step.append(current_set)
        current_obj._assumptions=DrawingSet(*elems,*projections)
        current_obj._point_B=B
        current_obj._point_C=C
        current_obj._point_D=D
        current_obj.point_E=E
        return current_obj

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

class TriangularPyramid(GeometricalCase):

    point_A = [Point(x,y,z) for x in [1,1.5,2,2.5] for y in [2,2.5,3,3.5,4,4.5,5] for z in [2,2.5,3,3.5]  ]

    point_B=  [Point(x,y,z) for x in range(4,6) for y in range(8,12) for z in [2,2.5,3,3.5] ]
    
    point_C = [Point(x,y,z) for x in [1,1.5,2,2.5] for y in [13,13.5,14,14.5,15] for z in [6,6.5,7] ]
    
    point_O = [Point(x,y,z) for x in range(7,10) for y in [6,6.5,7,7.5,8.5] for z in range(6,9) ]
    

    
class TriangularPyramidHFLines(GeometricalCase):
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