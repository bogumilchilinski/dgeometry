import matplotlib.pyplot as plt
from ..dgeometry import GeometryScene
import numpy as np
from numbers import Number

import numpy as np
from matplotlib.patches import Circle
from matplotlib.patches import RegularPolygon
import mpl_toolkits.mplot3d.art3d as art3d
import matplotlib.pyplot as plt


class ShaftPreview:
    def __init__(self, x0, y0, z0, *args):
        self.x0 = x0
        self.y0 = y0
        self.z0 = z0
        self.data = []
        self.total_length = 0

        #self.fig = plt.figure()
        self.ax = GeometryScene.ax_3d
        self.Xc = None
        self.Yc = None
        self.Zc = None
        self.ax.azim = 128
        self.ax.elev = 26

        for arg in args:
            self.data.append(arg)

        for i in range(len(self.data)):
            if i == 5:
                self.shaft_steps_sides((self.x0, self.y0), self.data[-1][0], self.total_length, self.data[i][3])
                self.total_length = 0
            self.shaft_steps_sides((self.x0, self.y0), self.data[i][0], self.z0, self.data[i][3])
            self.total_length += self.data[i][1]
        self.shaft_steps_sides((self.x0, self.y0), self.data[-1][0], self.z0+self.total_length, self.data[i][3])
        self.total_length = 0

        for i in range(len(self.data)):
            if i == 5:
                self.total_length = 0
            self.Xc, self.Yc, self.Zc = data_for_cylinder_along_z(self.x0, self.y0,
                                                                  self.data[i][0], self.data[i][1], self.z0)

            self.total_length += self.data[i][1]
            self.ax.plot_surface(self.Xc, self.Yc, self.Zc, alpha=self.data[i][3], color=self.data[i][4], edgecolor="black")

    def shaft_steps_sides(self, begin_cords, radius, zlength, transparency):

        # Draw a circle on the x axis 'wall'
        p = Circle(begin_cords, radius, alpha=transparency, color='#6b7aa1')
        self.ax.add_patch(p)
        art3d.pathpatch_2d_to_3d(p, z=zlength, zdir="x")



def data_for_cylinder_along_z(center_z, center_y, radius, height_x, x_begin):
    x = np.linspace(x_begin, x_begin + height_x, 500)
    theta = np.linspace(0, 2 * np.pi, 500)
    theta_grid, x_grid = np.meshgrid(theta, x)
    z_grid = radius * np.cos(theta_grid) + center_z
    y_grid = radius * np.sin(theta_grid) + center_y
    return x_grid, y_grid, z_grid



class HexPreview:
    def __init__(self, x0, y0, z0, *args):
        self.x0 = x0
        self.y0 = y0
        self.z0 = z0
        self.data = []
        self.total_length = 0

        #self.fig = plt.figure()
        self.ax = GeometryScene.ax_3d
        self.Xc = None
        self.Yc = None
        self.Zc = None
        self.ax.azim = 128
        self.ax.elev = 26

        for arg in args:
            self.data.append(arg)

        for i in range(len(self.data)):
            if i == 5:
                self.shaft_steps_sides((self.x0, self.y0), self.data[-1][0], self.total_length, self.data[i][3])
                self.total_length = 0
            self.shaft_steps_sides((self.x0, self.y0), self.data[i][0], self.z0, self.data[i][3])
            self.total_length += self.data[i][1]
        self.shaft_steps_sides((self.x0, self.y0), self.data[-1][0], self.z0+self.total_length, self.data[i][3])
        self.total_length = 0

        for i in range(len(self.data)):
            if i == 5:
                self.total_length = 0
            self.Xc, self.Yc, self.Zc = data_for_cylinder_along_z(self.x0, self.y0,
                                                                  self.data[i][0], self.data[i][1], self.z0)

            self.total_length += self.data[i][1]
            self.ax.plot_surface(self.Xc, self.Yc, self.Zc, alpha=self.data[i][3], color=self.data[i][4], edgecolor="black")
        self.ax.scatter(10,0 ,0)

    def shaft_steps_sides(self, begin_cords, radius, zlength, transparency):

        # Draw a circle on the x axis 'wall'
        p = RegularPolygon(begin_cords,6, 1.2*radius, alpha=0.6, color='#6b7aa1')
        self.ax.add_patch(p)
        

        art3d.pathpatch_2d_to_3d(p, z=zlength, zdir="x")



def data_for_cylinder_along_z(center_z, center_y, radius, height_x, x_begin):
    x = np.linspace(x_begin, x_begin + height_x, 500)
    theta = np.linspace(0, 2 * np.pi, 500)
    theta_grid, x_grid = np.meshgrid(theta, x)
    z_grid = radius * np.cos(theta_grid) + center_z
    y_grid = radius * np.sin(theta_grid) + center_y
    return x_grid, y_grid, z_grid


class DrawingObject:

    def __init__(self, **kwargs):
        self._element_dict = kwargs

    def get_lines_number(self, key):
        if key in self._element_dict.keys():

            return self._element_dict[key]
        else:
            return 0

    def horizontal_lines(self):
        return self.get_lines_number('horizontal_lines')

    def vertical_lines(self):
        return self.get_lines_number('vertical_lines')

    def inclined_lines(self):
        return self.get_lines_number('inclined_lines')


class View(DrawingObject):
    pass


class Section(DrawingObject):
    pass


class HalfSection(DrawingObject):
    pass


class FrontView(DrawingObject):
    pass


class Solid:

    def __init__(self, view, section, halfsection, front_view):
        self._parameters = tuple()
        self._class_description = 'with parameters'
        self._views = {
            'view': view,
            'section': section,
            'halfsection': halfsection,
            'front_view': front_view
        }

        #         print('views_dict')
        #         print(self._views)
        self.elements = []

        self._name = {}
        self._name['pl'] = 'Bryła'

        self._ref_elem=None
        self._origin = 0


    @property
    def origin(self):

        if self._ref_elem is not None:
            origin=self._ref_elem.end
        else:
            origin = self._origin



#         print(origin)
        return origin

    @property
    def end(self):

        end = self.origin + self.height

#         print('end =' + str(end))
        return end

    def _plot_2d(self,language='en'):

        

        class_name = self.__class__.__name__

        span = np.linspace(0, len(class_name), 100)

        res = GeometryScene.ax_2d.plot(span,
                                       np.cos(5 * len(class_name) * span),
                                       label=class_name)


    @property
    def views(self):
        return self._views

    @property
    def view(self):
        return self._views['view']

    @property
    def section(self):
        return self._views['section']

    @property
    def halfsection(self):
        return self._views['halfsection']

    @property
    def front_view(self):
        return self._views['front_view']

    def str_en(self):
        return '{name} {description}'.format(
            name=self.__class__.__name__, description=self._class_description)

    def str_pl(self):
        return '{name} {description}'.format(
            name=self._name['pl'], description=self._class_description_pl)

    def __str__(self):
        return '{name}{args}'.format(name=self.__class__.__name__,
                                     args=self._parameters)

    def __repr__(self):
        return self.__str__()
    
    def preview(self, example=False):

              self._plot_2d()
            

