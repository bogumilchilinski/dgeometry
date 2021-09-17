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
from sympy import Symbol

class GeometryScene:
    plt.clf()

    plt.figure(figsize=(12,9))
    ax_2d = plt.subplot(121)
    ax_2d.set(ylabel=(r'<-x | z ->'))

    plt.xlim(0, 16)
    plt.ylim(-12, 12)

    ax_3d = plt.subplot(122, projection='3d')

    plt.xlim(0, 10)
    plt.ylim(0, 10)
    ax_3d.set_zlim(0, 10)
    plt.tight_layout()
    
    def __init__(self):

        plt.figure(figsize=(12,9))
        ax_2d = plt.subplot(121)
        ax_2d.set(ylabel=(r'<-x | z ->'))

        plt.xlim(0, 16)
        plt.ylim(-12, 12)

        ax_3d = plt.subplot(122, projection='3d')

        plt.xlim(0, 10)
        plt.ylim(0, 10)
        ax_3d.set_zlim(0, 10)
        plt.tight_layout()  

        self.__class__.ax_2d=ax_2d 
        self.__class__.ax_3d=ax_3d 



def entity_convert(entity):
    '''
    return: new result as a list 
    '''

    if isinstance(entity, geo.Point3D):
        new_result = (Point(*entity.coordinates))
    elif isinstance(entity, geo.Line3D):
        new_result = (Line(Point(*entity.p1.coordinates), Point(*entity.p2.coordinates)))
    elif isinstance(entity, geo.Plane):
        new_result = (Plane(Point(*entity.p1.coordinates), entity.normal_vector))

    return new_result


def intersection(method):
    def inner():
        pass
    


#         ax_vert = plt.subplot(221)
#         ax_vert.set(ylabel=('Frontal view'))
#         ax_vert.xaxis.tick_top()

#         plt.xlim(0, 10)
#         plt.ylim(0, 10)

#         ax_horz = plt.subplot(223)
#         ax_horz.set(ylabel=('Horizontal view'))
#         plt.xlim(0, 10)
#         plt.ylim(0, 10)
#         ax_horz.invert_yaxis()





class Entity:



    '''
    Parent class
    '''
    #     ax_vert = plt.subplot(221)
    #     ax_vert.set(ylabel=('Frontal view'))
    #     ax_vert.xaxis.tick_top()

    #     plt.xlim(0, 10)
    #     plt.ylim(0, 10)

    #     ax_horz = plt.subplot(223)
    #     ax_horz.set(ylabel=('Horizontal view'))
    #     plt.xlim(0, 10)
    #     plt.ylim(0, 10)
    #     ax_horz.invert_yaxis()

#     ax_2d = plt.subplot(121)
#     ax_2d.set(ylabel=(r'<-x | z ->'))

#     plt.xlim(0, 16)
#     plt.ylim(-12, 12)

#     ax_3d = plt.subplot(122, projection='3d')

