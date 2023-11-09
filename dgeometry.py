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

from pylatex import Document, Section, Subsection, Subsubsection, Itemize, Package, HorizontalSpace, Description, Marker, Ref, Marker, Figure
from pylatex.section import Paragraph, Chapter
from pylatex.utils import italic, NoEscape

#from dynpy.utilities.report import ReportText

import itertools as it

linewidth = 1.5

default_colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

def plots_no():
    num = 0
    while True:
        yield num
        num += 1

def get_color():
    colours_no = len(default_colors)
    
    num = 0
    while True:
        yield default_colors[num % colours_no]
        num += 1

color_source = get_color() 


class GeometrySceneDG:


    ax_2d = None
    ax_3d = None

    #def __init__(self,height=12,width=9,figsize=(12,9)):
    def __init__(self, init_3d=(30, 10), height=12, width=16, figsize=(12, 9)):
        
        
        
        plt.figure(figsize=figsize)
        ax_2d = plt.subplot(121)
        ax_2d.set(ylabel=(r'<-x | z ->'), xlabel='y')

        plt.xlim(0, width)
        plt.ylim(-height, height)
        plt.grid(True)

        ax_2d.set_yticks(range(-12, 12, 1))
        ax_2d.set_yticklabels(
            list(map(lambda tick: str(abs(tick)), range(-12, 12, 1))))

        ax_2d.set_xticks(range(0, 16, 1))
        ax_2d.set_xticklabels(
            list(map(lambda tick: str(abs(tick)), range(0, 16, 1))))

        ax_3d = plt.subplot(122, projection='3d')
        ax_3d.set(xlabel='x', ylabel='y', zlabel='z')

        plt.xlim(0, 16)
        plt.ylim(0, 16)

        ax_3d.set_zlim(0, 16)

        ax_3d.view_init(*init_3d)
        plt.tight_layout()

        self.__class__.ax_2d = ax_2d
        self.__class__.ax_3d = ax_3d
        self.__class__.size_3d=16

class GeometryScene:
    #     plt.clf()

    # #     plt.figure(figsize=(12,9))
    # #     ax_2d = plt.subplot(121)
    # #     ax_2d.set(ylabel=(r'<-x | z ->'),xlabel='y')

    # #     plt.xlim(0, 16)
    # #     plt.ylim(-12, 12)
    # #     plt.grid(True)
    # #
    # #     ax_2d.set_yticks(  range(-12,12,2) )
    # #     ax_2d.set_yticklabels(  list(map(lambda tick: str(abs(tick)),range(-12,12,2)))  )

    # #     ax_3d = plt.subplot(122, projection='3d')
    # #     ax_3d.view_init(30,10)
    # #     ax_3d.set(xlabel='x',ylabel='y',zlabel='z')

    # #     plt.xlim(0, 16)
    # #     plt.ylim(0, 16)

    # #
    # #     ax_3d.set_zlim(0, 16)
    # #     plt.tight_layout()

    #     plt.figure(figsize=(12,12))
    #     ax_2d = plt.subplot(121)
    #     #ax_2d.set(ylabel=(r'<-x | z ->'),xlabel='y')

    #     plt.xlim(0, 200)
    #     plt.ylim(-100, 100)
    #     plt.grid(False)

    #     ax_2d.axis('off')

    #     #ax_2d.set_yticks(  range(-12,12,2) )
    #     #ax_2d.set_yticklabels(  list(map(lambda tick: str(abs(tick)),range(-12,12,2)))  )

    #     ax_3d = plt.subplot(122, projection='3d')
    #     #ax_3d.set(xlabel='x',ylabel='y',zlabel='z')

    #     #plt.xlim(0, 16)
    #     #plt.ylim(0, 16)

    #     #ax_3d.set_zlim(0, 16)

    #     ax_3d.view_init(30,80)
    #     plt.tight_layout()
    #     plt.axis("off")

    ax_2d = None
    ax_3d = None

    #    def __init__(self,height=12,width=16,figsize=(12,9)):

    #         plt.figure(figsize=figsize)
    #         ax_2d = plt.subplot(121)
    #         ax_2d.set(ylabel=(r'<-x | z ->'),xlabel='y')

    #         plt.xlim(0, width)
    #         plt.ylim(-height, height)
    #         plt.grid(True)

    #         ax_2d.set_yticks(  range(-12,12,2) )
    #         ax_2d.set_yticklabels(  list(map(lambda tick: str(abs(tick)),range(-12,12,2)))  )

    #         ax_3d = plt.subplot(122, projection='3d')
    #         ax_3d.set(xlabel='x',ylabel='y',zlabel='z')

    #         plt.xlim(0, 16)
    #         plt.ylim(0, 16)

    #         ax_3d.set_zlim(0, 16)

    #         ax_3d.view_init(30,10)
    #         plt.tight_layout()

    #         self.__class__.ax_2d=ax_2d
    #         self.__class__.ax_3d=ax_3d

    def __init__(self, height=12, width=12, figsize=(12, 9)):

        plt.figure(figsize=figsize)
        ax_2d = plt.subplot(121)
        #ax_2d.set(ylabel=(r'<-x | z ->'),xlabel='y')

        plt.xlim(-0.1 * width, width)
        plt.ylim(-height, height)
        plt.grid(False)

        plt.axis('off')
        
        #ax_2d.set_yticks(  range(-12,12,2) )
        #ax_2d.set_yticklabels(  list(map(lambda tick: str(abs(tick)),range(-12,12,2)))  )

        ax_3d = plt.subplot(122, projection='3d')
        #ax_3d.set(xlabel='x',ylabel='y',zlabel='z')

        #plt.xlim(0, 16)
        #plt.ylim(0, 16)

        #ax_3d.set_zlim(0, 16)

        ax_3d.view_init(30, 80)
        plt.tight_layout()
        plt.axis("off")

        self.__class__.ax_2d = ax_2d
        self.__class__.ax_3d = ax_3d