class ComposedPart:
    scheme_name = 'engine.png'
    real_name = 'engine_real.PNG'

    def __init__(self, *args):
        if args:
            self.elements = list(args)
        else:
            self.elements = []

    @classmethod
    def _scheme(cls):

        path = __file__.replace('solids.py', 'images/') + cls.scheme_name

        return path

    @classmethod
    def _real_example(cls):

        path = __file__.replace('solids.py', 'images/') + cls.real_name

        return path


    def preview(self, example=False,language='en'):

        print(*list(enumerate(self.elements)))

        #self.elements[0]._origin = 0
        #self.elements[-1]._origin = -30
        
        for no, elem in enumerate(self.elements):

            elem._plot_2d(language=language)


    def add(self, other):

        new_element_list = list(self.elements)

        if isinstance(other, Solid):
            new_element_list.append(other)

        return ComposedPart(*new_element_list)

    def __add__(self, other):
        return self.add(other)

    @property
    def view(self):

        num_of_lines = {
            'horizontal_lines':
            1 + sum([
                solid.view.get_lines_number('horizontal_lines') - 1
                for solid in self.elements
            ]),
            'vertical_lines':
            1 + sum([
                solid.view.get_lines_number('vertical_lines') - 1
                for solid in self.elements
            ]),
            'horizontal_dimensions':
            sum([
                solid.view.get_lines_number('horizontal_dimensions')
                for solid in self.elements
            ]),
            'vertical_dimensions':
            sum([
                solid.view.get_lines_number('vertical_dimensions')
                for solid in self.elements
            ]),
            'angular_dimensions':
            sum([
                solid.view.get_lines_number('angular_dimensions')
                for solid in self.elements
            ]),
            'inclined_lines':
            sum([
                solid.view.get_lines_number('inclined_lines')
                for solid in self.elements
            ]),
            'arcs':
            sum([
                solid.view.get_lines_number('arcs') for solid in self.elements
            ]),
            'circles':
            sum([
                solid.view.get_lines_number('circles')
                for solid in self.elements
            ]),
            'phi_dimensions':
            sum([
                solid.view.get_lines_number('phi_dimensions')
                for solid in self.elements
            ]),
        }

        return View(**num_of_lines)

    @property
    def section(self):

        num_of_lines = {
            'horizontal_lines':
            1 + sum([
                solid.section.get_lines_number('horizontal_lines') - 1
                for solid in self.elements
            ]),
            'vertical_lines':
            sum([
                solid.section.get_lines_number('vertical_lines')
                for solid in self.elements
            ]),
            'horizontal_dimensions':
            sum([
                solid.section.get_lines_number('horizontal_dimensions')
                for solid in self.elements
            ]),
            'vertical_dimensions':
            sum([
                solid.section.get_lines_number('vertical_dimensions')
                for solid in self.elements
            ]),
            'angular_dimensions':
            sum([
                solid.section.get_lines_number('angular_dimensions')
                for solid in self.elements
            ]),
            'inclined_lines':
            sum([
                solid.section.get_lines_number('inclined_lines')
                for solid in self.elements
            ]),
            'arcs':
            sum([
                solid.section.get_lines_number('arcs')
                for solid in self.elements
            ]),
            'circles':
            sum([
                solid.section.get_lines_number('circles')
                for solid in self.elements
            ]),
            'phi_dimensions':
            sum([
                solid.section.get_lines_number('phi_dimensions')
                for solid in self.elements
            ]),
        }

        return Section(**num_of_lines)

    @property
    def halfsection(self):

        num_of_lines = {
            'horizontal_lines':
            1 + sum([
                solid.halfsection.get_lines_number('horizontal_lines') - 1
                for solid in self.elements
            ]),
            'vertical_lines':
            sum([
                solid.halfsection.get_lines_number('vertical_lines')
                for solid in self.elements
            ]),
            'horizontal_dimensions':
            sum([
                solid.halfsection.get_lines_number('horizontal_dimensions')
                for solid in self.elements
            ]),
            'vertical_dimensions':
            sum([
                solid.halfsection.get_lines_number('vertical_dimensions')
                for solid in self.elements
            ]),
            'angular_dimensions':
            sum([
                solid.halfsection.get_lines_number('angular_dimensions')
                for solid in self.elements
            ]),
            'inclined_lines':
            sum([
                solid.halfsection.get_lines_number('inclined_lines')
                for solid in self.elements
            ]),
            'arcs':
            sum([
                solid.halfsection.get_lines_number('arcs')
                for solid in self.elements
            ]),
            'circles':
            sum([
                solid.halfsection.get_lines_number('circles')
                for solid in self.elements
            ]),
            'phi_dimensions':
            sum([
                solid.halfsection.get_lines_number('phi_dimensions')
                for solid in self.elements
            ]),
        }

        return HalfSection(**num_of_lines)

    @property
    def front_view(self):

        num_of_lines = {
            'horizontal_lines':
            1 + sum([
                solid.front_view.get_lines_number('horizontal_lines')
                for solid in self.elements
            ]),
            'vertical_lines':
            1 + sum([
                solid.front_view.get_lines_number('vertical_lines')
                for solid in self.elements
            ]),
            'horizontal_dimensions':
            sum([
                solid.front_view.get_lines_number('horizontal_dimensions')
                for solid in self.elements
            ]),
            'vertical_dimensions':
            sum([
                solid.front_view.get_lines_number('vertical_dimensions')
                for solid in self.elements
            ]),
            'angular_dimensions':
            sum([
                solid.front_view.get_lines_number('angular_dimensions')
                for solid in self.elements
            ]),
            'inclined_lines':
            sum([
                solid.front_view.get_lines_number('inclined_lines')
                for solid in self.elements
            ]),
            'arcs':
            sum([
                solid.front_view.get_lines_number('arcs')
                for solid in self.elements
            ]),
            'circles':
            sum([
                solid.front_view.get_lines_number('circles')
                for solid in self.elements
            ]),
            'phi_dimensions':
            sum([
                solid.front_view.get_lines_number('phi_dimensions')
                for solid in self.elements
            ]),
        }

        return FrontView(**num_of_lines)

    @property
    def views(self):

        #print('simple check')
        return {
            'view': self.view,
            'halfsection': self.halfsection,
            'section': self.section,
            'front_view': self.front_view,
        }


#     @propery
#     def side_view(self):

#         num_of_lines={
#             'horizontal_lines':
#            sum([2 for solid in self.element
#                 if solid.__class__.__name__ == 'HexagonalPrism'])
#             'vertical_lines':
#             None,
#             'horizontal_dimensions':
#             None,
#             'vertical_dimensions':
#             None,
#             'inclined_lines':
#             sum([4 for solid in self.element
#                 if solid.__class__.__name__ == 'HexagonalPrism'])
#             'circle':
#             None
# #             sum([for solid in self.element:
# #                      if solid.__class__.__name__ != 'Gear' | 'HexagonalPrism' | 'Thread':
# #                          if solid == self.element[0]:

# #                          else:
# #                              solid
# #                 ])
#         }

    def view_horizontal_lines(self):
        return sum([solid.view.horizontal_lines() for solid in self.elements])


class Cone(Solid):
    """Object represents Cone solid.
    
    The Cone object contains numbers of lines and dimensions required to make a engineering drawing. Object also includes values of height and both diameters' dimensions.
    
    Parameters
    ==========
    
    height: int
        The value of Cone's hight.
        
    top_diameter: int
        The value of Cone's top diameter.
        
    bottom_diameter: int
        The value of Cone's bottom diameter.
        
    Example
    ==========
    
    >>> from solids import Cone
    >>> st=Cone(10,4,8)
    >>> st._parameters
    (10,4,8)
    
    >>> st._class_description
    'with L=10mm, top diameter = 4mm and bottom diameter=8mm'
    
    >>> st._name
    >>> st._class_description
    {'pl': 'Stożek'}
    'o L=10mm, średnicy górnej podstawy = 4mm i średnicy dolnej podstawy=8mm'
    
    """

    def __init__(self, height, top_diameter, bottom_diameter):

        num_of_lines = {
            'horizontal_lines': 2,
            'vertical_lines': 1,
            'inclined_lines': 2,
            'horizontal_dimensions': 2,
            'vertical_dimensions': 1,
        }

        num_of_lines_front = {'circles': 1, 'phi_dimensions': 0}

        super().__init__(View(**num_of_lines), Section(**num_of_lines),
                         HalfSection(**num_of_lines),
                         FrontView(**num_of_lines_front))
        self.height = height
        self.top_diameter = top_diameter
        self.bottom_diameter = bottom_diameter

        self._parameters = height, top_diameter, bottom_diameter
        self._class_description = "with L={}mm, top diameter = {}mm and bottom diameter={}mm".format(
            *self._parameters)

        self._name['pl'] = 'Stożek'
        self._class_description_pl = "o L={}mm, średnicy górnej podstawy = {}mm i średnicy dolnej podstawy={}mm".format(
            *self._parameters)
    
    def _plot_2d(self):

        #         print(f'self.origin property is {self.origin()}')
        #         print(f'self.end property is {self.end()}')

        class_name = self.__class__.__name__

        span = np.linspace(0, len(class_name), 100)
#         print(f'plot_2d is called for {class_name}')

        r_b = self.bottom_diameter /2 /10
        r_t = self.top_diameter / 2 / 10
        l = self.height / 10
        origin = self.origin / 10
        end = self.end / 10
        
        t_l = origin + l / 4
        t_r = (r_t + 0.5)

        res = GeometryScene.ax_2d.plot(
            [origin + 0, origin + 0, origin + l, origin + l, origin + 0],
            [-r_b, r_b, r_t, -r_t, -r_b],
            color='k') + GeometryScene.ax_2d.plot(
            [origin - 0.5, origin + l + 0.5],
            [0,0],'-.',
            color='k', linewidth = 1) 
        text = GeometryScene.ax_2d.text(t_l,t_r,self.str_en(),rotation='vertical',multialignment='center')
        
        
        ShaftPreview(5,5,origin/2 ,[2*r_t/2, l/2, "bez fazy", 0.2, '#6b7aa1'])
        
        print(res)


class Cylinder(Solid):
    """This object represents cylinder solid.
    
    The cylinder object has predefined numbers of lines and dimensions that are needed make a engineering drawing. Also it stores information about height and diameter.
    
    Parameters
    ==========
    
    height : int
        The value of height of cylinder
        
    diameter : int
        The value of diameter of cylinder
    
    Examples
    ========
    
    >>> from solids import Cylinder
    >>> cyl = Cylinder(5,2)
    >>> cyl._parameters
    (5, 2)
    
    >>> cyl._class_description
    'with L=5mm and diameter =2mm'
    
    >>> cyl._class_description_pl
    'o L=5mm i średnicy =2mm'
    
    >>> cyl._name
    {'pl': 'Walec'}
    
    """

    line_type = '-'
    color='k'
    
    
    def __init__(self, height, diameter):
        num_of_lines = {
            'horizontal_lines': 3,
            'vertical_lines': 2,
            'horizontal_dimensions': 1,
            'vertical_dimensions': 1,
            'inclined_lines': 0,
        }

        num_of_lines_front = {'circles': 1, 'phi_dimensions': 0}

        num_of_lines_front = {'circles': 1, 'phi_dimensions': 1}

        super().__init__(View(**num_of_lines), Section(**num_of_lines),
                         HalfSection(**num_of_lines),
                         FrontView(**num_of_lines_front))
        self.height = height
        self.diameter = diameter

        self._parameters = height, diameter
        self._class_description = "with L={}mm and diameter ={}mm".format(
            *self._parameters)

        self._name['pl'] = 'Walec'
        self._class_description_pl = "o L={}mm i średnicy ={}mm".format(
            *self._parameters)

    def str_en(self):
        return 'Cylinder \n with L={length}mm \n and diameter={d}mm'.format(
            length=self.height,
            d=self.diameter)

    def str_pl(self):
        return 'Walec \n o L={length}mm i średnicy={d}mm'.format(
            length=self.height,
            d=self.diameter).replace('right',
                                          'prawej').replace('left', 'lewej')
        
    def _plot_2d(self,language='en'):

        #         print(f'self.origin property is {self.origin()}')
        #         print(f'self.end property is {self.end()}')

        class_name = self.__class__.__name__

        span = np.linspace(0, len(class_name), 100)
