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




import itertools as it

def plots_no():
    num = 0
    while True:
        yield num
        num += 1

class GeometryScene:
    plt.clf()

    plt.figure(figsize=(12,9))
    ax_2d = plt.subplot(121)
    ax_2d.set(ylabel=(r'<-x | z ->'),xlabel='y')

    plt.xlim(0, 16)
    plt.ylim(-12, 12)
    plt.grid(True)    
    
    ax_2d.set_yticks(  range(-12,12,2) )
    ax_2d.set_yticklabels(  list(map(lambda tick: str(abs(tick)),range(-12,12,2)))  )

    ax_3d = plt.subplot(122, projection='3d')
    ax_3d.view_init(30,10)
    ax_3d.set(xlabel='x',ylabel='y',zlabel='z')

    plt.xlim(0, 16)
    plt.ylim(0, 16)

    
    ax_3d.set_zlim(0, 16)
    plt.tight_layout()
    
    def __init__(self):

        plt.figure(figsize=(12,9))
        ax_2d = plt.subplot(121)
        ax_2d.set(ylabel=(r'<-x | z ->'),xlabel='y')

        plt.xlim(0, 16)
        plt.ylim(-12, 12)
        plt.grid(True)      
      
        
        ax_2d.set_yticks(  range(-12,12,2) )
        ax_2d.set_yticklabels(  list(map(lambda tick: str(abs(tick)),range(-12,12,2)))  )

        ax_3d = plt.subplot(122, projection='3d')
        ax_3d.set(xlabel='x',ylabel='y',zlabel='z')

        plt.xlim(0, 16)
        plt.ylim(0, 16)


        ax_3d.set_zlim(0, 16)

        ax_3d.view_init(30,10)
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

    _at_symbol='@'

    def __init__(self,
                 coding_points=None,
                 label=None,
                 fmt='b',
                 color=None,
                 marker='o',
                 style='-',
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
        self.__text = None
        self.__marker = marker
        self.__style = style
        self.__fmt = None
        self._projection=projection




        
        
    def __call__(self,
                 label=None,
                 fmt=None,
                 color=None,
                 marker=None,
                 style=None,
                 text=None,
                 *args,
                 **kwargs):
        """
        The object allows to assign a variable symbol (letter)
        to the points in the plane
        """
        obj = copy.deepcopy(self)
        if label is not None:
            obj._label = label
            
        if color is not None:
            obj.__color = color
        
        if marker is not None:
            obj.__marker = marker
            
        if style is not None:
            obj.__style = style
        obj.__fmt = fmt

        return obj

#     def _coding_points(self):
#         return [geo.Point3D(0,0,0)]

    def __repr__(self):
        
        
        if self._label is None:
            self._label = self.__class__.__name__#+' '+ str(self._coding_point())
        
        return self._label
    
    def __str__(self):
        
        if self._label is None:
            self._label = self.__class__.__name__
        
        return self._label
    
    @property
    def label(self):
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
        
        coords_dict=self._generating_points()
        
        limits_dict = {name:[min(container),max(container)] for name,container in coords_dict.items()}
        
        return limits_dict
        
        
    
    def plot(
        self,
        fmt=None,
        marker=None,
        color=None,
        style='-',
        text=None,
        fontsize=13,
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
            text = self._label

        if marker is None:
            marker = self.__marker

        if color is None:
            color = self.__color
            
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
        fontsize=13,
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
            text = self._label

        if marker is None:
            marker = self.__marker

        if color is None:
            color = self.__color
            
        if str(self)[-1]=="\'" and str(self)[-2]!="\'":
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
        fontsize=13,
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
            text = self._label

        if marker is None:
            marker = self.__marker

        if color is None:
            color = self.__color
            
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

        if str(self)[-1]=="\'" and str(self)[-2]=="\'":
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
                        fontsize=13):
        '''
        Set the coordinates of the points with the text explanation 
        Return: Line with the text that presents the actual point on the chosen plane
        '''

        if text is None:
            text = self._label

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



#     def intersection(self, other):
#         return [self.entity_convert(entry) for entry in other.intersection(self)]
    def intersection(self, other):
        common_part = self._geo_ref.intersection(other._geo_ref)
        #print(common_part)
        return [entity_convert(elem)    for elem  in   common_part ]
        
    def projection(self, other):
        
        projection = self._geo_ref.projection(other._geo_ref)

        new_entity = entity_convert(projection)
        
        at=other.__class__._at_symbol
        
        new_entity._label= f'{self._label}{at}{other._label}'
    
        new_entity._projection=other
    
        return new_entity
    
    def __matmul__(self, entity):
        new_obj = entity.projection(self)
        at=entity.__class__._at_symbol
        
        new_obj._label= f'{self._label}{at}{entity._label}'
        
        return new_obj
    
    def __and__(self,o):
        return o.intersection(self)


class Point(Entity):
    
    """
    Point class is used to create point object in Entity space and manipulate them
    """
    
    def __init__(self,*args,**kwargs):
        super().__init__()
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
    
#     def __repr__(self):
#         return f'{self.__class__.__name__}{(self._geo_ref.coordinates)}({self._label})'
    
#     def __str__(self):
#         return f'{self.__class__.__name__}{(self._geo_ref.coordinates)}({self._label})'
        

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
    
    
    def rotate_about(self,axis=None,plane=None):
        point = copy.deepcopy(self)
        
        if axis is None:
            axis = Line(point,(point + Point(0,0,10)))
            print(axis)
            
            
        if plane is None:
            plane = HorizontalPlane(axis.p1)
        
        point_rot_center = (point @ axis)(f'S_{point._label}')
        
        
        radius = point.distance(point_rot_center)
        
        if radius == 0:
            rotated_point = copy.deepcopy(point)(f'{point._label}_0')
        else:

            # zaimplementować w metode dla punktu 
            rotation_dir =(point @ plane) - point_rot_center

            #display(dir_I_on_HPP.coordinates)
            #display((point_I @ plane_beta).distance( S_I ))
            #display(point_I.distance( S_I ))

            ratio = radius / ((point @ plane).distance( point_rot_center ))

            rotated_point =(point_rot_center+(rotation_dir)*ratio)(f'{point._label}_0')

        return rotated_point
        
class Line(Entity):
    
    """
    Line calass is used to create line objects and manipulate them
    """

    def __init__(self, p1, p2, **kwargs):
        self._p1=p1
        self._p2=p2
        super().__init__()
        self._geo_ref = geo.Line3D(p1=p1._geo_ref,pt=p2._geo_ref,**kwargs)

#     def __repr__(self):
#         return self.__class__.__name__
    
#     def __str__(self):
#         return self.__class__.__name__
        
    def _coding_points(self):
        return (self._geo_ref.p1,self._geo_ref.p2)

#     def __repr__(self):
#         return self.__class__.__name__ +str(self._coding_points())
    
#     def __str__(self):
#         return self.__class__.__name__ +str(self._coding_points())
    
    def __xor__(self,other):
        if isinstance(other,geo.Point3D):
            return (Plane(self.p1,self.p2,other))
        elif isinstance(other,geo.Line3D):
            return (Plane(self.p1,self.p2,other.p1))
        
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
    
    
    def __init__(self,p1, a=None, b=None, **kwargs):
        super().__init__()
        
        if a is not None:
            _a_geo_ref = a._geo_ref

        if b is not None:
            _b_geo_ref = b._geo_ref
            
        self._geo_ref = geo.Plane(p1=p1._geo_ref, a=_a_geo_ref, b=_b_geo_ref, **kwargs)
        
        self._p1 = p1
        
        if a is None:
            self._p2=entity_convert(self._geo_ref.arbitrary_point('u','v').subs({'u':1,'v':0}))
        else:
            self._p2=a
        
        if b is None:
            self._p3=entity_convert(self._geo_ref.arbitrary_point('u','v').subs({'u':0,'v':1}))
        else:
            self._p3=b
        
#         if a == normal_vector:
#             self._geo_ref = geo.Plane(p1=p1._geo_ref, a = normal_vector._geo_ref, b = None, **kwargs)
#             b = Point(-20,-20,solve(Eq(self.equation(-20,-20),0))[0])
        
#         elif a == self._p2 and b == self._p3 :
#             self._geo_ref = geo.Plane(p1=p1._geo_ref, a=a._geo_ref, b=b._geo_ref, **kwargs)
            
    def _vertices(self):
        return self._p1,self._p2,self._p3
    
    def _coding_points(self):
        return (self._geo_ref.p1,self._p2,self._p3,self._geo_ref.p1)

    def projection(self, other):
        if isinstance(other,Point):
            projection = self._geo_ref.projection(other._geo_ref)
            
        elif isinstance(other,Line):
            projection = self._geo_ref.projection_line(other._geo_ref)            
            
        new_obj=entity_convert(projection)
        
        at=self.__class__._at_symbol
        
        new_obj._label = f'{self._label}{at}{other._label}'
        
        return new_obj
    
    def perpendicular_line(self, p):
        return entity_convert(self._geo_ref.perpendicular_line(p._geo_ref))
    
    def perpendicular_plane(self, p):
        return entity_convert(self._geo_ref.perpendicular_plane(p._geo_ref))

    def parallel_plane(self, p):

        return entity_convert(self._geo_ref.parallel_plane(p._geo_ref))
    
class HorizontalPlane(Plane):
    _at_symbol=''
    def __init__(self,p1=None):
        
        if p1 is None:
            p1=Point(0,0,0)
        super().__init__(p1, p1+Point(0,5,0),p1+Point(5,0,0))

        self._label="\'"
        
        
class VerticalPlane(Plane):
    _at_symbol=''
    def __init__(self,p1=None):
        
        if p1 is None:
            p1=Point(0,0,0)
            
        super().__init__(p1, p1+Point(0,5,0),p1+Point(0,0,5))
        self._label="\'\'"
        
HPP=HorizontalPlane()
VPP=VerticalPlane()

class DrawingSet(Entity,list):
    def __init__(self,*entities,scene=None):
        super(list,self).__init__()
        super(Entity,self).__init__()
        self._label=None

        self += list(entities)

    def set_label(self,label):
        
        obj = copy.deepcopy(self)
        obj._label = label
        
        return obj
        
    def __repr__(self):
        return super().__repr__() + f' labeled {self._label}'

    def __str__(self):
        return super().__str__() + f' labeled {self._label}'

    def _entity_limits(self):
        
  
        x_min=min([obj._entity_limits()['x'][0] for obj in self])
        y_min=min([obj._entity_limits()['y'][0] for obj in self])
        z_min=min([obj._entity_limits()['z'][0] for obj in self])
        

        x_max=max([obj._entity_limits()['x'][1] for obj in self])
        y_max=max([obj._entity_limits()['y'][1] for obj in self])
        z_max=max([obj._entity_limits()['z'][1] for obj in self])
        
        
        return {'x':[x_min,x_max],'y':[y_min,y_max],'z':[z_min,z_max]}
   
    def plot(
        self,
        fmt=None,
        marker=None,
        color=None,
        style='-',
        text=None,
        fontsize=13,
        scene=GeometryScene.ax_3d,
        ):

        obj = copy.deepcopy(self)
        
        for elem in obj:
            elem.plot(fmt=fmt,marker=marker,color=color,style=style,text=text,fontsize=fontsize,scene=scene)
            
        obj._label = self._label
        plt.title(obj._label)
            
            
            
        return obj

    def plot_hp(
        self,
        fmt=None,
        marker=None,
        color=None,
        style='-',
        text=None,
        fontsize=13,
        scene=GeometryScene.ax_2d,
        ):


        obj = copy.deepcopy(self)
        
        for elem in obj:
            elem.plot_hp(fmt=fmt,marker=marker,color=color,style=style,text=text,fontsize=fontsize,scene=scene)
            
        obj._label = self._label
        plt.title(obj._label)
            
            
            
        return obj

    def plot_vp(
        self,
        fmt=None,
        marker=None,
        color=None,
        style='-',
        text=None,
        fontsize=13,
        scene=GeometryScene.ax_2d,
        ):

        obj = copy.deepcopy(self)
        
        for elem in obj:
            elem.plot_vp(fmt=fmt,marker=marker,color=color,style=style,text=text,fontsize=fontsize,scene=scene)
            
        obj._label = self._label
        plt.title(obj._label)
            
            
            
        return obj






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




    
    def preview(self, example=False):
        GeometryScene()

        print('preview')
        print(self._assumptions3d)
        if self._assumptions3d is None:
            self._assumptions3d = self._assumptions
            
        print(self._assumptions3d)        
        
        self._assumptions3d.plot()
        self._assumptions.plot_hp()
        self._assumptions.plot_vp()

        
        
        path = __file__.replace('dgeometry.py', 'images/') + self.__class__.__name__ + str(next(self.__class__._case_no)) + '.png'

        
        
        plt.savefig(path)

        plt.close()




        self._path = path




        print('check'*100)
        print(self._path)        
        print('check'*100)        
        plt.close()


        with open(f"{path}", "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        image_file.close()

        return IP.display.Image(base64.b64decode(encoded_string))


    @classmethod
    def from_random_data(cls):
        new_obj = cls()
        data_set=new_obj.get_random_parameters()
        print(data_set)
        entities = [point(str(label))  for label,point in data_set.items()]
        print(entities)
        return cls(*entities)

    def __init__(self,*assumptions,**kwargs):
        super().__init__()
        self._solution_step=[]
        self._solution3d_step=[]
        
        
        self._label = None

        self._assumptions=DrawingSet(*([elem@HPP for  elem in assumptions] + [elem@VPP for  elem in assumptions]  ))('Assumptions')
        self._assumptions3d=DrawingSet(*assumptions)
        
        self._given_data={str(elem):elem  for no,elem in enumerate(assumptions)}
        
        self._solution_step=list(assumptions)
        
        self._cached_solution=None


    def add_solution_step(self,title,elements=[],projections=None):
        
        self+=elements

        elements_set=DrawingSet(*elements)(title)

        if projections is None:
            projections = [obj@HPP for obj  in elements if obj is not None] + [obj@VPP for obj  in elements if obj is not None]

        projections_set = DrawingSet(*projections)(title)

        #it sets the step elements
        self._solution3d_step.append(elements_set)
        self._solution_step.append(projections_set)

        return DrawingSet(*elements,*projections)(f'{title} - preview')
        
        
        
    def get_projections(self):
        
        return [obj@HPP for obj  in self if obj is not None] + [obj@VPP for obj  in self if obj is not None]
        
        
        
    def plot(
        self,
        fmt=None,
        marker=None,
        color=None,
        style='-',
        text=None,
        fontsize=13,
        scene=GeometryScene.ax_3d,
        ):

        print(type(self._assumptions))
        print(self._assumptions)

        if self._assumptions3d is None:
            self._assumptions3d=self._assumptions
        
        self._assumptions3d.plot(fmt=fmt,marker=marker,color=color,style=style,text=text,fontsize=fontsize,scene=scene)

        return copy.deepcopy(self)

    def plot_hp(
        self,
        fmt=None,
        marker=None,
        color=None,
        style='-',
        text=None,
        fontsize=13,
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
        fontsize=13,
        scene=GeometryScene.ax_3d,
        ):

        self._assumptions.plot_vp(fmt=fmt,marker=marker,color=color,style=style,text=text,fontsize=fontsize,scene=scene)

        return copy.deepcopy(self)

    def solution(self,solved_case=None):

        if self._cached_solution is None:
        
            new_obj = copy.deepcopy(self)
            self._cached_solution=new_obj
            
        else:
            new_obj = self._cached_solution

        return new_obj

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
            parameters_dict=None

        return parameters_dict
    
    def subs(self,*args,**kwargs):
        if len(args)>0 and isinstance(args[0],dict):
            data_set=args[0]
            entities = [point(str(label))  for label,point in data_set.items()]

            new_obj=self.__class__(*entities)
            new_obj._given_data=args[0]

        else:
            new_obj = copy.deepcopy(self)
            #new_obj._cached_solution=None
            
        return new_obj
        
        
class Prism(GeometricalCase):

    names=['D','E','F','G','H']
    
    @classmethod
    def right_from_parallel_plane(cls,base,point,names=None,**kwargs):
        
        point_at_base = point @ base
        
        return cls(base=base,height=(point - point_at_base  ),names=names)
        
    
    
    def __init__(self,base,height,names=None,**kwargs):

        super().__init__()


        self._base=base
        self._height=height
        
        
        if names is not None: self.names=names

        upper_base = [(vertex+height)(self.names[no])  for  no,vertex  in enumerate(base._vertices())]
        
        
        elements= [*base._vertices(),*upper_base, *[proj@HPP for proj in base._vertices()], *[proj@VPP for proj in base._vertices()],
                                    *[proj@HPP for proj in upper_base], *[proj@VPP for proj in upper_base]
                   ]

        self._assumptions=DrawingSet(*elements)
        
        self += [*base._vertices(),*upper_base]

        
        
        
    def solution(self):
        
        
        current_obj=copy.deepcopy(self)

        return current_obj
        
        
######################################################### cases
        
# class PyramidWithSquareBaseFromDiagonalAndPoint(GeometricalCase):

#     scheme_name = 'abs.png'
#     real_name = 'abs.png'

 


#     # @classmethod
#     # def from_random_data(cls):
#     #     new_obj = cls()
#     #     data_set=new_obj.get_random_parameters()
        
#     #     entities = [point(str(label))  for label,point in data_set.items()]
#     #     print(entities)
#     #     return cls(*entities)

#     def __init__(self,point_A,distance_CA,distance_OA,top_projection=None,relative_height=1,**kwargs):
#         self._assumptions=DrawingSet(point_A,distance_CA,distance_OA)
#         self._given_data=None

#         self._point_A=point_A
#         self._distance_CA=distance_CA
#         self._distance_OA=distance_OA

#         if top_projection:
#             self._top_projection= top_projection
#         else:
#             self._top_projection = self._point_A
        
#         self._relative_height = relative_height



#     def solution(self):

#         A = self._point_A
#         CA = self._distance_CA
#         OA = self._distance_OA

#         relative_h = self._relative_height
#         W_projection = self._top_projection
 

#         xshift,yshift,zshift = 0,0,0
#         #print(counter)

#         A=Point(A.x,A.y,A.z)('A',marker='o').plot('ko').plot_hp('go').plot_vp('go')
#         O=(A+OA)('O',marker='o').plot('ko').plot_hp('go').plot_vp('go')
#         C=(A+CA)('C',marker='o').plot('ko').plot_hp('go').plot_vp('go') 
#         #D=(A+Point(4,3,4))('D',marker='o').plot('ko').plot_hp('go').plot_vp('go')
#         G=(A+Point(-4,3,-1))('D',marker='o')#.plot('ko').plot_hp('go').plot_vp('go')

#         HPP_A = Plane(A,A+Point(0,1,0),A+Point(1,0,0)  )
#         VPP_A = Plane(A,A+Point(0,1,0),A+Point(0,0,1)  )

        

#         # A=Point(0,0,0)('A')
#         # B=Point(A.x+2,A.y+1,A.z+3)('B')
#         # C=Point(4,3,5)('C')
#         E=Point(4,4,5)('E')
#         F=Point(3,3,5)('F')


#         #B._geo_ref
#         a=Line(A,O)('a')
#         b=Line(O,C)('b')

#         P1=(A @ b)('1',marker='o').plot('ko').plot_hp('go').plot_vp('go')
#         alpha=Plane(A,O,C)

#         #alpha.intersection(Plane(E,F,A))[0]

#         e=Line(E,F)
#         e.projection(Line(A,O))

#         alpha.projection(e)

#         c = alpha.perpendicular_line(A)
#         # c('nn',marker='o').plot().plot_hp().plot_vp()

#         # (alpha & HPP_A)[0]('go',marker='o').plot().plot().plot_hp().plot_vp()
#         # (alpha & VPP_A)[0]('go',marker='o').plot().plot().plot_hp().plot_vp()

#         #(e @ VPP)('A',marker='o').plot().plot_hp().plot_vp()
#         # Plane(A._geo_ref,B._geo_ref,C._geo_ref).projection_line(Line(E._geo_ref,F._geo_ref))
#         # Line(E._geo_ref,F._geo_ref).projection(Line(A._geo_ref,B._geo_ref))
#         #dg2.entity_convert(alpha.intersection(dg2.Line(A,B))[0])

#         # Line(A,B)('a',marker='o').plot().plot_hp().plot_vp()


#         # B1=Point(A.x,(A.y+(B@HPP).distance(A@HPP)),B.z,evaluate=True)('B1',marker='o').plot().plot_hp().plot_vp()
#         # B1.n()
#         # B1.distance(A).n(),B.distance(A)

#         # (B1.x.n(),B1.y.n(),B1.z.n())


#         # Line(D,C-A+D  )('e').plot().plot_hp().plot_vp()
#         # Line(D,B-A+D  )('f').plot().plot_hp().plot_vp()
#         M = (O @ (Line(A,C)))('M',marker='o').plot().plot_hp().plot_vp()
        
#         Q=G @ alpha
#         Q('Q',marker='o')#.plot_hp().plot_vp()

#         S=(A+(C-A)*0.5)
        
#         B=(S+((M^O).direction()/M.distance(O))*(A.distance(S)).n())('B',marker='o').plot().plot_hp().plot_vp()
#         D=(S+((M^O).direction()/M.distance(O))*(-A.distance(S)).n())('D',marker='o').plot().plot_hp().plot_vp()
#         #C=(M+((M^O).direction()/M.distance(O))*(A.distance(M))*(-sqrt(3)/3).n())
        
#     #     H=(A+((P^D).direction()/D.distance(P))*(A.distance(F))*(-1))
#     #     H('H',marker='o').plot().plot_hp().plot_vp()
        
#         W=(C+((Q^G).direction()/G.distance(Q))*(A.distance(B))*(-1))
#         W('W',marker='o').plot().plot_hp().plot_vp()
        
#         (W @ alpha)('W_test',marker='o').plot().plot_hp().plot_vp()
        
#         A, c@alpha

#         Line(A,B)(marker='o').plot().plot_hp().plot_vp()
#         Line(A,D)(marker='o').plot().plot_hp().plot_vp()
#         Line(B,C)(marker='o').plot().plot_hp().plot_vp()
#         Line(C,D)(marker='o').plot().plot_hp().plot_vp()
        
        
#         Line(A,W)(marker='o').plot().plot_hp().plot_vp()
#         Line(B,W)(marker='o').plot().plot_hp().plot_vp()
#         Line(C,W)(marker='o').plot().plot_hp().plot_vp()

#         new_obj = copy.deepcopy(self)

#         new_obj._solution_dict=({'Ax':A.x,'Ay':A.y,'Az':A.z,'Bx':B.x.n(4),'By':B.y.n(4),
#                             'Bz':B.z.n(4),'Cx':C.x,'Cy':C.y,'Cz':C.z,'Dx':D.x.n(4),'Dy':D.y.n(4),
#                             'Dz':D.z.n(4),'Wx':W.x.n(4),'Wy':W.y.n(4),'Wz':W.z.n(4),
#                             'Ox':O.x,'Oy':O.y,'Oz':O.z})

#         new_obj._all_points = DrawingSet(A,B,C,D,W)

#         return new_obj

#     def get_default_data(self):

        

#         default_data_dict = {
#             Symbol('A'): [Point(4,5,8),Point(4,6,8),Point(5,10,8),Point(6,10,8),Point(7,10,8),Point(8,10,8),Point(-1,10,8),Point(3,10,8)],
#             Symbol('C'): [Point(2,-4,-1),Point(1,-4,-2),Point(2,-5,-1),],
#             Symbol('O'): [Point(1,-5,2),Point(0,-5,1),],
#         }
#         return default_data_dict

# class SegmentMidpoint(GeometricalCase):
    
#     def __init__(self,point_A=None,point_B=None,**kwargs):
        
#         super().__init__()
        
#         if point_A and point_B:
#             projections=point_A@HPP,point_A@VPP,point_B@HPP,point_B@VPP,
#         else:
#             projections=[]
        
#         self._assumptions=DrawingSet(point_A,point_B,*projections)
#         self._given_data={'A':point_A,'B':point_B}

#         self._point_A=point_A
#         self._point_B=point_B
        
#         self._solution_step.append(self._assumptions)



#     def solution(self):
        
#         current_obj=copy.deepcopy(self)
        
#         A=current_obj._point_A
#         B=current_obj._point_B
        

#         current_set=DrawingSet(*current_obj._solution_step[-1])
        
#         midpoint=(A+ (B-A)*0.5)('C')
#         current_set += [midpoint]
        
#         current_obj._solution_step.append(current_set)
        
        
#         current_obj.midpoint = midpoint
#         current_obj.point_C = midpoint
        
#         return current_obj
    
#     def get_default_data(self):

#         print('jesteś tu - dziedziczenie')

#         default_data_dict = {
#             Symbol('A'): [Point(4,5,8),Point(4,6,8),Point(5,10,8),Point(6,10,8),Point(7,10,8),Point(8,10,8),Point(-1,10,8),Point(3,10,8)],
#             Symbol('B'): [Point(2,2,4),Point(1,3,3),Point(2,4,-1),Point(4,6,-2),Point(3,8,0)],

#         }
#         print(default_data_dict)
#         return default_data_dict

# class PointOnLine(GeometricalCase):
    
#     def __init__(self,point_A=None,point_B=None,point_D=None,**kwargs):
        
#         super().__init__()
        
#         if point_A and point_B and point_D:
            
#             point_C=(point_D+Point(0,0,-3))('C')
#             projections=point_D,point_A@HPP,point_A@VPP,point_B@HPP,point_B@VPP,point_D@HPP,point_D@VPP,
#             self._given_data={'A':point_A,'B':point_B,'D':point_D}
#             self._point_C=point_C
#             self._point_D=point_D
#         else:
#             projections=[]
#             self._given_data={'A':point_A,'B':point_B}
        
#         self._assumptions=DrawingSet(point_A,point_B,*projections)
#         #self._given_data={'A':point_A,'B':point_B,'D':point_D}

#         self._point_A=point_A
#         self._point_B=point_B
        
#         print('given_data',self._given_data)
        
#         self._solution_step.append(self._assumptions)



#     def solution(self):
        
#         current_obj=copy.deepcopy(self)
        
#         A=current_obj._point_A
#         B=current_obj._point_B
#         C=current_obj._point_C
        
        

#         current_set=DrawingSet(*current_obj._solution_step[-1])
        

#         current_set += [C]
        
#         current_obj._solution_step.append(current_set)
        
        

#         current_obj.point_C = C
        
#         return current_obj
    
#     def get_default_data(self):


        
        
        
        
#         point_A = [Point(x,y,z) for x in range(1,5) for y in range(1,7) for z in range(1,5) ]
#         distance_AB = [Point(2,5,2),Point(2,6,2),Point(2,4,2),Point(3,7,4)]
        
        
#         point_B=[pt + dist  for pt,dist   in  it.product(point_A,distance_AB)]
        


#         default_data_dict = {
#             Symbol('A'): point_A,
#             Symbol('B'): point_B,

#         }
        
#         return default_data_dict

#     def get_random_parameters(self):

#         parameters_dict=super().get_random_parameters()



#         point_A=parameters_dict[Symbol('A')]
#         point_B=parameters_dict[Symbol('B')] 
#         point_C=((point_A+ (point_B-point_A)*0.3))('C')
#         point_D=(point_C+Point(0,0,3))('D')
        
#         parameters_dict[Symbol('D')]=point_D

#         return parameters_dict
    
    
# class PlanesIntersection(GeometricalCase):
    
#     def __init__(self,point_A=None,point_B=None,**kwargs):
        
#         super().__init__()
        
#         self._assumptions=DrawingSet(point_A,point_B)
#         self._given_data=None

#         self._point_A=point_A
#         self._point_B=point_B



#     def solution(self):
        
#         A=self._point_A
#         B=self._point_B
        
        
#         Aprim = A @ HPP
#         Abis = A @ VPP
        
#         self.append(Aprim)
#         self.append(Abis)
        
#         self.append(Line(A,B))
#         self.append(A^B)

#         return copy.deepcopy(self)
    
#     def get_default_data(self):

        

#         default_data_dict = {
#             Symbol('A'): [Point(4,5,8),Point(4,6,8),Point(5,10,8),Point(6,10,8),Point(7,10,8),Point(8,10,8),Point(-1,10,8),Point(3,10,8)],
#             Symbol('B'): [Point(2,2,4),Point(1,3,3),Point(2,4,-1),],

#         }
#         return default_data_dict
    
# class VerticalLineOnPlane(GeometricalCase):

#     def __init__(self,point_A=None,point_B=None,point_O=None,**kwargs):

#         super().__init__()

#         if point_A and point_B and point_O:
#             projections=Line(point_A@HPP,point_B@HPP),Line(point_A@VPP,point_B@VPP),point_O@HPP,point_O@VPP,point_A@HPP,point_A@VPP,point_B@HPP,point_B@VPP

#         else:
#             projections=[]

#         self._assumptions=DrawingSet(*projections)

#         self._point_A=point_A
#         self._point_B=point_B
#         self._point_O=point_O
        
#         self._given_data={'A':point_A,'B':point_B,'O':point_O}

#     def solution(self):
        
#         current_obj=copy.deepcopy(self)
        
#         O=self._point_O
#         A=self._point_A
#         B=self._point_B
        
#         a=Line(A,B)('a')
        
#         alpha=Plane(A,B,O)('alpha')
#         beta=VerticalPlane(A)('beta')
        
#         k=alpha.intersection(beta)[0]
#         C=entity_convert(k._coding_points()[0])
#         c=Line(C,O)('c')
        
#         I=a.intersection(c)[0]('I')
        
#         new_set= DrawingSet(self._assumptions)
        
        
        
#         current_obj._solution_step.append(new_set)
#         current_obj.point_P=I
        
#         return current_obj
    
#     def get_default_data(self):


#         default_data_dict = {
#             Symbol('A'): [Point(4,5,8),Point(4,6,8),Point(5,10,8),Point(6,10,8),Point(7,10,8),Point(8,10,8),Point(-1,10,8),Point(3,10,8)],
#             Symbol('B'): [Point(2,2,4),Point(1,3,3),Point(2,4,-1),],
#             Symbol('O'): [Point(1,6,2),Point(0,7,1),],
#         }
#         return default_data_dict
# class FrontalLineOnPlane(GeometricalCase):
    
#     def __init__(self,point_A=None,point_B=None,point_O=None,**kwargs):
        
#         super().__init__()
#         if point_A and point_B and point_O:
#             projections=(point_A@HPP,point_B@HPP,point_A@VPP,point_B@VPP,point_O@HPP,point_O@VPP)
#         else:
#             projections=[]
#         self._assumptions=DrawingSet(*projections)

#         self._point_A=point_A
#         self._point_B=point_B
#         self._point_O=point_O
#         self._given_data={'A':point_A,'B':point_B,'O':point_O}

#         self._solution_step.append(self._assumptions)
#     def solution(self):
#         current_obj=copy.deepcopy(self)
#         O=current_obj._point_O
#         A=current_obj._point_A
#         B=current_obj._point_B
#         current_set=DrawingSet(*current_obj._solution_step[-1])
#         f=Line(A,B)('a')
        
#         alpha=Plane(A,B,O)('alpha')
#         beta=VerticalPlane(O)('beta')
        
#         k=alpha.intersection(beta)[0] 
#         P=entity_convert(k._coding_points()[0])
#         p=Line(P,O)('f')
        
#         I=f.intersection(p)[0]('I')
#         current_obj._point_I=I
#         elems=[O,A,B]
#         projections=[O@HPP,A@HPP,B@HPP,I@HPP]
#         current_set+=[*elems,*projections]
        
#         return current_obj
    
#     def get_default_data(self):


#         default_data_dict = {
#             Symbol('A'): [Point(4,5,8),Point(4,6,8),Point(5,10,8),Point(6,10,8),Point(7,10,8),Point(8,10,8),Point(-1,10,8),Point(3,10,8)],
#             Symbol('B'): [Point(6,2,3),Point(4,2,5),Point(8,7,1),],
#             Symbol('O'): [Point(5,4,7),Point(4,8,2),],
#         }
#         return default_data_dict
# class HorizontalLineOnPlane(GeometricalCase):
    
#     def __init__(self,point_A=None,point_B=None,point_O=None,**kwargs):
        
#         super().__init__()
#         if point_A and point_B and point_O:
#             projections=(point_A@HPP,point_B@HPP,point_A@VPP,point_B@VPP,point_O@HPP,point_O@VPP)
#         else:
#             projections=[]
#         self._assumptions=DrawingSet(*projections)

#         self._point_A=point_A
#         self._point_B=point_B
#         self._point_O=point_O
#         self._given_data={'A':point_A,'B':point_B,'O':point_O}

#         self._solution_step.append(self._assumptions)
#     def solution(self):
#         current_obj=copy.deepcopy(self)
#         O=current_obj._point_O
#         A=current_obj._point_A
#         B=current_obj._point_B
#         current_set=DrawingSet(*current_obj._solution_step[-1])
#         f=Line(A,B)('a')
        
#         alpha=Plane(A,B,O)('alpha')
#         beta=HorizontalPlane(O)('beta')
        
#         k=alpha.intersection(beta)[0] 
#         P=entity_convert(k._coding_points()[0])
#         p=Line(P,O)('f')
        
#         I=f.intersection(p)[0]('I')
#         current_obj._point_I=I
#         elems=[O,A,B]
#         projections=[O@VPP,A@VPP,B@VPP,I@VPP]
#         current_set+=[*elems,*projections]
        
#         return current_obj
    
#     def get_default_data(self):


#         default_data_dict = {
#             Symbol('A'): [Point(4,5,8),Point(4,6,8),Point(5,10,8),Point(6,10,8),Point(7,10,8),Point(8,10,8),Point(-1,10,8),Point(3,10,8)],
#             Symbol('B'): [Point(6,2,3),Point(4,2,5),Point(8,7,1),],
#             Symbol('O'): [Point(5,4,7),Point(4,8,2),],
#         }
#         return default_data_dict

# class LineOnPlane(GeometricalCase):

#     point_A = [Point(x,y,z) for x in [2,2.5,3,3.5] for y in range(1,6) for z in [1.5,2,2.5,3,3.5] ]
# #     distance_AO = [Point(2,4,2),Point(2,5,2),Point(2,6,2),Point(3,4,4)]

# #     point_O = [pt + dist  for pt,dist   in  it.product(point_A,distance_AO)]
#     point_O = [Point(x,y,z) for x in range(7,11) for y in range(8,12) for z in range(8,12) ]
#     distance_OB = [Point(-4,4,-4),Point(-5,5,-4),Point(-4,5,-6),Point(-5,4,-7)]

#     point_B=[Point(x,y,z) for x in [1,1.5,2,2.5,3,3.5] for y in [13,13.5,14,14.5,15] for z in [1,1.5,2,2.5,3,3.5] ]


#     distance_AD = [Point(x,y,z) for x in range(1,4) for y in range(0,3) for z in range(1,4) ]
#     distance_OE = [Point(x,y,z) for x in range(-4,-1) for y in range(-1,3) for z in range(-4,-1) ]
#     distance_BF = [Point(x,y,z) for x in range(1,4) for y in range(-2,2) for z in range(1,4) ]

# #     point_D=[pt + dist  for pt,dist   in  it.product(point_A,distance_AD) if (pt+dist).x != 0]
# #     point_E = [pt + dist  for pt,dist   in  it.product(point_O,distance_OE) if (pt+dist).x != 0]
# #     point_F = [pt + dist  for pt,dist   in  it.product(point_B,distance_BF) if (pt+dist).x != 0]

#     point_D=[Point(x,y,z) for x in range(7,11) for y in range(2,6) for z in range(8,12) ]
#     point_E = [Point(x,y,z) for x in range(1,5) for y in range(8,12) for z in range(2,5) ]
#     point_F = [Point(x,y,z) for x in range(7,11) for y in range(13,16) for z in range(8,12) ]
    
    
#     def __init__(self,point_A=None,point_B=None,point_O=None,point_C=None,point_D=None,**kwargs):

#         super().__init__()

#         if point_A and point_B and point_O and point_C and point_D:
#             projections=(point_A@HPP,point_B@HPP,Line(point_A@HPP,point_O@HPP),Line(point_A@VPP,point_O@VPP),
#                          Line(point_B@HPP,point_O@HPP),Line(point_B@VPP,point_O@VPP),point_A@VPP,point_B@VPP,
#                          point_O@HPP,point_O@VPP,point_C@VPP,point_D@VPP,point_C@HPP,point_D@HPP,point_C@VPP,point_D@VPP
#                         )
#         else:
#             projections=[]

#         self._assumptions=DrawingSet(*projections)


#         self._point_A=point_A
#         self._point_B=point_B
#         self._point_O=point_O
#         self._point_C=point_C
#         self._point_D=point_D


#         self._given_data={'A':point_A,'B':point_B,'O':point_A,'C':point_C,'D':point_D}


        
#         self._solution_step.append(self._assumptions)
# #     def solution(self):

        
# #         midpoint=(A+ (B-A)*0.5)('C')
# #         current_set += [midpoint]
        
# #         current_obj._solution_step.append(current_set)
        
        
# #         current_obj.midpoint = midpoint
# #         current_obj.point_C = midpoint
        
# #         return current_obj
#     def solution(self):
#         self._line=Line(self._point_C,self._point_D)
#         current_obj=copy.deepcopy(self)
        
#         A=current_obj._point_A
#         B=current_obj._point_B
#         O=current_obj._point_O
#         n=current_obj._line
#         current_set=DrawingSet(*current_obj._solution_step[-1])

#         base_plane=Plane(A,B,O)('base')
#         line_a=Line(self._point_C,self._point_C+Point(15,0,0))('a')
#         line_b=Line(self._point_D,self._point_D+Point(15,0,0))('b')

#         plane_v=base_plane('alpha') #why is the line created? #looks unnecessary
#         #plane_h=Plane(n.p1,n.p2,n.p1@HPP)('beta')
#         #int_line_h=Line(plane_h.intersection(line_a)[0],plane_h.intersection(line_b)[0])('n')
#         int_line_v=Line(plane_v.intersection(line_a)[0],plane_v.intersection(line_b)[0])('n') 

#         elems=[line_a,line_b,int_line_v]
#         projections=[line_a@HPP,line_b@HPP,line_a@VPP,line_b@VPP]
#         current_set+=[*elems,*projections]

#         current_obj._solution_step.append(current_set)
#         current_obj.int_line_v_p1=(int_line_v).p1 #names
#         current_obj.int_line_v_p2=(int_line_v).p2 #names
        
#         current_obj.point_P=(int_line_v).p1 #names
#         current_obj.point_Q=(int_line_v).p2 #names
        
        
#         return current_obj
    
#     def get_default_data(self):

#         point_A = self.__class__.point_A
#         #distance_AO = self.__class__.distance_AO
        
#         point_O = self.__class__.point_O 
#         #distance_OB = self.__class__.distance_OB
        
#         point_B=self.__class__.point_B
        

#         #distance_AD = self.__class__.distance_AD
#         #distance_OE = self.__class__.distance_OE
#         #distance_BF = self.__class__.distance_BF
        
        
#         point_D=self.__class__.point_D
#         point_E = self.__class__.point_E
#         point_F = self.__class__.point_F


        
# #         point_A = [Point(x,y,z) for x in range(1,5) for y in range(1,7) for z in range(1,5) ]
# #         distance_AO = [Point(2,3,2),Point(2,4,2),Point(2,4,2),Point(3,3,4)]
        
# #         point_O = [pt + dist  for pt,dist   in  it.product(point_A,distance_AO)]
# #         distance_OB = [Point(-4,2,-4),Point(-5,3,-4),Point(-4,4,-6),Point(-5,3,-7)]
        
# #         point_B=[pt + dist  for pt,dist   in  it.product(point_O,distance_OB)]
        
# #         distance_AC  = [Point(2,1,1),Point(2,2,1),Point(2,1,2),Point(1,2,3)]
# #         distance_AD = [Point(2,5,1),Point(2,6,1),Point(2,6,2),Point(1,5,3)]

#         default_data_dict = {
#             Symbol('A'): point_A,
#             Symbol('B'): point_B,
#             Symbol('O'): point_O,

#             Symbol('C'): point_D,
#             Symbol('D'): point_F,
#         }
#         return default_data_dict
    
    
    
# class PointOnPlane(GeometricalCase):

#     point_A = [Point(x,y,z) for x in [1,1.5,2,2.5,3,3.5] for y in range(2,6) for z in [1,1.5,2,2.5,3,3.5] ]
# #     distance_AO = [Point(2,4,2),Point(2,5,2),Point(2,6,2),Point(3,4,4)]

# #     point_O = [pt + dist  for pt,dist   in  it.product(point_A,distance_AO)]
#     point_O = [Point(x,y,z) for x in range(7,11) for y in range(8,12) for z in range(8,12) ]
#     distance_OB = [Point(-4,4,-4),Point(-5,5,-4),Point(-4,5,-6),Point(-5,4,-7)]

#     point_B=[Point(x,y,z) for x in [1,1.5,2,2.5,3,3.5] for y in [13,13.5,14,14.5,15] for z in [1,1.5,2,2.5,3,3.5] ]


#     distance_AD = [Point(x,y,z) for x in range(1,5) for y in range(0,4) for z in range(1,5) ]
#     distance_OE = [Point(x,y,z) for x in range(-5,-1) for y in range(-1,4) for z in range(-5,-1) ]
#     distance_BF = [Point(x,y,z) for x in range(1,5) for y in range(-2,3) for z in range(1,5) ]

# #     point_D=[pt + dist  for pt,dist   in  it.product(point_A,distance_AD) if (pt+dist).x != 0]
# #     point_E = [pt + dist  for pt,dist   in  it.product(point_O,distance_OE) if (pt+dist).x != 0]
# #     point_F = [pt + dist  for pt,dist   in  it.product(point_B,distance_BF) if (pt+dist).x != 0]

#     point_D=[Point(x,y,z) for x in range(7,11) for y in range(2,6) for z in range(8,12) ]
#     point_E = [Point(x,y,z) for x in range(1,5) for y in range(8,12) for z in range(2,5) ]
#     point_F = [Point(x,y,z) for x in range(7,11) for y in range(13,16) for z in range(8,12) ]
    
    
#     def __init__(self,point_A=None,point_B=None,point_O=None,point_D=None,**kwargs):

#         super().__init__()

#         if point_A and point_B and point_O and point_D:
#             projections=(point_A@HPP,point_B@HPP,Line(point_A@HPP,point_O@HPP),Line(point_A@VPP,point_O@VPP),
#                          Line(point_B@HPP,point_O@HPP),Line(point_B@VPP,point_O@VPP),point_A@VPP,point_B@VPP,
#                          point_O@HPP,point_O@VPP,point_D@HPP,point_D@VPP)
#         else:
#             projections=[]

#         self._assumptions=DrawingSet(*projections)


#         self._point_A=point_A
#         self._point_B=point_B
#         self._point_O=point_O
#         self._point_D=point_D



#         self._given_data={'A':point_A,'B':point_B,'O':point_A,'D':point_D}


        
#         self._solution_step.append(self._assumptions)

        
#     def solution(self):
# #         self._line=Line(self._point_N1,self._point_N2)
#         current_obj=copy.deepcopy(self)
        
#         A=current_obj._point_A
#         B=current_obj._point_B
#         O=current_obj._point_O
#         D=current_obj._point_D
#         current_set=DrawingSet(*current_obj._solution_step[-1])

#         base_plane=Plane(A,B,O)('base')
#         line_a=Line(A,O)('a')
#         line_b=Line(B,O)('b')

#         line_D=Line(D,D@VPP)
#         intersection_ABO_D=base_plane.intersection(line_D)[0]('C')
#         C=intersection_ABO_D
#         elems=[line_a,line_b,line_D]
#         projections=[line_a@HPP,line_b@HPP,line_a@VPP,line_b@VPP,C@HPP,C@VPP]
#         current_set+=[*elems,*projections]

#         current_obj._solution_step.append(current_set)
#         current_obj.point_C = C

#         return current_obj
    
#     def get_default_data(self):

# #         point_A = [Point(x,y,z) for x in range(1,5) for y in range(1,7) for z in range(1,5) ]
# #         distance_AO = [Point(2,3,2),Point(2,4,2),Point(2,4,2),Point(3,3,4)]
        
# #         point_O = [pt + dist  for pt,dist   in  it.product(point_A,distance_AO)]
# #         distance_OB = [Point(-4,2,-4),Point(-5,3,-4),Point(-4,4,-6),Point(-5,3,-7)]
        
# #         point_B=[pt + dist  for pt,dist   in  it.product(point_O,distance_OB)]
        


# #         distance_AD = [Point(x,y,z) for x in range(3,5) for y in range(0,5) for z in range(1,4) ]

#         point_A = self.__class__.point_A
#         #distance_AO = self.__class__.distance_AO
        
#         point_O = self.__class__.point_O 
#         #distance_OB = self.__class__.distance_OB
        
#         point_B=self.__class__.point_B
        

#         #distance_AD = self.__class__.distance_AD
#         #distance_OE = self.__class__.distance_OE
#         #distance_BF = self.__class__.distance_BF
        
        
#         point_D=self.__class__.point_D
#         point_E = self.__class__.point_E
#         point_F = self.__class__.point_F


#         default_data_dict = {
#             Symbol('A'): point_A,
#             Symbol('B'): point_B,
#             Symbol('O'): point_O,

#             Symbol('D'): point_E, #it's not a mistake - selected due to convenient position
#         }
#         return default_data_dict

    
    
# class TriangleOnPlane(GeometricalCase):
    
#     point_A = [Point(x,y,z) for x in [1,1.5,2,2.5,3,3.5] for y in range(2,6) for z in [1,1.5,2,2.5,3,3.5] ]
# #     distance_AO = [Point(2,4,2),Point(2,5,2),Point(2,6,2),Point(3,4,4)]

# #     point_O = [pt + dist  for pt,dist   in  it.product(point_A,distance_AO)]
#     point_O = [Point(x,y,z) for x in range(7,11) for y in range(8,12) for z in range(8,12) ]
#     distance_OB = [Point(-4,4,-4),Point(-5,5,-4),Point(-4,5,-6),Point(-5,4,-7)]

#     point_B=[Point(x,y,z) for x in [1,1.5,2,2.5,3,3.5] for y in [13,13.5,14,14.5,15] for z in [1,1.5,2,2.5,3,3.5] ]


#     distance_AD = [Point(x,y,z) for x in range(1,4) for y in range(0,3) for z in range(1,4) ]
#     distance_OE = [Point(x,y,z) for x in range(-4,-1) for y in range(-1,3) for z in range(-4,-1) ]
#     distance_BF = [Point(x,y,z) for x in range(1,4) for y in range(-2,2) for z in range(1,4) ]

# #     point_D=[pt + dist  for pt,dist   in  it.product(point_A,distance_AD) if (pt+dist).x != 0]
# #     point_E = [pt + dist  for pt,dist   in  it.product(point_O,distance_OE) if (pt+dist).x != 0]
# #     point_F = [pt + dist  for pt,dist   in  it.product(point_B,distance_BF) if (pt+dist).x != 0]

#     point_D=[Point(x,y,z) for x in range(7,11) for y in range(2,6) for z in range(8,12) ]
#     point_E = [Point(x,y,z) for x in range(1,5) for y in range(8,12) for z in range(2,5) ]
#     point_F = [Point(x,y,z) for x in range(7,11) for y in range(13,16) for z in range(8,12) ]


#     def __init__(self,point_A=None,point_B=None,point_O=None,point_D=None,point_E=None,point_F=None,**kwargs):

#         super().__init__()

#         if point_A and point_B and point_O and point_D and point_E and point_F:
#             projections=(point_A@HPP,point_B@HPP,Line(point_A@HPP,point_O@HPP),Line(point_A@VPP,point_O@VPP),
#                          Line(point_B@HPP,point_O@HPP),Line(point_B@VPP,point_O@VPP),point_A@VPP,point_B@VPP,
#                          point_O@HPP,point_O@VPP,point_D@HPP,point_D@VPP,point_E@HPP,point_E@VPP,point_F@HPP,point_F@VPP)
#         else:
#             projections=[]

#         self._assumptions=DrawingSet(*projections)




#         self._point_A=point_A
#         self._point_B=point_B
#         self._point_O=point_O
#         self._point_D=point_D
#         self._point_E=point_E
#         self._point_F=point_F

#         self._given_data={'A':point_A,'B':point_B,'O':point_A,'D':point_D,'E':point_E,'F':point_F}
        
#         self._solution_step.append(self._assumptions)

        
#     def solution(self):
# #         self._line=Line(self._point_N1,self._point_N2)
#         current_obj=copy.deepcopy(self)
        
#         A=current_obj._point_A
#         B=current_obj._point_B
#         O=current_obj._point_O
#         D=current_obj._point_D
#         E=current_obj._point_E
#         F=current_obj._point_F
        
#         current_set=DrawingSet(*current_obj._solution_step[-1])

#         base_plane=Plane(A,B,O)('base')
#         line_a=Line(A,O)('a')
#         line_b=Line(B,O)('b')

#         line_D=Line(D,D@VPP)
#         intersection_ABO_D=base_plane.intersection(line_D)[0]('K')
#         K=intersection_ABO_D
        
#         line_E=Line(E,E@VPP)
#         intersection_ABO_E=base_plane.intersection(line_E)[0]('L')
#         L=intersection_ABO_E

#         line_F=Line(F,F@VPP)
#         intersection_ABO_F=base_plane.intersection(line_F)[0]('M')
#         M=intersection_ABO_F
        
#         elems=[line_a,line_b,line_D]
        
#         #to remove
#         C=K
        
#         projections=[line_a@HPP,line_b@HPP,line_a@VPP,line_b@VPP,C@HPP,C@VPP]
#         current_set+=[*elems,*projections]

#         current_obj._solution_step.append(current_set)
#         # to remove
#         current_obj.point_C=C
#         current_obj.point_K = K
#         current_obj.point_L = L
#         current_obj.point_M = M

#         return current_obj
    
#     def get_default_data(self):

#         point_A = self.__class__.point_A
#         #distance_AO = self.__class__.distance_AO
        
#         point_O = self.__class__.point_O 
#         #distance_OB = self.__class__.distance_OB
        
#         point_B=self.__class__.point_B
        

#         #distance_AD = self.__class__.distance_AD
#         #distance_OE = self.__class__.distance_OE
#         #distance_BF = self.__class__.distance_BF
        
        
#         point_D=self.__class__.point_D
#         point_E = self.__class__.point_E
#         point_F = self.__class__.point_F

        
#         default_data_dict = {
#             Symbol('A'): point_A,
#             Symbol('B'): point_B,
#             Symbol('O'): point_O,

#             Symbol('D'): point_D,
#             Symbol('E'): point_E,
#             Symbol('F'): point_F,
#         }
#         return default_data_dict

    
# class LineAndPlaneIntersection(GeometricalCase):
    
#     point_A = [Point(x,y,z) for x in [1,1.5,2,2.5,3,3.5] for y in [2,2.5,3,3.5,4,4.5,5] for z in [1,1.5,2,2.5,3,3.5] ]

#     point_O = [Point(x,y,z) for x in range(7,11) for y in range(8,12) for z in range(8,12) ]


#     point_B=[Point(x,y,z) for x in [1,1.5,2,2.5,3,3.5] for y in [13,13.5,14,14.5,15] for z in [1,1.5,2,2.5,3,3.5] ]


#     point_D=[Point(x,y,z) for x in [1,1.5,2,2.5,3,3.5] for y in [7,7.5,8.5,9,9.5] for z in range(8,12) ]
#     point_E = [Point(x,y,z) for x in [7,7.5,8,8.5,9] for y in [10,10.5,11,11.5,12] for z in range(2,5) ]


    

#     def __init__(self,point_A=None,point_B=None,point_O=None,point_D=None,point_E=None,**kwargs):

#         super().__init__()

#         if point_A and point_B and point_O and point_D and point_E:
#             projections=(point_A@HPP,point_B@HPP,Line(point_A@HPP,point_O@HPP),Line(point_A@VPP,point_O@VPP),
#                          Line(point_B@HPP,point_O@HPP),Line(point_B@VPP,point_O@VPP),point_A@VPP,point_B@VPP,
#                          point_O@HPP,point_O@VPP,point_D@HPP,point_D@VPP,point_E@HPP,point_E@VPP)
#         else:
#             projections=[]

#         self._assumptions=DrawingSet(*projections)




#         self._point_A=point_A
#         self._point_B=point_B
#         self._point_O=point_O
#         self._point_D=point_D
#         self._point_E=point_E


#         self._given_data={'A':point_A,'B':point_B,'O':point_A,'D':point_D,'E':point_E}
        
#         self._solution_step.append(self._assumptions)

        
#     def solution(self):
# #         self._line=Line(self._point_N1,self._point_N2)
#         current_obj=copy.deepcopy(self)
        
#         A=current_obj._point_A
#         B=current_obj._point_B
#         O=current_obj._point_O
#         D=current_obj._point_D
#         E=current_obj._point_E

        
#         current_set=DrawingSet(*current_obj._solution_step[-1])

#         base_plane=Plane(A,B,O)('base')
#         line_a=Line(A,O)('a')
#         line_b=Line(B,O)('b')

#         line_d=Line(D,E)
#         intersection_ABO_DE=base_plane.intersection(line_d)[0]('P')
#         P=intersection_ABO_DE
        

        
#         elems=[line_a,line_b,line_d,intersection_ABO_DE]

        
#         projections=[line_a@HPP,line_b@HPP,line_a@VPP,line_b@VPP,intersection_ABO_DE@HPP,intersection_ABO_DE@VPP,line_d@HPP,line_d@VPP]
#         current_set+=[*elems,*projections]

#         current_obj._solution_step.append(current_set)
#         # to remove
#         current_obj.point_P=P
#         current_obj._assumptions=DrawingSet(*elems,*projections)

#         return current_obj

#     def get_default_data(self):

#         point_A = self.__class__.point_A
#         #distance_AO = self.__class__.distance_AO
        
#         point_O = self.__class__.point_O 
#         #distance_OB = self.__class__.distance_OB
        
#         point_B=self.__class__.point_B
        

#         #distance_AD = self.__class__.distance_AD
#         #distance_OE = self.__class__.distance_OE
#         #distance_BF = self.__class__.distance_BF
        
        
#         point_D=self.__class__.point_D
#         point_E = self.__class__.point_E


        
#         default_data_dict = {
#             Symbol('A'): point_A,
#             Symbol('B'): point_B,
#             Symbol('O'): point_O,

#             Symbol('D'): point_D,
#             Symbol('E'): point_E,

#         }
#         return default_data_dict
    
    
# class TwoPlanesIntersection(GeometricalCase):
    
#     point_A = [Point(x,y,z) for x in [1,1.5,2,2.5,3,3.5] for y in [2,2.5,3,3.5,4,4.5,5] for z in [1,1.5,2,2.5,3,3.5] ]

#     point_O = [Point(x,y,z) for x in range(7,11) for y in range(8,12) for z in range(8,12) ]


#     point_B=[Point(x,y,z) for x in [1,1.5,2,2.5,3,3.5] for y in [13,13.5,14,14.5,15] for z in [1,1.5,2,2.5,3,3.5] ]



#     point_D=[Point(x,y,z) for x in [1,1.5,2,2.5,3,3.5] for y in [7,7.5,8.5,9,9.5] for z in range(8,12) ]
#     point_E = [Point(x,y,z) for x in [7,7.5,8,8.5,9] for y in [10,10.5,11,11.5,12] for z in range(2,5) ]

#     point_F = [Point(x,y,z) for x in  [1,1.5,2,2.5,3,3.5] for y in [13,13.5,14,14.5,15] for z in range(8,12) ]


#     def __init__(self,point_A=None,point_B=None,point_O=None,point_D=None,point_E=None,point_F=None,**kwargs):

#         super().__init__()

#         if point_A and point_B and point_O and point_D and point_E and point_F:
#             projections=(point_A@HPP,point_B@HPP,Line(point_A@HPP,point_O@HPP),Line(point_A@VPP,point_O@VPP),
#                          Line(point_B@HPP,point_O@HPP),Line(point_B@VPP,point_O@VPP),point_A@VPP,point_B@VPP,
#                          point_O@HPP,point_O@VPP,point_D@HPP,point_D@VPP,point_E@HPP,point_E@VPP,point_F@HPP,point_F@VPP)
#         else:
#             projections=[]

#         self._assumptions=DrawingSet(*projections)




#         self._point_A=point_A
#         self._point_B=point_B
#         self._point_O=point_O
#         self._point_D=point_D
#         self._point_E=point_E
#         self._point_F=point_F

#         self._given_data={'A':point_A,'B':point_B,'O':point_A,'D':point_D,'E':point_E,'F':point_F}
        
#         self._solution_step.append(self._assumptions)

        
#     def solution(self):
# #         self._line=Line(self._point_N1,self._point_N2)
#         current_obj=copy.deepcopy(self)
        
#         A=current_obj._point_A
#         B=current_obj._point_B
#         O=current_obj._point_O
#         D=current_obj._point_D
#         E=current_obj._point_E
#         F=current_obj._point_F
        
#         current_set=DrawingSet(*current_obj._solution_step[-1])

#         base_plane=Plane(A,B,O)('base')
#         line_a=Line(A,O)('a')
#         line_b=Line(B,O)('b')
#         line_d=Line(D,E)('d')
#         line_f=Line(F,E)('f')
#         cutting_plane=Plane(D,E,F)('cutting')
# #         intersection_line=base_plane.intersection(cutting_plane)[0]('k')
#         P=base_plane.intersection(line_d)[0]('P')
#         Q=base_plane.intersection(line_f)[0]('Q')
#         intersection_line=Line(P,Q)('k')

        
#         elems=[line_a,line_b,line_d,line_f,intersection_line,P,Q]

        
#         projections=[line_d@HPP,line_f@HPP,line_d@VPP,line_f@VPP,line_a@HPP,line_b@HPP,line_a@VPP,line_b@VPP,P@VPP,P@HPP,Q@VPP,Q@HPP,intersection_line@HPP,intersection_line@VPP]
#         current_set+=[*elems,*projections]

#         current_obj._solution_step.append(current_set)
#         # to remove
#         current_obj.point_P=P
#         current_obj.point_Q=Q
#         current_obj._assumptions=DrawingSet(*elems,*projections)

#         return current_obj

#     def get_default_data(self):

#         point_A = self.__class__.point_A
#         #distance_AO = self.__class__.distance_AO
        
#         point_O = self.__class__.point_O 
#         #distance_OB = self.__class__.distance_OB
        
#         point_B=self.__class__.point_B
        

#         #distance_AD = self.__class__.distance_AD
#         #distance_OE = self.__class__.distance_OE
#         #distance_BF = self.__class__.distance_BF
        
        
#         point_D=self.__class__.point_D
#         point_E = self.__class__.point_E
#         point_F = self.__class__.point_F

        
#         default_data_dict = {
#             Symbol('A'): point_A,
#             Symbol('B'): point_B,
#             Symbol('O'): point_O,

#             Symbol('D'): point_D,
#             Symbol('E'): point_E,
#             Symbol('F'): point_F,
#         }
#         return default_data_dict
# class HorizontalEgdePlaneAndPlaneIntersection(TwoPlanesIntersection):
    
#     point_A = [Point(x,y,z) for x in [4,4.5,5,5.5,6,6.5] for y in [2,2.5,3,3.5,4,4.5,5] for z in [1,1.5,2,2.5,3,3.5] ]

#     point_O = [Point(x,y,z) for x in range(7,11) for y in range(8,12) for z in range(8,12) ]


#     point_B=[Point(x,y,z) for x in [1,1.5,2,2.5,3,3.5] for y in [13,13.5,14,14.5,15] for z in [1,1.5,2,2.5,3,3.5] ]

#     point_D=[Point(x,y,z) for x in [1,1.5,2,2.5,3,3.5] for y in [1,1.5,2,2.5,3,3.5] for z in range(8,12) ]
#     point_E = [Point(x,y,z) for x in [7,7.5,8,8.5,9] for y in [7,7.5,8.5,9,9.5] for z in range(2,5) ]

#     point_F = [Point(x,y,z) for x in  [1,1.5,2,2.5,3,3.5] for y in [10,10.5,11,11.5,12] for z in range(8,12) ]


#     def get_default_data(self):

#         point_A = self.__class__.point_A
        
#         point_O = self.__class__.point_O 
        
#         point_B=self.__class__.point_B
        
#         point_D=self.__class__.point_D
#         point_E = self.__class__.point_E
#         point_F = self.__class__.point_F
        
#         default_data_dict = {
#             Symbol('A'): point_A,
#             Symbol('B'): point_B,
#             Symbol('O'): point_O,

#             Symbol('D'): point_D,
#             Symbol('E'): point_E,
#             Symbol('F'): point_F,
#         }
#         return default_data_dict

#     def get_random_parameters(self):

#         parameters_dict=super().get_random_parameters()



#         point_A=parameters_dict[Symbol('A')]
#         point_B=parameters_dict[Symbol('B')] 

        
#         parameters_dict[Symbol('O')]=(point_A+point_B)*0.5+Point(0,0,5)

#         return parameters_dict
    
    
# class LinePerpendicularToPlaneIntersection(GeometricalCase):
    
#     point_A = [Point(x,y,z) for x in [1,1.5,2,2.5] for y in [2,2.5,3,3.5,4,4.5,5] for z in [3,3.5,4,4.5]  ]

#     point_O = [Point(x,y,z) for x in range(7,11) for y in range(8,12) for z in range(8,12) ]


#     point_B=[Point(x,y,z) for x in [3,3.5,4,4.5] for y in [13,13.5,14,14.5,15] for z in [1,1.5,2,2.5] ]


#     point_D=[Point(x,y,z) for x in [1,1.5,2,2.5,3,3.5] for y in [7,7.5,8.5,9,9.5] for z in range(8,12) ]



    

#     def __init__(self,point_A=None,point_B=None,point_O=None,point_D=None,**kwargs):

#         super().__init__()

#         if point_A and point_B and point_O and point_D:
#             projections=(point_A@HPP,point_B@HPP,Line(point_A@HPP,point_O@HPP),Line(point_A@VPP,point_O@VPP),
#                          Line(point_B@HPP,point_O@HPP),Line(point_B@VPP,point_O@VPP),point_A@VPP,point_B@VPP,
#                          point_O@HPP,point_O@VPP,point_D@HPP,point_D@VPP)
#         else:
#             projections=[]

#         self._assumptions=DrawingSet(*projections)




#         self._point_A=point_A
#         self._point_B=point_B
#         self._point_O=point_O
#         self._point_D=point_D



#         self._given_data={'A':point_A,'B':point_B,'O':point_A,'D':point_D}
        
#         self._solution_step.append(self._assumptions)

        
#     def solution(self):
# #         self._line=Line(self._point_N1,self._point_N2)
#         current_obj=copy.deepcopy(self)
        
#         A=current_obj._point_A
#         B=current_obj._point_B
#         O=current_obj._point_O
#         D=current_obj._point_D


        
#         current_set=DrawingSet(*current_obj._solution_step[-1])

#         base_plane=Plane(A,B,O)('base')
#         line_a=Line(A,O)('a')
#         line_b=Line(B,O)('b')

#         #line_d=Line(D,D@base_plane  )
#         intersection_ABO_DE=(D@base_plane)('P')
#         P=intersection_ABO_DE
        

        
#         elems=[line_a,line_b,intersection_ABO_DE]

        
#         projections=[line_a@HPP,line_b@HPP,line_a@VPP,line_b@VPP,intersection_ABO_DE@HPP,intersection_ABO_DE@VPP]
#         current_set+=[*elems,*projections]

#         current_obj._solution_step.append(current_set)
#         # to remove
#         current_obj.point_P=P
#         current_obj._assumptions=DrawingSet(*elems,*projections)

#         return current_obj

#     def get_default_data(self):

#         point_A = self.__class__.point_A
#         #distance_AO = self.__class__.distance_AO
        
#         point_O = self.__class__.point_O 
#         #distance_OB = self.__class__.distance_OB
        
#         point_B=self.__class__.point_B
        

#         #distance_AD = self.__class__.distance_AD
#         #distance_OE = self.__class__.distance_OE
#         #distance_BF = self.__class__.distance_BF
        
        
#         point_D=self.__class__.point_D



        
#         default_data_dict = {
#             Symbol('A'): point_A,
#             Symbol('B'): point_B,
#             Symbol('O'): point_O,

#             Symbol('D'): point_D,


#         }
#         return default_data_dict


# class LinePerpendicularToHFLinesIntersection(LinePerpendicularToPlaneIntersection):
    
#     point_A = [Point(x,y,z) for x in [1,1.5,2,2.5] for y in [2,2.5,3,3.5,4,4.5,5] for z in [2,2.5,3,3.5]  ]

#     point_O = [Point(x,y,z) for x in range(7,11) for y in range(8,12) for z in [5,5.5,6,6.5,7] ]


#     point_B=[Point(x,y,z) for x in [4,4.5,5,5.5,6] for y in [13,13.5,14,14.5,15] for z in [1,1.5,2,2.5] ]


#     point_D=[Point(x,y,z) for x in range(7,10) for y in [6,6.5,7,7.5,8.5] for z in range(9,12) ]


#     def get_random_parameters(self):

#         parameters_dict=super().get_random_parameters()



#         point_A=parameters_dict[Symbol('A')]
#         point_B=parameters_dict[Symbol('B')] 
#         point_O=parameters_dict[Symbol('O')] 

        
#         parameters_dict[Symbol('O')]=Point(point_A.x,point_O.y,point_O.z)
#         parameters_dict[Symbol('B')]=Point(point_B.x,point_B.y,point_A.z)

#         return parameters_dict
    
    
# class PlanePerpendicularToLineIntersection(GeometricalCase):
    
#     point_A = [Point(x,y,z) for x in [1,1.5,2,2.5,3,3.5] for y in [2,2.5,3,3.5,4,4.5,5] for z in [1,1.5,2,2.5,3,3.5] ]




#     point_D=[Point(x,y,z) for x in [1,1.5,2,2.5,3,3.5] for y in [6,6.5,7,7.5] for z in range(8,12) ]

#     point_E = [Point(x,y,z) for x in [7,7.5,8,8.5,9] for y in [8,8.5,9,9.5] for z in range(2,5) ]
    

#     def __init__(self,point_A=None,point_D=None,point_E=None,**kwargs):

#         super().__init__()

#         if point_A and point_D and point_E:
            
#             line_DE=Line(point_D,point_E)('n')
#             projections=(point_A@HPP,point_A@VPP,point_D@HPP,point_D@VPP,point_E@HPP,point_E@VPP,line_DE@HPP,line_DE@VPP)
#         else:
#             projections=[]

#         self._assumptions=DrawingSet(*projections)




#         self._point_A=point_A
#         self._point_E=point_E
#         self._point_D=point_D



#         self._given_data={'A':point_A,'E':point_E,'D':point_D}
        
#         self._solution_step.append(self._assumptions)

        
#     def solution(self):
# #         self._line=Line(self._point_N1,self._point_N2)
#         current_obj=copy.deepcopy(self)
        
#         A=current_obj._point_A
#         E=current_obj._point_E
#         D=current_obj._point_D


        
#         current_set=DrawingSet(*current_obj._solution_step[-1])

#         base_plane=Plane(A,normal_vector=(D-E)('d').coordinates)('base')


#         #line_d=Line(D,D@base_plane  )
#         intersection_ABO_DE=(D@base_plane)('P')
#         P=intersection_ABO_DE
        

        
#         elems=[intersection_ABO_DE]

        
#         projections=[intersection_ABO_DE@HPP,intersection_ABO_DE@VPP]
#         current_set+=[*elems,*projections]

#         current_obj._solution_step.append(current_set)
#         # to remove
#         current_obj.point_P=P
#         current_obj._assumptions=DrawingSet(*elems,*projections)

#         return current_obj

#     def get_default_data(self):

#         point_A = self.__class__.point_A
        
#         point_D=self.__class__.point_D
#         point_E=self.__class__.point_E


        
#         default_data_dict = {
#             Symbol('A'): point_A,

#             Symbol('D'): point_D,
#             Symbol('E'): point_E,

#         }
#         return default_data_dict
    
    
    
# class PlanePerpendicularToPlaneIntersection(GeometricalCase):
    
#     point_A = [Point(x,y,z) for x in [1,1.5,2,2.5] for y in [2,2.5,3,3.5,4,4.5,5] for z in [3,3.5,4,4.5]  ]

#     point_O = [Point(x,y,z) for x in range(7,11) for y in range(8,12) for z in range(8,12) ]


#     point_B=[Point(x,y,z) for x in [3,3.5,4,4.5] for y in [13,13.5,14,14.5,15] for z in [1,1.5,2,2.5] ]



#     point_D=[Point(x,y,z) for x in [1,1.5,2,2.5,3,3.5] for y in [7,7.5,8.5,9,9.5] for z in range(8,12) ]
#     point_E = [Point(x,y,z) for x in  [1,1.5,2,2.5,3,3.5] for y in [13,13.5,14,14.5,15] for z in range(8,12) ]


#     def __init__(self,point_A=None,point_B=None,point_O=None,point_D=None,point_E=None,**kwargs):

#         super().__init__()

#         if point_A and point_B and point_O and point_D and point_E:
#             projections=(point_A@HPP,point_B@HPP,Line(point_A@HPP,point_O@HPP),Line(point_A@VPP,point_O@VPP),
#                          Line(point_B@HPP,point_O@HPP),Line(point_B@VPP,point_O@VPP),point_A@VPP,point_B@VPP,
#                          point_O@HPP,point_O@VPP,point_D@HPP,point_D@VPP,point_E@HPP,point_E@VPP)
#         else:
#             projections=[]

#         self._assumptions=DrawingSet(*projections)




#         self._point_A=point_A
#         self._point_B=point_B
#         self._point_O=point_O
#         self._point_D=point_D
#         self._point_E=point_E


#         self._given_data={'A':point_A,'B':point_B,'O':point_A,'D':point_D,'E':point_E}
        
#         self._solution_step.append(self._assumptions)

        
#     def solution(self):
# #         self._line=Line(self._point_N1,self._point_N2)
#         current_obj=copy.deepcopy(self)
        
#         A=current_obj._point_A
#         B=current_obj._point_B
#         O=current_obj._point_O
#         D=current_obj._point_D
#         E=current_obj._point_E

        
#         current_set=DrawingSet(*current_obj._solution_step[-1])

#         base_plane=Plane(A,B,O)('base')
#         line_a=Line(A,O)('a')
#         line_b=Line(B,O)('b')
#         line_d=Line(D,E)('d')


# #         intersection_line=base_plane.intersection(cutting_plane)[0]('k')
#         P=(D@base_plane)('P')
#         Q=(E@base_plane)('Q')
#         intersection_line=Line(P,Q)('k')

        
#         elems=[line_a,line_b,line_d,intersection_line,P,Q]

        
#         projections=[line_d@HPP,line_d@VPP,line_a@HPP,line_b@HPP,line_a@VPP,line_b@VPP,P@VPP,P@HPP,Q@VPP,Q@HPP,intersection_line@HPP,intersection_line@VPP]
#         current_set+=[*elems,*projections]

#         current_obj._solution_step.append(current_set)
#         # to remove
#         current_obj.point_P=P
#         current_obj.point_Q=Q
#         current_obj._assumptions=DrawingSet(*elems,*projections)

#         return current_obj

#     def get_default_data(self):

#         point_A = self.__class__.point_A
#         #distance_AO = self.__class__.distance_AO
        
#         point_O = self.__class__.point_O 
#         #distance_OB = self.__class__.distance_OB
        
#         point_B=self.__class__.point_B
        

#         #distance_AD = self.__class__.distance_AD
#         #distance_OE = self.__class__.distance_OE
#         #distance_BF = self.__class__.distance_BF
        
        
#         point_D=self.__class__.point_D
#         point_E = self.__class__.point_E


        
#         default_data_dict = {
#             Symbol('A'): point_A,
#             Symbol('B'): point_B,
#             Symbol('O'): point_O,

#             Symbol('D'): point_D,
#             Symbol('E'): point_E,

#         }
#         return default_data_dict
# class LineParallelToPlane(TwoPlanesIntersection):
    
#     point_A = [Point(x,y,z) for x in [4,4.5,5,5.5,6,6.5] for y in [2,2.5,3,3.5,4,4.5,5] for z in [1,1.5,2,2.5,3,3.5] ]

#     point_O = [Point(x,y,z) for x in range(7,11) for y in range(8,12) for z in range(8,12) ]


#     point_B=[Point(x,y,z) for x in [1,1.5,2,2.5,3,3.5] for y in [13,13.5,14,14.5,15] for z in [1,1.5,2,2.5,3,3.5] ]

#     point_D=[Point(x,y,z) for x in [1,1.5,2,2.5,3,3.5] for y in [1,1.5,2,2.5,3,3.5] for z in range(8,12) ]
#     point_E = [Point(x,y,z) for x in [7,7.5,8,8.5,9] for y in [7,7.5,8.5,9,9.5] for z in range(2,5) ]

#     point_F = [Point(x,y,z) for x in  [1,1.5,2,2.5,3,3.5] for y in [10,10.5,11,11.5,12] for z in range(8,12) ]

#     def solution(self):
# #         self._line=Line(self._point_N1,self._point_N2)
#         current_obj=copy.deepcopy(self)
        
#         A=current_obj._point_A
#         B=current_obj._point_B
#         O=current_obj._point_O
#         D=current_obj._point_D
#         E=current_obj._point_E
#         F=current_obj._point_F
        
#         current_set=DrawingSet(*current_obj._solution_step[-1])

#         base_plane=Plane(A,B,O)('base')
#         line_a=Line(A,O)('a')
#         line_b=Line(B,O)('b')
#         line_d=Line(D,E)('d')
#         line_f=line_d.parallel_line(F)('f')
#         edge_plane=Plane(line_f.p1,line_f.p2,line_f.p1@VPP)
#         line_q=edge_plane.intersection(base_plane)[0]('q')
# #         point_G=line_f_on_AOB.intersection(line_a)[0]
# #         point_H=line_f_on_AOB.intersection(line_b)[0]
# # #         intersection_line=base_plane.intersection(cutting_plane)[0]('k')
# #         P=base_plane.intersection(line_d)[0]('P')
# #         Q=base_plane.intersection(line_f)[0]('Q')
# #         intersection_line=Line(P,Q)('k')
        
        
#         elems=[line_a,line_b,line_d,line_f,line_q]

        
#         projections=[line_d@HPP,line_f@HPP,line_d@VPP,line_f@VPP,line_a@HPP,line_b@HPP,line_a@VPP,line_b@VPP,line_q@VPP,line_q@HPP]
#         current_set+=[*elems,*projections]

#         current_obj._solution_step.append(current_set)

#         current_obj._assumptions=DrawingSet(*elems,*projections)

#         return current_obj

#     def get_default_data(self):

#         point_A = self.__class__.point_A
        
#         point_O = self.__class__.point_O 
        
#         point_B=self.__class__.point_B
        
#         point_D=self.__class__.point_D
#         point_E = self.__class__.point_E
#         point_F = self.__class__.point_F
        
#         default_data_dict = {
#             Symbol('A'): point_A,
#             Symbol('B'): point_B,
#             Symbol('O'): point_O,

#             Symbol('D'): point_D,
#             Symbol('E'): point_E,
#             Symbol('F'): point_F,
#         }
#         return default_data_dict

# class TriangularPrism(GeometricalCase):

#     point_A = [Point(x,y,z) for x in [1,1.5,2,2.5] for y in [2,2.5,3,3.5,4,4.5,5] for z in [2,2.5,3,3.5]  ]

#     point_B=  [Point(x,y,z) for x in range(4,6) for y in range(8,12) for z in [2,2.5,3,3.5] ]
    
#     point_C = [Point(x,y,z) for x in [1,1.5,2,2.5] for y in [13,13.5,14,14.5,15] for z in [6,6.5,7] ]
    
#     point_O = [Point(x,y,z) for x in range(7,10) for y in [6,6.5,7,7.5,8.5] for z in range(6,9) ]
    
#     def __init__(self,point_A=None,point_B=None,point_C=None,point_O=None,**kwargs):

#         super().__init__()

#         if point_A and point_B and point_C and point_O:
#             projections=(point_A@HPP,point_B@HPP,point_C@HPP,point_O@HPP,point_A@VPP,point_B@VPP,point_C@VPP,point_O@VPP,
#                          #Plane(point_A@HPP,point_B@HPP,point_C@HPP),Plane(point_A@VPP,point_B@VPP,point_C@VPP),
#                         )
#         else:
#             projections=[]

#         self._assumptions=DrawingSet(*projections)

#         self._point_A=point_A
#         self._point_B=point_B
#         self._point_C=point_C
#         self._point_O=point_O
        
#         self._given_data={'A':point_A,'B':point_B,'C':point_C,'O':point_O,}
        
#         self._solution_step.append(self._assumptions)

#     def solution(self):
#         current_obj=copy.deepcopy(self)
        
#         A=current_obj._point_A
#         B=current_obj._point_B
#         C=current_obj._point_C
#         O=current_obj._point_O
        
#         current_set=DrawingSet(*current_obj._solution_step[-1])

#         plane_alpha=Plane(A,B,C)
        
        
        
#         plane_beta=Plane(O,O+(B-A),O-(C-A))
#         D=(A@plane_beta)('D')
#         E=(B@plane_beta)('E')
#         F=(C@plane_beta)('F')
#         plane_gamma=Plane(D,E,F)

#         line_ad=Line(A,D)('a')
#         line_be=Line(B,E)('b')
#         line_cf=Line(C,F)('c')

#         elems=[D,E,F,plane_alpha,plane_gamma,line_ad,line_be,line_cf]

#         projections=[line_ad@HPP,line_ad@VPP,line_be@HPP,line_be@VPP,line_cf@HPP,line_cf@VPP,
#                      D@HPP,D@VPP,E@HPP,E@VPP,F@HPP,F@VPP,]

#         current_set+=[*elems,*projections]

#         current_obj._solution_step.append(current_set)
#         current_obj.point_D=D
#         current_obj.point_E=E
#         current_obj.point_F=F
#         current_obj._assumptions+=[DrawingSet(*elems,*projections)]

#         return current_obj

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

# class TriangularPyramid(TriangularPrism):

#     point_A = [Point(x,y,z) for x in [1,1.5,2,2.5] for y in [2,2.5,3,3.5,4,4.5,5] for z in [2,2.5,3,3.5]  ]

#     point_B=  [Point(x,y,z) for x in range(4,6) for y in range(8,12) for z in [2,2.5,3,3.5] ]
    
#     point_C = [Point(x,y,z) for x in [1,1.5,2,2.5] for y in [13,13.5,14,14.5,15] for z in [6,6.5,7] ]
    
#     point_O = [Point(x,y,z) for x in range(7,10) for y in [6,6.5,7,7.5,8.5] for z in range(6,9) ]
    

    
# class TetragonalPrism(GeometricalCase):

#     point_A = [Point(x,y,z) for x in [1,1.5,2,2.5] for y in [2,2.5,3,3.5,4,4.5,5] for z in [2.5,3,3.5]  ]

#     point_B=  [Point(x,y,z) for x in range(0,2) for y in range(7,10) for z in range(4,6) ]
    
#     point_C = [Point(x,y,z) for x in [2,2.5,3,3.5] for y in [13.5,14,14.5,15.5] for z in [6.5,7,7.5] ]
    
#     point_Z=  [Point(x,y,z) for x in range(4,8) for y in range(11,13) for z in [2,2.5,3,3.5] ]
    
#     point_O = [Point(x,y,z) for x in range(7,10) for y in [6,6.5,7,7.5,8.5] for z in range(6,9) ]
    
#     def __init__(self,point_A=None,point_B=None,point_C=None,point_Z=None,point_O=None,**kwargs):

#         super().__init__()

#         if point_A and point_B and point_C and point_Z and point_O:
#             projections=(point_A@HPP,point_B@HPP,point_C@HPP,point_O@HPP,point_Z@HPP,point_A@VPP,point_B@VPP,point_C@VPP,point_O@VPP,point_Z@VPP
#                          #Plane(point_A@HPP,point_B@HPP,point_C@HPP),Plane(point_A@VPP,point_B@VPP,point_C@VPP),
#                         )
#         else:
#             projections=[]

#         self._assumptions=DrawingSet(*projections)

#         self._point_A=point_A
#         self._point_B=point_B
#         self._point_C=point_C
#         self._point_Z=point_Z
#         self._point_O=point_O
        
#         self._given_data={'A':point_A,'B':point_B,'C':point_C,'Z':point_Z,'O':point_O,}
        
#         self._solution_step.append(self._assumptions)

#     def solution(self):
#         current_obj=copy.deepcopy(self)
        
#         A=current_obj._point_A
#         B=current_obj._point_B
#         C=current_obj._point_C
#         Z=current_obj._point_Z
#         O=current_obj._point_O
        
#         current_set=DrawingSet(*current_obj._solution_step[-1])

#         plane_alpha=Plane(A,B,C)
#         line_z=Line(Z,Z@HPP)
#         D=line_z.intersection(plane_alpha)[0]('D')
        
        
#         plane_beta=Plane(O,O+(B-A),O+(C-A))
#         E=(A@plane_beta)('E')
#         F=(B@plane_beta)('F')
#         G=(C@plane_beta)('G')
#         H=(D@plane_beta)('H')
#         plane_gamma=Plane(E,F,G)

#         line_ae=Line(A,E)('a')
#         line_bf=Line(B,F)('b')
#         line_cg=Line(C,G)('c')
#         line_dh=Line(D,H)('d')
#         elems=[E,F,G,H,line_ae,line_bf,line_cg,line_dh]

#         projections=[line_ae@HPP,line_ae@VPP,line_bf@HPP,line_bf@VPP,line_cg@HPP,line_cg@VPP,line_dh@HPP,line_dh@VPP,
#                      E@HPP,E@VPP,F@HPP,F@VPP,G@HPP,G@VPP,H@HPP,H@VPP,D@HPP,D@VPP]

#         current_set+=[*elems,*projections]

#         current_obj._solution_step.append(current_set)
        
#         current_obj.horizontal_line_cross_BC = (HorizontalPlane(A) & (B^C))[0]
#         current_obj.frontal_line_cross_BC = (VerticalPlane(A) & (B^C))[0]
        
#         current_obj.point_P=(O@plane_alpha)('P')
#         current_obj.point_D=D
#         current_obj.point_E=E
#         current_obj.point_F=F
#         current_obj.point_G=G
#         current_obj.point_H=H
#         current_obj._assumptions+=[DrawingSet(*elems,*projections)]

#         return current_obj

#     def get_default_data(self):

#         point_A = self.__class__.point_A
#         point_B = self.__class__.point_B
#         point_C = self.__class__.point_C
#         point_Z = self.__class__.point_Z
#         point_O = self.__class__.point_O

#         default_data_dict = {
#             Symbol('A'): point_A,
#             Symbol('B'): point_B,
#             Symbol('C'): point_C,
#             Symbol('Z'): point_Z,
#             Symbol('O'): point_O,
#         }
#         return default_data_dict
    
# class TruncatedTetragonalPrism(GeometricalCase):

#     point_A = [Point(x,y,z) for x in [1,1.5,2,2.5] for y in [2,2.5,3,3.5,4,4.5,5] for z in [2.5,3,3.5]  ]

#     point_B=  [Point(x,y,z) for x in range(0,2) for y in range(7,10) for z in range(4,6) ]
    
#     point_C = [Point(x,y,z) for x in [2,2.5,3,3.5] for y in [13.5,14,14.5,15.5] for z in [6.5,7,7.5] ]
    
#     point_Z=  [Point(x,y,z) for x in range(4,8) for y in range(11,13) for z in [2,2.5,3,3.5] ]
    
# #     point_O = [Point(x,y,z) for x in range(7,10) for y in [6,6.5,7,7.5,8.5] for z in range(6,9) ]
    
    

    
    
#     point_M=[Point(x,y,z) for x in [1,1.5,2,2.5,3,3.5] for y in [7,7.5,8.5,9,9.5] for z in range(8,12) ]
#     point_N = [Point(x,y,z) for x in [7,7.5,8,8.5,9] for y in [10,10.5,11,11.5,12] for z in range(2,5) ]

#     point_O = [Point(x,y,z) for x in  [1,1.5,2,2.5,3,3.5] for y in [13,13.5,14,14.5,15] for z in range(8,12) ]


#     def __init__(self,point_A=None,point_B=None,point_C=None,point_Z=None,point_M=None,point_N=None,point_O=None,**kwargs):

#         super().__init__()

#         if point_A and point_B and point_O and point_C and point_Z and point_M and point_N:
#             projections=(point_A@HPP,point_B@HPP,Line(point_A@HPP,point_B@HPP),Line(point_A@VPP,point_B@VPP),
#                          Line(point_B@HPP,point_C@HPP),Line(point_B@VPP,point_C@VPP),point_A@VPP,point_B@VPP,
#                          point_C@HPP,point_C@VPP,point_M@HPP,point_M@VPP,point_N@HPP,point_N@VPP,point_O@HPP,point_O@VPP,point_Z@VPP,point_Z@HPP)
#         else:
#             projections=[]

#         self._assumptions=DrawingSet(*projections)




#         self._point_A=point_A
#         self._point_B=point_B
#         self._point_C=point_C
#         self._point_Z=point_Z
#         self._point_M=point_M
#         self._point_N=point_N
#         self._point_O=point_O

#         self._given_data={'A':point_A,'B':point_B,'C':point_C,'M':point_M,'N':point_N,'O':point_O,'Z':point_Z}
        
#         self._solution_step.append(self._assumptions)

    


#     def solution(self):
#         current_obj=copy.deepcopy(self)
        
#         A=current_obj._point_A
#         B=current_obj._point_B
#         C=current_obj._point_C
#         Z=current_obj._point_Z
#         M=current_obj._point_M
#         N=current_obj._point_N
#         O=current_obj._point_O
        
#         current_set=DrawingSet(*current_obj._solution_step[-1])

#         plane_alpha=Plane(A,B,C)
#         line_z=Line(Z,Z@HPP)
#         D=line_z.intersection(plane_alpha)[0]('D')
        
        
#         plane_beta=Plane(M,N,O)

        

#         E=(plane_alpha.perpendicular_line(A) & plane_beta)[0]('E')
#         F=(plane_alpha.perpendicular_line(B) & plane_beta)[0]('F')
#         G=(plane_alpha.perpendicular_line(C) & plane_beta)[0]('G')
#         H=(plane_alpha.perpendicular_line(D) & plane_beta)[0]('H')
        
#         plane_gamma=Plane(E,F,G)

#         line_ae=Line(A,E)('a')
#         line_bf=Line(B,F)('b')
#         line_cg=Line(C,G)('c')
#         line_dh=Line(D,H)('d')
#         plane_gamma=Plane(D,E,F)

#         current_obj.point_P=(O@plane_alpha)('P')

#         elems=[E,F,G,H,line_ae,line_bf,line_cg,line_dh]

#         projections=[line_ae@HPP,line_ae@VPP,line_bf@HPP,line_bf@VPP,line_cg@HPP,line_cg@VPP,line_dh@HPP,line_dh@VPP,
#                      E@HPP,E@VPP,F@HPP,F@VPP,G@HPP,G@VPP,H@HPP,H@VPP,D@HPP,D@VPP]

#         current_set+=[*elems,*projections]

#         current_obj.horizontal_line_cross_BC = (HorizontalPlane(A) & (B^C))[0]
#         current_obj.frontal_line_cross_BC = (VerticalPlane(A) & (B^C))[0]
        
#         current_obj.point_D=D
#         current_obj.point_E=E
#         current_obj.point_F=F
#         current_obj.point_G=G
#         current_obj.point_H=H
#         current_obj._assumptions+=[DrawingSet(*elems,*projections)]

#         return current_obj

#     def get_default_data(self):

#         point_A = self.__class__.point_A
#         point_B = self.__class__.point_B
#         point_C = self.__class__.point_C
#         point_Z = self.__class__.point_Z
#         point_O = self.__class__.point_O
#         point_M = self.__class__.point_M
#         point_N = self.__class__.point_N

#         default_data_dict = {
#             Symbol('A'): point_A,
#             Symbol('B'): point_B,
#             Symbol('C'): point_C,
#             Symbol('Z'): point_Z,
#             Symbol('M'): point_M,
#             Symbol('N'): point_N,
#             Symbol('O'): point_O,
#         }
#         return default_data_dict

# class TruncatedTetragonalPrismByEdgePlane(TruncatedTetragonalPrism):

#     point_A = [Point(x,y,z) for x in [1,1.5,2,2.5] for y in [2,2.5,3,3.5,4,4.5,5] for z in [2.5,3,3.5]  ]

#     point_B=  [Point(x,y,z) for x in range(0,2) for y in range(7,10) for z in range(4,6) ]
    
#     point_C = [Point(x,y,z) for x in [2,2.5,3,3.5] for y in [13.5,14,14.5,15.5] for z in [6.5,7,7.5] ]
    
#     point_Z=  [Point(x,y,z) for x in range(4,8) for y in range(11,13) for z in [2,2.5,3,3.5] ]
    
    

    
    
#     point_M=[Point(x,y,z) for x in [7,7.5,8,8.5,9] for y in [7,7.5,8.5,9,9.5] for z in range(7,10) ]
#     point_N = [Point(x,y,z) for x in [7,7.5,8,8.5,9] for y in [10,10.5,11,11.5,12] for z in range(2,5) ]

#     point_O = [Point(x,y,z) for x in  [7,7.5,8,8.5,9] for y in [13,13.5,14,14.5,15] for z in range(9,12) ]
    
#     def get_random_parameters(self):

#         parameters_dict=super().get_random_parameters()



#         point_M=parameters_dict[Symbol('M')]
#         point_O=parameters_dict[Symbol('O')] 

        
#         parameters_dict[Symbol('N')]=(point_M+point_O)*0.5+Point(3,0,0)

#         return parameters_dict
    
    
# class TruncatedTriangularPrism(GeometricalCase):

#     point_A = [Point(x,y,z) for x in [1,1.5,2,2.5] for y in [2,2.5,3,3.5,4,4.5,5] for z in [2,2.5,3,3.5]  ]

#     point_B=  [Point(x,y,z) for x in range(4,6) for y in range(8,12) for z in [2,2.5,3,3.5] ]
    
#     point_C = [Point(x,y,z) for x in [1,1.5,2,2.5] for y in [13,13.5,14,14.5,15] for z in [6,6.5,7] ]
    
    

    
    
#     point_M=[Point(x,y,z) for x in [1,1.5,2,2.5,3,3.5] for y in [7,7.5,8.5,9,9.5] for z in range(8,12) ]
#     point_N = [Point(x,y,z) for x in [7,7.5,8,8.5,9] for y in [10,10.5,11,11.5,12] for z in range(2,5) ]

#     point_O = [Point(x,y,z) for x in  [1,1.5,2,2.5,3,3.5] for y in [13,13.5,14,14.5,15] for z in range(8,12) ]


#     def __init__(self,point_A=None,point_B=None,point_C=None,point_M=None,point_N=None,point_O=None,**kwargs):

#         super().__init__()

#         if point_A and point_B and point_O and point_C and point_M and point_N:
#             projections=(point_A@HPP,point_B@HPP,Line(point_A@HPP,point_B@HPP),Line(point_A@VPP,point_B@VPP),
#                          Line(point_B@HPP,point_C@HPP),Line(point_B@VPP,point_C@VPP),point_A@VPP,point_B@VPP,
#                          point_C@HPP,point_C@VPP,point_M@HPP,point_M@VPP,point_N@HPP,point_N@VPP,point_O@HPP,point_O@VPP)
#         else:
#             projections=[]

#         self._assumptions=DrawingSet(*projections)




#         self._point_A=point_A
#         self._point_B=point_B
#         self._point_C=point_C
#         self._point_M=point_M
#         self._point_N=point_N
#         self._point_O=point_O

#         self._given_data={'A':point_A,'B':point_B,'C':point_C,'M':point_M,'N':point_N,'O':point_O}
        
#         self._solution_step.append(self._assumptions)

    


#     def solution(self):
#         current_obj=copy.deepcopy(self)
        
#         A=current_obj._point_A
#         B=current_obj._point_B
#         C=current_obj._point_C
        
#         M=current_obj._point_M
#         N=current_obj._point_N
#         O=current_obj._point_O
        
#         current_set=DrawingSet(*current_obj._solution_step[-1])

#         plane_alpha=Plane(A,B,C)
        
        
        
#         plane_beta=Plane(M,N,O)
#         D=(plane_alpha.perpendicular_line(A) & plane_beta)[0]('D')
#         E=(plane_alpha.perpendicular_line(B) & plane_beta)[0]('E')
#         F=(plane_alpha.perpendicular_line(C) & plane_beta)[0]('F')
#         plane_gamma=Plane(D,E,F)

#         line_ad=Line(A,D)('a')
#         line_be=Line(B,E)('b')
#         line_cf=Line(C,F)('c')

#         elems=[D,E,F,plane_alpha,plane_gamma,line_ad,line_be,line_cf]

#         projections=[line_ad@HPP,line_ad@VPP,line_be@HPP,line_be@VPP,line_cf@HPP,line_cf@VPP,
#                      D@HPP,D@VPP,E@HPP,E@VPP,F@HPP,F@VPP,]

#         current_set+=[*elems,*projections]

#         current_obj._solution_step.append(current_set)
#         current_obj.point_D=D
#         current_obj.point_E=E
#         current_obj.point_F=F
#         current_obj._assumptions+=[DrawingSet(*elems,*projections)]

#         return current_obj

#     def get_default_data(self):

#         point_A = self.__class__.point_A
#         point_B = self.__class__.point_B
#         point_C = self.__class__.point_C
#         point_O = self.__class__.point_O
#         point_M = self.__class__.point_M
#         point_N = self.__class__.point_N        

#         default_data_dict = {
#             Symbol('A'): point_A,
#             Symbol('B'): point_B,
#             Symbol('C'): point_C,
#             Symbol('M'): point_M,
#             Symbol('N'): point_N,
#             Symbol('O'): point_O,
#         }
#         return default_data_dict
    

# class TruncatedTriangularPrismByEdgePlane(TruncatedTriangularPrism):

#     point_A = [Point(x,y,z) for x in [1,1.5,2,2.5] for y in [2,2.5,3,3.5,4,4.5,5] for z in [2,2.5,3,3.5]  ]

#     point_B=  [Point(x,y,z) for x in range(4,6) for y in range(8,12) for z in [2,2.5,3,3.5] ]
    
#     point_C = [Point(x,y,z) for x in [1,1.5,2,2.5] for y in [13,13.5,14,14.5,15] for z in [6,6.5,7] ]
    
    

    
    
#     point_M=[Point(x,y,z) for x in [7,7.5,8,8.5,9] for y in [7,7.5,8.5,9,9.5] for z in range(7,10) ]
#     point_N = [Point(x,y,z) for x in [7,7.5,8,8.5,9] for y in [10,10.5,11,11.5,12] for z in range(2,5) ]

#     point_O = [Point(x,y,z) for x in  [7,7.5,8,8.5,9] for y in [13,13.5,14,14.5,15] for z in range(9,12) ]
    
#     def get_random_parameters(self):

#         parameters_dict=super().get_random_parameters()



#         point_M=parameters_dict[Symbol('M')]
#         point_O=parameters_dict[Symbol('O')] 

        
#         parameters_dict[Symbol('N')]=(point_M+point_O)*0.5+Point(3,0,0)

#         return parameters_dict

    
# class LineRotation(GeometricalCase):


#     point_A = [Point(x,y,z) for x in [1,1.5,2,2.5,3,3.5] for y in [2,2.5,3,3.5,4] for z in [1,1.5,2,2.5,3,3.5] ]

#     point_B=[Point(x,y,z) for x in [4,4.5,5,5.5,6,6.5] for y in [6.5,7,7.5,8,8.5,9] for z in [4,4.5,5,5.5,6,6.5] ]

#     def __init__(self,point_A=None,point_B=None,**kwargs):

#         super().__init__()

#         if point_A and point_B:
#             projections=(point_A@HPP,point_B@HPP,point_A@VPP,point_B@VPP)
#         else:
#             projections=[]

#         self._assumptions=DrawingSet(*projections)

#         self._point_A=point_A
#         self._point_B=point_B

#         self._given_data={'A':point_A,'B':point_B,}

#         self._solution_step.append(self._assumptions)

#     def solution(self):
#         current_obj=copy.deepcopy(self)

#         A=current_obj._point_A
#         B=current_obj._point_B

#         current_set=DrawingSet(*current_obj._solution_step[-1])

#         line_a=Line(A,B)('a')
#         S=Point(B.x,B.y,A.z)('S')
#         line_l=Line(B,S)('l')
#         epsilon=HorizontalPlane(A)
#         A_0=Point(B.x,B.y+(B@HPP).distance(A@HPP),A.z)
#         line_k=Line(B,A_0)

#         elems=[line_a,S,line_l,epsilon,A_0,line_k,]

#         projections=[line_l@HPP,line_k@HPP,line_l@VPP,line_k@VPP,line_a@HPP,line_a@VPP,S@VPP,S@HPP,A_0@VPP,A_0@HPP]
#         current_set+=[*elems,*projections]

#         current_obj._solution_step.append(current_set)
#         current_obj.point_S=S

#         current_obj.point_A_0=A_0
#         current_obj._assumptions=DrawingSet(*elems,*projections)
#         return current_obj

#     def get_default_data(self):

#         point_A = self.__class__.point_A
#         point_B = self.__class__.point_B
        
#         default_data_dict = {
#             Symbol('A'): point_A,
#             Symbol('B'): point_B,
#         }
#         return default_data_dict

# class PlaneRotation(GeometricalCase):


#     point_A = [Point(x,y,z) for x in [8,8.5,9,7.5,7] for y in [5,5.5,6,6.5] for z in   [8,8.5,7.5,7]  ]

#     point_B=[Point(x,y,z) for x in [5,5.5,6,6.5] for y in [8,8.5,9,9.5,10] for z in   [4,4.5,5,5.5] ]

#     point_C = [Point(x,y,z) for x in [1,1.5,2,2.5] for y in [2,2.5,3,3.5]  for z in [1,1.5,2,2.5] ]





#     def __init__(self,point_A=None,point_B=None,point_C=None,**kwargs):

#         super().__init__()

#         if point_A and point_B and point_C:
#             projections=(point_A@HPP,point_B@HPP,point_A@VPP,point_B@VPP,point_C@HPP,point_C@VPP,)
#         else:
#             projections=[]

#         self._assumptions=DrawingSet(*projections)

#         self._point_A=point_A
#         self._point_B=point_B
#         self._point_C=point_C

        
#         self._given_data={'A':point_A,'B':point_B,'C':point_C}
        
#         self._solution_step.append(self._assumptions)

#     def solution(self):
#         current_obj=copy.deepcopy(self)
        
#         A=current_obj._point_A
#         B=current_obj._point_B
#         C=current_obj._point_C


        
#         current_set=DrawingSet(*current_obj._solution_step[-1])

#         line_a=Line(A,B)('a')
#         line_b=Line(C,A)('b')
#         plane_alpha=Plane(A,B,C)

#         plane_beta=HorizontalPlane(C)

#         line_k = plane_alpha.intersection(plane_beta)[0]

#         elems=self._assumptions
#         projections=[]
#         point_0_dict={}
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
#             projections+=[I_o@HPP,I_o@VPP]

            
#         line_kk=Line(C,S_I)
#         #print(point_0_dict)
#         elems+=[line_a,line_b,#,E,F,G,H,line_s1,line_s2,line_s3,line_s4
#               ]

#         projections+=[line_a@HPP,line_a@VPP,line_b@HPP,line_b@VPP,line_kk@HPP,line_kk@VPP,#line_s1@HPP,line_s1@VPP,line_s2@HPP,line_s2@VPP,line_s3@HPP,line_s3@VPP,
#                      #line_s4@HPP,line_s4@VPP
#                     ]
#         current_set+=[*elems,*projections]
#         current_obj.A0=point_0_dict['A']
#         current_obj.B0=point_0_dict['B']
#         current_obj.C0=C
#         current_obj._solution_step.append(current_set)
#         current_obj._assumptions=DrawingSet(*elems,*projections)

#         return current_obj

#     def get_default_data(self):

#         point_A = self.__class__.point_A
#         point_B = self.__class__.point_B
#         point_C = self.__class__.point_C


        
#         default_data_dict = {
#             Symbol('A'): point_A,
#             Symbol('B'): point_B,
#             Symbol('C'): point_C,


#         }
#         return default_data_dict

    
# class TriangularPyramidHFLines(TriangularPyramid):
#     point_A = [Point(x,y,z) for x in [1,1.5,2,2.5] for y in [2,2.5,3,3.5,4,4.5,5] for z in [2,2.5,3,3.5]  ]

#     point_B = [Point(x,y,z) for x in range(7,11) for y in range(8,12) for z in [5,5.5,6,6.5,7] ]


#     point_C=[Point(x,y,z) for x in [4,4.5,5,5.5,6] for y in [13,13.5,14,14.5,15] for z in [1,1.5,2,2.5] ]


#     point_O=[Point(x,y,z) for x in range(9,12) for y in [6,6.5,7,7.5,8.5] for z in range(9,12) ]


#     def get_random_parameters(self):

#         parameters_dict=super().get_random_parameters()



#         point_A=parameters_dict[Symbol('A')]
#         point_B=parameters_dict[Symbol('B')] 
#         point_C=parameters_dict[Symbol('C')] 

        
#         parameters_dict[Symbol('B')]=Point(point_A.x,point_C.y,point_C.z)
#         parameters_dict[Symbol('C')]=Point(point_B.x,point_B.y,point_A.z)

#         return parameters_dict

# class EquilateralTriangleRotation(GeometricalCase):


#     point_A = [Point(x,y,z) for x in [8,8.5,9,7.5,7] for y in [5,5.5,6,6.5] for z in   [8,8.5,7.5,7]  ]

#     point_O=[Point(x,y,z) for x in [5,5.5,6,6.5] for y in [8,8.5,9,9.5,10] for z in   [4,4.5,5,5.5] ]

#     point_P = [Point(x,y,z) for x in [1,1.5,2,2.5] for y in [2,2.5,3,3.5]  for z in [1,1.5,2,2.5] ]





#     def __init__(self,point_A=None,point_P=None,point_O=None,**kwargs):

#         super().__init__()

#         if point_A and point_O and point_P:
#             projections=(point_A@HPP,point_O@HPP,point_O@VPP,point_P@VPP,point_P@HPP,point_A@VPP,)
#         else:
#             projections=[]

#         self._assumptions=DrawingSet(*projections)

#         self._point_A=point_A
#         self._point_P=point_P
#         self._point_O=point_O

        
#         self._given_data={'A':point_A,'P':point_P,'O':point_O}
        
#         self._solution_step.append(self._assumptions)

#     def solution(self):
#         current_obj=copy.deepcopy(self)
        
#         A=current_obj._point_A
#         O=current_obj._point_O
#         P=current_obj._point_P
        
#         S = (A @ (O^P))('S') #'Srodek' podstawy
        
#         dirPS = P-S
#         dirOS = O-S
#         triangle_height = A.distance(S)
#         triangle_side =  triangle_height / ((3**(1/2))/2)
        
#         B = (S + dirPS/(P.distance(S))*(triangle_side/2))('B')
#         C = (S - dirPS/(P.distance(S))*(triangle_side/2))('C')


        
#         current_set=DrawingSet(*current_obj._solution_step[-1])

#         line_a=Line(A,B)('a')
#         line_b=Line(C,A)('b')
#         plane_alpha=Plane(A,O,P)

#         plane_beta=HorizontalPlane(P)

#         line_k = plane_alpha.intersection(plane_beta)[0]

#         elems=self._assumptions
#         projections=[]
#         point_0_dict={}
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
#             projections+=[I_o@HPP,I_o@VPP]

            
#         line_kk=Line(P,S_I)('k')
        
#         current_obj.A0=point_0_dict['A']
#         current_obj.B0=point_0_dict['B']
#         current_obj.C0=point_0_dict['C']
        
        
#         #print(point_0_dict)
#         elems+=[line_a,line_b,#,E,F,G,H,line_s1,line_s2,line_s3,line_s4
#               ]

#         projections+=[current_obj.A0@HPP,current_obj.A0@VPP,current_obj.B0@HPP,current_obj.B0@VPP,
#                       current_obj.C0@HPP,current_obj.C0@VPP,B@HPP,B@VPP,C@HPP,C@VPP,line_a@HPP,line_a@VPP,line_b@HPP,line_b@VPP,
#                       line_kk@HPP,line_kk@VPP,#line_s1@HPP,line_s1@VPP,line_s2@HPP,line_s2@VPP,line_s3@HPP,line_s3@VPP,
#                      #line_s4@HPP,line_s4@VPP
#                     ]
#         current_set+=[*elems,*projections]

#         current_obj._solution_step.append(current_set)
#         current_obj._assumptions=DrawingSet(*elems,*projections)
#         current_obj._point_B=B
#         current_obj._point_C=C
#         return current_obj

#     def get_default_data(self):

#         point_A = self.__class__.point_A
#         point_O = self.__class__.point_O
#         point_P = self.__class__.point_P


        
#         default_data_dict = {
#             Symbol('A'): point_A,
#             Symbol('P'): point_P,
#             Symbol('O'): point_O,



#         }
#         return default_data_dict
    
# class SquareRotation(GeometricalCase):


#     point_A = [Point(x,y,z) for x in [8,8.5,9,7.5,7] for y in [5,5.5,6,6.5] for z in   [8,8.5,7.5,7]  ]

#     point_O=[Point(x,y,z) for x in [5,5.5,6,6.5] for y in [8,8.5,9,9.5,10] for z in   [4,4.5,5,5.5] ]

#     point_P = [Point(x,y,z) for x in [1,1.5,2,2.5] for y in [2,2.5,3,3.5]  for z in [1,1.5,2,2.5] ]





#     def __init__(self,point_A=None,point_P=None,point_O=None,**kwargs):

#         super().__init__()

#         if point_A and point_O and point_P:
#             projections=(point_A@HPP,point_O@HPP,point_O@VPP,point_P@VPP,point_P@HPP,point_A@VPP,)
#         else:
#             projections=[]

#         self._assumptions=DrawingSet(*projections)

#         self._point_A=point_A
#         self._point_P=point_P
#         self._point_O=point_O

        
#         self._given_data={'A':point_A,'P':point_P,'O':point_O}
        
#         self._solution_step.append(self._assumptions)

#     def solution(self):
#         current_obj=copy.deepcopy(self)
        
#         A=current_obj._point_A
#         O=current_obj._point_O
#         P=current_obj._point_P
        
#         S = (A @ (O^P))('S') #'Srodek' podstawy
        
#         dirPS = P-S
#         dirOS = O-S
#         dirAS = S-A
#         square_diagonal = 2*A.distance(S)
#         #square_side =  square_diagonal / (((3)**(1/2))/2)
#         print(square_diagonal)
#         B = (S + dirPS/(P.distance(S))*(square_diagonal/2))('B')
#         D = (S - dirPS/(P.distance(S))*(square_diagonal/2))('D')
#         C = (A + 2*dirAS)('C')
# #         line_AD=A^D
# #         line_AB=A^B
# #         line_BC=line_AD.parallel_line(P)
# #         line_AS=Line(A,S)
# #         C=line_BC.intersection(line_AS)[0]


        
#         current_set=DrawingSet(*current_obj._solution_step[-1])

#         line_a=Line(A,B)('a')
#         line_b=Line(B,C)('b')
#         line_c=Line(C,D)('c')
#         line_d=Line(D,A)('d')
#         plane_alpha=Plane(A,O,P)

#         plane_beta=HorizontalPlane(P)

#         line_k = plane_alpha.intersection(plane_beta)[0]

#         elems=self._assumptions
#         projections=[]
#         point_0_dict={}
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
        
#         current_obj.A0=point_0_dict['A']
#         current_obj.B0=point_0_dict['B']
#         current_obj.C0=point_0_dict['C']
#         current_obj.D0=point_0_dict['D']
        
#         #print(point_0_dict)
#         elems+=[line_a,line_b,#,E,F,G,H,line_s1,line_s2,line_s3,line_s4
#               ]

#         projections+=[current_obj.D0@HPP,current_obj.D0@VPP,D@HPP,D@VPP,
#             current_obj.A0@HPP,current_obj.A0@VPP,current_obj.B0@HPP,current_obj.B0@VPP,
#                       current_obj.C0@HPP,current_obj.C0@VPP,B@HPP,B@VPP,C@HPP,C@VPP,line_a@HPP,line_a@VPP,line_b@HPP,line_b@VPP,
#                       line_kk@HPP,line_kk@VPP,#line_s1@HPP,line_s1@VPP,line_s2@HPP,line_s2@VPP,line_s3@HPP,line_s3@VPP,
#                      #line_s4@HPP,line_s4@VPP
#                     ]
#         current_set+=[*elems,*projections]

#         current_obj._solution_step.append(current_set)
#         current_obj._assumptions=DrawingSet(*elems,*projections)
#         current_obj._point_B=B
#         current_obj._point_C=C
#         current_obj._point_D=D
#         return current_obj

#     def get_default_data(self):

#         point_A = self.__class__.point_A
#         point_O = self.__class__.point_O
#         point_P = self.__class__.point_P


        
#         default_data_dict = {
#             Symbol('A'): point_A,
#             Symbol('P'): point_P,
#             Symbol('O'): point_O,



#         }
#         return default_data_dict
    
# class IsoscelesRightTriangleRotation(GeometricalCase):


#     point_A = [Point(x,y,z) for x in [3,3.5] for y in [8,8.5,9] for z in   [6,7]  ]

#     point_O=[Point(x,y,z) for x in  [6,7] for y in [11,11.5,12] for z in   [2.5,3,3.5] ]

#     point_P = [Point(x,y,z) for x in [1,1.5,2] for y in [3,3.5]  for z in [1,1.5,2] ]


    

#     def __init__(self,point_A=None,point_P=None,point_O=None,**kwargs):

#         super().__init__()

#         if point_A and point_O and point_P:
#             projections=(point_A@HPP,point_O@HPP,point_O@VPP,point_P@VPP,point_P@HPP,point_A@VPP)
#         else:
#             projections=[]

#         self._assumptions=DrawingSet(*projections)

#         self._point_A=point_A
#         self._point_P=point_P
#         self._point_O=point_O


        
#         self._given_data={'A':point_A,'P':point_P,'O':point_O}
        
#         self._solution_step.append(self._assumptions)

#     def solution(self):
#         current_obj=copy.deepcopy(self)
        
#         A=current_obj._point_A
#         O=current_obj._point_O
#         P=current_obj._point_P

        
#         S = (A @ (O^P))('S') #'Srodek' podstawy
        
#         dirPS = P-S
#         dirOS = O-S
#         triangle_height = A.distance(S)
#         #triangle_side =  triangle_height / ((3**(1/2))/2)
        
#         B = (S + dirPS/(P.distance(S))*(triangle_height))('B')
#         C = (S - dirPS/(P.distance(S))*(triangle_height))('C')


        
#         current_set=DrawingSet(*current_obj._solution_step[-1])

#         line_a=Line(A,B)('a')
#         line_b=Line(C,A)('b')
#         plane_alpha=Plane(A,O,P)

#         plane_beta=HorizontalPlane(P)

#         line_k = plane_alpha.intersection(plane_beta)[0]

#         elems=self._assumptions
#         projections=[]
#         point_0_dict={}
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
#             projections+=[I_o@HPP,I_o@VPP]

            
#         line_kk=Line(P,S_I)('k')
        
#         current_obj.A0=point_0_dict['A']
#         current_obj.B0=point_0_dict['B']
#         current_obj.C0=point_0_dict['C']
        
        
     
        
#         #print(point_0_dict)
#         elems+=[line_a,line_b,#,E,F,G,H,line_s1,line_s2,line_s3,line_s4
#               ]

#         projections+=[current_obj.A0@HPP,current_obj.A0@VPP,current_obj.B0@HPP,current_obj.B0@VPP,
#                       current_obj.C0@HPP,current_obj.C0@VPP,B@HPP,B@VPP,C@HPP,C@VPP,line_a@HPP,line_a@VPP,line_b@HPP,line_b@VPP,
#                       line_kk@HPP,line_kk@VPP,#line_s1@HPP,line_s1@VPP,line_s2@HPP,line_s2@VPP,line_s3@HPP,line_s3@VPP,
#                      #line_s4@HPP,line_s4@VPP
#                     ]
#         current_set+=[*elems,*projections]

#         current_obj._solution_step.append(current_set)
#         current_obj._assumptions=DrawingSet(*elems,*projections)
#         current_obj._point_B=B
#         current_obj._point_C=C

#         return current_obj

#     def get_default_data(self):

#         point_A = self.__class__.point_A
#         point_O = self.__class__.point_O
#         point_P = self.__class__.point_P


        
#         default_data_dict = {
#             Symbol('A'): point_A,
#             Symbol('P'): point_P,
#             Symbol('O'): point_O,

            



#         }
#         return default_data_dict

    
# class IsoscelesRightTrianglePrism(GeometricalCase):

#     #quite good data
#     #point_A = [Point(x,y,z) for x in [4,5.5,5] for y in [5,5.5,6] for z in   [5.5,6,6.5]  ]

#     #point_O=[Point(x,y,z) for x in [3,3.5] for y in [8,8.5,9] for z in   [3,3.5,4] ]

#     #point_P = [Point(x,y,z) for x in [6,6.5,7] for y in [3,3.5]  for z in [1,1.5,2] ]

#     #point_H = [Point(x,y,z) for x in range(9,11) for y in [3,3.5] for z in range(9,11) ]

#     # new set
#     point_A = [Point(x,y,z) for x in [3,3.5] for y in [8,8.5,9] for z in   [6,7]  ]

#     point_O=[Point(x,y,z) for x in  [6,7] for y in [11,11.5,12] for z in   [2.5,3,3.5] ]

#     point_P = [Point(x,y,z) for x in [1,1.5,2] for y in [3,3.5]  for z in [1,1.5,2] ]

#     point_H = [Point(x,y,z) for x in range(7,9) for y in [3,3.5] for z in range(9,11) ]
    

#     def __init__(self,point_A=None,point_P=None,point_O=None,point_H=None,**kwargs):

#         super().__init__()
#         self._solution_step=[]
#         self._solution3d_step=[]

#         if point_A and point_O and point_P and point_H:
#             projections=(point_A@HPP,point_O@HPP,point_O@VPP,point_P@VPP,point_P@HPP,point_A@VPP,point_H@VPP,point_H@HPP)
            
#         else:
#             projections=[]

#         self._assumptions=DrawingSet(*projections)('Assumptions')
#         self._assumptions3d=DrawingSet(point_A,point_O,point_P,point_H)('Assumptions')
        

#         self._point_A=point_A
#         self._point_P=point_P
#         self._point_O=point_O
#         self._point_H=point_H

        
#         self._given_data={'A':point_A,'P':point_P,'O':point_O,'H':point_H}
        
#         self._solution_step.append(self._assumptions)
#         self._solution3d_step.append(self._assumptions3d)

#     def solution(self):
#         current_obj=copy.deepcopy(self)
        
#         A=current_obj._point_A
#         O=current_obj._point_O
#         P=current_obj._point_P
#         H=current_obj._point_H
        
#         S = (A @ (O^P))('S') #'Srodek' podstawy
        
#         dirPS = P-S
#         dirOS = O-S
#         triangle_height = A.distance(S)
#         #triangle_side =  triangle_height / ((3**(1/2))/2)
        
#         B = (S + dirPS/(P.distance(S))*(triangle_height))('B')
#         C = (S - dirPS/(P.distance(S))*(triangle_height))('C')


        
#         current_set=DrawingSet(*current_obj._solution_step[-1])

#         line_a=Line(A,B)('a')
#         line_b=Line(C,A)('b')
#         plane_alpha=Plane(A,O,P)

#         plane_beta=HorizontalPlane(P)
        
        

#         line_k = plane_alpha.intersection(plane_beta)[0]('a')
        
        
#         point_P1 = plane_beta.intersection(A^O)[0]('1')
#         line_kk = (P^point_P1)('a')
        
        
#         #current_step3d=copy.deepcopy(current_obj._solution3d_step[-1])+[(A^point_P1)('AO'),point_P1,(P^point_P1)('a')]
#         current_step3d=[(A^point_P1)('AO'),point_P1,(P^point_P1)('a')]
        
        
        
#         current_obj._solution3d_step.append(DrawingSet(*current_step3d)('Step 1 - axis of rotation'))
#         current_obj._solution_step.append(DrawingSet(*([obj@HPP for obj  in current_step3d] + [obj@VPP for obj  in current_step3d])   )('Step 1 - axis of rotation'))


#         elems=self._assumptions
#         projections=[]
#         point_0_dict={}
#         eps_dict={}
        
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

            
# #         line_kk=Line(P,S_I)('k')
        
#         current_obj.A0=point_0_dict['A']
#         current_obj.B0=point_0_dict['B']
#         current_obj.C0=point_0_dict['C']
#         current_obj.O0=point_0_dict['O']
        
#         A0= current_obj.A0
#         O0= current_obj.O0


#         #current_step3d=copy.deepcopy(current_obj._solution3d_step[-1])+[eps_dict['A'],eps_dict['O']]
#         current_step3d=[eps_dict['A'],eps_dict['O']]
        
        
        
#         current_obj._solution3d_step.append(DrawingSet(*current_step3d)('Step 2 - planes of rotation for A and O'))
#         current_obj._solution_step.append(DrawingSet(*([obj@HPP for obj  in current_step3d] + [obj@VPP for obj  in current_step3d])   )('Step 2 - planes of rotation for A and O'))
        
        
#         #current_step3d=copy.deepcopy(current_obj._solution3d_step[-1])+[A0,O0]
#         current_step3d=[A0,O0]
        
#         current_obj._solution3d_step.append(DrawingSet(*current_step3d)('Step 3 - rotated A0 and O0'))
#         current_obj._solution_step.append(DrawingSet(*([obj@HPP for obj  in current_step3d] + [obj@VPP for obj  in current_step3d])   )('Step 3 - rotated A0 and O0'))
        
#         current_step3d=[(P^O0)('PO0')]
#         #current_step3d=copy.deepcopy(current_obj._solution3d_step[-1])+[(P^O0)('PO0')]
        
#         current_obj._solution3d_step.append(DrawingSet(*current_step3d)('Step 4 - P0O0 line'))
#         current_obj._solution_step.append(DrawingSet(*([obj@HPP for obj  in current_step3d] + [obj@VPP for obj  in current_step3d])   )('Step 4 - P0O0 line'))
        
#         B0= current_obj.B0
#         C0= current_obj.C0
        
        
#         #current_step3d=copy.deepcopy(current_obj._solution3d_step[-1])+[B0,C0]
#         current_step3d=[B0,C0]
        
#         current_obj._solution3d_step.append(DrawingSet(*current_step3d)('Step 5 - triangle vertices B0 and C0'))
#         current_obj._solution_step.append(DrawingSet(*([obj@HPP for obj  in current_step3d] + [obj@VPP for obj  in current_step3d])   )('Step 5 - triangle vertices B0 and C0'))
        
        
#         #current_step3d=copy.deepcopy(current_obj._solution3d_step[-1])+[eps_dict['B'],eps_dict['C']]
#         current_step3d=[eps_dict['B'],eps_dict['C']]
        
#         current_obj._solution3d_step.append(DrawingSet(*current_step3d)('Step 6 - planes of rotation for B and C'))
#         current_obj._solution_step.append(DrawingSet(*([obj@HPP for obj  in current_step3d] + [obj@VPP for obj  in current_step3d])   )('Step 6 - planes of rotation for B and C'))
        
        
#         #current_step3d=copy.deepcopy(current_obj._solution3d_step[-1])+[C,B]
#         current_step3d=[C,B]
        
#         current_obj._solution3d_step.append(DrawingSet(*current_step3d)('Step 7 - triangle vertices B and C'))
#         current_obj._solution_step.append(DrawingSet(*([obj@HPP for obj  in current_step3d] + [obj@VPP for obj  in current_step3d])   )('Step 7 - triangle vertices B and C'))
        
#         plane_beta=Plane(H,H+(A-P),H-(O-P))
        
#         #current_step3d=copy.deepcopy(current_obj._solution3d_step[-1])+[((H+(A-P))^H)('e'),(H+(O-P)^H)('f')]
#         current_step3d=[((H+(A-P))^H)('e'),(H+(O-P)^H)('f')]
        
#         current_obj._solution3d_step.append(DrawingSet(*current_step3d)('Step 8 - parallel plane'))
#         current_obj._solution_step.append(DrawingSet(*([obj@HPP for obj  in current_step3d] + [obj@VPP for obj  in current_step3d])   )('Step 8 - parallel plane'))
        
        
        
        
#         D=(A@plane_beta)('D')
#         E=(B@plane_beta)('E')
#         F=(C@plane_beta)('F')


#         #current_step3d=copy.deepcopy(current_obj._solution3d_step[-1])+[(B^E)('n')]
#         current_step3d=[(B^E)('n')]
        
#         current_obj._solution3d_step.append(DrawingSet(*current_step3d)('Step 9 - perpendicular line (prism height)'))
#         current_obj._solution_step.append(DrawingSet(*([obj@HPP for obj  in current_step3d] + [obj@VPP for obj  in current_step3d])   )('Step 9 - perpendicular line (prism height)'))
        
        
#         #current_step3d=copy.deepcopy(current_obj._solution3d_step[-1])+[D,E,F]
#         current_step3d=[D,E,F]

#         current_obj._solution3d_step.append(DrawingSet(*current_step3d)('Step 10 - prims vertices'))
#         current_obj._solution_step.append(DrawingSet(*([obj@HPP for obj  in current_step3d] + [obj@VPP for obj  in current_step3d])   )('Step 10 - prims vertices'))
        
#         line_ad=Line(A,D)('a')
#         line_be=Line(B,E)('b')
#         line_cf=Line(C,F)('c')
        
#         #current_step3d=copy.deepcopy(current_obj._solution3d_step[-1])+[line_ad,line_be,line_cf,(A^B)('_'),(B^C)('_'),(A^C)('_'), (D^E)('_'),(E^F)('_'),(F^D)('_')]
#         current_step3d=[line_ad,line_be,line_cf,(A^B)('_'),(B^C)('_'),(A^C)('_'), (D^E)('_'),(E^F)('_'),(F^D)('_')]
        
#         current_obj._solution3d_step.append(DrawingSet(*current_step3d)('Step 11 - solid'))
#         current_obj._solution_step.append(DrawingSet(*([obj@HPP for obj  in current_step3d] + [obj@VPP for obj  in current_step3d])   )('Step 11 - solid'))
        

#         elems+=[D,E,F,plane_alpha,line_ad,line_be,line_cf]

#         projections+=[line_ad@HPP,line_ad@VPP,line_be@HPP,line_be@VPP,line_cf@HPP,line_cf@VPP,
#                      D@HPP,D@VPP,E@HPP,E@VPP,F@HPP,F@VPP,]
        
        
#         #print(point_0_dict)
#         elems+=[line_a,line_b,#,E,F,G,H,line_s1,line_s2,line_s3,line_s4
#               ]

#         projections+=[current_obj.A0@HPP,current_obj.A0@VPP,current_obj.B0@HPP,current_obj.B0@VPP,
#                       current_obj.C0@HPP,current_obj.C0@VPP,B@HPP,B@VPP,C@HPP,C@VPP,line_a@HPP,line_a@VPP,line_b@HPP,line_b@VPP,
#                       line_kk@HPP,line_kk@VPP,#line_s1@HPP,line_s1@VPP,line_s2@HPP,line_s2@VPP,line_s3@HPP,line_s3@VPP,
#                      #line_s4@HPP,line_s4@VPP
#                     ]
#         current_set+=[*elems,*projections]

#         current_obj._solution_step.append(current_set)
#         current_obj._assumptions=DrawingSet(*elems,*projections)
#         current_obj._point_B=B
#         current_obj._point_C=C
#         current_obj.point_D=D
#         current_obj.point_E=E
#         current_obj.point_F=F

#         return current_obj

#     def present_solution(self):
        
#         doc_model = Document(f'{self.__class__.__name__} solution')

#         doc_model.packages.append(Package('booktabs'))
#         doc_model.packages.append(Package('float'))
#         doc_model.packages.append(Package('standalone'))
#         doc_model.packages.append(Package('siunitx'))


#         #ReportText.set_container(doc_model)
#         #ReportText.set_directory('./SDAresults')

#         for no,step3d in enumerate(self._solution3d_step):
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
#         point_O = self.__class__.point_O
#         point_P = self.__class__.point_P
#         point_H = self.__class__.point_H

        
#         default_data_dict = {
#             Symbol('A'): point_A,
#             Symbol('P'): point_P,
#             Symbol('O'): point_O,
#             Symbol('H'): point_H,
            



#         }
#         return default_data_dict

# class SquarePrism(GeometricalCase):


#     point_A = [Point(x,y,z) for x in [3,3.5] for y in [8,8.5,9] for z in   [6,7]  ]

#     point_O=[Point(x,y,z) for x in  [6,7] for y in [11,11.5,12] for z in   [2.5,3,3.5] ]

#     point_P = [Point(x,y,z) for x in [1,1.5,2] for y in [3,3.5]  for z in [1,1.5,2] ]

#     point_K = [Point(x,y,z) for x in range(7,9) for y in [3,3.5] for z in range(9,11) ]
    

#     def __init__(self,point_A=None,point_P=None,point_O=None,point_K=None,**kwargs):

#         super().__init__()

#         if point_A and point_O and point_P and point_K:
#             projections=(point_A@HPP,point_O@HPP,point_O@VPP,point_P@VPP,point_P@HPP,point_A@VPP,point_K@VPP,point_K@HPP)
#         else:
#             projections=[]

#         self._assumptions=DrawingSet(*projections)

#         self._point_A=point_A
#         self._point_P=point_P
#         self._point_O=point_O
#         self._point_K=point_K

        
#         self._given_data={'A':point_A,'P':point_P,'O':point_O,'K':point_K}
        
#         self._solution_step.append(self._assumptions)

#     def solution(self):
#         current_obj=copy.deepcopy(self)
        
#         A=current_obj._point_A
#         O=current_obj._point_O
#         P=current_obj._point_P
#         K=current_obj._point_K
#         S = (A @ (O^P))('S') #'Srodek' podstawy
        
#         dirPS = P-S
#         dirOS = O-S
#         dirAS = S-A
#         square_diagonal = 2*A.distance(S)
#         #square_side =  square_diagonal / (((3)**(1/2))/2)
#         print(square_diagonal)
#         B = (S + dirPS/(P.distance(S))*(square_diagonal/2))('B')
#         D = (S - dirPS/(P.distance(S))*(square_diagonal/2))('D')
#         C = (A + 2*dirAS)('C')
# #         line_AD=A^D
# #         line_AB=A^B
# #         line_BC=line_AD.parallel_line(P)
# #         line_AS=Line(A,S)
# #         C=line_BC.intersection(line_AS)[0]


        
#         current_set=DrawingSet(*current_obj._solution_step[-1])

#         line_a=Line(A,B)('a')
#         line_b=Line(B,C)('b')
#         line_c=Line(C,D)('c')
#         line_d=Line(D,A)('d')
#         plane_alpha=Plane(A,O,P)

#         plane_beta=HorizontalPlane(P)

#         line_k = plane_alpha.intersection(plane_beta)[0]

#         elems=self._assumptions
#         projections=[]
#         point_0_dict={}
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
        
#         current_obj.A0=point_0_dict['A']
#         current_obj.B0=point_0_dict['B']
#         current_obj.C0=point_0_dict['C']
#         current_obj.D0=point_0_dict['D']
        
        
#         #plane_beta=Plane(H,H+(B-A),H-(C-A))
#         plane_beta=Plane(K,K+(A-P),K-(O-P))
#         E=(A@plane_beta)('E')
#         F=(B@plane_beta)('F')
#         G=(C@plane_beta)('G')
#         H=(D@plane_beta)('H')

#         line_ae=Line(A,E)('a')
#         line_bf=Line(B,F)('b')
#         line_cg=Line(C,G)('c')
#         line_dh=Line(D,H)('d')
#         elems+=[E,F,G,H,plane_alpha,line_ae,line_bf,line_cg,line_dh]

#         projections+=[line_ae@HPP,line_ae@VPP,line_bf@HPP,line_bf@VPP,line_cg@HPP,line_cg@VPP,line_dh@HPP,line_dh@VPP,
#                      E@HPP,E@VPP,F@HPP,F@VPP,G@HPP,G@VPP,H@HPP,H@VPP]
        
        
#         #print(point_0_dict)
#         elems+=[line_a,line_b,#,E,F,G,H,line_s1,line_s2,line_s3,line_s4
#               ]

#         projections+=[current_obj.A0@HPP,current_obj.A0@VPP,current_obj.B0@HPP,current_obj.B0@VPP,
#                       current_obj.C0@HPP,current_obj.C0@VPP,current_obj.D0@HPP,current_obj.D0@VPP,B@HPP,B@VPP,C@HPP,C@VPP,D@HPP,D@VPP,line_a@HPP,line_a@VPP,line_b@HPP,line_b@VPP,line_c@HPP,line_c@VPP,line_d@HPP,line_d@VPP,
#                       line_kk@HPP,line_kk@VPP,#line_s1@HPP,line_s1@VPP,line_s2@HPP,line_s2@VPP,line_s3@HPP,line_s3@VPP,
#                      #line_s4@HPP,line_s4@VPP
#                     ]
#         current_set+=[*elems,*projections]

#         current_obj._solution_step.append(current_set)
#         current_obj._assumptions=DrawingSet(*elems,*projections)
#         current_obj._point_B=B
#         current_obj._point_C=C
#         current_obj._point_D=D
#         current_obj.point_E=E
#         current_obj.point_F=F
#         current_obj.point_G=G
#         current_obj.point_H=H
#         return current_obj

#     def get_default_data(self):

#         point_A = self.__class__.point_A
#         point_O = self.__class__.point_O
#         point_P = self.__class__.point_P
#         point_K = self.__class__.point_K

        
#         default_data_dict = {
#             Symbol('A'): point_A,
#             Symbol('P'): point_P,
#             Symbol('O'): point_O,
#             Symbol('K'): point_K,
            



#         }
#         return default_data_dict
    
# class SquarePyramid(GeometricalCase):


#     point_A = [Point(x,y,z) for x in [3,3.5] for y in [8,8.5,9] for z in   [6,7]  ]

#     point_O=[Point(x,y,z) for x in  [6,7] for y in [11,11.5,12] for z in   [2.5,3,3.5] ]

#     point_P = [Point(x,y,z) for x in [1,1.5,2] for y in [3,3.5]  for z in [1,1.5,2] ]

#     point_H = [Point(x,y,z) for x in range(7,9) for y in [3,3.5] for z in range(9,11) ]
    

#     def __init__(self,point_A=None,point_P=None,point_O=None,point_H=None,**kwargs):

#         super().__init__()

#         if point_A and point_O and point_P and point_H:
#             projections=(point_A@HPP,point_O@HPP,point_O@VPP,point_P@VPP,point_P@HPP,point_A@VPP,point_H@VPP,point_H@HPP)
#         else:
#             projections=[]

#         self._assumptions=DrawingSet(*projections)

#         self._point_A=point_A
#         self._point_P=point_P
#         self._point_O=point_O
#         self._point_H=point_H

        
#         self._given_data={'A':point_A,'P':point_P,'O':point_O,'H':point_H}
        
#         self._solution_step.append(self._assumptions)

#     def solution(self):
#         current_obj=copy.deepcopy(self)
        
#         A=current_obj._point_A
#         O=current_obj._point_O
#         P=current_obj._point_P
#         H=current_obj._point_H
        
#         S = (A @ (O^P))('S') #'Srodek' podstawy
        
#         dirPS = P-S
#         dirOS = O-S
#         dirAS = S-A
#         square_diagonal = 2*A.distance(S)
#         #square_side =  square_diagonal / (((3)**(1/2))/2)
#         print(square_diagonal)
#         B = (S + dirPS/(P.distance(S))*(square_diagonal/2))('B')
#         D = (S - dirPS/(P.distance(S))*(square_diagonal/2))('D')
#         C = (A + 2*dirAS)('C')
# #         line_AD=A^D
# #         line_AB=A^B
# #         line_BC=line_AD.parallel_line(P)
# #         line_AS=Line(A,S)
# #         C=line_BC.intersection(line_AS)[0]


        
#         current_set=DrawingSet(*current_obj._solution_step[-1])

#         line_a=Line(A,B)('a')
#         line_b=Line(B,C)('b')
#         line_c=Line(C,D)('c')
#         line_d=Line(D,A)('d')
#         plane_alpha=Plane(A,O,P)

#         plane_beta=HorizontalPlane(P)

#         line_k = plane_alpha.intersection(plane_beta)[0]

#         elems=self._assumptions
#         projections=[]
#         point_0_dict={}
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
        
#         current_obj.A0=point_0_dict['A']
#         current_obj.B0=point_0_dict['B']
#         current_obj.C0=point_0_dict['C']
#         current_obj.D0=point_0_dict['D']
        
        
#         #plane_beta=Plane(H,H+(B-A),H-(C-A))
#         plane_beta=Plane(H,H+(A-P),H-(O-P))
#         E=(S@plane_beta)('E')


#         line_ae=Line(S,E)('a')

#         elems+=[E,plane_alpha,line_ae]

#         projections+=[line_ae@HPP,line_ae@VPP,
#                      E@HPP,E@VPP]
        
        
#         #print(point_0_dict)
#         elems+=[line_a,line_b,#,E,F,G,H,line_s1,line_s2,line_s3,line_s4
#               ]

#         projections+=[current_obj.A0@HPP,current_obj.A0@VPP,current_obj.B0@HPP,current_obj.B0@VPP,
#                       current_obj.C0@HPP,current_obj.C0@VPP,current_obj.D0@HPP,current_obj.D0@VPP,B@HPP,B@VPP,C@HPP,C@VPP,D@HPP,D@VPP,line_a@HPP,line_a@VPP,
#                       line_kk@HPP,line_kk@VPP,#line_s1@HPP,line_s1@VPP,line_s2@HPP,line_s2@VPP,line_s3@HPP,line_s3@VPP,
#                      #line_s4@HPP,line_s4@VPP
#                     ]
#         current_set+=[*elems,*projections]

#         current_obj._solution_step.append(current_set)
#         current_obj._assumptions=DrawingSet(*elems,*projections)
#         current_obj._point_B=B
#         current_obj._point_C=C
#         current_obj._point_D=D
#         current_obj.point_E=E
#         return current_obj

#     def get_default_data(self):

#         point_A = self.__class__.point_A
#         point_O = self.__class__.point_O
#         point_P = self.__class__.point_P
#         point_H = self.__class__.point_H

        
#         default_data_dict = {
#             Symbol('A'): point_A,
#             Symbol('P'): point_P,
#             Symbol('O'): point_O,
#             Symbol('H'): point_H,
            



#         }
#         return default_data_dict
    
# class RightTriangleLongLegAtPOPyramid(GeometricalCase):


#     point_A = [Point(x,y,z) for x in [6,6.5] for y in [7,7.5] for z in   [8,8.5]  ]

#     point_O=[Point(x,y,z) for x in  [4,5] for y in [4.5,5] for z in   [4.5,5,5.5] ]

#     point_P = [Point(x,y,z) for x in [2,2.5] for y in [13,13.5]  for z in [2,2.5] ]

#     point_H = [Point(x,y,z) for x in [9,9.5,10] for y in [6,7] for z in range(9,11) ]
    
#     shift = [Point(x,y,z) for x in [-1,-0.5,0,0.5,1] for y in [-1,-0.5,0,1,1.5,2] for z in [-1,-0.5,0,0.5,1] ]
    
#     def __init__(self,point_A=None,point_P=None,point_O=None,point_H=None,*args,**kwargs):

#         super().__init__()

#         if point_A and point_O and point_P and point_H:
#             projections=(point_A@HPP,point_O@HPP,point_O@VPP,point_P@VPP,point_P@HPP,point_A@VPP,point_H@VPP,point_H@HPP)
#         else:
#             projections=[]

#         self._assumptions=DrawingSet(*projections)

#         self._point_A=point_A
#         self._point_P=point_P
#         self._point_O=point_O
#         self._point_H=point_H

        
#         self._given_data={'A':point_A,'P':point_P,'O':point_O,'H':point_H}
        
#         self._solution_step.append(self._assumptions)

#     def solution(self):
        

        
#         if self._cached_solution is None:
            
#             current_obj = copy.deepcopy(self)
        
#             A=current_obj._point_A
#             O=current_obj._point_O
#             P=current_obj._point_P
#             H=current_obj._point_H

#             S = (A @ (O^P))('S') #'Srodek' podstawy

#             dirPS = P-S
#             dirOS = O-S
#             dirAS = S-A
#             longer_leg = 2*A.distance(S)

#             #square_side =  square_diagonal / (((3)**(1/2))/2)
#     #         print(square_diagonal)
#             C = (S + dirPS/(P.distance(S))*(longer_leg))('C')
#     #         D = (S - dirPS/(P.distance(S))*(diamond_diagonal))('D')
#             B = (A @ (O^P))('B')
#     #         line_AD=A^D
#     #         line_AB=A^B
#     #         line_BC=line_AD.parallel_line(P)
#     #         line_AS=Line(A,S)
#     #         C=line_BC.intersection(line_AS)[0]



#             current_set=DrawingSet(*current_obj._solution_step[-1])

#             line_a=Line(A,B)('a')
#             line_b=Line(B,C)('b')
#             line_c=Line(C,A)('c')
#             #line_d=Line(D,A)('d')
#             plane_alpha=Plane(A,O,P)

#             plane_beta=HorizontalPlane(P)

#             line_k = plane_alpha.intersection(plane_beta)[0]

#             elems=self._assumptions
#             projections=[]
#             point_0_dict={}


#             line_kk=Line(P, (O@line_k)  )('k')

#             current_obj.A0=A.rotate_about(axis=line_k)('A_0')
#             current_obj.B0=B.rotate_about(axis=line_k)('B_0')
#             current_obj.C0=C.rotate_about(axis=line_k)('C_0')
#             #current_obj.D0=D.rotate_about(axis=line_k)('D_0')
#             current_obj.O0=O.rotate_about(axis=line_k)('O_0')


#             #plane_beta=Plane(H,H+(B-A),H-(C-A))
#             plane_beta=Plane(H,H+(A-P),H-(O-P))
#             E=(A@plane_beta)('E')


#             line_ae=Line(S,E)('a')

#             elems+=[E,plane_alpha,line_ae]

#             projections+=[line_ae@HPP,line_ae@VPP,
#                          E@HPP,E@VPP]


#             #print(point_0_dict)
#             elems+=[line_a,line_b,#,E,F,G,H,line_s1,line_s2,line_s3,line_s4
#                   ]

#             projections+=[current_obj.A0@HPP,current_obj.A0@VPP,current_obj.B0@HPP,current_obj.B0@VPP,
#                           current_obj.C0@HPP,current_obj.C0@VPP,
#                           #current_obj.D0@HPP,current_obj.D0@VPP,
#                           B@HPP,B@VPP,C@HPP,C@VPP,
#                           #D@HPP,D@VPP,
#                           line_a@HPP,line_a@VPP,
#                           line_kk@HPP,line_kk@VPP,#line_s1@HPP,line_s1@VPP,line_s2@HPP,line_s2@VPP,line_s3@HPP,line_s3@VPP,
#                          #line_s4@HPP,line_s4@VPP
#                         ]
#             current_set+=[*elems,*projections]

#             current_obj._solution_step.append(current_set)
#             current_obj._assumptions=DrawingSet(*elems,*projections)
#             current_obj._point_B=B
#             current_obj._point_C=C
#             #current_obj._point_D=D
#             current_obj.point_E=E
            
#             self._cached_solution = current_obj
            
#         else:
#             current_obj = copy.deepcopy(self._cached_solution)
            
            
#         return current_obj

#     def get_default_data(self):

#         point_A = self.__class__.point_A
#         point_O = self.__class__.point_O
#         point_P = self.__class__.point_P
#         point_H = self.__class__.point_H
#         shift = self.shift

        
#         default_data_dict = {
#             Symbol('A'): point_A,
#             Symbol('P'): point_P,
#             Symbol('O'): point_O,
#             Symbol('H'): point_H,
#             'shift':shift



#         }
#         return default_data_dict
    
#     def get_random_parameters(self):
        


#         parameters_dict=super().get_random_parameters()

#         point_H=parameters_dict[Symbol('H')] 
#         point_O=parameters_dict[Symbol('O')] 
#         point_A=parameters_dict[Symbol('A')] 
#         point_P=parameters_dict[Symbol('P')]
        
#         shift = parameters_dict['shift']
#         parameters_dict.pop('shift')
        

#         for point in symbols('H O A P'): 
#             parameters_dict[point]=parameters_dict[point] + shift
            
            

        

#         return parameters_dict



# class RightTriangleShortLegAtPOPyramid(GeometricalCase):


#     point_A = [Point(x,y,z) for x in [6,6.5] for y in [7,7.5] for z in   [8,8.5]  ]

#     point_O=[Point(x,y,z) for x in  [4,5] for y in [4.5,5] for z in   [7,7.5] ]

#     point_P = [Point(x,y,z) for x in [2,2.5] for y in [13,13.5]  for z in [2,2.5] ]

#     point_H = [Point(x,y,z) for x in [9,9.5,10] for y in [6,7] for z in range(9,11) ]
    
#     shift = [Point(x,y,z) for x in [-1,-0.5,0,0.5,1] for y in [1,1.5,2] for z in [-1,-0.5,0,0.5,1] ]
    

#     def __init__(self,point_A=None,point_P=None,point_O=None,point_H=None,*args,**kwargs):

#         super().__init__()

#         if point_A and point_O and point_P and point_H:
#             projections=(point_A@HPP,point_O@HPP,point_O@VPP,point_P@VPP,point_P@HPP,point_A@VPP,point_H@VPP,point_H@HPP)
#         else:
#             projections=[]

#         self._assumptions=DrawingSet(*projections)

#         self._point_A=point_A
#         self._point_P=point_P
#         self._point_O=point_O
#         self._point_H=point_H

        
#         self._given_data={'A':point_A,'P':point_P,'O':point_O,'H':point_H}
        
#         self._solution_step.append(self._assumptions)

#     def solution(self):
            

        
#         if self._cached_solution is None:
            
#             current_obj = copy.deepcopy(self)
        
#             A=current_obj._point_A
#             O=current_obj._point_O
#             P=current_obj._point_P
#             H=current_obj._point_H

#             S = (A @ (O^P))('S') #'Srodek' podstawy

#             dirPS = P-S
#             dirOS = O-S
#             dirAS = S-A
#             shorter_leg = 1.5*A.distance(S)

#             #square_side =  square_diagonal / (((3)**(1/2))/2)
#     #         print(square_diagonal)
#             C = (S + dirOS/(O.distance(S))*(shorter_leg))('C')
#     #         D = (S - dirPS/(P.distance(S))*(diamond_diagonal))('D')
#             B = (A @ (O^P))('B')
#     #         line_AD=A^D
#     #         line_AB=A^B
#     #         line_BC=line_AD.parallel_line(P)
#     #         line_AS=Line(A,S)
#     #         C=line_BC.intersection(line_AS)[0]



#             current_set=DrawingSet(*current_obj._solution_step[-1])

#             line_a=Line(A,B)('a')
#             line_b=Line(B,C)('b')
#             line_c=Line(C,A)('c')
#             #line_d=Line(D,A)('d')
#             plane_alpha=Plane(A,O,P)

#             plane_beta=HorizontalPlane(P)

#             line_k = plane_alpha.intersection(plane_beta)[0]

#             elems=self._assumptions
#             projections=[]
#             point_0_dict={}
#             for point_I in [A,B,C,O]:

#                 S_I = (point_I @ line_k)('k')



#                 # zaimplementować w metode dla punktu 
#                 dir_I_on_HPP =(point_I @ plane_beta) - S_I

#                 #display(dir_I_on_HPP.coordinates)
#                 #display((point_I @ plane_beta).distance( S_I ))
#                 #display(point_I.distance( S_I ))

#                 ratio = (point_I.distance( S_I )) /(point_I @ plane_beta).distance( S_I )

#                 I_o =(S_I+(dir_I_on_HPP)*ratio)(point_I._label+'_0')

#                 point_0_dict[str(point_I)]=I_o
#                 elems += [I_o]
#                 projections+=[I_o@HPP,I_o@VPP]


#             line_kk=Line(P,S_I)('k')

#             current_obj.A0=point_0_dict['A']
#             current_obj.B0=point_0_dict['B']
#             current_obj.C0=point_0_dict['C']
#             #current_obj.D0=point_0_dict['D']

#             #plane_beta=Plane(H,H+(B-A),H-(C-A))
#             plane_beta=Plane(H,H+(A-P),H-(O-P))
#             E=(A@plane_beta)('E')


#             line_ae=Line(S,E)('a')

#             elems+=[E,plane_alpha,line_ae]

#             projections+=[line_ae@HPP,line_ae@VPP,
#                          E@HPP,E@VPP]


#             #print(point_0_dict)
#             elems+=[line_a,line_b,#,E,F,G,H,line_s1,line_s2,line_s3,line_s4
#                   ]

#             projections+=[current_obj.A0@HPP,current_obj.A0@VPP,current_obj.B0@HPP,current_obj.B0@VPP,
#                           current_obj.C0@HPP,current_obj.C0@VPP,
#                           #current_obj.D0@HPP,current_obj.D0@VPP,
#                           B@HPP,B@VPP,C@HPP,C@VPP,
#                           #D@HPP,D@VPP,
#                           line_a@HPP,line_a@VPP,
#                           line_kk@HPP,line_kk@VPP,#line_s1@HPP,line_s1@VPP,line_s2@HPP,line_s2@VPP,line_s3@HPP,line_s3@VPP,
#                          #line_s4@HPP,line_s4@VPP
#                         ]
#             current_set+=[*elems,*projections]

#             current_obj._solution_step.append(current_set)
#             current_obj._assumptions=DrawingSet(*elems,*projections)
#             current_obj._point_B=B
#             current_obj._point_C=C
#             #current_obj._point_D=D
#             current_obj.point_E=E
            
#             self._cached_solution = current_obj
            
#         else:
#             current_obj = copy.deepcopy(self._cached_solution)
            
#         return current_obj

#     def get_default_data(self):

#         point_A = self.__class__.point_A
#         point_O = self.__class__.point_O
#         point_P = self.__class__.point_P
#         point_H = self.__class__.point_H
#         shift = self.shift

        
#         default_data_dict = {
#             Symbol('A'): point_A,
#             Symbol('P'): point_P,
#             Symbol('O'): point_O,
#             Symbol('H'): point_H,
#             'shift':shift



#         }
#         return default_data_dict
    
#     def get_random_parameters(self):
        


#         parameters_dict=super().get_random_parameters()

#         point_H=parameters_dict[Symbol('H')] 
#         point_O=parameters_dict[Symbol('O')] 
#         point_A=parameters_dict[Symbol('A')] 
#         point_P=parameters_dict[Symbol('P')]
        
#         shift = parameters_dict['shift']
#         parameters_dict.pop('shift')        

#         for point in symbols('H O A P'): 
#             parameters_dict[point]=parameters_dict[point] + shift

        

#         return parameters_dict

    
# class RectangleLongSideAtPOPyramid(GeometricalCase):


#     point_A = [Point(x,y,z) for x in [3,3.5] for y in [8,8.5,9] for z in   [6,7]  ]

#     point_O=[Point(x,y,z) for x in  [6,7] for y in [11,11.5,12] for z in   [2.5,3,3.5] ]

#     point_P = [Point(x,y,z) for x in [1,1.5,2] for y in [3,3.5]  for z in [1,1.5,2] ]

#     point_H = [Point(x,y,z) for x in range(7,9) for y in [3,3.5] for z in range(9,11) ]
    

#     def __init__(self,point_A=None,point_P=None,point_O=None,point_H=None,**kwargs):

#         super().__init__()

#         if point_A and point_O and point_P and point_H:
#             projections=(point_A@HPP,point_O@HPP,point_O@VPP,point_P@VPP,point_P@HPP,point_A@VPP,point_H@VPP,point_H@HPP)
#         else:
#             projections=[]

#         self._assumptions=DrawingSet(*projections)

#         self._point_A=point_A
#         self._point_P=point_P
#         self._point_O=point_O
#         self._point_H=point_H

        
#         self._given_data={'A':point_A,'P':point_P,'O':point_O,'H':point_H}
        
#         self._solution_step.append(self._assumptions)

#     def solution(self):
#         current_obj=copy.deepcopy(self)
        
#         A=current_obj._point_A
#         O=current_obj._point_O
#         P=current_obj._point_P
#         H=current_obj._point_H
        
#         S = (A @ (O^P))('S') #'Srodek' podstawy
        
#         dirPS = P-S
#         dirOS = O-S
#         dirAS = S-A
#         longer_leg = 2*A.distance(S)
        
#         #square_side =  square_diagonal / (((3)**(1/2))/2)
# #         print(square_diagonal)
#         C = (S + dirPS/(P.distance(S))*(longer_leg))('C')

#         B = (A @ (O^P))('B')
        
#         D = (A + (C-B) )('D')
# #         line_AD=A^D
# #         line_AB=A^B
# #         line_BC=line_AD.parallel_line(P)
# #         line_AS=Line(A,S)
# #         C=line_BC.intersection(line_AS)[0]


        
#         current_set=DrawingSet(*current_obj._solution_step[-1])

#         line_a=Line(A,B)('a')
#         line_b=Line(B,C)('b')
#         line_c=Line(C,D)('c')
#         line_d=Line(D,A)('d')
#         plane_alpha=Plane(A,O,P)

#         plane_beta=HorizontalPlane(P)

#         line_k = plane_alpha.intersection(plane_beta)[0]

#         elems=self._assumptions
#         projections=[]
#         point_0_dict={}
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
        
#         current_obj.A0=point_0_dict['A']
#         current_obj.B0=point_0_dict['B']
#         current_obj.C0=point_0_dict['C']
#         current_obj.D0=point_0_dict['D']
        
        
#         #plane_beta=Plane(H,H+(B-A),H-(C-A))
#         plane_beta=Plane(H,H+(A-P),H-(O-P))
#         E=(A@plane_beta)('E')


#         line_ae=Line(S,E)('a')

#         elems+=[E,plane_alpha,line_ae]

#         projections+=[line_ae@HPP,line_ae@VPP,
#                      E@HPP,E@VPP]
        
        
#         #print(point_0_dict)
#         elems+=[line_a,line_b,#,E,F,G,H,line_s1,line_s2,line_s3,line_s4
#               ]

#         projections+=[current_obj.A0@HPP,current_obj.A0@VPP,current_obj.B0@HPP,current_obj.B0@VPP,
#                       current_obj.C0@HPP,current_obj.C0@VPP,
#                       #current_obj.D0@HPP,current_obj.D0@VPP,
#                       B@HPP,B@VPP,C@HPP,C@VPP,
#                       D@HPP,D@VPP,
#                       line_a@HPP,line_a@VPP,
#                       line_kk@HPP,line_kk@VPP,#line_s1@HPP,line_s1@VPP,line_s2@HPP,line_s2@VPP,line_s3@HPP,line_s3@VPP,
#                      #line_s4@HPP,line_s4@VPP
#                     ]
#         current_set+=[*elems,*projections]

#         current_obj._solution_step.append(current_set)
#         current_obj._assumptions=DrawingSet(*elems,*projections)
#         current_obj._point_B=B
#         current_obj._point_C=C
#         current_obj._point_D=D
#         current_obj.point_E=E
#         return current_obj


    
#     def get_default_data(self):

#         point_A = self.__class__.point_A
#         point_O = self.__class__.point_O
#         point_P = self.__class__.point_P
#         point_H = self.__class__.point_H

        
#         default_data_dict = {
#             Symbol('A'): point_A,
#             Symbol('P'): point_P,
#             Symbol('O'): point_O,
#             Symbol('H'): point_H,
            



#         }
#         return default_data_dict
    
# class EquilateralTrianglePrism(GeometricalCase):

#     #quite good data
#     #point_A = [Point(x,y,z) for x in [4,5.5,5] for y in [5,5.5,6] for z in   [5.5,6,6.5]  ]

#     #point_O=[Point(x,y,z) for x in [3,3.5] for y in [8,8.5,9] for z in   [3,3.5,4] ]

#     #point_P = [Point(x,y,z) for x in [6,6.5,7] for y in [3,3.5]  for z in [1,1.5,2] ]

#     #point_H = [Point(x,y,z) for x in range(9,11) for y in [3,3.5] for z in range(9,11) ]

#     # new set
#     point_A = [Point(x,y,z) for x in [3,3.5] for y in [8,8.5,9] for z in   [6,7]  ]

#     point_O=[Point(x,y,z) for x in  [6,7] for y in [11,11.5,12] for z in   [2.5,3,3.5] ]

#     point_P = [Point(x,y,z) for x in [1,1.5,2] for y in [3,3.5]  for z in [1,1.5,2] ]

#     point_H = [Point(x,y,z) for x in range(7,9) for y in [3,3.5] for z in range(9,11) ]
    

#     def __init__(self,point_A=None,point_P=None,point_O=None,point_H=None,**kwargs):

#         super().__init__()

#         if point_A and point_O and point_P and point_H:
#             projections=(point_A@HPP,point_O@HPP,point_O@VPP,point_P@VPP,point_P@HPP,point_A@VPP,point_H@VPP,point_H@HPP)
#         else:
#             projections=[]

#         self._assumptions=DrawingSet(*projections)

#         self._point_A=point_A
#         self._point_P=point_P
#         self._point_O=point_O
#         self._point_H=point_H

        
#         self._given_data={'A':point_A,'P':point_P,'O':point_O,'H':point_H}
        
#         self._solution_step.append(self._assumptions)

#     def solution(self):
#         current_obj=copy.deepcopy(self)
        
#         A=current_obj._point_A
#         O=current_obj._point_O
#         P=current_obj._point_P
#         H=current_obj._point_H
        
#         S = (A @ (O^P))('S') #'Srodek' podstawy
        
#         dirPS = P-S
#         dirOS = O-S
#         triangle_height = A.distance(S)
#         triangle_side =  triangle_height / ((3**(1/2))/2)
        
#         B = (S + dirPS/(P.distance(S))*(triangle_side/2))('B')
#         C = (S - dirPS/(P.distance(S))*(triangle_side/2))('C')


        
#         current_set=DrawingSet(*current_obj._solution_step[-1])

#         line_a=Line(A,B)('a')
#         line_b=Line(C,A)('b')
#         plane_alpha=Plane(A,O,P)

#         plane_beta=HorizontalPlane(P)

#         line_k = plane_alpha.intersection(plane_beta)[0]

#         elems=self._assumptions
#         projections=[]
#         point_0_dict={}
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
#             projections+=[I_o@HPP,I_o@VPP]

            
#         line_kk=Line(P,S_I)('k')
        
#         current_obj.A0=point_0_dict['A']
#         current_obj.B0=point_0_dict['B']
#         current_obj.C0=point_0_dict['C']
        
        
#         #print(point_0_dict)
#         elems+=[line_a,line_b,#,E,F,G,H,line_s1,line_s2,line_s3,line_s4
#               ]

#         projections+=[current_obj.A0@HPP,current_obj.A0@VPP,current_obj.B0@HPP,current_obj.B0@VPP,
#                       current_obj.C0@HPP,current_obj.C0@VPP,B@HPP,B@VPP,C@HPP,C@VPP,line_a@HPP,line_a@VPP,line_b@HPP,line_b@VPP,
#                       line_kk@HPP,line_kk@VPP,#line_s1@HPP,line_s1@VPP,line_s2@HPP,line_s2@VPP,line_s3@HPP,line_s3@VPP,
#                      #line_s4@HPP,line_s4@VPP
#                     ]
#         current_set+=[*elems,*projections]

#         current_obj._solution_step.append(current_set)
#         current_obj._assumptions=DrawingSet(*elems,*projections)
#         current_obj._point_B=B
#         current_obj._point_C=C
        
        
#         #plane_beta=Plane(H,H+(B-A),H-(C-A))
#         plane_beta=Plane(H,H+(A-P),H-(O-P))
#         D=(A@plane_beta)('D')
#         E=(B@plane_beta)('E')
#         F=(C@plane_beta)('F')


#         line_ad=Line(A,D)('a')
#         line_be=Line(B,E)('b')
#         line_cf=Line(C,F)('c')

#         elems+=[D,E,F,plane_alpha,line_ad,line_be,line_cf]

#         projections+=[line_ad@HPP,line_ad@VPP,line_be@HPP,line_be@VPP,line_cf@HPP,line_cf@VPP,
#                      D@HPP,D@VPP,E@HPP,E@VPP,F@HPP,F@VPP,]
        
        
#         #print(point_0_dict)
#         elems+=[line_a,line_b,#,E,F,G,H,line_s1,line_s2,line_s3,line_s4
#               ]

#         projections+=[current_obj.A0@HPP,current_obj.A0@VPP,current_obj.B0@HPP,current_obj.B0@VPP,
#                       current_obj.C0@HPP,current_obj.C0@VPP,B@HPP,B@VPP,C@HPP,C@VPP,line_a@HPP,line_a@VPP,line_b@HPP,line_b@VPP,
#                       line_kk@HPP,line_kk@VPP,#line_s1@HPP,line_s1@VPP,line_s2@HPP,line_s2@VPP,line_s3@HPP,line_s3@VPP,
#                      #line_s4@HPP,line_s4@VPP
#                     ]
#         current_set+=[*elems,*projections]

#         current_obj._solution_step.append(current_set)
#         current_obj._assumptions=DrawingSet(*elems,*projections)

#         current_obj.point_D=D
#         current_obj.point_E=E
#         current_obj.point_F=F
#         return current_obj

#     def get_default_data(self):

#         point_A = self.__class__.point_A
#         point_O = self.__class__.point_O
#         point_P = self.__class__.point_P
#         point_H = self.__class__.point_H

        
#         default_data_dict = {
#             Symbol('A'): point_A,
#             Symbol('P'): point_P,
#             Symbol('O'): point_O,
#             Symbol('H'): point_H,
            



#         }
#         return default_data_dict
    
    
# class HFLinesIsoscelesRightTrianglePyramid(GeometricalCase):

#     #quite good data
#     #point_A = [Point(x,y,z) for x in [4,5.5,5] for y in [5,5.5,6] for z in   [5.5,6,6.5]  ]

#     #point_O=[Point(x,y,z) for x in [3,3.5] for y in [8,8.5,9] for z in   [3,3.5,4] ]

#     #point_P = [Point(x,y,z) for x in [6,6.5,7] for y in [3,3.5]  for z in [1,1.5,2] ]

#     #point_H = [Point(x,y,z) for x in range(9,11) for y in [3,3.5] for z in range(9,11) ]

#     # new set
#     point_A = [Point(x,y,z) for x in [3,3.5] for y in [8,8.5,9] for z in   [6,7]  ]

#     point_O=[Point(x,y,z) for x in  [6,7] for y in [11,11.5,12] for z in   [2.5,3,3.5] ]

#     point_P = [Point(x,y,z) for x in [1,1.5,2] for y in [3,3.5]  for z in [1,1.5,2] ]

#     point_H = [Point(x,y,z) for x in [7,7.5,8] for y in [1,1.5,2] for z in [5.5,6,6.5] ]
#     #point_H = [Point(x,y,z) for x in [1,1.5] for y in [1,1.5,2] for z in [5.5,6,6.5] ]
    

#     def __init__(self,point_A=None,point_P=None,point_O=None,point_H=None,**kwargs):

#         super().__init__()
#         self._solution_step=[]
#         self._solution3d_step=[]

#         if point_A and point_O and point_P and point_H:
#             projections=(point_A@HPP,point_O@HPP,point_O@VPP,point_P@VPP,point_P@HPP,point_A@VPP,point_H@VPP,point_H@HPP)
            
#         else:
#             projections=[]

#         self._assumptions=DrawingSet(*projections)('Assumptions')
#         self._assumptions3d=DrawingSet(point_A,point_O,point_P,point_H)('Assumptions')
        

#         self._point_A=point_A
#         self._point_P=point_P
#         self._point_O=point_O
#         self._point_H=point_H

        
#         self._given_data={'A':point_A,'P':point_P,'O':point_O,'H':point_H}
        
#         self._solution_step.append(self._assumptions)
#         self._solution3d_step.append(self._assumptions3d)

#     def solution(self):
#         current_obj=copy.deepcopy(self)
        
#         A=current_obj._point_A
#         O=current_obj._point_O
#         P=current_obj._point_P
#         H=current_obj._point_H
        
#         S = (A @ (O^P))('S') #'Srodek' podstawy
        
#         dirPS = P-S
#         dirOS = O-S
#         triangle_height = A.distance(S)
#         #triangle_side =  triangle_height / ((3**(1/2))/2)
        
#         B = (S + dirPS/(P.distance(S))*(triangle_height))('B')
#         C = (S - dirPS/(P.distance(S))*(triangle_height))('C')


        
#         current_set=DrawingSet(*current_obj._solution_step[-1])

#         line_a=Line(A,B)('a')
#         line_b=Line(C,A)('b')
#         plane_alpha=Plane(A,O,P)

#         plane_beta=HorizontalPlane(P)
        
        

#         line_k = plane_alpha.intersection(plane_beta)[0]('a')
        
        
#         point_P1 = plane_beta.intersection(A^O)[0]('1')
#         line_kk = (P^point_P1)('a')
        
        
#         #current_step3d=copy.deepcopy(current_obj._solution3d_step[-1])+[(A^point_P1)('AO'),point_P1,(P^point_P1)('a')]
#         current_step3d=[(A^point_P1)('AO'),point_P1,(P^point_P1)('a')]
        
        
        
#         current_obj._solution3d_step.append(DrawingSet(*current_step3d)('Step 1 - axis of rotation'))
#         current_obj._solution_step.append(DrawingSet(*([obj@HPP for obj  in current_step3d] + [obj@VPP for obj  in current_step3d])   )('Step 1 - axis of rotation'))


#         elems=self._assumptions
#         projections=[]
#         point_0_dict={}
#         eps_dict={}
        
#         for point_I in [A]:
        
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

            
# #         line_kk=Line(P,S_I)('k')
#         point_B=B
#         point_C=C
#         point_O=O
#         current_obj.A0=point_0_dict['A']
#         current_obj.B0=point_B
#         current_obj.C0=point_C
#         current_obj.O0=point_O

#         plane_beta=Plane(H,H+(A-P),H-(O-P))
#         D=(C@plane_beta)('D')



        

#         elems+=[D]

#         projections+=[
#                      D@HPP,D@VPP]
        
        
#         #print(point_0_dict)
#         elems+=[line_a,line_b,#,E,F,G,H,line_s1,line_s2,line_s3,line_s4
#               ]

#         projections+=[current_obj.A0@HPP,current_obj.A0@VPP,current_obj.B0@HPP,current_obj.B0@VPP,
#                       current_obj.C0@HPP,current_obj.C0@VPP,B@HPP,B@VPP,C@HPP,C@VPP,line_a@HPP,line_a@VPP,line_b@HPP,line_b@VPP,
#                       line_kk@HPP,line_kk@VPP,#line_s1@HPP,line_s1@VPP,line_s2@HPP,line_s2@VPP,line_s3@HPP,line_s3@VPP,
#                      #line_s4@HPP,line_s4@VPP
#                     ]
#         current_set+=[*elems,*projections]

#         current_obj._solution_step.append(current_set)
#         current_obj._assumptions=DrawingSet(*elems,*projections)
#         current_obj._point_B=B
#         current_obj._point_C=C
#         current_obj.point_D=D


#         return current_obj

#     def present_solution(self):
        
#         doc_model = Document(f'{self.__class__.__name__} solution')

#         doc_model.packages.append(Package('booktabs'))
#         doc_model.packages.append(Package('float'))
#         doc_model.packages.append(Package('standalone'))
#         doc_model.packages.append(Package('siunitx'))


# #         ReportText.set_container(doc_model)
# #         ReportText.set_directory('./SDAresults')

#         for no,step3d in enumerate(self._solution3d_step):
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
#         point_O = self.__class__.point_O 
#         point_P=self.__class__.point_P
#         point_H=self.__class__.point_H




        
#         default_data_dict = {
#             Symbol('A'): point_A,
#             Symbol('P'): point_P,
#             Symbol('O'): point_O,
            

#             Symbol('H'): point_H,


#         }
#         return default_data_dict
#     def get_random_parameters(self):
        


#         parameters_dict=super().get_random_parameters()

#         point_H=parameters_dict[Symbol('H')] 
#         point_O=parameters_dict[Symbol('O')] 
#         point_A=parameters_dict[Symbol('A')] 
#         point_P=parameters_dict[Symbol('P')] 

#         parameters_dict[Symbol('A')]=Point(point_O.x,point_A.y,point_A.z)
#         parameters_dict[Symbol('P')]=Point(point_P.x,point_P.y,point_O.z)
        

#         return parameters_dict
    
# class GivenHeightHFLinesIsoscelesRightTrianglePrism(GeometricalCase):

#     #quite good data
#     #point_A = [Point(x,y,z) for x in [4,5.5,5] for y in [5,5.5,6] for z in   [5.5,6,6.5]  ]

#     #point_O=[Point(x,y,z) for x in [3,3.5] for y in [8,8.5,9] for z in   [3,3.5,4] ]

#     #point_P = [Point(x,y,z) for x in [6,6.5,7] for y in [3,3.5]  for z in [1,1.5,2] ]

#     #point_H = [Point(x,y,z) for x in range(9,11) for y in [3,3.5] for z in range(9,11) ]

#     # new set
#     point_A = [Point(x,y,z) for x in [3,3.5] for y in [8,8.5,9] for z in   [6,7]  ]

#     point_O=[Point(x,y,z) for x in  [6,7] for y in [11,11.5,12] for z in   [2.5,3,3.5] ]

#     point_P = [Point(x,y,z) for x in [1,1.5,2] for y in [3,3.5]  for z in [1,1.5,2] ]

#     point_H = [Point(x,y,z) for x in [7,7.5,8] for y in [1,1.5,2] for z in [5.5,6,6.5] ]
#     #point_H = [Point(x,y,z) for x in [1,1.5] for y in [1,1.5,2] for z in [5.5,6,6.5] ]
    

#     def __init__(self,point_A=None,point_P=None,point_O=None,point_H=None,**kwargs):

#         super().__init__()
#         self._solution_step=[]
#         self._solution3d_step=[]

#         if point_A and point_O and point_P and point_H:
#             projections=(point_A@HPP,point_O@HPP,point_O@VPP,point_P@VPP,point_P@HPP,point_A@VPP,point_H@VPP,point_H@HPP)
            
#         else:
#             projections=[]

#         self._assumptions=DrawingSet(*projections)('Assumptions')
#         self._assumptions3d=DrawingSet(point_A,point_O,point_P,point_H)('Assumptions')
        

#         self._point_A=point_A
#         self._point_P=point_P
#         self._point_O=point_O
#         self._point_H=point_H

        
#         self._given_data={'A':point_A,'P':point_P,'O':point_O,'H':point_H}
        
#         self._solution_step.append(self._assumptions)
#         self._solution3d_step.append(self._assumptions3d)
        
        
#     def solution(self):
#         current_obj=copy.deepcopy(self)
        
#         A=current_obj._point_A
#         O=current_obj._point_O
#         P=current_obj._point_P
        
#         H=current_obj._point_H
        
        
#         S = (A @ (O^P))('S') #'Srodek' podstawy
        
#         dirPS = P-S
#         dirOS = O-S
#         triangle_height = A.distance(S).n(5)
#         #triangle_side =  triangle_height / ((3**(1/2))/2)
        
#         B = (S + dirPS/(P.distance(S))*(triangle_height))('B')
#         C = (S - dirPS/(P.distance(S))*(triangle_height))('C')


        
#         current_set=DrawingSet(*current_obj._solution_step[-1])

#         line_a=Line(A,B)('a')
#         line_b=Line(C,A)('b')
#         plane_alpha=Plane(A,O,P)

#         plane_beta=HorizontalPlane(P)
        
        

#         line_k = plane_alpha.intersection(plane_beta)[0]('a')
        
        
#         point_P1 = plane_beta.intersection(A^O)[0]('1')
#         line_kk = (P^point_P1)('a')
        
        
#         #current_step3d=copy.deepcopy(current_obj._solution3d_step[-1])+[(A^point_P1)('AO'),point_P1,(P^point_P1)('a')]
#         current_step3d=[(A^point_P1)('AO'),point_P1,(P^point_P1)('a')]
        
        
        
#         current_obj._solution3d_step.append(DrawingSet(*current_step3d)('Step 1 - axis of rotation'))
#         current_obj._solution_step.append(DrawingSet(*([obj@HPP for obj  in current_step3d] + [obj@VPP for obj  in current_step3d])   )('Step 1 - axis of rotation'))


#         elems=self._assumptions
#         projections=[]
#         point_0_dict={}
#         eps_dict={}
        
#         for point_I in [A]:
        
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

            
# #         line_kk=Line(P,S_I)('k')
#         point_B=B
#         point_C=C
#         point_O=O
#         current_obj.A0=point_0_dict['A']
#         current_obj.B0=point_B
#         current_obj.C0=point_C
#         current_obj.O0=point_O
        
#         G = (H@plane_alpha)('G')
        
#         dirHG = H-G
#         distance_HG = (H.distance(G)).n(5)
        
#         D = (A + dirHG/distance_HG*triangle_height)('D')
#         E = (B + dirHG/distance_HG*triangle_height)('E')
#         F = (C + dirHG/distance_HG*triangle_height)('F')




        

#         elems+=[D,E,F,G]

#         projections+=[G@HPP,G@VPP,
#                      D@HPP,D@VPP,E@HPP,E@VPP,F@HPP,F@VPP]
        
        
#         #print(point_0_dict)
#         elems+=[line_a,line_b,D,E,F#,E,F,G,H,line_s1,line_s2,line_s3,line_s4
#               ]

#         projections+=[current_obj.A0@HPP,current_obj.A0@VPP,current_obj.B0@HPP,current_obj.B0@VPP,
#                       current_obj.C0@HPP,current_obj.C0@VPP,B@HPP,B@VPP,C@HPP,C@VPP,line_a@HPP,line_a@VPP,line_b@HPP,line_b@VPP,
#                       line_kk@HPP,line_kk@VPP,#line_s1@HPP,line_s1@VPP,line_s2@HPP,line_s2@VPP,line_s3@HPP,line_s3@VPP,
#                      #line_s4@HPP,line_s4@VPP
#                     ]
#         current_set+=[*elems,*projections]

#         current_obj._solution_step.append(current_set)
#         current_obj._assumptions=DrawingSet(*elems,*projections)
#         current_obj._point_B=B
#         current_obj._point_C=C
#         current_obj.point_D=D
#         current_obj.point_E=E
#         current_obj.point_F=F


#         return current_obj

#     def present_solution(self):
        
#         doc_model = Document(f'{self.__class__.__name__} solution')

#         doc_model.packages.append(Package('booktabs'))
#         doc_model.packages.append(Package('float'))
#         doc_model.packages.append(Package('standalone'))
#         doc_model.packages.append(Package('siunitx'))


# #         ReportText.set_container(doc_model)
# #         ReportText.set_directory('./SDAresults')

#         for no,step3d in enumerate(self._solution3d_step):
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
#         point_O = self.__class__.point_O 
#         point_P=self.__class__.point_P
#         point_H=self.__class__.point_H




        
#         default_data_dict = {
#             Symbol('A'): point_A,
#             Symbol('P'): point_P,
#             Symbol('O'): point_O,
            

#             Symbol('H'): point_H,


#         }
#         return default_data_dict
#     def get_random_parameters(self):
        


#         parameters_dict=super().get_random_parameters()

#         point_H=parameters_dict[Symbol('H')] 
#         point_O=parameters_dict[Symbol('O')] 
#         point_A=parameters_dict[Symbol('A')] 
#         point_P=parameters_dict[Symbol('P')] 

#         parameters_dict[Symbol('A')]=Point(point_O.x,point_A.y,point_A.z)
#         parameters_dict[Symbol('P')]=Point(point_P.x,point_P.y,point_O.z)
        

#         return parameters_dict