def entity_convert(entity):
    '''
    return: new result as a list 
    '''

    if isinstance(entity, geo.Point3D):
        new_result = (Point(*entity.coordinates))
    elif isinstance(entity, geo.Line3D):
        new_result = (Line(Point(*entity.p1.coordinates),
                           Point(*entity.p2.coordinates)))
    elif isinstance(entity, geo.Plane):
        new_result = (Plane(Point(*entity.p1.coordinates),
                            entity.normal_vector))

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
    display = 'Name'
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

    _at_symbol = '@'

    __color = None
    __text = None
    __marker = None
    __style = None
    __fmt = None
    _linewidth = 1.5

    _share_color = True

    def __init__(self,
                 coding_points=None,
                 display=None,
                 label=None,
                 fmt='b',
                 color=None,
                 marker='o',
                 style='-',
                 linewidth = None,
                 projection=False,
                 *args,
                 **kwargs):
        '''
        It allows to create new object of the Entity class.
        Input: Coordinates of code points
        '''
        self.__coding_points = coding_points
        self._label = label
        self.__color = color
        self._linewidth = linewidth
        self.__text = None
        self.__marker = marker
        self.__style = style
        self.__fmt = None
        self._projection = projection
        self._caption = None
        self.display = display

    def __call__(self,
                 label=None,
                 fmt=None,
                 color=None,
                 marker=None,
                 style=None,
                 linewidth = None,
                 text=None,
                 caption=None,
                 *args,
                 **kwargs):
        """
        The object allows to assign a variable symbol (letter)
        to the points in the plane
        """
        obj = copy.deepcopy(self)
#         if label is not None:
#             if obj.display is None:
#                 obj._label = label
        if label is not None:
            obj._label = label

        if label is not None:
            obj._linewidth = linewidth

        if color is not None:
            obj.__color = color

        if marker is not None:
            obj.__marker = marker

        if style is not None:
            obj.__style = style
        obj.__fmt = fmt

        obj._caption = caption

        return obj