#         print(f'plot_2d is called for {class_name}')

        r = self.diameter / 2 / 10
        l = self.height / 10
        origin = self.origin / 10
        end = self.end / 10
        
        t_l = origin # + l / 8
        t_r = (r + 0.5)

        line_type = self.line_type
        color = self.color
        
        res = GeometryScene.ax_2d.plot(
            [origin + 0, origin + 0, origin + l, origin + l, origin + 0],
            [-r, r, r, -r, -r],line_type,
            color=color) + GeometryScene.ax_2d.plot(
            [origin - 0.5, origin + l + 0.5],
            [0,0],'-.',
            color='k', linewidth = 1)
        
        if language == 'pl':
            text = GeometryScene.ax_2d.text(t_l,t_r,self.str_pl(),rotation='vertical',multialignment='center')
        else:
            text = GeometryScene.ax_2d.text(t_l,t_r,self.str_en(),rotation='vertical',multialignment='center')
        
        
        ShaftPreview(5,5,origin/2 ,[2*r/2, l/2, "bez fazy", 0.2, '#6b7aa1'])
        
        print(res)

 


        
class ScrewCore(Cylinder):
    """This object represents core of the screw.
    
    The cylinder object has predefined numbers of lines and dimensions that are needed make a engineering drawing. Also it stores information about height and diameter.
    
    Parameters
    ==========
    
    height : int
        The value of height of cylinder
        
    diameter : int
        The value of diameter of cylinder
    
    Examples
    ========
    
    >>> from solids import Cylinder
    >>> cyl = ScrewCore(5,2)
    >>> cyl._parameters
    (5, 2)
    
    >>> cyl._class_description
    'with L=5mm and diameter =2mm'
    
    >>> cyl._class_description_pl
    'o L=5mm i średnicy =2mm'
    
    >>> cyl._name
    {'pl': 'Walec'}
    
    """
    
    line_type = '--'
    color='r'
    
    def str_en(self):
        return 'Cylinder of the screw \n with L={length}mm \n and diameter={d}mm'.format(
            length=self.height,
            d=self.diameter)

    def str_pl(self):
        return 'Trzpień śruby \n o L={length}mm i średnicy={d}mm'.format(
            length=self.height,
            d=self.diameter).replace('right',
                                          'prawej').replace('left', 'lewej')
    

class PlateWithHole(Cylinder):
    """This object represents core of the screw.
    
    The cylinder object has predefined numbers of lines and dimensions that are needed make a engineering drawing. Also it stores information about height and diameter.
    
    Parameters
    ==========
    
    height : int
        The value of height of cylinder
        
    diameter : int
        The value of diameter of cylinder
    
    Examples
    ========
    
    >>> from solids import Cylinder
    >>> cyl = ScrewCore(5,2)
    >>> cyl._parameters
    (5, 2)
    
    >>> cyl._class_description
    'with L=5mm and diameter =2mm'
    
    >>> cyl._class_description_pl
    'o L=5mm i średnicy =2mm'
    
    >>> cyl._name
    {'pl': 'Walec'}
    
    """
    
    line_type = '--'
    color='b'
    
    def _plot_2d(self,language='en'):

        class_name = self.__class__.__name__

        span = np.linspace(0, len(class_name), 100)
#         print(f'plot_2d is called for {class_name}')
       
        origin = self.origin / 10
        r = self.diameter / 2 / 10
        l = self.height / 10
        end = self.end / 10
        
        t_l = origin + l / 8
        t_r = (-r - 13)

        res = GeometryScene.ax_2d.plot([origin + 0, origin + 0, origin + l, origin + l, origin + 0], [-r, r, r, -r, -r],
                                       '--',
                                       color='b') + GeometryScene.ax_2d.plot(
                                        [origin - 0.5, origin + l + 0.5],
                                        [0,0],'-.',
                                        color='k', linewidth = 1)
    
        res = GeometryScene.ax_2d.plot(
            [origin + 0, origin + 0, origin + l, origin + l],
            [-r, r, r, -r, -r],'-',
            color=color) + GeometryScene.ax_2d.plot(
            [origin - 0.5, origin + l + 0.5],
            [0,0],'-.',
            color='color', linewidth = 1)
class Hole(Solid):
    """This object represents hole that can be made inside solid.
    
    The hole object has predefined numbers of lines and dimensions that are needed to make a engineering drawing in view, section and half-section. It also stores information about height and diameter.
    
    Parameters
    ==========
    
    height : int
        The value of height of hole
        
    diameter : int
        The value of diameter of hole
    
    Examples
    ========
    
    >>> from solids import Hole
    >>> hole = Hole(5,2)
    >>> hole._parameters
    (5, 2)
    
    >>> hole._class_description
    'with L=5mm and diameter =2mm'
    
    >>> hole._class_description_pl
    'o L=5mm i średnicy =2mm'
    
    >>> hole._name
    {'pl': 'Otwór'}
    
    """

    def __init__(self, height, diameter):
        num_of_lines_view = {
            'horizontal_lines': 1,
            'vertical_lines': 1,
            'horizontal_dimensions': 0,
            'vertical_dimensions': 0,
            'inclined_lines': 0,
        }
        num_of_lines_sec = {
            'horizontal_lines': 3,
            'vertical_lines': 1,
            'horizontal_dimensions': 1,
            'vertical_dimensions': 1,
            'inclined_lines': 0,
        }

        num_of_lines_half_sec = {
            'horizontal_lines': 2,
            'vertical_lines': 1,
            'horizontal_dimensions': 1,
            'vertical_dimensions': 1,
            'inclined_lines': 0,
        }

        num_of_lines_front = {'circles': 1, 'phi_dimensions': 0}

        super().__init__(View(**num_of_lines_view),
                         Section(**num_of_lines_sec),
                         HalfSection(**num_of_lines_half_sec),
                         FrontView(**num_of_lines_front))
        self.height = height
        self.diameter = diameter

        self._parameters = height, diameter
        self._class_description = "with L={}mm and diameter={}mm".format(
            *self._parameters)

        self._name['pl'] = 'Otwór'
        self._class_description_pl = "o L={}mm i średnicy ={}mm".format(
            *self._parameters)
 
    def str_en(self):
        return 'Hole \n with L={length}mm \n and diameter={d}mm'.format(
            length=self.height,
            d=self.diameter
        )

    def str_pl(self):
        return 'Otwór \n o L={length}mm i średnicy={d}mm'.format(
            length=self.height,
            d=self.diameter).replace('right',
                                          'prawej').replace('left', 'lewej')

    def _plot_2d(self,language='en'):

        class_name = self.__class__.__name__

        span = np.linspace(0, len(class_name), 100)
#         print(f'plot_2d is called for {class_name}')
       
        origin = self.origin / 10
        r = self.diameter / 2 / 10
        l = self.height / 10
        end = self.end / 10
        
        t_l = origin + l / 8
        t_r = (-r - 13)

        res = GeometryScene.ax_2d.plot([origin + 0, origin + 0, origin + l, origin + l, origin + 0], [-r, r, r, -r, -r],
                                       '--',
                                       color='b') + GeometryScene.ax_2d.plot(
                                        [origin - 0.5, origin + l + 0.5],
                                        [0,0],'-.',
                                        color='k', linewidth = 1)
        
        if language == 'pl':
            text = GeometryScene.ax_2d.text(t_l,t_r,self.str_pl(),rotation='vertical',multialignment='center')
        else:
            text = GeometryScene.ax_2d.text(t_l,t_r,self.str_en(),rotation='vertical',multialignment='center')

        ShaftPreview(5,5,origin/2 ,[2*r/2, l/2, "bez fazy", 0.7, '#6b7aa1'])