#     plt.xlim(0, 10)
#     plt.ylim(0, 10)
#     ax_3d.set_zlim(0, 10)
#     plt.tight_layout()

    def __init__(self,
                 coding_points,
                 label=None,
                 fmt='b',
                 color=None,
                 marker=None,
                 style='-',
                 *args,
                 **kwargs):
        '''
        It allows to create new object of the Entity class.
        Input: Coordinates of code points
        '''
        self.__coding_points = coding_points
        self.__label = label
        self.__color = color
        self.__text = text
        self.__marker = marker
        self.__style = style
        self.__fmt = fmt




        
        
    def __call__(self,
                 label=None,
                 fmt='b',
                 color=None,
                 marker=None,
                 style='-',
                 text=None,
                 *args,
                 **kwargs):
        """
        The object allows to assign a variable symbol (letter)
        to the points in the plane
        """
        self.__label = label
        self.__color = color

        self.__marker = marker
        self.__style = style
        self.__fmt = fmt

        return self

    def _coding_points(self):
        return [geo.Point3D(0,0,0)]

    def __repr__(self):
        return self.__class__.__name__ +str(self._coding_points())
    
    def __str__(self):
        return self.__class__.__name__ +str(self._coding_points())    
    
    @property
    def label(self):
        return self.__label
    
    
    def _generating_points(self):
        '''
        That generates points regarding n vector
        Returns: x,y,z coordinates regarding n vector
        '''
        coding_points = self._coding_points()

        return {
            'x': [point.x.n() for point in coding_points],
            'y': [point.y.n() for point in coding_points],
            'z': [point.z.n() for point in coding_points]
        }

    def plot(
        self,
        fmt=None,
        marker=None,
        color=None,
        style='-',
        text=None,
        fontsize=20,
        scene=GeometryScene.ax_3d,
    ):
        '''
        Set the coordinates of the points with the text explanation 
        Return: Line with the text that presents the actual point on the chosen plane
        '''

        scene = GeometryScene.ax_3d   

        if fmt is None:
            fmt = self.__fmt

        if text is None:
            text = self.__label

        if marker is None:
            marker = self.__marker

        points_cooridinates = self._generating_points()

        scene.plot(points_cooridinates['x'],
                   points_cooridinates['y'],
                   points_cooridinates['z'],
                   linestyle=style,
                   color=color,
                   marker=marker)
        scene.text(*[
            sum(points_cooridinates[coord_name]) /
            len(points_cooridinates[coord_name]) for coord_name in 'xyz'
        ],
                   text,
                   fontsize=fontsize)

        return self

    def plot_hp(
        self,
        fmt=None,
        marker=None,
        color=None,
        style='-',
        text=None,
        fontsize=20,
        scene=GeometryScene.ax_2d,
    ):
        '''
        Set the coordinates of the points with the text explanation         
        Return: Line with the text that presents the actual point on the chosen plane
        '''

        scene = GeometryScene.ax_2d

        if fmt is None:
            fmt = self.__fmt

        if text is None:
            text = self.__label

        if marker is None:
            marker = self.__marker

        points_cooridinates = self._generating_points()
        points_cooridinates['x'] = -np.asarray(points_cooridinates['x'])
        scene.plot(points_cooridinates['y'],
                   points_cooridinates['x'],
                   linestyle=style,
                   color=color,
                   marker=marker)
        scene.text(*[
            sum(points_cooridinates[coord_name]) /
            len(points_cooridinates[coord_name]) for coord_name in 'yx'
        ],
                   text,
                   fontsize=fontsize)

        return self

    def plot_vp(
        self,
        fmt=None,
        marker=None,
        color=None,
        style='-',
        text=None,
        fontsize=20,
        scene=GeometryScene.ax_2d,
    ):
        '''
        Set the coordinates of the points with the text explanation 
        Return: Line with the text that presents the actual point on the chosen plane
        '''
        scene = GeometryScene.ax_2d

        if fmt is None:
            fmt = self.__fmt

        if text is None:
            text = self.__label

        if marker is None:
            marker = self.__marker

        points_cooridinates = self._generating_points()

        # plt.figure(figsize=(12,9))
        # ax_2d = plt.subplot(121)
        # ax_2d.set(ylabel=(r'<-x | z ->'))

        

        # plt.xlim(0, 16)
        # plt.ylim(-12, 12)

        # ax_3d = plt.subplot(122, projection='3d')

        # plt.xlim(0, 10)
        # plt.ylim(0, 10)
        # ax_3d.set_zlim(0, 10)
        # plt.tight_layout()

        # scene=ax_2d


        scene.plot(points_cooridinates['y'],
                   points_cooridinates['z'],
                   linestyle=style,
                   color=color,
                   marker=marker)
        scene.text(*[
            sum(points_cooridinates[coord_name]) /
            len(points_cooridinates[coord_name]) for coord_name in 'yz'
        ],
                   text,
                   fontsize=fontsize)

        return self

    def draw_projection(self,
                        projection_name='frontal',
                        scene=GeometryScene.ax_2d,
                        marker=None,
                        style='-',
                        color=None,
                        text=None,
                        fontsize=20):
        '''
        Set the coordinates of the points with the text explanation 
        Return: Line with the text that presents the actual point on the chosen plane
        '''

        if text is None:
            text = self.__label

        points_cooridinates = self._generating_points()

        scene.plot(points_cooridinates['x'],
                   points_cooridinates['y'],
                   points_cooridinates['z'],
                   linestyle=style,
                   color=color,
                   marker=marker)
        scene.text(*[
            sum(points_cooridinates[coord_name].values()) /
            len(points_cooridinates[coord_name]) for coord_name in 'xyz'
        ],
                   text,
                   fontsize=fontsize)

        return self

    def entity_convert(self, entity, *args, **kwargs):
        '''
        return: new result as a list 
        '''

        if isinstance(entity, geo.Point3D):
            new_result = (Point(*entity.coordinates))
        elif isinstance(entity, geo.Line3D):
            new_result = (Line(entity.p1, entity.p2))
        elif isinstance(entity, geo.Plane):
            new_result = (Plane(entity.p1, entity.normal_vector))

        return new_result

    def __matmul__(self, entity):
        return self.entity_convert(entity.projection(self))