#     def _coding_points(self):
#         return [geo.Point3D(0,0,0)]

    def __repr__(self):

        if self._label is None:
            self._label = self.__class__.__name__ 

        return self._label

    def __str__(self):

        if self._label is None:
            self._label = self.__class__.__name__

        return self._label

    @property
    def label(self):
        return self.getLabel()

    def getLabel(self):
        return self._label

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

    def _entity_limits(self):

        coords_dict = self._generating_points()

        limits_dict = {
            name: [min(container), max(container)]
            for name, container in coords_dict.items()
        }

        return limits_dict

    def plot(
        self,
        fmt=None,
        marker=None,
        color=None,
        style='-',
        text=None,
        fontsize=13,
        linewidth=None,
        scene=GeometrySceneDG.ax_3d,
    ):
        '''
        Set the coordinates of the points with the text explanation 
        Return: Line with the text that presents the actual point on the chosen plane
        '''

        scene = GeometrySceneDG.ax_3d

        if fmt is None:
            fmt = self.__fmt

        if text is None:
            text = self.getLabel()

        if marker is None:
            marker = self.__marker

        if color is None:
            color = self.color
            
        if linewidth is None:
            linewidth = self.linewidth
            

        points_cooridinates = self._generating_points()

        scene.plot(points_cooridinates['x'],
                   points_cooridinates['y'],
                   points_cooridinates['z'],
                   linestyle=style,
                   color=color,
                   linewidth=linewidth,
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
        fontsize=13,
        linewidth=None,
        scene=GeometrySceneDG.ax_2d,
    ):
        '''
        Set the coordinates of the points with the text explanation
        Return: Line with the text that presents the actual point on the chosen plane
        '''

        scene = GeometrySceneDG.ax_2d

        if fmt is None:
            fmt = self.__fmt

        if text is None:
            text = self.getLabel()

        if marker is None:
            marker = self.__marker

        if color is None:
            color = self.color
            
        if linewidth is None:
            linewidth = self.linewidth

        if str(self)[-1] == "\'" and str(self)[-2] != "\'":
            points_cooridinates = self._generating_points()
            points_cooridinates['x'] = -np.asarray(points_cooridinates['x'])
            scene.plot(points_cooridinates['y'],
                       points_cooridinates['x'],
                       linestyle=style,
                       color=color,
                       linewidth=linewidth,
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
        fontsize=13,
        linewidth=None,
        scene=GeometrySceneDG.ax_2d,
    ):
        '''
        Set the coordinates of the points with the text explanation 
        Return: Line with the text that presents the actual point on the chosen plane
        '''
        scene = GeometrySceneDG.ax_2d

        if fmt is None:
            fmt = self.__fmt

        if text is None:
            text = self.getLabel()

        if marker is None:
            marker = self.__marker

        if color is None:
            color = self.color
            
        if linewidth is None:
            linewidth = self.linewidth

        points_cooridinates = self._generating_points()



        if str(self)[-1] == "\'" and str(self)[-2] == "\'":
            scene.plot(points_cooridinates['y'],
                       points_cooridinates['z'],
                       linestyle=style,
                       color=color,
                       linewidth=linewidth,
                       marker=marker)
            scene.text(*[
                sum(points_cooridinates[coord_name]) /
                len(points_cooridinates[coord_name]) for coord_name in 'yz'
            ],
                       text,
                       fontsize=fontsize)

        return self

    def plot_all(
        self,
        fmt=None,
        marker=None,
        color=None,
        style='-',
        text=None,
        fontsize=13,
        linewidth=None,
        scene=GeometrySceneDG.ax_3d,
    ):
        '''
        Set the coordinates of the points with the text explanation 
        Return: Line with the text that presents the actual point on the chosen plane
        '''

        self.plot(
            fmt=fmt,
            marker=marker,
            color=color,
            style=style,
            text=text,
            fontsize=fontsize,
            linewidth=linewidth,
            scene=scene)

        self.plot_hp(
            fmt=fmt,
            marker=marker,
            color=color,
            style=style,
            text=text,
            fontsize=fontsize,
            linewidth=linewidth,
            scene=scene)
        
        
        self.plot_vp(
            fmt=fmt,
            marker=marker,
            color=color,
            style=style,
            text=text,
            fontsize=fontsize,
            linewidth=linewidth,
            scene=scene)
        
        
        return self

    def draw_projection(self,
                        projection_name='frontal',
                        scene=GeometrySceneDG.ax_2d,
                        marker=None,
                        style='-',
                        color=None,
                        text=None,
                        fontsize=13):
        '''
        Set the coordinates of the points with the text explanation 
        Return: Line with the text that presents the actual point on the chosen plane
        '''

        if text is None:
            text = self._label

        points_cooridinates = self._generating_points()

        if color is None:
            color = self.color
        
        scene.plot(points_cooridinates['x'],
                   points_cooridinates['y'],
                   points_cooridinates['z'],
                   linestyle=style,
                   color=color,
                   linewidth=linewidth,
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


#     def intersection(self, other):
#         return [self.entity_convert(entry) for entry in other.intersection(self)]

    def intersection(self, other):
        common_part = self._geo_ref.intersection(other._geo_ref)
        #print(common_part)
        return [entity_convert(elem) for elem in common_part]

    def projection(self, other):

        projection = self._geo_ref.projection(other._geo_ref)

        new_entity = entity_convert(projection)

        at = other.__class__._at_symbol

        new_entity._label = f'{self._label}{at}{other._label}'

        new_entity._projection = other

        return new_entity

    def __matmul__(self, entity):
        new_obj = entity.projection(self)
        at = entity.__class__._at_symbol

        new_obj._label = f'{self._label}{at}{entity._label}'

        if self._share_color is True:
            new_obj.color = self.color
        
        return new_obj

    def __and__(self, o):
        return o.intersection(self)

    @property
    def color(self):
        if self.__color is not None:
            return self.__color
        else:
            self.__color = next(color_source)
            return self.__color

    @color.setter
    def color(self,color):
        self.__color=color


    @property
    def linewidth(self):
        if self._linewidth is not None:
            return self._linewidth
        else:
            return self.__class__._linewidth
            #return type(self)._linewidth

    @linewidth.setter
    def linewidth(self,linewidth):
        self._linewidth=linewidth
        
        
    def _gp(self):
        result = [self @ HPP,self @ VPP]
        
        return DrawingSet(*result)
     
        

    def get_projections(self):
        return self._gp()
    
    def _wp(self):

        result = self._gp()
        
        return DrawingSet(self,*result)
    
    def with_projections(self):
        return self._wp()



class Point(Entity):
    """
    Point class is used to create point object in Entity space and manipulate them
    """



    def __init__(self, *args, **kwargs):
        super().__init__()
        self._geo_ref = geo.Point3D(*args, **kwargs)  #geometrical reference

    def _coding_points(self):
        return (self._geo_ref, )

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

    def getCords(self):
        return str(self.x) + ',' + str(self.y) + ',' + str(self.z)

    def getLabel(self):
        if Entity.display == 'Name':
            return self._label
        if Entity.display == 'Cords':
            return self._label + '(' + self.getCords() + ')'


#     def __repr__(self):
#         return f'{self.__class__.__name__}{(self._geo_ref.coordinates)}({self._label})'

#     def __str__(self):
#         return f'{self.__class__.__name__}{(self._geo_ref.coordinates)}({self._label})'

    def distance(self, other):
        return self._geo_ref.distance(other._geo_ref)

    def __xor__(self, other):
        if isinstance(other, Point):
            return (Line(self, other))
        elif isinstance(other, Line):
            return (Plane(self, other.p1, other.p2))

    def __add__(self, other):

        result = self._geo_ref + (other.coordinates)
        return entity_convert(result)

    def __mul__(self, factor):

        result = self._geo_ref.__mul__(factor)
        return entity_convert(result)

    def __rmul__(self, factor):

        result = self._geo_ref.__rmul__(factor)
        return entity_convert(result)

    def __truediv__(self, divisor):

        result = self._geo_ref.__truediv__(divisor)
        return entity_convert(result)

    def __sub__(self, other):

        result = self._geo_ref - (other.coordinates)
        return entity_convert(result)

    def rotate_about(self, axis=None, plane=None):
        point = copy.deepcopy(self)

        if axis is None:
            axis = Line(point + Point(0, 1, 0), (point + Point(0, 1, 10)))
            print(axis)

        if plane is None:
            plane = HorizontalPlane(axis.p1)

        point_rot_center = (point @ axis)(f'S_{point._label}')

        radius = point.distance(point_rot_center)

        if radius == 0:
            rotated_point = copy.deepcopy(point)(f'{point._label}_0')
        else:

            # zaimplementować w metode dla punktu
            
            norm_vec=Point(*(Plane(axis.p1,point,axis.p2)._geo_ref.normal_vector))
            print('rot coords',norm_vec.coordinates)
            
            lever_pnt = point+norm_vec
            
            rotation_dir = ((lever_pnt) @ plane) - point_rot_center

            #display(dir_I_on_HPP.coordinates)
            #display((point_I @ plane_beta).distance( S_I ))
            #display(point_I.distance( S_I ))
            
            

            ratio = radius / ((lever_pnt @ plane).distance(point_rot_center))

            rotated_point = (point_rot_center +
                             (rotation_dir) * ratio)(f'{point._label}_0')

        rotated_point._axis = axis
        rotated_point._plane = plane

        return rotated_point


class Line(Entity):
    """
    Line calass is used to create line objects and manipulate them
    """

    _default_extension = 0.2
    
    def __init__(self, p1, p2, **kwargs):
        self._p1 = p1
        self._p2 = p2
        super().__init__(marker=None)
        self._geo_ref = geo.Line3D(p1=p1._geo_ref, pt=p2._geo_ref, **kwargs)

#     def __repr__(self):
#         return self.__class__.__name__

#     def __str__(self):
#         return self.__class__.__name__

    @property
    def extension(self):
        return self._default_extension

    def _coding_points(self):
        
        delta =  self._p2-self._p1
        
        return (self._p1+(-self.extension * delta), self._p2+self.extension * delta)

#     def __repr__(self):
#         return self.__class__.__name__ +str(self._coding_points())

#     def __str__(self):
#         return self.__class__.__name__ +str(self._coding_points())

    def __xor__(self, other):
        if isinstance(other, geo.Point3D):
            return (Plane(self.p1, self.p2, other))
        elif isinstance(other, geo.Line3D):
            return (Plane(self.p1, self.p2, other.p1))

    def perpendicular_line(self, p):
        return entity_convert(self._geo_ref.perpendicular_line(p._geo_ref))

    def parallel_line(self, p):
        return entity_convert(self._geo_ref.parallel_line(p._geo_ref))

    @property
    def direction(self):
        return entity_convert(self._geo_ref.direction)

    @property
    def p1(self):
        return self._p1

    @property
    def p2(self):
        return self._p2


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

    _linewidth = 0.5
    
    def __init__(self, p1, a=None, b=None, **kwargs):
        super().__init__(marker=None)

        if a is not None:
            _a_geo_ref = a._geo_ref
        else:
            _a_geo_ref = a

        if b is not None:
            _b_geo_ref = b._geo_ref
        else:
            _b_geo_ref = b

        self._geo_ref = geo.Plane(p1=p1._geo_ref,
                                  a=_a_geo_ref,
                                  b=_b_geo_ref,
                                  **kwargs)

        self._p1 = p1

        if a is None:
            _a_geo_ref = self._geo_ref.arbitrary_point('u', 'v').subs({
                'u': 1,
                'v': 0
            })
            self._p2 = entity_convert(_a_geo_ref)
        else:
            self._p2 = a

        if b is None:
            _b_geo_ref = self._geo_ref.arbitrary_point('u', 'v').subs({
                'u': 0,
                'v': 1
            })
            self._p3 = entity_convert(_b_geo_ref)
        else:
            self._p3 = b


#         if a == normal_vector:
#             self._geo_ref = geo.Plane(p1=p1._geo_ref, a = normal_vector._geo_ref, b = None, **kwargs)
#             b = Point(-20,-20,solve(Eq(self.equation(-20,-20),0))[0])

#         elif a == self._p2 and b == self._p3 :
#             self._geo_ref = geo.Plane(p1=p1._geo_ref, a=a._geo_ref, b=b._geo_ref, **kwargs)

    def _vertices(self):
        return self._p1, self._p2, self._p3,

    def _coding_points(self):
        #return (self._p1, self._p2,self._p2 + (self._p3 - self._p1)  , self._p3,   self._geo_ref.p1)
        return (*self._vertices(),self._p1)

    def projection(self, other):
        if isinstance(other, Point):
            projection = self._geo_ref.projection(other._geo_ref)
            new_obj = entity_convert(projection)

        elif isinstance(other, Line):
            projection = self._geo_ref.projection_line(other._geo_ref)
            new_obj = entity_convert(projection)

        elif isinstance(other, Plane):
            projected_pts=[(pts @ self)  for pts in other._vertices()]
            
            if geo.Point.is_collinear(*[pts._geo_ref for pts in projected_pts]):
                
                new_obj = Line(*projected_pts[0:2])
                #new_obj = Plane(*projected_pts)
            else:
                new_obj = Plane(*projected_pts)
            #new_obj = Plane(*projected_pts)
        

        at = self.__class__._at_symbol

        new_obj._label = f'{self._label}{at}{other._label}'

        return new_obj

    def perpendicular_line(self, p):
        return entity_convert(self._geo_ref.perpendicular_line(p._geo_ref))

    def perpendicular_plane(self, p):
        return entity_convert(self._geo_ref.perpendicular_plane(p._geo_ref))

    def parallel_plane(self, p):

        return entity_convert(self._geo_ref.parallel_plane(p._geo_ref))

    
    def get_associated_point(self,point,projection=None):
        
        if projection is None:
            proj = VPP

        aux_p = (Line(point @ proj ,point)  & self)[0]
            
        return aux_p
    
    def get_associated_line(self,line,projection=None):
        
        if projection is None:
            proj = VPP

        aux_p1 = self.get_associated_point(line.p1,projection)
        aux_p2 = self.get_associated_point(line.p2,projection)
            
        return Line(aux_p1,aux_p2)
    
    def get_horizontal_line(self,p=None):
        
        
        if p is not None: 
            p1=p
            new_vertices_list=[*self._vertices(),]
            new_vertices_list.remove(p1)
            new_vertices_tuple=tuple(new_vertices_list)
            p2,p3=new_vertices_tuple
        else:
            p1,p2,p3=self._vertices()
            
        other_points = (Line(p2,p3) & HorizontalPlane(p1))
        
        if len(other_points) == 0:
            return Line(p2,p3)
        else:
            
            result = Line(p1,other_points[0])
            result._label = f'$h_{{{self._label.replace("$","")}}}$'
            return result



    def get_frontal_line(self,p=None):

        if p is not None: 
            p1=p
            new_vertices_list=[*self._vertices(),]
            new_vertices_list.remove(p1)
            new_vertices_tuple=tuple(new_vertices_list)
            p2,p3=new_vertices_tuple
        else:
            p1,p2,p3=self._vertices()
            
        other_points = (Line(p2,p3) & FrontalPlane(p1))
        
        if len(other_points) == 0:
            return Line(p2,p3)
        else:
            
            result = Line(p1,other_points[0])
            result._label = f'$h_{{{self._label.replace("$","")}}}$'
            return result


class Tetragon(Plane):
    _label = 'Tetragon'

    def __init__(self, p1, a=None, b=None, c=None, **kwargs):
        #         super().__init__()

        if a is not None:
            _a_geo_ref = a._geo_ref
        else:
            _a_geo_ref = a

        if b is not None:
            _b_geo_ref = b._geo_ref
        else:
            _b_geo_ref = b

        if c is not None:
            _c_geo_ref = c._geo_ref
        else:
            _c_geo_ref = c

        self._geo_ref = geo.Plane(p1=p1._geo_ref,
                                  a=_a_geo_ref,
                                  b=_b_geo_ref,
                                  **kwargs)

        self._p1 = p1

        if a is None:
            _a_geo_ref = self._geo_ref.arbitrary_point('u', 'v').subs({
                'u': 1,
                'v': 0
            })
            self._p2 = entity_convert(_a_geo_ref)
        else:
            self._p2 = a

        if b is None:
            _b_geo_ref = self._geo_ref.arbitrary_point('u', 'v').subs({
                'u': 0,
                'v': 1
            })
            self._p3 = entity_convert(_b_geo_ref)
        else:
            self._p3 = b
        if c is None:
            _c_geo_ref = self._geo_ref.arbitrary_point('u', 'v').subs({
                'u': 0,
                'v': 1
            })
            self._p4 = entity_convert(_c_geo_ref)
        else:
            self._p4 = c


#         if a == normal_vector:
#             self._geo_ref = geo.Plane(p1=p1._geo_ref, a = normal_vector._geo_ref, b = None, **kwargs)
#             b = Point(-20,-20,solve(Eq(self.equation(-20,-20),0))[0])

#         elif a == self._p2 and b == self._p3 :
#             self._geo_ref = geo.Plane(p1=p1._geo_ref, a=a._geo_ref, b=b._geo_ref, **kwargs)

    def _vertices(self):
        return self._p1, self._p2, self._p3, self._p4


class HorizontalPlane(Plane):
    _at_symbol =  ''

    def __init__(self, p1=None):

        if p1 is None:
            p1 = Point(0, 0, 0)
        super().__init__(p1, p1 + Point(0, 5, 0), p1 + Point(5, 0, 0))

        self._label = "\'"


class FrontalPlane(Plane):
    _at_symbol = ''

    def __init__(self, p1=None):

        if p1 is None:
            p1 = Point(0, 0, 0)

        super().__init__(p1, p1 + Point(0, 5, 0), p1 + Point(0, 0, 5))
        self._label = "\'\'"

class VerticalPlane(FrontalPlane):
    pass

class LateralPlane(Plane):
    _at_symbol = ''

    def __init__(self, p1=None):

        if p1 is None:
            p1 = Point(0, 0, 0)

        super().__init__(p1, p1 + Point(5, 0, 0), p1 + Point(0, 0, 5))
        self._label = "\'\'\'"
        
HPP = HorizontalPlane()
FPP = FrontalPlane()
VPP = VerticalPlane()
LPP = LateralPlane()
        
        
HPPend = HorizontalPlane( Point(0,0,16) )
VPPend = VerticalPlane( Point(16,0,0) )
FPPend = FrontalPlane( Point(16,0,0) )
LPPend = LateralPlane( Point(0,16,0) )





class DrawingSet(Entity, list):
    __color = None

    def __init__(self, *entities, scene=None):
        super(list, self).__init__()
        super(Entity, self).__init__()
        self._label = None

        self += list(entities)

    def set_label(self, label):

        obj = copy.deepcopy(self)
        obj._label = label

        return obj
    
    def set_display(self, display):

        obj = copy.deepcopy(self)
        obj._display = display

        return obj

    def __repr__(self):
        return super().__repr__() + f' labeled {self._label}'

    def __str__(self):
        return super().__str__() + f' labeled {self._label}'

    def _entity_limits(self):

        x_min = min([obj._entity_limits()['x'][0] for obj in self])
        y_min = min([obj._entity_limits()['y'][0] for obj in self])
        z_min = min([obj._entity_limits()['z'][0] for obj in self])

        x_max = max([obj._entity_limits()['x'][1] for obj in self])
        y_max = max([obj._entity_limits()['y'][1] for obj in self])
        z_max = max([obj._entity_limits()['z'][1] for obj in self])

        return {'x': [x_min, x_max], 'y': [y_min, y_max], 'z': [z_min, z_max]}

    @property
    def color(self):
        return self.__color
    
    def plot(
        self,
        fmt=None,
        marker=None,
        color=None,
        style='-',
        linewidth = linewidth,
        text=None,
        fontsize=13,
        scene=GeometrySceneDG.ax_3d
    ):


        obj = copy.deepcopy(self)

        if color is None:
            color = obj.color
            
        for elem in obj:
            elem.plot(fmt=fmt,
                      marker=marker,
                      color=color,
                      style=style,
                      text=text,
                      fontsize=fontsize,
                      scene=scene)

        obj._label = self._label
        plt.title(obj._label)

        return obj

    def plot_hp(
        self,
        fmt=None,
        marker=None,
        color=None,
        style='-',
        linewidth = linewidth,
        text=None,
        fontsize=13,
        scene=GeometrySceneDG.ax_2d,
    ):

        obj = copy.deepcopy(self)
        if color is None:
            color = obj.color   
        
        for elem in obj:
            elem.plot_hp(fmt=fmt,
                         marker=marker,
                         color=color,
                         style=style,
                         text=text,
                         fontsize=fontsize,
                         scene=scene)

        obj._label = self._label
        plt.title(obj._label)

        return obj

    def plot_vp(
        self,
        fmt=None,
        marker=None,
        color=None,
        style='-',
        linewidth = linewidth,
        text=None,
        fontsize=13,
        scene=GeometrySceneDG.ax_2d,
    ):

        obj = copy.deepcopy(self)

        if color is None:
            color = obj.color   
        
        for elem in obj:
            elem.plot_vp(fmt=fmt,
                         marker=marker,
                         color=color,
                         style=style,
                         text=text,
                         fontsize=fontsize,
                         scene=scene)

        obj._label = self._label
        plt.title(obj._label)

        return obj

    def get_projections(self):

        return [obj @ HPP for obj in self if obj is not None
                ] + [obj @ VPP for obj in self if obj is not None]


class GeometricalCase(DrawingSet):

    _case_no = plots_no()
    scheme_name = 'absxyz'
    real_name = 'abs'

    def _scheme(self):

        self.preview()

        return self._path

    def _real_example(self):

        self.preview()

        return self._path

    def preview(self, example=False,force=False):


        #print('preview')
        #print(self._assumptions3d)
        #print(len(self._assumptions3d))        
        #print('preview')        
        
        if self._assumptions3d is None or len(self._assumptions3d)==0:
            self._assumptions3d = self._solution3d_step[0]

        #print(self._assumptions3d)
        
        set_to_plot = self._assumptions
        set_to_plot_3d = self._assumptions3d
        
        if len(set_to_plot) == 0:
            set_to_plot = self._solution_step[0]
        
        self._set_to_plot = set_to_plot
        
        if self._path and force == False:
            path = self._path
            
        else:
            
            print("++++++++",list(set_to_plot),"++++++++++")
            print("++++++++",type(set_to_plot),"++++++++++")
            
            GeometrySceneDG()

            set_to_plot_3d.plot()
            set_to_plot.plot_hp()
            set_to_plot.plot_vp()

            #self._assumptions3d.plot()
            #self._assumptions.plot_hp()
            #self._assumptions.plot_vp()
            
            path = __file__.replace('dgeometry.py',
                                    'images/') + self.__class__.__name__ + str(
                                        next(self.__class__._case_no)) + '.png'
            plt.title('Assumptions')

            plt.savefig(path)
            self._path=path

            plt.close()

        

#        print('check' * 100)
        print(self._path)
#        print('check' * 100)
        plt.close()

        with open(f"{path}", "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        image_file.close()

        return IP.display.Image(base64.b64decode(encoded_string))

    @classmethod
    def from_random_data(cls):
        new_obj = cls()
        data_set = new_obj.get_random_parameters()
        print(data_set)
        entities = [point(str(label)) for label, point in data_set.items()]
        print(entities)
        return cls(*entities)

    def __init__(self, *assumptions, **kwargs):
        super().__init__()
        self._solution_step = []
        self._solution3d_step = []

        self._label = None

        self._assumptions = DrawingSet(
            *([elem @ HPP for elem in assumptions] +
              [elem @ VPP for elem in assumptions]))('Assumptions')
        self._assumptions3d = DrawingSet(*assumptions)

        self._given_data = {
            str(elem): elem
            for no, elem in enumerate(assumptions)
        }

        self._solution_step = list(assumptions)

        self._cached_solution = None
        
        self._path = None

    def add_solution_step(self,
                          title,
                          elements=[],
                          projections=None,
                          caption=None):

        self += elements

        print(f'solution step name: {caption}')

        elements_set = DrawingSet(*elements)(title, caption=caption)

        if projections is None:
            projections = elements_set.get_projections()

        projections_set = DrawingSet(*projections)(title, caption=caption)

        #it sets the step elements
        self._solution3d_step.append(elements_set)
        self._solution_step.append(projections_set)

        return DrawingSet(*elements, *projections)(f'{title} - preview',
                                                   caption=caption)

    def _add_solution_steps(self, steps_3d, steps_2d):

        result = [
            self.add_solution_step(step_3d._label,
                                   list(step_3d),
                                   list(step_2d),
                                   caption=step_3d._caption)
            for step_3d, step_2d in zip(steps_3d, steps_2d)
        ]

        return DrawingSet(*sum([list(entity) for entity in result], []))

    def _append_case(self, case):

        return self._add_solution_steps(steps_3d=case._solution3d_step,
                                        steps_2d=case._solution_step)

    def plot(
        self,
        fmt=None,
        marker=None,
        color=None,
        style='-',
        text=None,
        fontsize=13,
        scene=GeometrySceneDG.ax_3d,
    ):

        print(type(self._assumptions))
        print(self._assumptions)

        if self._assumptions3d is None:
            self._assumptions3d = self._assumptions

        self._assumptions3d.plot(fmt=fmt,
                                 marker=marker,
                                 color=color,
                                 style=style,
                                 text=text,
                                 fontsize=fontsize,
                                 scene=scene)

        return copy.deepcopy(self)

    def plot_hp(
        self,
        fmt=None,
        marker=None,
        color=None,
        style='-',
        text=None,
        fontsize=13,
        scene=GeometrySceneDG.ax_2d,
    ):

        self._assumptions.plot_hp(fmt=fmt,
                                  marker=marker,
                                  color=color,
                                  style=style,
                                  text=text,
                                  fontsize=fontsize,
                                  scene=scene)

        return copy.deepcopy(self)

    def plot_vp(
        self,
        fmt=None,
        marker=None,
        color=None,
        style='-',
        text=None,
        fontsize=13,
        scene=GeometrySceneDG.ax_3d,
    ):

        
        
        self._assumptions.plot_vp(fmt=fmt,
                                  marker=marker,
                                  color=color,
                                  style=style,
                                  text=text,
                                  fontsize=fontsize,
                                  scene=scene)

        return copy.deepcopy(self)

    def solution(self, solved_case=None):

        if self._cached_solution is None:

            new_obj = self._solution()
            self._cached_solution = new_obj

        else:
            new_obj = self._cached_solution

        return new_obj

    
    def _solution(self):

        print("Changed solution"*100)
        return  copy.copy(self)
    
    def present_solution(self):

        doc_model = Document(f'{self.__class__.__name__} solution')

        doc_model.packages.append(Package('booktabs'))
        doc_model.packages.append(Package('float'))
        doc_model.packages.append(Package('standalone'))
        doc_model.packages.append(Package('siunitx'))
        doc_model.packages.append(Package('mathtools'))
        doc_model.packages.append(Package('amssymb'))

        #ReportText.set_container(doc_model)
        #ReportText.set_directory('./SDAresults')

        for no, step3d in enumerate(self._solution3d_step):
            GeometrySceneDG()

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

                if step3d._caption is not None:
                    caption = step3d._caption
                else:
                    caption = step3d._label

                if caption is not None:
                    fig.add_caption(caption)
                    

            print(f"it's given  caption - {caption}")
            print(f"it's given  caption - {step3d._label}")
            print('\n +++++++++++++++++++++++++++ \n')
            plt.show()

        return doc_model

    def get_default_data(self):

        return None

    def get_random_parameters(self):

        default_data_dict = self.get_default_data()

        if default_data_dict:
            parameters_dict = {
                key: random.choice(items_list)
                for key, items_list in default_data_dict.items()
            }
        else:
            parameters_dict = None

        return parameters_dict

    def subs(self, *args, **kwargs):
        if len(args) > 0 and isinstance(args[0], dict):
            data_set = args[0]
            entities = [point(str(label)) for label, point in data_set.items()]

            new_obj = self.__class__(*entities)
            new_obj._given_data = args[0]

        else:
            new_obj = copy.deepcopy(self)
            #new_obj._cached_solution=None

        return new_obj


class Prism(GeometricalCase):

    names = ['D', 'E', 'F', 'G', 'H']

    @classmethod
    def right_from_parallel_plane(cls, base, point, names=None, **kwargs):

        point_at_base = point @ base

        return cls(base=base, height=(point - point_at_base), names=names)

    def __init__(self, base, height, names=None, **kwargs):

        super().__init__()

        self._base = base
        self._height = height

        if names is not None: self.names = names

        upper_base = [(vertex + height)(self.names[no])
                      for no, vertex in enumerate(base._vertices())]

        elements = [
            *base._vertices(), *upper_base,
            *[proj @ HPP for proj in base._vertices()],
            *[proj @ VPP for proj in base._vertices()],
            *[proj @ HPP
              for proj in upper_base], *[proj @ VPP for proj in upper_base]
        ]

        self._assumptions = DrawingSet(*elements)

        self += [*base._vertices(), *upper_base]

    def solution(self):

        current_obj = copy.deepcopy(self)

        return current_obj


class TetraPrism(Prism):

    names = ['E', 'F', 'G', 'H']