class ChamferedHole(Solid):
    """This object represents chamfered hole that can be made inside solid.
    
    The chamfered hole object has predefined numbers of lines and dimensions that are needed to make a engineering drawing in view, section and half-section. It also stores information about height, diameter, chamfer length, angle and position.
    
    Parameters
    ==========
    
    height : int
        The value of height of hole
        
    diameter : int
        The value of diameter of hole
    
    chamfer_length=1 : int
        The value of chamfer length
    
    chamfer_angle=45 : int
        The value of chamfer angle
    
    chamfer_pos='left' : str
        The position of chamfer
    
    Examples
    ========
    
    >>> from solids import ChamferedHole
    >>> chamf_hole = ChamferedHole(5,2)
    >>> chamf_hole._parameters
    (5, 2)
    
    >>> chamf_hole.str_en()
    'Hole with L=5mm, diameter=2mm and 1x45 chamfer on the left side'
    
    >>> chamf_hole.str_pl()
    'Otwór o L=5mm, średnicy=2mm i fazie 1x45 znajdującej się po lewej stronie'
    
    >>> chamf_hole._class_description
    'with L=5mm and diameter=2mm'
    
    """

    def __init__(self,
                 height,
                 diameter,
                 chamfer_length=1,
                 chamfer_angle=45,
                 chamfer_pos='left'):

        num_of_lines_view = {
            'horizontal_lines': 1,
            'vertical_lines': 1,
            'horizontal_dimensions': 0,
            'vertical_dimensions': 0,
            'inclined_lines': 0,
        }
        num_of_lines_sec = {
            'horizontal_lines': 3,
            'vertical_lines': 2,
            'horizontal_dimensions': 2,
            'vertical_dimensions': 1,
            'inclined_lines': 2,
            'angular_dimensions': 1,
        }

        num_of_lines_half_sec = {
            'horizontal_lines': 2,
            'vertical_lines': 2,
            'horizontal_dimensions': 2,
            'vertical_dimensions': 1,
            'inclined_lines': 1,
            'angular_dimensions': 1,
        }

        num_of_lines_front = {'circles': 2, 'phi_dimensions': 0}

        super().__init__(View(**num_of_lines_view),
                         Section(**num_of_lines_sec),
                         HalfSection(**num_of_lines_half_sec),
                         FrontView(**num_of_lines_front))
        self.height = height
        self.diameter = diameter
        self.chamfer_length = chamfer_length
        self.chamfer_angle = chamfer_angle
        self.chamfer_pos = chamfer_pos
        self._parameters = height, diameter
        self._class_description = "with L={}mm and diameter={}mm".format(
            *self._parameters)

    def str_en(self):
        return 'Hole \n with L={length}mm, diameter={d}mm \n and {l_ch}x{angle} chamfer on the {pos} side'.format(
            length=self.height,
            d=self.diameter,
            angle=self.chamfer_angle,
            l_ch=self.chamfer_length,
            pos=self.chamfer_pos)

    def str_pl(self):
        return 'Otwór \n o L={length}mm, średnicy={d}mm \n i fazie {l_ch}x{angle} znajdującej się po {pos} stronie'.format(
            length=self.height,
            d=self.diameter,
            angle=self.chamfer_angle,
            l_ch=self.chamfer_length,
            pos=self.chamfer_pos).replace('right',
                                          'prawej').replace('left', 'lewej')
    
#     def _plot_2d(self,language='en'):

#         class_name = self.__class__.__name__

#         span = np.linspace(0, len(class_name), 100)
#         print(f'plot_2d is called for {class_name}')
       
#         origin = self.origin / 10
#         r = self.diameter / 2 / 10
#         l = self.height / 10
#         end = self.end / 10
#         c_l = self.chamfer_length / 10
#         c_a = self.chamfer_angle
#         c_h = c_l * np.tan(c_a)
        
#         t_l = origin + l / 2
#         t_r = (r + 1)

#         res = GeometryScene.ax_2d.plot(
#             [origin+c_l,origin+c_l,origin+l,origin+l,origin+c_l],[ -r, +r, +r, -r, -r],'--',color='c') + GeometryScene.ax_2d.plot(
#                 [origin+c_l,origin,origin,origin+c_l],[ -r, -r-c_h, +r+c_h, +r],'--',color='c')+ GeometryScene.ax_2d.plot(
#                     [origin,origin+l],[ -r-c_h, -r-c_h],'--',linewidth=1,color='c') + GeometryScene.ax_2d.plot(
#                         [origin,origin+l],[ +r+c_h, +r+c_h],'--',linewidth=1,color='c') + GeometryScene.ax_2d.plot(
#                             [origin+l,origin+l],[r+c_h,-r-c_h],'--',color='c')
        
#         text = GeometryScene.ax_2d.text(t_l,t_r,self.str_pl(),rotation='vertical',multialignment='center')
#         print(res)
        
    def _plot_2d(self,language='en'):

        class_name = self.__class__.__name__

        span = np.linspace(0, len(class_name), 100)
#         print(f'plot_2d is called for {class_name}')
       
        origin = self.origin / 10
        r = self.diameter / 2 / 10
        l = self.height / 10
        end = self.end / 10
        
        t_l = origin + l / 7
        t_r = (-r - 14.5)

        res = GeometryScene.ax_2d.plot([origin + 0, origin + 0, origin + l, origin + l, origin + 0], [-r, r, r, -r, -r],
                                       '--',
                                       color='c') + GeometryScene.ax_2d.plot(
                                        [origin - 0.5, origin + l + 0.5],
                                        [0,0],'-.',
                                        color='k', linewidth = 1)
        
        if language == 'pl':
            text = GeometryScene.ax_2d.text(t_l,t_r,self.str_pl(),rotation='vertical',multialignment='center')
        else:
            text = GeometryScene.ax_2d.text(t_l,t_r,self.str_en(),rotation='vertical',multialignment='center')

        ShaftPreview(5,5,origin/2 ,[2*r/2, l/2, "bez fazy", 0.7, '#6b7aa1'])


class ChamferedCylinder(Solid):
    """This object represents chamfered cylinder solid.
    
    The chamfered cylinder object has predefined numbers of lines and dimensions that are needed to make a engineering drawing in view, section and half-section. It also stores information about height, diameter, chamfer length, angle and position.
    
    Parameters
    ==========
    
    height : int
        The value of height of hole
        
    diameter : int
        The value of diameter of hole
    
    chamfer_length=1 : int
        The value of chamfer length
    
    chamfer_angle=45 : int
        The value of chamfer angle
    
    chamfer_pos='left' : str
        The position of chamfer
    
    Examples
    ========
    
    >>> from solids import ChamferedCylinder
    >>> chamf_cyl = ChamferedCylinder(5,2)
    >>> chamf_cyl._parameters
    (5, 2)
    
    >>> chamf_cyl.str_en()
    'Cylinder with L=5mm, diameter=2mm and 1x45 chamfer on the left side'
    
    >>> chamf_cyl.str_pl()
    'Walec o L=5mm, średnicy=2mm i fazie 1x45 znajdującej się po lewej stronie'
    
    >>> chamf_cyl._class_description
    'with L=5mm and diameter=2mm'
    
    """

    def __init__(self,
                 height,
                 diameter,
                 chamfer_length=1,
                 chamfer_angle=45,
                 chamfer_pos='left'):

        num_of_lines_view = {
            'horizontal_lines': 3,
            'vertical_lines': 3,
            'horizontal_dimensions': 2,
            'vertical_dimensions': 1,
            'inclined_lines': 2,
            'angular_dimensions': 1,
        }

        num_of_lines_sec = {
            'horizontal_lines': 3,
            'vertical_lines': 2,
            'horizontal_dimensions': 2,
            'vertical_dimensions': 1,
            'inclined_lines': 2,
            'angular_dimensions': 1,
        }

        num_of_lines_half_sec = {
            'horizontal_lines': 3,
            'vertical_lines': 3,
            'horizontal_dimensions': 2,
            'vertical_dimensions': 1,
            'inclined_lines': 2,
            'angular_dimensions': 1,
        }

        num_of_lines_front = {'circles': 2, 'phi_dimensions': 0}

        super().__init__(View(**num_of_lines_view),
                         Section(**num_of_lines_sec),
                         HalfSection(**num_of_lines_half_sec),
                         FrontView(**num_of_lines_front))
        self.height = height
        self.diameter = diameter
        self.chamfer_length = chamfer_length
        self.chamfer_angle = chamfer_angle
        self.chamfer_pos = chamfer_pos
        self._parameters = height, diameter
        self._class_description = "with L={}mm and diameter={}mm".format(
            *self._parameters)

    def str_en(self):
        return 'Cylinder \n with L={length}mm, diameter={d}mm \n and {l_ch}x{angle} chamfer on the {pos} side'.format(
            length=self.height,
            d=self.diameter,
            angle=self.chamfer_angle,
            l_ch=self.chamfer_length,
            pos=self.chamfer_pos)

    def str_pl(self):
        return 'Walec \n o L={length}mm, średnicy={d}mm \n i fazie {l_ch}x{angle} znajdującej się po {pos} stronie'.format(
            length=self.height,
            d=self.diameter,
            angle=self.chamfer_angle,
            l_ch=self.chamfer_length,
            pos=self.chamfer_pos).replace('right',
                                          'prawej').replace('left', 'lewej')

#     def _plot_2d(self,language='en'):

#         class_name = self.__class__.__name__

#         span = np.linspace(0, len(class_name), 100)
#         print(f'plot_2d is called for {class_name}')

#         r = self.diameter / 2 / 10
#         l = self.height / 10
#         origin = self.origin / 10
#         c_l = self.chamfer_length / 10
#         c_a = self.chamfer_angle
#         c_h = c_l * np.tan(c_a)
        
#         t_l = origin + l / 2
#         t_r = (r + 1)

#         res = GeometryScene.ax_2d.plot(
#             [origin + c_l, origin + c_l, origin + l, origin + l, origin + c_l], [-r, r, r, -r, -r],
#             color='g') + GeometryScene.ax_2d.plot(
#                 [ origin + c_l, origin + 0, origin + 0, origin + c_l], [-r, -r + c_h, r - c_h, r],
#                 color='g')
#         text = GeometryScene.ax_2d.text(t_l,t_r,self.str_pl(),rotation='vertical',multialignment='center')
#         print(res)

#         ShaftPreview(5,5,origin/2 ,[2*r/2, l/2, "bez fazy", 0.2, '#6b7aa1'])
        
    def _plot_2d(self,language='en'):

        #         print(f'self.origin property is {self.origin()}')
        #         print(f'self.end property is {self.end()}')

        class_name = self.__class__.__name__

        span = np.linspace(0, len(class_name), 100)