#     def intersection(self, other):
#         return [self.entity_convert(entry) for entry in other.intersection(self)]
    def intersection(self, other):
        common_part = self._geo_ref.intersection(other._geo_ref)
        #print(common_part)
        return [entity_convert(elem)    for elem  in   common_part ]
        
    def projection(self, other):
        
        projection = self._geo_ref.projection(other._geo_ref)

        return entity_convert(projection)
    
    def __matmul__(self, entity):
        return entity.projection(self)
    
    def __and__(self,o):
        return o.intersection(self)


        
class Point(Entity):
    
    """
    Point class is used to create point object in Entity space and manipulate them
    """
    
    def __init__(self,*args,**kwargs):
        self._geo_ref =  geo.Point3D(*args,**kwargs)     #geometrical reference

    def _coding_points(self):
        return (self._geo_ref,)
    
    @property
    def x(self):
        return self._geo_ref.x

    @property
    def y(self):
        return self._geo_ref.y
    
    @property
    def z(self):
        return self._geo_ref.z
    
    @property
    def coordinates(self):
        return self._geo_ref.coordinates
    

    def n(self):
        return (self._geo_ref.n())
    
    def __repr__(self):
        return self.__class__.__name__ +str(self._geo_ref.coordinates)
    
    def __str__(self):
        return self.__class__.__name__ +str(self._geo_ref.coordinates)
        

    def distance(self,other):
        return self._geo_ref.distance(other._geo_ref)
    
    def __xor__(self,other):
        if isinstance(other,Point):
            return (Line(self,other))
        elif isinstance(other,Line):
            return (Plane(self,other.p1,other.p2))

    def __add__(self,other):
        
        result=self._geo_ref+(other.coordinates)
        return entity_convert(result)
    
    def __mul__(self,factor):
        
        result=self._geo_ref.__mul__(factor)
        return entity_convert(result)
    
    def __rmul__(self,factor):
        
        result=self._geo_ref.__rmul__(factor)
        return entity_convert(result)    

    def __truediv__(self,divisor):
        
        result=self._geo_ref.__truediv__(divisor)
        return entity_convert(result)       
    
    
    def __sub__(self,other):
        
        result=self._geo_ref-(other.coordinates)
        return entity_convert(result)
        
class Line(Entity):
    
    """
    Line calass is used to create line objects and manipulate them
    """

    def __init__(self, p1, p2, **kwargs):
        self._geo_ref = geo.Line3D(p1=p1._geo_ref,pt=p2._geo_ref,**kwargs)

#     def __repr__(self):
#         return self.__class__.__name__
    