#         print(f'plot_2d is called for {class_name}')

        r = self.diameter / 2 / 10
        l = self.height / 10
        origin = self.origin / 10
        end = self.end / 10
        
        t_l = origin + l / 4
        t_r = (r + 0.5)

        res = GeometryScene.ax_2d.plot(
            [origin + 0, origin + 0, origin + l, origin + l, origin + 0],
            [-r, r, r, -r, -r],
            color='g') + GeometryScene.ax_2d.plot(
            [origin - 0.5, origin + l + 0.5],
            [0,0],'-.',
            color='k', linewidth = 1)
        
        if language == 'pl':
            text = GeometryScene.ax_2d.text(t_l,t_r,self.str_pl(),rotation='vertical',multialignment='center')
        else:
            text = GeometryScene.ax_2d.text(t_l,t_r,self.str_en(),rotation='vertical',multialignment='center')


        ShaftPreview(5,5,origin/2 ,[2*r/2, l/2, "bez fazy", 0.2, '#6b7aa1'])
        
#     def _plot_2d(self,language='en'):

#         #         print(f'self.origin property is {self.origin()}')
#         #         print(f'self.end property is {self.end()}')

#         class_name = self.__class__.__name__

#         span = np.linspace(0, len(class_name), 100)
#         print(f'plot_2d is called for {class_name}')

#         r = self.diameter / 2 / 10
#         l = self.height / 10
#         origin = self.origin / 10

#         res = GeometryScene.ax_2d.plot(
#             [origin + 0, origin + 0, origin + l, origin + l, origin + 0],
#             [-r, r, r, -r, -r],
#             color='k')
#         print(res)

        
        

class Thread(Solid):

    def __init__(self,
                 height,
                 diameter,
                 chamfer_length=1,
                 chamfer_angle=45,
                 thread='M'):

        num_of_lines_view = {
            'horizontal_lines': 5,
            'vertical_lines': 3,
            'inclined_lines': 2,
            'horizontal_dimensions': 2,
            'vertical_dimensions': 1,
            'angular_dimensions': 1,
        }

        num_of_lines_sec = {
            'horizontal_lines': 5,
            'vertical_lines': 2,
            'inclined_lines': 2,
            'horizontal_dimensions': 2,
            'vertical_dimensions': 1,
            'angular_dimensions': 1,
        }

        num_of_lines_half_sec = {
            'horizontal_lines': 5,
            'vertical_lines': 3,
            'inclined_lines': 2,
            'horizontal_dimensions': 2,
            'vertical_dimensions': 1,
            'angular_dimensions': 1,
        }

        num_of_lines_front = {'circles': 1, 'arcs': 1}

        super().__init__(View(**num_of_lines_view),
                         Section(**num_of_lines_sec),
                         HalfSection(**num_of_lines_half_sec),
                         FrontView(**num_of_lines_front))

        self.height = height
        self.diameter = diameter
        self.thread = thread
        self.chamfer_length = chamfer_length
        self.chamfer_angle = chamfer_angle
        self._parameters = thread + str(
            diameter), height, chamfer_length, chamfer_angle,
        self._class_description = "{} with L={}mm and chamfer {}x{}".format(
            *(self._parameters))

        self._name['pl'] = 'Gwint'
        self._class_description_pl = "{} o L={}mm i fazie {}x{}".format(
            *self._parameters)
        
    def str_en(self):
        return 'Threaded Cylinder \n with L={length}mm, thread M{d} \n and chamfer {l_ch}x{angle}'.format(
            length=self.height,
            d=self.diameter,
            angle=self.chamfer_angle,
            l_ch=self.chamfer_length,
            )

    def str_pl(self):
        return 'Walec gwintowany \n o L={length}mm, gwincie M{d}mm \n i fazie {l_ch}x{angle}'.format(
            length=self.height,
            d=self.diameter,
            angle=self.chamfer_angle,
            l_ch=self.chamfer_length,
            )

    def _plot_2d(self,language='en'):

        class_name = self.__class__.__name__

        span = np.linspace(0, len(class_name), 100)
        print(f'plot_2d is called for {class_name}')

        r = self.diameter / 2 / 10
        l = self.height / 10
        r_t = 0.9 * r
        origin = self.origin / 10
        end = self.end / 10
        
        t_l = origin + l /2
        t_r = (- r - 8.5)

        res = GeometryScene.ax_2d.plot([origin + 0, origin + 0, origin + l, origin + l, origin + 0], [-r, r, r, -r, -r],
                                       color='k') + GeometryScene.ax_2d.plot(
                                           [origin + 0, origin + 0, origin + l, origin + l, origin + 0],
                                           [-r_t, r_t, r_t, -r_t, -r_t],
                                           linewidth=1, color='r') + GeometryScene.ax_2d.plot(
                                           [origin - 0.5, origin + l + 0.5],
                                           [0,0],'-.',
                                           color='k', linewidth = 1)
        
        
        if language == 'pl':
            text = GeometryScene.ax_2d.text(t_l,t_r,self.str_pl(),rotation='vertical',multialignment='center')
        else:
            text = GeometryScene.ax_2d.text(t_l,t_r,self.str_en(),rotation='vertical',multialignment='center')

        ShaftPreview(5,5,origin/2 ,[2*r/2, l/2, "bez fazy", 0.2, '#56754A'])
        


class ThreadedOpenHole(Solid):
    """This object represents threaded hole that can be made inside solid.
    
    The threaded hole object has predefined numbers of lines and dimensions that are needed to make a engineering drawing in view, section and half-section. It also stores information about height, diameter, chamfer length, angle and position.
    
    Parameters
    ==========
    
    height : int
        The value of height of hole
        
    diameter : int
        The value of diameter of hole
    
    chamfer_length=1 : int
        The value of chamfer length
    
    chamfer_angle=45 : int
        The value of chamfer angle
    
    chamfer_pos='left' : str
        The position of chamfer
    
    Examples
    ========
    
    >>> from solids import ThreadedOpenHole
    >>> thr_hole = ThreadedOpenHole(5,2)
    >>> thr_hole._parameters
    (5, 2)
    
    >>> chamf_hole.str_en()
    'Hole with L=5mm, diameter=2mm and 1x45 chamfer on the left side'
    
    >>> chamf_hole.str_pl()
    'Otwór o L=5mm, średnicy=2mm i fazie 1x45 znajdującej się po lewej stronie'
    
    >>> chamf_hole._class_description
    'with L=5mm and diameter=2mm'
    
    """

    def __init__(self,
                 height,
                 diameter,
                 chamfer_length=1,
                 chamfer_angle=45,
                 thread='M'):

        num_of_lines_view = {
            'horizontal_lines': 1,
            'vertical_lines': 1,
            'horizontal_dimensions': 0,
            'vertical_dimensions': 0,
            'inclined_lines': 0,
        }
        num_of_lines_sec = {
            'horizontal_lines': 5,
            'vertical_lines': 2,
            'horizontal_dimensions': 2,
            'vertical_dimensions': 1,
            'inclined_lines': 4,
            'angular_dimensions': 2,
        }

        num_of_lines_half_sec = {
            'horizontal_lines': 3,
            'vertical_lines': 2,
            'horizontal_dimensions': 2,
            'vertical_dimensions': 1,
            'inclined_lines': 2,
            'angular_dimensions': 2,
        }

        num_of_lines_front = {'circles': 3, 'phi_dimensions': 0}

        super().__init__(View(**num_of_lines_view),
                         Section(**num_of_lines_sec),
                         HalfSection(**num_of_lines_half_sec),
                         FrontView(**num_of_lines_front))

        self.diameter = diameter
        self.height = height
        self.chamfer_length = chamfer_length
        self.chamfer_angle = chamfer_angle
        self.thread = thread
        self._parameters = thread, diameter,
        self._class_description = "Threaded open hole {}{}".format(
            *self._parameters)

    def str_en(self):
        return 'Open threaded hole \n (to the end of solid) \n {thread}{d} with {l_ch}x{angle} \n chamfers on both sides'.format(
            thread=self.thread,
            d=self.diameter,
            angle=self.chamfer_angle,
            l_ch=self.chamfer_length)

    def str_pl(self):
        return 'Gwintowany otwór przelotowy {thread}{d} \n z fazą {l_ch}x{angle} \n po obu stronach'.format(
            thread=self.thread,
            d=self.diameter,
            angle=self.chamfer_angle,
            l_ch=self.chamfer_length)

    def _plot_2d(self,language='en'):

        class_name = self.__class__.__name__

        span = np.linspace(0, len(class_name), 100)
        print(f'plot_2d is called for {class_name}')

        r = self.diameter / 2 / 10
        l = self.height / 10
        c_l = self.chamfer_length / 10
        c_a = self.chamfer_angle
        c_h = c_l * np.tan(c_a)
        t = 1.1*r
        
        origin = self.origin / 10
        end = self.end / 10

        res = GeometryScene.ax_2d.plot(
            [origin + 0,origin +  0,origin +  l,origin +  l,origin +  0], [-r, r, r, -r, -r], '--',
            color='y') + GeometryScene.ax_2d.plot(
                [origin + 0,origin +  0 - c_l,origin +  0 - c_l,origin +  0], [-r, -r - c_h, r + c_h, r],
                '--',
                color='y') + GeometryScene.ax_2d.plot(
                    [origin - c_l,origin + l], [-t, -t], '--', linewidth=1,
                    color='y') + GeometryScene.ax_2d.plot(
                        [origin - c_l,origin + l], [t, t], '--', linewidth=1,
                        color='y') + GeometryScene.ax_2d.plot(
                            [origin + l,origin +  l], [t, -t], '--', color='y')
        
        t_l = origin + l / 7
        t_r = (-r - 13.5)
        
        if language == 'pl':
            text = GeometryScene.ax_2d.text(t_l,t_r,self.str_pl(),rotation='vertical',multialignment='center')
        else:
            text = GeometryScene.ax_2d.text(t_l,t_r,self.str_en(),rotation='vertical',multialignment='center')

        ShaftPreview(5,5,origin/2 ,[2*r/2, l/2, "bez fazy", 0.7, '#6b7aa1'])


class Gear(Solid):
    """This object represents a gear.
    
    The gear object has predefined numbers of lines and dimensions that are needed to make a engineering drawing in view, section and half-section. It also stores information about height, teeth number, module, chamfer length and chamfer angle.
    
    Parameters
    ==========
    
    height : int
        The value of height of the gear
        
    teeth_no : int
        The number of teeth

    module : int
        The value of module
    
    chamfer_length=1 : int
        The value of chamfer length
    
    chamfer_angle=45 : int
        The value of chamfer angle
    
    Examples
    ========
    
    >>> from solids import Gear
    >>> gear = Gear(50,21,2)
    >>> gear._parameters
    (50, 21, 2, 1, 45)
    
    >>> gear.str_en()
    'Gear with outside diameter 50, module 2 and 1x45 chamfers on both sides'
    
    >>> gear.str_pl()
    'Koło zębate o średnicy wierzchołkowej 50, module 2 z fazą 1x45 po obu stronach'

    
    """

    def __init__(self,
                 height,
                 teeth_no,
                 module,
                 chamfer_length=1,
                 chamfer_angle=45):

        num_of_lines_view = {
            'horizontal_lines': 5,
            'vertical_lines': 4,
            'inclined_lines': 4,
            'horizontal_dimensions': 3,
            'vertical_dimensions': 1,
            'angular_dimensions': 2,
        }

        num_of_lines_sec = {
            'horizontal_lines': 7,
            'vertical_lines': 2,
            'inclined_lines': 4,
            'horizontal_dimensions': 3,
            'vertical_dimensions': 1,
            'angular_dimensions': 2,
        }

        num_of_lines_half_sec = {
            'horizontal_lines': 6,
            'vertical_lines': 4,
            'inclined_lines': 4,
            'horizontal_dimensions': 3,
            'vertical_dimensions': 1,
            'angular_dimensions': 2,
        }

        num_of_lines_front = {'circles': 3, 'phi_dimensions': 0}

        super().__init__(View(**num_of_lines_view),
                         Section(**num_of_lines_sec),
                         HalfSection(**num_of_lines_half_sec),
                         FrontView(**num_of_lines_front))
        self.height = height
        self.teeth_no = teeth_no
        self.module = module
#         self.diameter = round(module * (teeth_no + 2)) # Grzegorz - usuwam z inita i daję do plot 2d
        self.chamfer_length = chamfer_length
        self.chamfer_angle = chamfer_angle
        self._parameters = height, teeth_no, module, chamfer_length, chamfer_angle,
        self._class_description = "with L={}mm, z={}, m={} and chamfer {}x{}".format(
            *(self._parameters))

        self._name['pl'] = 'Koło zębate'
        self._class_description_pl = "o  L={}mm, z={}, m={} i fazie {}x{}".format(
            *self._parameters)

    def str_en(self):
        return f'Gear with teeth number {self.teeth_no}, \n  module {self.module}, width {self.height} \n and {self.chamfer_length}x{self.chamfer_angle} chamfers on both sides'


#         super().__init__(View(horizontal_lines,vertical_lines,diagonal_lines,horizontal_dimensions,vertical_dimensions,diagonal_dimensions))

    def str_pl(self):
        return f'Koło zębate o liczbie zębów {self.teeth_no}, \n module {self.module} oraz szerokości {self.height} \n z fazą {self.chamfer_length}x{self.chamfer_angle} po obu stronach'

    def _plot_2d(self,language='en'):

        #         print(f'self.origin property is {self.origin()}')
        #         print(f'self.end property is {self.end()}')

        class_name = self.__class__.__name__

        span = np.linspace(0, len(class_name), 100)
#         print(f'plot_2d is called for {class_name}')

        r = round(self.module * (self.teeth_no + 2)) / 10 /2
        rp =round(self.module * (self.teeth_no)) / 10 / 2
        l = self.height / 10
        origin = self.origin / 10
        end = self.end / 10
        
        t_l = origin + l / 4
        t_r = (r + 2.5)

        res = GeometryScene.ax_2d.plot(
            [origin + 0, origin + 0, origin + l, origin + l, origin + 0],
            [-r, r, r, -r, -r],
            color='tab:pink') + GeometryScene.ax_2d.plot(
            [origin - 0.5, origin + l + 0.5],
            [0,0],'-.',
            color='k', linewidth = 1) + GeometryScene.ax_2d.plot(
            [origin - 0.5, origin + l + 0.5],
            [-rp,-rp],'-.',
            color='k', linewidth = 1) + GeometryScene.ax_2d.plot(
            [origin - 0.5, origin + l + 0.5],
            [rp,rp],'-.',
            color='k', linewidth = 1) #Jaś Fasola
        
        
        if language == 'pl':
            text = GeometryScene.ax_2d.text(t_l,t_r,self.str_pl(),rotation='vertical',multialignment='center')
        else:
            text = GeometryScene.ax_2d.text(t_l,t_r,self.str_en(),rotation='vertical',multialignment='center')
        
        
        ShaftPreview(5,5,origin/2 ,[2*r/2, l/2, "bez fazy", 0.2, '#6b7aa1'])
        
        print(res)

class HexagonalPrism(Solid):

    def __init__(self, height, indiameter):

        num_of_lines_view = {
            'horizontal_lines': 5,
            'vertical_lines': 2,
            'inclined_lines': 0,
            'horizontal_dimensions': 1,
            'vertical_dimensions': 1,
            'angular_dimensions': 0,
        }

        num_of_lines_sec = {
            'horizontal_lines': 3,
            'vertical_lines': 2,
            'inclined_lines': 0,
            'horizontal_dimensions': 1,
            'vertical_dimensions': 1,
            'angular_dimensions': 0,
        }

        num_of_lines_half_sec = {
            'horizontal_lines': 4,
            'vertical_lines': 2,
            'inclined_lines': 0,
            'horizontal_dimensions': 1,
            'vertical_dimensions': 1,
            'angular_dimensions': 0,
        }

        num_of_lines_front = {'circles': 1, 'phi_dimensions': 0}  # to improve

        super().__init__(View(**num_of_lines_view),
                         Section(**num_of_lines_sec),
                         HalfSection(**num_of_lines_half_sec),
                         FrontView(**num_of_lines_front))

        self.height = height
        self.indiameter = indiameter
        self.diameter = round(indiameter * 0.5)
        self._parameters = height, indiameter,
        self._class_description = "with L={}mm and wrench size ={}".format(
            *(self._parameters))

        self._name['pl'] = 'Łeb śruby bez sfazowania'
        self._class_description_pl = "o  L={}mm i wymiarze pod klucz ={}".format(
            *self._parameters)

    def str_en(self):
        return 'Hexagonal prism \n with L={length}mm and internal diameter {d}mm '.format(
            length=self.height,
            d=self.indiameter,
            )

    def str_pl(self):
        return 'Łeb sześciokątny \n o L={length}mm i wymiarze pod klucz {d}mm'.format(
            length=self.height,
            d=self.indiameter,
            )
        
    def _plot_2d(self,language='en'):

        #         print(f'self.origin property is {self.origin()}')
        #         print(f'self.end property is {self.end()}')

        class_name = self.__class__.__name__

        span = np.linspace(0, len(class_name), 100)
#         print(f'plot_2d is called for {class_name}')

        r = self.indiameter / 2 / 10
        l = self.height / 10
        origin = self.origin / 10
        end = self.end / 10
        
        t_l = origin + l / 4
        t_r = (r + 0.5)

        res = GeometryScene.ax_2d.plot(
            [origin + 0, origin + 0, origin + l, origin + l, origin + 0],
            [-r, r, r, -r, -r],
            color='g') + GeometryScene.ax_2d.plot(
            [origin - 0.5, origin + l + 0.5],
            [0,0],'-.',
            color='g', linewidth = 1)
        
        if language == 'pl':
            text = GeometryScene.ax_2d.text(t_l,t_r,self.str_pl(),rotation='vertical',multialignment='center')
        else:
            text = GeometryScene.ax_2d.text(t_l,t_r,self.str_en(),rotation='vertical',multialignment='center')
        
        
        HexPreview(5,5,origin/2 ,[2*r/2, l/2, "bez fazy", 0.6, '#6b7aa1'])
        
        print(res)