#     def __str__(self):
#         return self.__class__.__name__
        
    def _coding_points(self):
        return (self._geo_ref.p1,self._geo_ref.p2)

    def __repr__(self):
        return self.__class__.__name__ +str(self._coding_points())
    
    def __str__(self):
        return self.__class__.__name__ +str(self._coding_points())
    
    def __xor__(self,other):
        if isinstance(other,geo.Point3D):
            return (Plane(self.p1,self.p2,other))
        elif isinstance(other,geo.Line3D):
            return (Plane(self.p1,self.p2,other.p1))
        
    def perpendicular_line(self, p):
        return entity_convert(self._geo_ref.perpendicular_line(p._geo_ref))

    @property
    def direction(self):
        return entity_convert(self._geo_ref.direction)
    
#     def intersection(self, other):
#         common_part_line = self._geo_ref.intersection(other._geo_ref)
        
#         return [ entity_convert(elem)    for elem  in   common_part_line ]    
        
#     def projection(self, other):
#         line_projection = self._geo_ref.projection(other.geo_ref)
        
#         return [ entity_conver(elem) for elem in line_projection ]
        

class Plane(Entity):
    
    """
    Plane class is used to create plane object and manipulate them
    """
    
    
    def __init__(self,p1, a=None, b=None, **kwargs):

        self._geo_ref = geo.Plane(p1=p1._geo_ref, a=a._geo_ref, b=b._geo_ref, **kwargs)
        self._p2=a
        self._p3=b
        
#         if a == normal_vector:
#             self._geo_ref = geo.Plane(p1=p1._geo_ref, a = normal_vector._geo_ref, b = None, **kwargs)
#             b = Point(-20,-20,solve(Eq(self.equation(-20,-20),0))[0])
        
#         elif a == self._p2 and b == self._p3 :
#             self._geo_ref = geo.Plane(p1=p1._geo_ref, a=a._geo_ref, b=b._geo_ref, **kwargs)
            

        
    def _coding_points(self):
        return (self._geo_ref.p1,self._p2,self._p3,self._geo_ref.p1)

    
    def projection(self, other):
        if isinstance(other,Point):
            projection = self._geo_ref.projection(other._geo_ref)
            
        elif isinstance(other,Line):
            projection = self._geo_ref.projection_line(other._geo_ref)            
            
        #print(projection)
        return entity_convert(projection)
    
    def perpendicular_line(self, p):
        return entity_convert(self._geo_ref.perpendicular_line(p._geo_ref))
    
    def perpendicular_plane(self, p):
        return entity_convert(self._geo_ref.perpendicular_plane(p._geo_ref))



class DrawingSet(Entity,list):
    def __init__(self,*entities,scene=None):
        super(list,self).__init__()
        super(Entity,self).__init__()

        self += list(entities)

    def plot(
        self,
        fmt=None,
        marker=None,
        color=None,
        style='-',
        text=None,
        fontsize=20,
        scene=GeometryScene.ax_3d,
        ):

        for elem in self:
            elem.plot(fmt=fmt,marker=marker,color=color,style=style,text=text,fontsize=fontsize,scene=scene)

        return scene

    def plot_hp(
        self,
        fmt=None,
        marker=None,
        color=None,
        style='-',
        text=None,
        fontsize=20,
        scene=GeometryScene.ax_2d,
        ):

        for elem in self:
            elem.plot_hp(fmt=fmt,marker=marker,color=color,style=style,text=text,fontsize=fontsize,scene=scene)

        return scene

    def plot_vp(
        self,
        fmt=None,
        marker=None,
        color=None,
        style='-',
        text=None,
        fontsize=20,
        scene=GeometryScene.ax_2d,
        ):

        for elem in self:
            elem.plot_vp(fmt=fmt,marker=marker,color=color,style=style,text=text,fontsize=fontsize,scene=scene)

        return scene