class ChamferedHexagonalPrism(HexagonalPrism):

    def __init__(self,
                 height,
                 indiameter,
                 chamfer_length=1,
                 chamfer_angle=45,
                 chamfer_pos='left'):

        num_of_lines_view = {
            'horizontal_lines': 5,
            'vertical_lines': 2,
            'inclined_lines': 2,
            'arcs': 3,
            'horizontal_dimensions': 2,
            'vertical_dimensions': 1,
            'angular_dimensions': 1,
        }

        num_of_lines_sec = {
            'horizontal_lines': 3,
            'vertical_lines': 2,
            'inclined_lines': 2,
            'arcs': 0,
            'horizontal_dimensions': 2,
            'vertical_dimensions': 1,
            'angular_dimensions': 1,
        }

        num_of_lines_half_sec = {
            'horizontal_lines': 4,
            'vertical_lines': 2,
            'inclined_lines': 2,
            'arcs': 2,
            'horizontal_dimensions': 2,
            'vertical_dimensions': 1,
            'angular_dimensions': 1,
        }

        num_of_lines_front = {'circles': 1, 'phi_dimensions': 0}  # to improve

        super().__init__(height=height, indiameter=indiameter)

        self._views = {
            'view': View(**num_of_lines_view),
            'section': Section(**num_of_lines_sec),
            'halfsection': HalfSection(**num_of_lines_half_sec),
            'front_view': FrontView(**num_of_lines_front)
        }

        self.chamfer_length = chamfer_length
        self.chamfer_angle = chamfer_angle
        #         self.chamfer=chamfer

        self._parameters = height, indiameter, chamfer_length
        self._class_description = " with L={}mm , wrench size ={} and chamfer = {} on the left side".format(
            *(self._parameters))

        self._name['pl'] = 'Łeb śruby ze sfazowaniem'
        self._class_description_pl = " o  L={}mm, wymiarze pod klucz ={} oraz sfazowaniu = {} po lewej stronie".format(
            *self._parameters)

    def str_en(self):
        return 'Hexagonal prism \n with L={length}mm, wrench size S={d} \n and chamfer {l_ch}x{angle}'.format(
            length=self.height,
            d=self.indiameter,
            angle=self.chamfer_angle,
            l_ch=self.chamfer_length,
            )

    def str_pl(self):
        return 'Łeb sześciokątny \n o L={length}mm, wymiarze pod klucz S={d}mm \n i fazie {l_ch}x{angle}'.format(
            length=self.height,
            d=self.indiameter,
            angle=self.chamfer_angle,
            l_ch=self.chamfer_length,
            )
        
    def _plot_2d(self,language='en'):

        #         print(f'self.origin property is {self.origin()}')
        #         print(f'self.end property is {self.end()}')

        class_name = self.__class__.__name__

        span = np.linspace(0, len(class_name), 100)
#         print(f'plot_2d is called for {class_name}')

        r = self.indiameter / 2 / 10
        l = self.height / 10
        origin = self.origin / 10
        end = self.end / 10
        
        t_l = origin # + l / 9
        t_r = (r + 0.5)

        res = GeometryScene.ax_2d.plot(
            [origin + 0, origin + 0, origin + l, origin + l, origin + 0],
            [-r, r, r, -r, -r],
            color='g') + GeometryScene.ax_2d.plot(
            [origin - 0.5, origin + l + 0.5],
            [0,0],'-.',
            color='g', linewidth = 1) +  GeometryScene.ax_2d.plot(
            [origin + 0, origin + l],
            [r*0.6,r*0.6], color='g') + GeometryScene.ax_2d.plot(
            [origin + 0, origin + l],
            [-r*0.6,-r*0.6], color='g')
        
        if language == 'pl':
            text = GeometryScene.ax_2d.text(t_l,t_r,self.str_pl(),rotation='vertical',multialignment='center')
        else:
            text = GeometryScene.ax_2d.text(t_l,t_r,self.str_en(),rotation='vertical',multialignment='center')
        
        
        #ShaftPreview(5,5,origin/2 ,[2*r/2, l/2, "bez fazy", 0.2, '#6b7aa1'])
        HexPreview(5,5,origin/2 ,[2*r/2, l/2, "bez fazy", 0.2, '#6b7aa1'])
        
        print(res)

class FlangeWithHoles(Solid):

    def __init__(self,
                 height,
                 diameter,
                 hole_diameter,
                 reference_diameter,
                 holes_no,
                 chamfer_length=1,
                 chamfer_angle=45):

        num_of_lines_view = {
            'horizontal_lines': 5,
            'vertical_lines': 4,
            'inclined_lines': 4,
            'horizontal_dimensions': 3,
            'vertical_dimensions': 1,
            'angular_dimensions': 2,
        }

        num_of_lines_sec = {
            'horizontal_lines': 9,
            'vertical_lines': 2,
            'inclined_lines': 4,
            'horizontal_dimensions': 3,
            'vertical_dimensions': 2,
            'angular_dimensions': 2,
        }

        num_of_lines_half_sec = {
            'horizontal_lines': 7,
            'vertical_lines': 4,
            'inclined_lines': 4,
            'horizontal_dimensions': 3,
            'vertical_dimensions': 2,
            'angular_dimensions': 2,
        }

        num_of_lines_front = {'circles': 2 + holes_no, 'phi_dimensions': 0}

        super().__init__(View(**num_of_lines_view),
                         Section(**num_of_lines_sec),
                         HalfSection(**num_of_lines_half_sec),
                         FrontView(**num_of_lines_front))
        self.height = height
        self.diameter = diameter
        self.hole_diameter = hole_diameter
        self.reference_diameter = reference_diameter
        self.holes_no = holes_no
        self.chamfer_length = chamfer_length
        self.chamfer_angle = chamfer_angle
        self._parameters = height, diameter, hole_diameter, reference_diameter, holes_no, chamfer_length, chamfer_angle
        self._class_description = "with L={}mm, D={}, hole diameter={}, reference diameter of hole pattern={}, holes number={} and chamfers {}x{} on both sides".format(
            *(self._parameters))

        self._name['pl'] = 'Kołnierz z otworami'
        self._class_description_pl = "o  L={}mm, D={}, średnicy otworu={}, średnicy rozmieszczenia otworów={}, liczbie otworów={} i fazach {}x{} po obu stronach".format(
            *self._parameters)

    def str_en(self):
        return "Flange /n with open holes with L={}mm, D={}, hole diameter={}, \n reference diameter of hole pattern={}, holes number={} \n and chamfers {}x{} on both sides".format(
            *(self._parameters))

    def str_pl(self):
        return "Kołnierz z przelotowymi otworami \n o  L={}mm, D={}, średnicy otworu={}, \n średnicy rozmieszczenia otworów={}, liczbie otworów={} \n i fazach {}x{} po obu stronach".format(
            *self._parameters)

    def _plot_2d(self,language='en'):

        class_name = self.__class__.__name__

        span = np.linspace(0, len(class_name), 100)
#         print(f'plot_2d is called for {class_name}')

        r = self.diameter / 2 / 10
        l = self.height / 10
        r_h = self.hole_diameter / 2 / 10
        r_r = self.reference_diameter / 2 / 10
        holes_no= self.holes_no
        c_l = self.chamfer_length / 10
        c_a = self.chamfer_angle
        c_h=c_l * np.tan(c_a)
        
        origin = self.origin / 10
        end = self.end / 10
        
        t_l = origin + l / 4
        t_r = (r + 0.5)

        res = GeometryScene.ax_2d.plot(
            [origin - 0.5, origin + l + 0.5],[0,0],'-.', color='k', linewidth = 1) + GeometryScene.ax_2d.plot(
                [origin + 0, origin + 0, origin + l, origin + l, origin + 0],[-r,r,r,-r,-r],color='m') + GeometryScene.ax_2d.plot(
                    [origin + 0, origin + 0, origin + l, origin + l, origin + 0],[r_r-r_h,r_r+r_h,r_r+r_h,r_r-r_h,r_r-r_h],'--',color='m',linewidth = 1) + GeometryScene.ax_2d.plot(
                        [origin - 0.5, origin + l + 0.5],[r_r+0,r_r+0],'-.', color='k', linewidth = 1) + GeometryScene.ax_2d.plot(
                               [origin + 0, origin + 0, origin + l, origin + l, origin + 0],[-r_r-r_h,-r_r+r_h,-r_r+r_h,-r_r-r_h,-r_r-r_h],'--',color='m',linewidth = 1) + GeometryScene.ax_2d.plot(
                                    [origin - 0.5, origin + l + 0.5],[-r_r+0,-r_r+0],'-.', color='k', linewidth = 1)

        text = GeometryScene.ax_2d.text(t_l,t_r,self.str_en(),rotation='vertical',multialignment='center')
        
        
        ShaftPreview(5,5,origin/2 ,[2*r/2, l/2, "bez fazy", 0.2, '#6b7aa1'])
        
        for hole_no in range(holes_no):
            
            xh = r_r * np.cos(hole_no*2*np.pi/holes_no)
            yh = r_r * np.sin(hole_no*2*np.pi/holes_no)
            
            ShaftPreview(5+xh,5+yh,origin/2 ,[2*r_h/2, l/2, "bez fazy", 0.2, '#6b7aa1'])
            
        
        print(res)

class BlockBearingHolder(Solid):
    """
    Block with hole in every corner and bearing place on the top. It's drawn in the horizontal position (symmetry axis is horizontal line).
    """

    def __init__(self, height, width, length):

        self.height = height
        self.width = width
        self.length = length
        self._parameters = height, width, length

        num_of_lines_view = {
            'horizontal_lines': 2 + 1,  #axis included
            'vertical_lines': 2,  #axis excluded
            'inclined_lines': 0,
            'horizontal_dimensions': 1,
            'vertical_dimensions': 1,
            'angular_dimensions': 0,
        }

        num_of_lines_sec = {
            'horizontal_lines': 2 + 1,  #axis included
            'vertical_lines': 2,  #axis excluded
            'inclined_lines': 0,
            'horizontal_dimensions': 1,
            'vertical_dimensions': 1,
            'angular_dimensions': 0,
        }

        num_of_lines_half_sec = {
            'horizontal_lines': 2 + 1,  #axis included
            'vertical_lines': 2,  #axis excluded
            'inclined_lines': 0,
            'horizontal_dimensions': 1,
            'vertical_dimensions': 1,
            'angular_dimensions': 0,
        }

        num_of_lines_front = {
            'horizontal_lines': 2,  #axis excluded
            'vertical_lines': 2,  #axis exclueded
            'inclined_lines': 0,
            'horizontal_dimensions': 2,
            'vertical_dimensions': 1,
            'angular_dimensions': 0,
        }

        super().__init__(View(**num_of_lines_view),
                         Section(**num_of_lines_sec),
                         HalfSection(**num_of_lines_half_sec),
                         FrontView(**num_of_lines_front))

    def str_en(self):
        return f"Block with H={self.height}mm, W={self.width}mm and L={self.length}mm where H is height, W is width and L is length (depth looking from the front view)"

    def str_pl(self):
        return f"Blok o H={self.height}mm, W={self.width}mm i L={self.length}mm"


class BlockEdgeFillet(Solid):
    """
    Block with rounded corners.  It's drawn in the horizontal position (symmetry axis is horizontal line).
    """

    def __init__(self, height, width, length, fillet_radius=2):

        self.height = height
        self.width = width
        self.length = length
        self.fillet_radius = fillet_radius
        self._parameters = height, width, length, fillet_radius

        num_of_lines_view = {
            'horizontal_lines': 3,  #axis included
            'vertical_lines': 2,  #axis excluded
            'inclined_lines': 0,
            'horizontal_dimensions': 1,
            'vertical_dimensions': 1,
            'angular_dimensions': 0,
        }

        num_of_lines_sec = {
            'horizontal_lines': 3,  #axis included
            'vertical_lines': 2,  #axis excluded
            'inclined_lines': 0,
            'horizontal_dimensions': 1,
            'vertical_dimensions': 1,
            'angular_dimensions': 0,
        }

        num_of_lines_half_sec = {
            'horizontal_lines': 3,  #axis included
            'vertical_lines': 2,  #axis excluded
            'inclined_lines': 0,
            'horizontal_dimensions': 1,
            'vertical_dimensions': 1,
            'angular_dimensions': 0,
        }

        num_of_lines_front = {
            'horizontal_lines': 2,  #axis excluded
            'vertical_lines': 2,  #axis exclueded
            'inclined_lines': 0,
            'horizontal_dimensions': 2,
            'vertical_dimensions': 0,
            'phi_dimensions': 1,
            'arcs': 2,
        }

        super().__init__(View(**num_of_lines_view),
                         Section(**num_of_lines_sec),
                         HalfSection(**num_of_lines_half_sec),
                         FrontView(**num_of_lines_front))

    def str_en(self):
        return f"Block with H={self.height}mm, W={self.width}mm, L={self.length}mm and fillet top edges R={self.fillet_radius}mm where H is height, W is width and L is length (depth looking from the front view) "

    def str_pl(self):
        return f"Blok o H={self.height}mm, W={self.width}mm, L={self.length}mm oraz zaokrąglonych górnych krawędziach R={self.fillet_radius}mm"


class BlockInverseTShape(Solid):
    """
    Block with shape of inverted T.  It's drawn in the horizontal position (symmetry axis is horizontal line).
    """

    def __init__(self, height, width, length, cut_height, cut_width):

        self.height = height
        self.width = width
        self.length = length
        self.cut_height = cut_height
        self.cut_width = cut_width
        self._parameters = height, width, length, cut_height, cut_width

        num_of_lines_view = {
            'horizontal_lines': 5,  #axis included
            'vertical_lines': 2,  #axis excluded
            'inclined_lines': 0,
            'horizontal_dimensions': 1,
            'vertical_dimensions': 1,
            'angular_dimensions': 0,
        }

        num_of_lines_sec = {
            'horizontal_lines': 4,  #axis included
            'vertical_lines': 2,  #axis excluded
            'inclined_lines': 0,
            'horizontal_dimensions': 1,
            'vertical_dimensions': 1,
            'angular_dimensions': 0,
        }

        num_of_lines_half_sec = {
            'horizontal_lines': 3,  #axis included
            'vertical_lines': 2,  #axis excluded
            'inclined_lines': 0,
            'horizontal_dimensions': 1,
            'vertical_dimensions': 1,
            'angular_dimensions': 0,
        }

        num_of_lines_front = {
            'horizontal_lines': 4,  #axis excluded
            'vertical_lines': 4,  #axis excluede
            'inclined_lines': 0,
            'horizontal_dimensions': 3,
            'vertical_dimensions': 1,
            'angular_dimensions': 0,
            'arcs': 0,
        }

        super().__init__(View(**num_of_lines_view),
                         Section(**num_of_lines_sec),
                         HalfSection(**num_of_lines_half_sec),
                         FrontView(**num_of_lines_front))

    def str_en(self):
        return f"Block with H={self.height}mm, W={self.width}mm, L={self.length}mm, symmetrical cut out (starting from the top of block) with H={self.cut_height}mm and W={self.cut_width}mm which makes the block look like inverted T and where H is height, W is width and L is length (depth looking from the front view)"

    def str_pl(self):
        return f"Blok o H={self.height}mm, W={self.width}mm, L={self.length}mm oraz symetrycznym wcięciu (licząc od górnej krawędzi bloku) o H={self.cut_height}mm i W={self.cut_width}mm co sprawia, że blok wygląda jak odwrócona litera T"


class DoubleChamferedHexagonalPrism(HexagonalPrism):

    def __init__(self,
                 height,
                 indiameter,
                 chamfer_length=1,
                 chamfer_angle=45,
                 chamfer_pos='left'):

        num_of_lines_view = {
            'horizontal_lines': 5,  #axis included
            'vertical_lines': 2,
            'inclined_lines': 4,
            'arcs': 6,
            'horizontal_dimensions': 3,
            'vertical_dimensions': 1,
            'angular_dimensions': 2,
        }

        num_of_lines_sec = {
            'horizontal_lines': 3,  #axis included
            'vertical_lines': 2,
            'inclined_lines': 4,
            'arcs': 0,
            'horizontal_dimensions': 3,
            'vertical_dimensions': 1,
            'angular_dimensions': 2,
        }

        num_of_lines_half_sec = {
            'horizontal_lines': 4,  # axis included
            'vertical_lines': 2,
            'inclined_lines': 4,
            'arcs': 4,
            'horizontal_dimensions': 3,
            'vertical_dimensions': 1,
            'angular_dimensions': 2,
        }

        num_of_lines_front = {'circles': 1, 'phi_dimensions': 0}  # to improve

        super().__init__(height=height, indiameter=indiameter)

        self._views = {
            'view': View(**num_of_lines_view),
            'section': Section(**num_of_lines_sec),
            'halfsection': HalfSection(**num_of_lines_half_sec),
            'front_view': FrontView(**num_of_lines_front)
        }

        self.chamfer_length = chamfer_length
        self.chamfer_angle = chamfer_angle
        #         self.chamfer=chamfer

        self._parameters = height, indiameter, chamfer_length
        self._class_description = " with L={}mm , wrench size ={} and chamfers = {} on the both sides".format(
            *(self._parameters))

        self._name['pl'] = 'Łeb śruby ze sfazowaniem'
        self._class_description_pl = " o  L={}mm, wymiarze pod klucz ={} oraz sfazowaniu = {} po obu stronach".format(
            *self._parameters)

    def str_en(self):
        return 'Hexagonal prism \n with L={length}mm, wrench size S={d} \n and chamfer {l_ch}x{angle} \n on the both sides'.format(
            length=self.height,
            d=self.indiameter,
            angle=self.chamfer_angle,
            l_ch=self.chamfer_length,
            )

    def str_pl(self):
        return 'Łeb sześciokątny \n o L={length}mm, wymiarze pod klucz S={d}mm \n i fazie {l_ch}x{angle} \n po oby stronach'.format(
            length=self.height,
            d=self.indiameter,
            angle=self.chamfer_angle,
            l_ch=self.chamfer_length,
            )
        
    def _plot_2d(self,language='en'):

        #         print(f'self.origin property is {self.origin()}')
        #         print(f'self.end property is {self.end()}')

        class_name = self.__class__.__name__

        span = np.linspace(0, len(class_name), 100)
#         print(f'plot_2d is called for {class_name}')

        r = self.indiameter / 2 / 10
        l = self.height / 10
        origin = self.origin / 10
        end = self.end / 10
        
        t_l = origin + l 
        t_r = (r + 0.5)

        res = GeometryScene.ax_2d.plot(
            [origin + 0, origin + 0, origin + l, origin + l, origin + 0],
            [-r, r, r, -r, -r],
            color='tab:purple') + GeometryScene.ax_2d.plot(
            [origin - 0.5, origin + l + 0.5],
            [0,0],'-.',
            color='k', linewidth = 1) +  GeometryScene.ax_2d.plot(
            [origin + 0, origin + l],
            [r*0.6,r*0.6], color='tab:purple') + GeometryScene.ax_2d.plot(
            [origin + 0, origin + l],
            [-r*0.6,-r*0.6], color='tab:purple')
        
        if language == 'pl':
            text = GeometryScene.ax_2d.text(t_l,t_r,self.str_pl(),rotation='vertical',multialignment='center')
        else:
            text = GeometryScene.ax_2d.text(t_l,t_r,self.str_en(),rotation='vertical',multialignment='center')
        
        
        #ShaftPreview(5,5,origin/2 ,[2*r/2, l/2, "bez fazy", 0.2, '#6b7aa1'])
        HexPreview(5,5,origin/2 ,[2*r/2, l/2, "bez fazy", 0.2, '#6b7aa1'])
        
        print(res)