class GeometricalCase(DrawingSet):

    scheme_name = 'abs.png'
    real_name = 'abs.png'

    @classmethod
    def _scheme(cls):

        path = __file__.replace('dgeometry.py', 'images/') + cls.scheme_name
        #path = './images/' + cls.scheme_name

        return path

    @classmethod
    def _real_example(cls):

        path = __file__.replace('dgeometry.py', 'images/') + cls.real_name
        #path = './images/' + cls.real_name


        return path




    @classmethod
    def preview(cls, example=False):
        if example:
            path = cls._real_example()

        else:
            path = cls._scheme()

        with open(f"{path}", "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        image_file.close()

        return IP.display.Image(base64.b64decode(encoded_string))


    @classmethod
    def from_random_data(cls):
        new_obj = cls()
        data_set=new_obj.get_random_parameters()
        
        entities = [point(str(label))  for label,point in data_set.items()]
        print(entities)
        return cls(*entities)

    def __init__(self,*assumptions,**kwargs):
        self._assumptions=DrawingSet(*assumptions)
        self._given_data=None

    def plot(
        self,
        fmt=None,
        marker=None,
        color=None,
        style='-',
        text=None,
        fontsize=20,
        scene=GeometryScene.ax_3d,
        ):

        print(type(self._assumptions))
        print(self._assumptions)

        self._assumptions.plot(fmt=fmt,marker=marker,color=color,style=style,text=text,fontsize=fontsize,scene=scene)

        return copy.deepcopy(self)

    def plot_hp(
        self,
        fmt=None,
        marker=None,
        color=None,
        style='-',
        text=None,
        fontsize=20,
        scene=GeometryScene.ax_2d,
        ):

        self._assumptions.plot_hp(fmt=fmt,marker=marker,color=color,style=style,text=text,fontsize=fontsize,scene=scene)

        

        return copy.deepcopy(self)

    def plot_vp(
        self,
        fmt=None,
        marker=None,
        color=None,
        style='-',
        text=None,
        fontsize=20,
        scene=GeometryScene.ax_3d,
        ):

        self._assumptions.plot_vp(fmt=fmt,marker=marker,color=color,style=style,text=text,fontsize=fontsize,scene=scene)

        return copy.deepcopy(self)

    def solution(self):

        A = self._assumptions[0]
        CA = self._assumptions[1]
        OA = self._assumptions[2]
 

        xshift,yshift,zshift = 0,0,0
        #print(counter)

        A=Point(A.x,A.y,A.z)('A',marker='o').plot('ko').plot_hp('go').plot_vp('go')
        O=(A+OA)('O',marker='o').plot('ko').plot_hp('go').plot_vp('go')
        C=(A+CA)('C',marker='o').plot('ko').plot_hp('go').plot_vp('go') 
        #D=(A+Point(4,3,4))('D',marker='o').plot('ko').plot_hp('go').plot_vp('go')
        G=(A+Point(-4,3,-1))('D',marker='o')#.plot('ko').plot_hp('go').plot_vp('go')

        HPP_A = Plane(A,A+Point(0,1,0),A+Point(1,0,0)  )
        VPP_A = Plane(A,A+Point(0,1,0),A+Point(0,0,1)  )

        

        # A=Point(0,0,0)('A')
        # B=Point(A.x+2,A.y+1,A.z+3)('B')
        # C=Point(4,3,5)('C')
        E=Point(4,4,5)('E')
        F=Point(3,3,5)('F')


        #B._geo_ref
        a=Line(A,O)('a')
        b=Line(O,C)('b')

        P1=(A @ b)('1',marker='o').plot('ko').plot_hp('go').plot_vp('go') 
        
        
        
        alpha=Plane(A,O,C)

        #alpha.intersection(Plane(E,F,A))[0]

        e=Line(E,F)
        e.projection(Line(A,O))

        alpha.projection(e)

        c = alpha.perpendicular_line(A)
        # c('nn',marker='o').plot().plot_hp().plot_vp()

        # (alpha & HPP_A)[0]('go',marker='o').plot().plot().plot_hp().plot_vp()
        # (alpha & VPP_A)[0]('go',marker='o').plot().plot().plot_hp().plot_vp()

        #(e @ VPP)('A',marker='o').plot().plot_hp().plot_vp()
        # Plane(A._geo_ref,B._geo_ref,C._geo_ref).projection_line(Line(E._geo_ref,F._geo_ref))
        # Line(E._geo_ref,F._geo_ref).projection(Line(A._geo_ref,B._geo_ref))
        #dg2.entity_convert(alpha.intersection(dg2.Line(A,B))[0])

        # Line(A,B)('a',marker='o').plot().plot_hp().plot_vp()


        # B1=Point(A.x,(A.y+(B@HPP).distance(A@HPP)),B.z,evaluate=True)('B1',marker='o').plot().plot_hp().plot_vp()
        # B1.n()
        # B1.distance(A).n(),B.distance(A)

        # (B1.x.n(),B1.y.n(),B1.z.n())


        # Line(D,C-A+D  )('e').plot().plot_hp().plot_vp()
        # Line(D,B-A+D  )('f').plot().plot_hp().plot_vp()
        M = (O @ (Line(A,C)))('M',marker='o').plot().plot_hp().plot_vp()
        
        Q=G @ alpha
        Q('Q',marker='o')#.plot_hp().plot_vp()

        S=(A+(C-A)*0.5)
        
        B=(S+((M^O).direction()/M.distance(O))*(A.distance(S)).n())('B',marker='o').plot().plot_hp().plot_vp()
        D=(S+((M^O).direction()/M.distance(O))*(-A.distance(S)).n())('D',marker='o').plot().plot_hp().plot_vp()
        #C=(M+((M^O).direction()/M.distance(O))*(A.distance(M))*(-sqrt(3)/3).n())
        
    #     H=(A+((P^D).direction()/D.distance(P))*(A.distance(F))*(-1))
    #     H('H',marker='o').plot().plot_hp().plot_vp()
        
        W=(C+((Q^G).direction()/G.distance(Q))*(A.distance(B))*(-1))
        W('W',marker='o').plot().plot_hp().plot_vp()
        
        (W @ alpha)('W_test',marker='o').plot().plot_hp().plot_vp()
        
        A, c@alpha

        Line(A,B)(marker='o').plot().plot_hp().plot_vp()
        Line(A,D)(marker='o').plot().plot_hp().plot_vp()
        Line(B,C)(marker='o').plot().plot_hp().plot_vp()
        Line(C,D)(marker='o').plot().plot_hp().plot_vp()
        
        
        Line(A,W)(marker='o').plot().plot_hp().plot_vp()
        Line(B,W)(marker='o').plot().plot_hp().plot_vp()
        Line(C,W)(marker='o').plot().plot_hp().plot_vp()

        new_obj = copy.deepcopy(self)

        new_obj._solution_dict=({'Ax':A.x,'Ay':A.y,'Az':A.z,'Bx':B.x.n(4),'By':B.y.n(4),
                            'Bz':B.z.n(4),'Cx':C.x,'Cy':C.y,'Cz':C.z,'Dx':D.x.n(4),'Dy':D.y.n(4),
                            'Dz':D.z.n(4),'Wx':W.x.n(4),'Wy':W.y.n(4),'Wz':W.z.n(4),
                            'Ox':O.x,'Oy':O.y,'Oz':O.z})

        new_obj._all_points = DrawingSet(A,B,C,D,W)

        return new_obj

    def get_default_data(self):

        

        default_data_dict = {
            Symbol('A'): [Point(4,5,8),Point(4,6,8),Point(5,10,8),Point(6,10,8),Point(7,10,8),Point(8,10,8),Point(-1,10,8),Point(3,10,8)],
            Symbol('C'): [Point(2,-4,-1),Point(1,-4,-2),Point(2,-5,-1),],
            Symbol('O'): [Point(1,-5,2),Point(0,-5,1),],
        }
        return default_data_dict

    def get_random_parameters(self):



        default_data_dict = self.get_default_data()

        parameters_dict = {
            key: random.choice(items_list)
            for key, items_list in default_data_dict.items()
            }
          
        return parameters_dict
    
    def subs(self,*args,**kwargs):
        if len(args)>0:
            data_set=args[0]
            entities = [point(str(label))  for label,point in data_set.items()]

            new_obj=self.__class__(*entities)
            new_obj._given_data=args[0]

        else:
            new_obj = copy.deepcopy(self)
        return new_obj
        
        