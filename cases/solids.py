import matplotlib.pyplot as plt
from ..dgeometry import GeometryScene
import numpy as np
from numbers import Number

import numpy as np
from matplotlib.patches import Circle
from matplotlib.patches import RegularPolygon, Polygon
import mpl_toolkits.mplot3d.art3d as art3d
import matplotlib.pyplot as plt
SPACE_BTW=250

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
                self.shaft_steps_sides((self.x0, self.y0), self.data[-1][0],
                                       self.total_length, self.data[i][3])
                self.total_length = 0
            self.shaft_steps_sides((self.x0, self.y0), self.data[i][0],
                                   self.z0, self.data[i][3])
            self.total_length += self.data[i][1]
        self.shaft_steps_sides((self.x0, self.y0), self.data[-1][0],
                               self.z0 + self.total_length, self.data[i][3])
        self.total_length = 0

        for i in range(len(self.data)):
            if i == 5:
                self.total_length = 0
            self.Xc, self.Yc, self.Zc = self.data_for_cylinder_along_z(
                self.x0, self.y0, self.data[i][0], self.data[i][1], self.z0)

            self.total_length += self.data[i][1]
            self.ax.plot_surface(self.Xc,
                                 self.Yc,
                                 self.Zc,
                                 alpha=self.data[i][3],
                                 color=self.data[i][4],
                                 edgecolor="black")
            self.ax.scatter(0, 0, 0)
            self.ax.scatter(10, 10, 10,marker='None')

       
            
    def shaft_steps_sides(self, begin_cords, radius, zlength, transparency):

        # Draw a circle on the x axis 'wall'
        p = Circle(begin_cords, radius, alpha=transparency, color='#6b7aa1')
        self.ax.add_patch(p)
        art3d.pathpatch_2d_to_3d(p, z=zlength, zdir="x")


    def data_for_cylinder_along_z(self,center_z, center_y, radius, height_x, x_begin):
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
                self.shaft_steps_sides((self.x0, self.y0), self.data[-1][0],
                                       self.total_length, self.data[i][3])
                self.total_length = 0
            self.shaft_steps_sides((self.x0, self.y0), self.data[i][0],
                                   self.z0, self.data[i][3])
            self.total_length += self.data[i][1]
        self.shaft_steps_sides((self.x0, self.y0), self.data[-1][0],
                               self.z0 + self.total_length, self.data[i][3])
        self.total_length = 0

        for i in range(len(self.data)):
            if i == 5:
                self.total_length = 0
            self.Xc, self.Yc, self.Zc = self.data_for_cylinder_along_z(
                self.x0, self.y0, self.data[i][0], self.data[i][1], self.z0)

            self.total_length += self.data[i][1]
            self.ax.plot_surface(self.Xc,
                                 self.Yc,
                                 self.Zc,
                                 alpha=self.data[i][3],
                                 color=self.data[i][4],
                                 edgecolor="black")
        self.ax.scatter(10, 0, 0)

    def shaft_steps_sides(self, begin_cords, radius, zlength, transparency):

        # Draw a circle on the x axis 'wall'
        p = RegularPolygon(begin_cords,
                           6,
                           1.2 * radius,
                           alpha=0.6,
                           color='#6b7aa1')
        self.ax.add_patch(p)

        art3d.pathpatch_2d_to_3d(p, z=zlength, zdir="x")


    def data_for_cylinder_along_z(self,center_z, center_y, radius, height_x, x_begin):
        x = np.linspace(x_begin, x_begin + height_x, 500)
        theta = np.linspace(0, 2 * np.pi, 500)
        theta_grid, x_grid = np.meshgrid(theta, x)
        z_grid = radius * np.cos(theta_grid) + center_z
        y_grid = radius * np.sin(theta_grid) + center_y
        return x_grid, y_grid, z_grid


class BlockPreview:

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
        
        self.contour= args[0]
        self.height =args[1]
        
        


        self.total_length = 0

        self.shaft_steps_sides((self.x0, self.y0), None  ,z0,transparency=0.6)
        

        self.Xc, self.Yc, self.Zc = self.data_for_cylinder_along_z(
                self.x0, self.y0,10, self.height, self.z0)


        self.ax.plot_surface(self.Xc,
                             self.Yc,
                             self.Zc,
                             alpha=0.2,
                             color='#6b7aa1',
                             edgecolor="black")
        
        self.shaft_steps_sides((self.x0, self.y0), None  ,z0+self.height,transparency=0.6)
        self.ax.scatter(10, 0, 0)

    def shaft_steps_sides(self, begin_cords, radius, zlength, transparency):

        # Draw a circle on the x axis 'wall'
        p = Polygon(self.contour,
                           alpha=0.6,
                           color='#6b7aa1')

        self.ax.add_patch(p)

        art3d.pathpatch_2d_to_3d(p, z=zlength, zdir="x")


    def data_for_cylinder_along_z(self,center_z, center_y, radius, height_x, x_begin):
        x = np.linspace(x_begin, x_begin + height_x, 2)
        theta = np.arange(len(self.contour))
        theta_grid, x_grid = np.meshgrid(theta, x)
        z_grid = self.contour[:,1][theta_grid] + center_z
        y_grid = self.contour[:,0][theta_grid]  + center_y
        
        
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

        self._ref_elem = None
        self._origin = 0

    @property
    def origin(self):

        if self._ref_elem is not None:
            origin = self._ref_elem.end
        else:
            origin = self._origin


#         print(origin)
        return origin

    @property
    def end(self):

        end = self.origin + self.height

        #         print('end =' + str(end))
        return end

    def _plot_2d(self, language='en'):

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

    def preview(self, example=False, language='en'):

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

        r_b = self.bottom_diameter / 2 / 10
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
                [origin - 0.5, origin + l + 0.5], [0, 0],
                '-.',
                color='k',
                linewidth=1)
        text = GeometryScene.ax_2d.text(t_l,
                                        t_r,
                                        self.str_en(),
                                        rotation='vertical',
                                        multialignment='center')

        ShaftPreview(0,0, origin / 2,
                     [2 * r_t / 2, l / 2, "bez fazy", 0.2, '#6b7aa1'])


class Cylinder(Solid):
    """This object represents cylinder solid.
    
    The cylinder object has predefined numbers of lines and dimensions that are needed 
    make a engineering drawing. Also it stores information about height and diameter.
    
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
    color = 'k'

    num_of_lines_view = {
        'horizontal_lines': 3,
        'vertical_lines': 2,
        'horizontal_dimensions': 1,
        'vertical_dimensions': 1,
        'inclined_lines': 0,
    }
    num_of_lines_sec = {
        'horizontal_lines': 3,
        'vertical_lines': 2,
        'horizontal_dimensions': 1,
        'vertical_dimensions': 1,
        'inclined_lines': 0,
    }

    num_of_lines_half_sec = {
        'horizontal_lines': 3,
        'vertical_lines': 2,
        'horizontal_dimensions': 1,
        'vertical_dimensions': 1,
        'inclined_lines': 0,
    }

    num_of_lines_front = {'circles': 1, 'phi_dimensions': 0}

    def __init__(self, height, diameter):
        super().__init__(View(**self.__class__.num_of_lines_view),
                         Section(**self.__class__.num_of_lines_sec),
                         HalfSection(**self.__class__.num_of_lines_half_sec),
                         FrontView(**self.__class__.num_of_lines_front))
        self.height = height
        self.diameter = diameter
        self._parameters = height, diameter

    def str_en(self):
        return f'Cylinder\nwith L={self.height}mm\nand diameter={self.diameter}mm'

    def str_pl(self):
        return f'Walec\no L={self.height}mm\ni średnicy={self.diameter}mm'

    def _plot_2d(self, language='en'):
        self._plot_2d_view(language=language)
        self._plot_2d_section(language=language)
        
        origin, r, l = self.origin/5, self.diameter/2/5, self.height/5
        ShaftPreview(0, 0, origin/2, [r, l, "Walec", 0.2, '#6b7aa1'])

    def _plot_2d_view(self, language='en'):
        """Góra: Widok + JEDYNY OPIS"""
        origin, r, l = self.origin/5, self.diameter/2/5, self.height/5

        # --- OBLICZENIE STYKU Z SĄSIADEM ---
        prev_r = 0
        if getattr(self, 'prev_elem', None) is not None:
            prev_r = getattr(self.prev_elem, 'diameter', 0) / 10
            
            # Sprawdzamy czy sąsiad ma fazę
            if hasattr(self.prev_elem, 'chamfer_pos') and getattr(self.prev_elem, 'chamfer_pos') in ['right', 'both']:
                # BEZPIECZNE POBIERANIE WARTOSCI: Jeśli nie ma chamfer_length, podstaw 0
                n_cl = getattr(self.prev_elem, 'chamfer_length', 0) / 5
                n_ca = getattr(self.prev_elem, 'chamfer_angle', 45)
                
                n_ch = n_cl * np.tan(np.radians(n_ca))
                prev_r -= n_ch

        x_pts, y_pts = [], []
        
        # Start od osi (żeby narysować pełne czoło wału) i przejście do promienia sąsiada
        x_pts.extend([origin, origin, origin])
        y_pts.extend([0, prev_r, r])
        
        # Górna krawędź
        x_pts.append(origin + l)
        y_pts.append(r)
        
        # --- ZMIANA: INTELIGENTNE ZAMYKANIE PRAWEJ KRAWĘDZI ---
        # Sprawdzamy, czy następny element to twardy materiał (nie "powietrze" czyli Hole)
        next_is_solid = self.next_elem is not None and 'Hole' not in type(self.next_elem).__name__
        
        # Zjazd do osi jeśli kończymy wał albo zaczyna się otwór
        if not next_is_solid:
            x_pts.append(origin + l)
            y_pts.append(0)

        res = GeometryScene.ax_2d.plot(x_pts, y_pts, color='k', linewidth=1, zorder=3)
        res += GeometryScene.ax_2d.plot([origin-1, origin+l+1], [0, 0], linestyle=(0, (25, 10, 2, 10)), color='k', linewidth=0.5, zorder=3)

        # OPIS TYLKO TUTAJ (Nad obiektem)
        label = self.str_pl() if language == 'pl' else self.str_en()
        GeometryScene.ax_2d.text(origin + l/2, r + 5, label,
                                 rotation='vertical', multialignment='center', 
                                 va='bottom', ha='center', color='k')
        return res

    def _plot_2d_section(self, language='en'):
        """Dół: Przekrój (szrafowanie + inteligentny obrys ze schodkami)"""
        origin, r, l = self.origin/5, self.diameter/2/5, self.height/5

        # Kreskowanie
        GeometryScene.ax_2d.fill_between([origin, origin+l], [0, 0], [-r, -r], 
                                         facecolor='none', hatch='//', edgecolor='k', linewidth=0, alpha=0.3, zorder=1)
        
        # --- OBLICZENIE STYKU Z SĄSIADEM ---
        prev_r = 0
        if getattr(self, 'prev_elem', None) is not None:
            prev_r = getattr(self.prev_elem, 'diameter', 0) / 10
            
            # Sprawdzamy czy sąsiad ma fazę
            if hasattr(self.prev_elem, 'chamfer_pos') and getattr(self.prev_elem, 'chamfer_pos') in ['right', 'both']:
                # BEZPIECZNE POBIERANIE WARTOSCI: Jeśli nie ma chamfer_length, podstaw 0
                n_cl = getattr(self.prev_elem, 'chamfer_length', 0) / 5
                n_ca = getattr(self.prev_elem, 'chamfer_angle', 45)
                
                n_ch = n_cl * np.tan(np.radians(n_ca))
                prev_r -= n_ch

        # --- INTELIGENTNY OBRYS ---
        x_pts = []
        y_pts = []
        
        # LEWA STRONA: Zjazd tylko od skorygowanego promienia sąsiada
        x_pts.extend([origin, origin])
        y_pts.extend([-prev_r, -r])
            
        # DNO
        x_pts.append(origin+l)
        y_pts.append(-r)
        
        # --- ZMIANA: INTELIGENTNE ZAMYKANIE PRAWEJ KRAWĘDZI ---
        next_is_solid = self.next_elem is not None and 'Hole' not in type(self.next_elem).__name__
        
        # Zjazd do zera, jeśli to koniec wału albo zaczyna się otwór
        if not next_is_solid:
            x_pts.append(origin+l)
            y_pts.append(0)

        res = GeometryScene.ax_2d.plot(x_pts, y_pts, color='k', linewidth=1, zorder=3)
        return res
    
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
    color = 'k'

    num_of_lines_view = {
        'horizontal_lines': 1,
        'vertical_lines': 1,
        'horizontal_dimensions': 0,
        'vertical_dimensions': 0,
        'inclined_lines': 0,
    }
    num_of_lines_sec = {
        'horizontal_lines': 3,
        'vertical_lines': 0,
        'horizontal_dimensions': 1,
        'vertical_dimensions': 1,
        'inclined_lines': 0,
    }

    num_of_lines_half_sec = {
        'horizontal_lines': 2,
        'vertical_lines': 0,
        'horizontal_dimensions': 1,
        'vertical_dimensions': 1,
        'inclined_lines': 0,
    }

    num_of_lines_front = {'circles': 1, 'phi_dimensions': 0}

    def str_en(self):
        return 'Shank of the screw \n with diameter={d}mm'.format(
            length=self.height,
            d=self.diameter)


    def str_pl(self):
        return 'Trzpień śruby \n o średnicy={d}mm'.format(
            length=self.height,
            d=self.diameter).replace('right',
                                     'prawej').replace('left', 'lewej')

    def _plot_2d(self, language='en'):

        #         print(f'self.origin property is {self.origin()}')
        #         print(f'self.end property is {self.end()}')

        class_name = self.__class__.__name__

        span = np.linspace(0, len(class_name), 100)
        #         print(f'plot_2d is called for {class_name}')

        r = self.diameter / 2 / 10
        l = self.height / 10
        origin = self.origin / 10
        end = self.end / 10

        t_l = origin + l / 3
        t_r = (r + 10.5)

        line_type = self.line_type
        color = self.color

        res = GeometryScene.ax_2d.plot(
            [origin + 0, origin + 0, origin + l, origin + l, origin + 0],
            [-r, r, r, -r, -r],
            line_type,
            color=color) + GeometryScene.ax_2d.plot(
                [origin - 0.5, origin + l + 0.5], [0, 0],
                '-.',
                color='k',
                linewidth=1)

        if language == 'pl':
            text = GeometryScene.ax_2d.text(t_l,
                                            t_r,
                                            self.str_pl(),
                                            rotation='vertical',
                                            multialignment='center')
        else:
            text = GeometryScene.ax_2d.text(t_l,
                                            t_r,
                                            self.str_en(),
                                            rotation='vertical',
                                            multialignment='center')

        ShaftPreview(0,0, origin / 2,
                     [2 * r / 2, l / 2, "bez fazy", 0.2, '#6b7aa1'])

        print(res)


class Plate(Cylinder):
    """This object represents a plate.

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
    num_of_lines_sec = {
        'horizontal_lines': 3,
        'vertical_lines': 2,
        'horizontal_dimensions': 1,
        'vertical_dimensions': 1,
        'inclined_lines': 0,
    }

    num_of_lines_half_sec = {
        'horizontal_lines': 3,
        'vertical_lines': 2,
        'horizontal_dimensions': 1,
        'vertical_dimensions': 1,
        'inclined_lines': 0,
    }
    def _plot_2d(self, language='en'):

        class_name = self.__class__.__name__

        span = np.linspace(0, len(class_name), 100)

        origin = self.origin / 10
        r = self.diameter / 2 / 10
        l = self.height / 10
        end = self.end / 10

        t_l = origin + l / 8
        t_r = (-r - 13)

        res = GeometryScene.ax_2d.plot([
            origin + 0,
            origin + l,
            origin + l,
            origin + 0,
            origin + 0,
        ], [
            r * 3,
            r * 3,
            -r * 3,
            -r * 3,
            r * 3,
        ],
                                       '-',
                                       color='b')

        if language == 'pl':
            text = GeometryScene.ax_2d.text(t_l,
                                            t_r,
                                            self.str_pl(),
                                            rotation='vertical',
                                            multialignment='center')
        else:
            text = GeometryScene.ax_2d.text(t_l,
                                            t_r,
                                            self.str_en(),
                                            rotation='vertical',
                                            multialignment='center')

        ShaftPreview(0,0, origin / 2,
                     [2 * r / 2, l / 2, "bez fazy", 0.2, '#6b7aa1'])

    def str_en(self):
        return 'Plate \n with thickness t={length}mm \n and width b={d}mm'.format(
            length=self.height, d=2*self.diameter)

    def str_pl(self):
        return 'Płyta \n o grubości g={length}mm i szerokości b={d}mm'.format(
            length=self.height,
            d=2*self.diameter).replace('right',
                                     'prawej').replace('left', 'lewej')


class Hole(Solid):
    """This object represents a hole that can be made inside a solid."""

    num_of_lines_view = {
        'horizontal_lines': 1, 'vertical_lines': 1,
        'horizontal_dimensions': 0, 'vertical_dimensions': 0,
        'inclined_lines': 0,
    }
    num_of_lines_sec = {
        'horizontal_lines': 3, 'vertical_lines': 1,
        'horizontal_dimensions': 1, 'vertical_dimensions': 1,
        'inclined_lines': 0,
    }
    num_of_lines_half_sec = {
        'horizontal_lines': 2, 'vertical_lines': 1,
        'horizontal_dimensions': 1, 'vertical_dimensions': 1,
        'inclined_lines': 0,
    }
    num_of_lines_front = {'circles': 1, 'phi_dimensions': 0}

    def __init__(self, height, diameter):
        super().__init__(View(**self.__class__.num_of_lines_view),
                         Section(**self.__class__.num_of_lines_sec),
                         HalfSection(**self.__class__.num_of_lines_half_sec),
                         FrontView(**self.__class__.num_of_lines_front))
        self.height = height
        self.diameter = diameter

        self._parameters = height, diameter
        self._class_description = "with L={}mm and diameter={}mm".format(*self._parameters)
        self._name['pl'] = 'Otwór'
        self._class_description_pl = "o L={}mm i średnicy ={}mm".format(*self._parameters)
        
        # Puste referencje dla sąsiadów (wypełnia je generator)
        self.prev_elem = None
        self.next_elem = None

    def str_en(self):
        return f'Hole \n with L={self.height}mm \n and diameter={self.diameter}mm'

    def str_pl(self):
        return f'Otwór \n o L={self.height}mm i średnicy={self.diameter}mm'

    def _plot_2d(self, language='en'):
        #self._plot_2d_view(language=language)
        self._plot_2d_section(language=language)
        
        origin, r, l = self.origin / 5, self.diameter / 2 / 5, self.height / 5
        ShaftPreview(0, 0, origin / 2, [r, l, "otwór", 0.7, '#6b7aa1'])

    def _plot_2d_view(self, language='en'):
        """Góra: Widok - zmieniono linię przerywaną na ciągłą. Brak opisu (przeniesiony na dół)."""
        origin, r, l = self.origin / 5, self.diameter / 2 / 5, self.height / 5

        # Zwykła linia ciągła wg. Twoich wytycznych
        x = [origin, origin, origin + l, origin + l]
        y = [0, r, r, 0]
        res = GeometryScene.ax_2d.plot(x, y, linestyle='-', color='k',linewidth=1, zorder=3)
        
        # Cienka oś symetrii z rzadszym wzorem
        res += GeometryScene.ax_2d.plot([origin-1, origin+l+1], [0, 0], 
                                        linestyle=(0, (25, 10, 2, 10)), color='k', linewidth=0.5, zorder=3)
        return res

    def _plot_2d_section(self, language='en'):
        """Dół: Przekrój - maskowanie materiału i dynamiczny opis na dole"""
        origin, r, l = self.origin / 5, self.diameter / 2 / 5, self.height / 5

        # --- INTELIGENTNE ODSUWANIE OPISU ---
        # Szukamy absolutnie największej średnicy w całym wałku!
        max_d = self.diameter
        
        # Skanujemy w lewo
        curr = self.prev_elem
        while curr is not None:
            if getattr(curr, 'diameter', 0) > max_d:
                max_d = curr.diameter
            curr = getattr(curr, 'prev_elem', None)
            
        # Skanujemy w prawo
        curr = self.next_elem
        while curr is not None:
            if getattr(curr, 'diameter', 0) > max_d:
                max_d = curr.diameter
            curr = getattr(curr, 'next_elem', None)
            
        # Skalujemy maksymalny promień do układu rysunku
        max_r = max_d / 2 / 5

        # 1. Biały blok "czyszczący"
        GeometryScene.ax_2d.fill_between(
            [origin, origin + l], 
            [0, 0], 
            [-r, -r], 
            facecolor='white', edgecolor='none', zorder=2
        )
        
        # 2. Widoczny kontur otworu w przekroju
        x_pts = [origin, origin, origin + l, origin + l]
        y_pts = [0, -r, -r, 0]
        res = GeometryScene.ax_2d.plot(x_pts, y_pts, linestyle='-', color='k',linewidth=1, zorder=3)

        # 3. Dynamiczny opis odsunięty poniżej absolutnie najgrubszego cylindra
        label = self.str_pl() if language == 'pl' else self.str_en()
        GeometryScene.ax_2d.text(origin + l/2, -max_r - 5, label, 
                                 rotation='vertical', multialignment='center', 
                                 va='top', ha='center', color='k')
        return res


class OpenHole(Hole):
    """This object represents hole that can be made inside solid."""
    num_of_lines_view = {
        'horizontal_lines': 1, 'vertical_lines': 1,
        'horizontal_dimensions': 0, 'vertical_dimensions': 0,
        'inclined_lines': 0,
    }
    num_of_lines_sec = {
        'horizontal_lines': 3, 'vertical_lines': 0,
        'horizontal_dimensions': 0, 'vertical_dimensions': 1,
        'inclined_lines': 0,
    }

    num_of_lines_half_sec = {
        'horizontal_lines': 2, 'vertical_lines': 0,
        'horizontal_dimensions': 0, 'vertical_dimensions': 1,
        'inclined_lines': 0,
    }

    def str_en(self):
        return 'Open hole \n with diameter={d}mm'.format(length=self.height, d=self.diameter)

    def str_pl(self):
        return 'Przelotowy otwór \n o średnicy={d}mm'.format(
            length=self.height, d=self.diameter).replace('right', 'prawej').replace('left', 'lewej')

    def _plot_2d(self, language='en'):
        self._plot_2d_section(top=False, language=language)

    def _plot_2d_section(self, top=True, language='en'):
        origin, r, l = self.origin / 5, self.diameter / 2 / 5, self.height / 5

        # --- INTELIGENTNE ODSUWANIE OPISU ---
        max_d = self.diameter
        
        curr = getattr(self, 'prev_elem', None)
        while curr is not None:
            if getattr(curr, 'diameter', 0) > max_d: max_d = curr.diameter
            curr = getattr(curr, 'prev_elem', None)
            
        curr = getattr(self, 'next_elem', None)
        while curr is not None:
            if getattr(curr, 'diameter', 0) > max_d: max_d = curr.diameter
            curr = getattr(curr, 'next_elem', None)
            
        max_r = max_d / 2 / 5

        # 1. Biały blok czyszczący
        GeometryScene.ax_2d.fill_between(
            [origin, origin + l], [0, 0], [-r, -r],
            facecolor='white', edgecolor='none', zorder=2
        )

        # --- BEZPIECZNE OBLICZENIE STYKU Z SĄSIADEM ---
        prev_r = 0
        if getattr(self, 'prev_elem', None) is not None:
            prev_r = getattr(self.prev_elem, 'diameter', 0) / 10
            if hasattr(self.prev_elem, 'chamfer_pos') and getattr(self.prev_elem, 'chamfer_pos') in ['right', 'both']:
                n_cl = getattr(self.prev_elem, 'chamfer_length', 0) / 5
                n_ca = getattr(self.prev_elem, 'chamfer_angle', 45)
                n_ch = n_cl * np.tan(np.radians(n_ca))
                prev_r += n_ch

        # 2. Widoczny kontur otworu ze schodkami
        x_pts, y_pts = [], []
        x_pts.extend([origin, origin])
        y_pts.extend([-prev_r, -r])
        
        x_pts.append(origin + l)
        y_pts.append(-r)
        
        if getattr(self, 'next_elem', None) is None:
            x_pts.append(origin + l)
            y_pts.append(0)

        res = GeometryScene.ax_2d.plot(x_pts, y_pts, linestyle='-', color='k', zorder=3)

        # 3. Dynamiczny opis
        label = self.str_pl() if language == 'pl' else self.str_en()
        GeometryScene.ax_2d.text(origin + l/2, -max_r - 5, label, 
                                 rotation='vertical', multialignment='center', 
                                 va='top', ha='center', color='k')

        ShaftPreview(0,0, origin / 2, [2 * r / 2, l / 2, "bez fazy", 0.7, '#6b7aa1'])
        return res
    
class ChamferedHole(Hole):
    """This object represents chamfered hole that can be made inside solid."""

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

    def __init__(self,
                 height,
                 diameter,
                 chamfer_length=None,
                 chamfer_angle=45,
                 chamfer_pos='left'):

        # Inicjalizacja poprzez Hole (automatycznie ustawi słowniki i parametry bazowe)
        super().__init__(height, diameter)

        # Prosta inicjalizacja fazy
        if chamfer_length is None:
            self.chamfer_length = max(1, min(4, round(diameter * 0.05)))
        else:
            self.chamfer_length = chamfer_length 
            
        self.chamfer_angle = chamfer_angle if chamfer_angle is not None else 45
        self.chamfer_pos = chamfer_pos if chamfer_pos is not None else 'none'

    def str_en(self):
        # Pobieramy bazowy opis z Hole
        base = super().str_en()
        if self.chamfer_pos == 'none':
            return base
        return f"{base}\n{self.chamfer_length}x{self.chamfer_angle} chamfer ({self.chamfer_pos})"

    def str_pl(self):
        # Pobieramy bazowy opis z Hole
        base = super().str_pl()
        if self.chamfer_pos == 'none':
            return base
        pos_pl = self.chamfer_pos.replace('right', 'prawa').replace('left', 'lewa').replace('both', 'obie strony')
        return f"{base}\nfaza {self.chamfer_length}x{self.chamfer_angle} ({pos_pl})"

    def _plot_2d_view(self, language='en'):
        """Góra: Widok - bezpieczne łączenie, czarny obrys (gr. 1) i oś symetrii"""
        origin, r, l = self.origin / 5, self.diameter / 2 / 5, self.height / 5
        c_l = self.chamfer_length / 5
        c_h = c_l * np.tan(np.radians(self.chamfer_angle))
        pos = self.chamfer_pos

        # --- BEZPIECZNE OBLICZENIE STYKU Z SĄSIADEM ---
        prev_r = 0
        if getattr(self, 'prev_elem', None) is not None:
            prev_r = getattr(self.prev_elem, 'diameter', 0) / 10
            
            # Sprawdzamy czy sąsiad ma fazę
            if hasattr(self.prev_elem, 'chamfer_pos') and getattr(self.prev_elem, 'chamfer_pos') in ['right', 'both']:
                n_cl = getattr(self.prev_elem, 'chamfer_length', 0) / 5
                n_ca = getattr(self.prev_elem, 'chamfer_angle', 45)
                n_ch = n_cl * np.tan(np.radians(n_ca))
                prev_r += n_ch  # Faza otworu go poszerza!

        x_pts, y_pts = [], []
        start_y = r + c_h if pos in ['left', 'both'] else r
        
        # Start od promienia sąsiada (w otworze nie dociągamy do osi!)
        x_pts.extend([origin, origin])
        y_pts.extend([prev_r, start_y])
        
        if pos in ['left', 'both']:
            x_pts.append(origin + c_l)
            y_pts.append(r)
            # Pionowa kreska brzegu fazy widoczna z zewnątrz (gr. 1, czarna)
            GeometryScene.ax_2d.plot([origin + c_l, origin + c_l], [0, r], color='k',linewidth=1,  zorder=3)
            
        # Prawa strona
        end_x = origin + l - c_l if pos in ['right', 'both'] else origin + l
        x_pts.append(end_x)
        y_pts.append(r)

        if pos in ['right', 'both']:
            x_pts.append(origin + l)
            y_pts.append(r + c_h)
            GeometryScene.ax_2d.plot([origin + l - c_l, origin + l - c_l], [0, r], color='k',linewidth=1, zorder=3)
            
        if getattr(self, 'next_elem', None) is None:
            x_pts.append(origin + l)
            y_pts.append(0)

        # Rysowanie obrysu (czarny, grubość 1) i osi (grubość 0.5)
        res = GeometryScene.ax_2d.plot(x_pts, y_pts, linestyle='-', color='k', linewidth=1, zorder=3)
        res += GeometryScene.ax_2d.plot([origin-1, origin+l+1], [0, 0], 
                                        linestyle=(0, (25, 10, 2, 10)), color='k',linewidth=0.5, zorder=3)
        return res

    def _plot_2d_section(self, language='en'):
        """Dół: Przekrój - maskowanie materiału, faza i dynamiczny tekst (czarny obrys gr. 1)"""
        origin, r, l = self.origin / 5, self.diameter / 2 / 5, self.height / 5
        c_l = self.chamfer_length / 5
        c_h = c_l * np.tan(np.radians(self.chamfer_angle))
        pos = self.chamfer_pos

        # --- INTELIGENTNE ODSUWANIE OPISU ---
        max_d = self.diameter
        curr = getattr(self, 'prev_elem', None)
        while curr is not None:
            if getattr(curr, 'diameter', 0) > max_d: max_d = curr.diameter
            curr = getattr(curr, 'prev_elem', None)
            
        curr = getattr(self, 'next_elem', None)
        while curr is not None:
            if getattr(curr, 'diameter', 0) > max_d: max_d = curr.diameter
            curr = getattr(curr, 'next_elem', None)
            
        max_r = max_d / 2 / 5

        # 1. Biały blok czyszczący szrafowanie pod osią
        GeometryScene.ax_2d.fill_between(
            [origin, origin + l], [0, 0], [-r, -r],
            facecolor='white', edgecolor='none', zorder=2
        )

        # --- BEZPIECZNE OBLICZENIE STYKU Z SĄSIADEM ---
        prev_r = 0
        if getattr(self, 'prev_elem', None) is not None:
            prev_r = getattr(self.prev_elem, 'diameter', 0) / 10
            if hasattr(self.prev_elem, 'chamfer_pos') and getattr(self.prev_elem, 'chamfer_pos') in ['right', 'both']:
                n_cl = getattr(self.prev_elem, 'chamfer_length', 0) / 5
                n_ca = getattr(self.prev_elem, 'chamfer_angle', 45)
                n_ch = n_cl * np.tan(np.radians(n_ca))
                prev_r += n_ch

        # 2. Widoczny kontur otworu ze schodkami i fazą
        x_pts, y_pts = [], []
        start_y = -r - c_h if pos in ['left', 'both'] else -r
        
        x_pts.extend([origin, origin])
        y_pts.extend([-prev_r, start_y])
        
        if pos in ['left', 'both']:
            x_pts.append(origin + c_l)
            y_pts.append(-r)
            # Wewnętrzna krawędź skosu w przekroju (gr. 1, czarna)
            GeometryScene.ax_2d.plot([origin + c_l, origin + c_l], [-r, 0], color='k',linewidth=1,  zorder=3)
            
        if pos in ['right', 'both']:
            x_pts.append(origin + l - c_l)
            y_pts.append(-r)
            x_pts.append(origin + l)
            y_pts.append(-r - c_h)
            GeometryScene.ax_2d.plot([origin + l - c_l, origin + l - c_l], [-r, 0], color='k', linewidth=1, zorder=3)
        else:
            x_pts.append(origin + l)
            y_pts.append(-r)
            
        if getattr(self, 'next_elem', None) is None:
            x_pts.append(origin + l)
            y_pts.append(0)

        # Obrys główny przekroju
        res = GeometryScene.ax_2d.plot(x_pts, y_pts, linestyle='-', color='k', linewidth=1, zorder=3)

        # 3. Dynamiczny opis
        label = self.str_pl() if language == 'pl' else self.str_en()
        GeometryScene.ax_2d.text(origin + l/2, -max_r - 5, label, 
                                 rotation='vertical', multialignment='center', 
                                 va='top', ha='center', color='k')

        return res


class ChamferedOpenHoleWithKeyway(ChamferedHole):
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
    def str_en(self):
        return 'Hole with keyway \n with L={length}mm, diameter={d}mm \n and {l_ch}x{angle} chamfers on the both sides'.format(
            length=self.height,
            d=self.diameter,
            angle=self.chamfer_angle,
            l_ch=self.chamfer_length,
            pos=self.chamfer_pos)

    def str_pl(self):
        return 'Otwór z wypust czółenkowy \n o L={length}mm, średnicy={d}mm \n i fazach {l_ch}x{angle} znajdującej się po obu stronach'.format(
            length=self.height,
            d=self.diameter,
            angle=self.chamfer_angle,
            l_ch=self.chamfer_length,
            pos=self.chamfer_pos).replace('right',
                                          'prawej').replace('left', 'lewej')

    def _plot_2d(self, language='en'):

        class_name = self.__class__.__name__

        span = np.linspace(0, len(class_name), 100)
        #         print(f'plot_2d is called for {class_name}')

        origin = self.origin / 5
        r = self.diameter / 2 / 5
        l = self.height / 5
        end = self.end / 5

        t_l = origin + l / 2
        t_r = (-r - 23)

        # Rysuje biały blok "czyszczący" pod osią, aby schować kreskowanie wałka
        GeometryScene.ax_2d.fill_between(
            [origin, origin + l], 
            [0, 0], 
            [-r, -r], # Gdzie -r to promień otworu
            facecolor='white', edgecolor='none', zorder=2
        )

        res = GeometryScene.ax_2d.plot(
            [
                origin + 0,
                origin + 0,
                origin + l,
                origin + l,
                origin + 0,
            ], [-r, r, r, -r, -r],
            '--',
            color='c') + GeometryScene.ax_2d.plot(
                [origin - 0.5, origin + l + 0.5], [0, 0],
                '-.',
                color='k',
                linewidth=1),
        GeometryScene.ax_2d.plot([origin,(origin+1)], [0.5,0.5],
                                        '-.',
                                        color='k',
                                        linewidth=1),
        GeometryScene.ax_2d.plot([origin,(origin+1)], [-0.5,-0.5],
                                        '-.',
                                        color='k',
                                        linewidth=1)
#         GeometryScene.ax_2d.plot([origin,origin+1], [1,1],
#                                         '-.',
#                                         color='k',
#                                         linewidth=1)
#         GeometryScene.ax_2d.plot([origin,origin+1], [-1,-1],
#                                         '-.',
#                                         color='k',
#                                         linewidth=1)
        if language == 'pl':
            text = GeometryScene.ax_2d.text(t_l,
                                            t_r,
                                            self.str_pl(),
                                            rotation='vertical',
                                            multialignment='center')
        else:
            text = GeometryScene.ax_2d.text(t_l,
                                            t_r,
                                            self.str_en(),
                                            rotation='vertical',
                                            multialignment='center')

        ShaftPreview(0,0, origin / 2,
                     [2 * r / 2, l / 2, "bez fazy", 0.7, '#6b7aa1'])


class ChamferedCylinder(Cylinder):
    def __init__(self, height, diameter, chamfer_length=None, chamfer_angle=45, chamfer_pos='left'):
        super().__init__(height, diameter)
        
        if chamfer_length is None:
            self.chamfer_length = max(1, min(4, round(diameter * 0.05)))
        else:
            self.chamfer_length = chamfer_length 
            
        self.chamfer_angle = chamfer_angle if chamfer_angle is not None else 45
        self._intended_chamfer_pos = chamfer_pos if chamfer_pos is not None else 'none'
        
        self.prev_elem = None
        self.next_elem = None

    @property
    def chamfer_pos(self):
        """Dynamiczne wygaszanie faz, jeśli brakuje na nie miejsca"""
        pos = self._intended_chamfer_pos
        radial_drop = self.chamfer_length * np.tan(np.radians(self.chamfer_angle))
        edge_diameter = self.diameter - (2 * radial_drop)
        
        if pos in ['left', 'both'] and self.prev_elem is not None:
            d_prev = getattr(self.prev_elem, 'diameter', 0)
            if d_prev >= self.diameter or edge_diameter < d_prev:
                pos = 'right' if pos == 'both' else 'none'
                
        if pos in ['right', 'both'] and self.next_elem is not None:
            d_next = getattr(self.next_elem, 'diameter', 0)
            if d_next >= self.diameter or edge_diameter < d_next:
                pos = 'left' if pos == 'both' else 'none'
                
        return pos
    
    @chamfer_pos.setter
    def chamfer_pos(self, value):
        """Pozwala generatorom na ręczne nadpisywanie pozycji fazy"""
        self._intended_chamfer_pos = value    

    def str_en(self):
        base = super().str_en()
        if self.chamfer_pos == 'none':
            return base
        return f"{base}\n{self.chamfer_length}x{self.chamfer_angle} chamfer ({self.chamfer_pos})"

    def str_pl(self):
        base = super().str_pl()
        if self.chamfer_pos == 'none':
            return base
        pos_pl = self.chamfer_pos.replace('right', 'prawa').replace('left', 'lewa').replace('both', 'obie strony')
        return f"{base}\nfaza {self.chamfer_length}x{self.chamfer_angle} ({pos_pl})"

    def _plot_2d_view(self, language='en'):
        origin, r, l = self.origin/5, self.diameter/2/5, self.height/5
        c_l = self.chamfer_length/5
        c_h = c_l * np.tan(np.radians(self.chamfer_angle))
        pos = self.chamfer_pos

        # --- OBLICZENIE STYKU Z SĄSIADEM ---
        prev_r = 0
        if getattr(self, 'prev_elem', None) is not None:
            prev_r = getattr(self.prev_elem, 'diameter', 0) / 10
            
            # Sprawdzamy czy sąsiad ma fazę
            if hasattr(self.prev_elem, 'chamfer_pos') and getattr(self.prev_elem, 'chamfer_pos') in ['right', 'both']:
                # BEZPIECZNE POBIERANIE WARTOSCI: Jeśli nie ma chamfer_length, podstaw 0
                n_cl = getattr(self.prev_elem, 'chamfer_length', 0) / 5
                n_ca = getattr(self.prev_elem, 'chamfer_angle', 45)
                
                n_ch = n_cl * np.tan(np.radians(n_ca))
                prev_r -= n_ch

        x_pts, y_pts = [], []
        start_y = r - c_h if pos in ['left', 'both'] else r
        
        # --- TUTAJ JEST POPRAWKA (NAPRAWIA ŻÓŁTE KRESKI) ---
        # Start rysowania: pionowa kreska od samej osi (0), przez sąsiada do nas
        x_pts.extend([origin, origin, origin])
        y_pts.extend([0, prev_r, start_y])
            
        if pos in ['left', 'both']:
            x_pts.append(origin + c_l)
            y_pts.append(r)
            GeometryScene.ax_2d.plot([origin + c_l, origin + c_l], [0, r], color='k',linewidth=1, zorder=3)

        # Góra i prawa strona
        end_x = origin + l - c_l if pos in ['right', 'both'] else origin + l
        x_pts.append(end_x)
        y_pts.append(r)

        if pos in ['right', 'both']:
            x_pts.append(origin + l)
            y_pts.append(r - c_h)
            GeometryScene.ax_2d.plot([origin + l - c_l, origin + l - c_l], [0, r], color='k',linewidth=1, zorder=3)
            
        # Jeśli nie ma sąsiada ALBO sąsiad jest Otworem, zamknij profil pionowo w dół do osi!
        next_is_solid = self.next_elem is not None and 'Hole' not in type(self.next_elem).__name__
        
        if not next_is_solid:
            x_pts.append(origin + l)
            y_pts.append(0)

        res = GeometryScene.ax_2d.plot(x_pts, y_pts, color='k', linewidth=1, zorder=3)
        res += GeometryScene.ax_2d.plot([origin-1, origin+l+1], [0, 0], linestyle=(0, (25, 10, 2, 10)), linewidth=0.5, color='k', zorder=3)

        label = self.str_pl() if language == 'pl' else self.str_en()
        GeometryScene.ax_2d.text(origin + l/2, r + 5, label, rotation='vertical', multialignment='center', va='bottom', ha='center', color='k')
        return res

    def _plot_2d_section(self, language='en'):
        origin, r, l = self.origin/5, self.diameter/2/5, self.height/5
        c_l = self.chamfer_length/5
        c_h = c_l * np.tan(np.radians(self.chamfer_angle))
        pos = self.chamfer_pos

        # --- OBLICZENIE STYKU Z SĄSIADEM ---
        prev_r = 0
        if getattr(self, 'prev_elem', None) is not None:
            prev_r = getattr(self.prev_elem, 'diameter', 0) / 10
            
            # Sprawdzamy czy sąsiad ma fazę
            if hasattr(self.prev_elem, 'chamfer_pos') and getattr(self.prev_elem, 'chamfer_pos') in ['right', 'both']:
                # BEZPIECZNE POBIERANIE WARTOSCI: Jeśli nie ma chamfer_length, podstaw 0
                n_cl = getattr(self.prev_elem, 'chamfer_length', 0) / 5
                n_ca = getattr(self.prev_elem, 'chamfer_angle', 45)
                
                n_ch = n_cl * np.tan(np.radians(n_ca))
                prev_r -= n_ch

        # Kreskowanie
        x_hatch = [origin, origin + (c_l if pos in ['left', 'both'] else 0), origin+l - (c_l if pos in ['right', 'both'] else 0), origin+l]
        y_hatch = [-(r-c_h) if pos in ['left', 'both'] else -r, -r, -r, -(r-c_h) if pos in ['right', 'both'] else -r]
        GeometryScene.ax_2d.fill_between([origin, origin+l], [0, 0], [-r, -r], facecolor='none', hatch='//', edgecolor='k', linewidth=0, alpha=0.3, zorder=1)

        # Obrys (NAPRAWIA NIEBIESKĄ KRESKĘ - nie schodzi do 0)
        x_pts, y_pts = [], []
        start_y = -r + c_h if pos in ['left', 'both'] else -r
        
        x_pts.extend([origin, origin])
        y_pts.extend([-prev_r, start_y]) # Start od promienia sąsiada, nie od osi!

        if pos in ['left', 'both']:
            x_pts.append(origin + c_l)
            y_pts.append(-r)

        if pos in ['right', 'both']:
            x_pts.append(origin + l - c_l)
            y_pts.append(-r)
            x_pts.append(origin + l)
            y_pts.append(-r + c_h)
        else:
            x_pts.append(origin + l)
            y_pts.append(-r)

        # --- ZMIANA: INTELIGENTNE ZAMYKANIE PRAWEJ KRAWĘDZI ---
        # Sprawdzamy, czy następny element to twardy materiał (nie "powietrze" czyli Hole)
        next_is_solid = self.next_elem is not None and 'Hole' not in type(self.next_elem).__name__
        
        # Zamknij zarys do osi symetrii (0) jeśli kończymy wał albo zaczyna się otwór
        if not next_is_solid:
            x_pts.append(origin + l)
            y_pts.append(0)

        return GeometryScene.ax_2d.plot(x_pts, y_pts, color='k',linewidth=1, zorder=3)
class Thread(ChamferedCylinder):

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

    def __init__(self,
                 height,
                 diameter,
                 chamfer_length=None,
                 chamfer_angle=45,
                 thread='M',
                 chamfer_pos=None):

        # Inicjalizacja poprzez ChamferedCylinder (obsłuży domyślne fazy z automatu!)
        super().__init__(height, diameter, chamfer_length, chamfer_angle, chamfer_pos)
        
        self.thread = thread
        self._parameters = thread + str(diameter), height, chamfer_length, chamfer_angle

    def str_en(self):
        pos = getattr(self, 'chamfer_pos', self._intended_chamfer_pos)
        if pos == 'none':
            return f'Threaded Cylinder \n with L={self.height}mm, thread M{self.diameter}'
        return f'Threaded Cylinder \n with L={self.height}mm, thread M{self.diameter} \n and chamfer {self.chamfer_length}x{self.chamfer_angle} ({pos})'

    def str_pl(self):
        pos = getattr(self, 'chamfer_pos', self._intended_chamfer_pos)
        pos_pl = pos.replace('right', 'prawa').replace('left', 'lewa').replace('both', 'obie strony')
        if pos == 'none':
            return f'Walec gwintowany \n o L={self.height}mm, gwincie M{self.diameter}'
        return f'Walec gwintowany \n o L={self.height}mm, gwincie M{self.diameter} \n i fazie {self.chamfer_length}x{self.chamfer_angle} ({pos_pl})'

    def _plot_2d(self, language='en'):
        self._plot_2d_view(language)
        self._plot_2d_section(language)
        
        origin, r, l = self.origin / 5, self.diameter / 2 / 5, self.height / 5
        ShaftPreview(0, 0, origin / 2, [r, l, "gwint", 0.2, '#56754A'])

    # UWAGA: _plot_2d_view usunięte! Dzięki temu w górnym widoku wygeneruje 
    # się sam, czysty walec z ChamferedCylinder, bez czerwonej linii gwintu!

    def _plot_2d_section(self, language='en'):
        """Dół: Przekrój - Szrafuje walec i dorysowuje tylko czerwony rdzeń i końce gwintu"""
        
        # 1. Baza: ChamferedCylinder odwala czarną robotę (obrys, szrafowanie, schodki z sąsiadem)
        res = super()._plot_2d_section(language)

        # 2. Parametry gwintu
        origin, r, l = self.origin/5, self.diameter/2/5, self.height/5
        r_t = 0.95 * r # Dno gwintu na przekroju
        
        pos = self.chamfer_pos
        c_l = self.chamfer_length/5

        # --- 3. Linia rdzenia gwintu (czerwona cienka) ---
        # POPRAWKA: Gwint idzie przez całą długość stopnia, przecinając fazę
        start_core_x = origin 
        end_core_x = origin + l
        
        res += GeometryScene.ax_2d.plot([start_core_x, end_core_x], [-r_t, -r_t], 
                                        '-', linewidth=0.5, color='r', zorder=3)

        # --- 4. PIONOWE LINIE KOŃCA GWINTU (Zgodnie z normą PN/ISO) ---
        # Jeśli NIE ma fazy na danym końcu (gwint dobija do progu), rysujemy grubą czarną kreskę
        # od zarysu zewnętrznego (-r) do rdzenia (-r_t)
        if pos not in ['left', 'both']:
            # Koniec gwintu z lewej strony
            res += GeometryScene.ax_2d.plot([origin, origin], [-r, -0.9*r_t], color='k', linewidth=1., zorder=3)
            
        if pos not in ['right', 'both']:
            # Koniec gwintu z prawej strony
            res += GeometryScene.ax_2d.plot([origin + l, origin + l], [-r, -0.9*r_t], color='k', linewidth=1., zorder=3)

        return res


class ThreadOfScrew(Thread):

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
        'vertical_lines': 0,
        'inclined_lines': 2,
        'horizontal_dimensions': 2,
        'vertical_dimensions': 1,
        'angular_dimensions': 1,
    }

    num_of_lines_half_sec = {
        'horizontal_lines': 5,
        'vertical_lines': 0,
        'inclined_lines': 2,
        'horizontal_dimensions': 2,
        'vertical_dimensions': 1,
        'angular_dimensions': 1,
    }

    num_of_lines_front = {'circles': 1, 'arcs': 1}

    def str_en(self):
        return 'Thread of screw \n with L={length}mm, thread M{d} \n and chamfer {l_ch}x{angle}'.format(
            length=self.height,
            d=self.diameter,
            angle=self.chamfer_angle,
            l_ch=self.chamfer_length,
        )

    def str_pl(self):
        return 'Gwint śruby \n o L={length}mm, gwincie M{d}mm \n i fazie {l_ch}x{angle}'.format(
            length=self.height,
            d=self.diameter,
            angle=self.chamfer_angle,
            l_ch=self.chamfer_length,
        )


class ThreadedOpenHole(ChamferedHole):
    """This object represents an open threaded hole with chamfers on both sides."""

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

    def __init__(self,
                 height,
                 diameter,
                 chamfer_length=None,
                 chamfer_angle=45,
                 thread='M'):

        # Wywołujemy inicjalizację z ChamferedHole, wymuszając fazę z obu stron ('both')
        super().__init__(height, diameter, chamfer_length, chamfer_angle, chamfer_pos='both')
        
        self.thread = thread
        self._parameters = thread, diameter

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

    def _plot_2d_view(self, language='en'):
        """Góra: Widok - naprawione połączenie (schodek), wewnętrzne krawędzie faz, docięty gwint"""
        origin, r, l = self.origin / 5, self.diameter / 2 / 5, self.height / 5
        c_l = self.chamfer_length / 5
        c_h = c_l * np.tan(np.radians(self.chamfer_angle))
        
        t = 1.1 * r # Linia gwintu wewnętrznego (rdzeń) - szersza niż otwór!

        # --- BEZPIECZNE OBLICZENIE STYKU Z SĄSIADEM ---
        prev_r = 0
        if getattr(self, 'prev_elem', None) is not None:
            prev_r = getattr(self.prev_elem, 'diameter', 0) / 10
            if hasattr(self.prev_elem, 'chamfer_pos') and getattr(self.prev_elem, 'chamfer_pos') in ['right', 'both']:
                n_cl = getattr(self.prev_elem, 'chamfer_length', 0) / 5
                n_ca = getattr(self.prev_elem, 'chamfer_angle', 45)
                n_ch = n_cl * np.tan(np.radians(n_ca))
                prev_r += n_ch

        x_pts, y_pts = [], []
        
        # POPRAWKA: Rysujemy połączenie z sąsiadem, a nie z pustym powietrzem!
        x_pts.extend([origin, origin])
        y_pts.extend([prev_r, r + c_h])
        
        # Lewy skos
        x_pts.append(origin + c_l)
        y_pts.append(r)
        
        # PIONOWA LINIA WEWNĘTRZNA FAZY
        GeometryScene.ax_2d.plot([origin + c_l, origin + c_l], [0, r], color='k', linewidth=1, zorder=3)
        
        # Prawy skos
        x_pts.append(origin + l - c_l)
        y_pts.append(r)
        x_pts.append(origin + l)
        y_pts.append(r + c_h)
        
        # PIONOWA LINIA WEWNĘTRZNA FAZY (Z PRAWEJ)
        GeometryScene.ax_2d.plot([origin + l - c_l, origin + l - c_l], [0, r], color='k', linewidth=1, zorder=3)
        
        # Główny obrys czarny, grubość 1 (przelotowy na końcu, bez zjazdu do 0)
        res = GeometryScene.ax_2d.plot(x_pts, y_pts, linestyle='-', color='k', linewidth=1, zorder=3)
        
        # --- WYLICZENIE STYKU GWINTU Z FAZĄ ---
        if c_h >= (t - r):
            dx = c_l * (t - r) / c_h
            start_t_x = origin + c_l - dx
            end_t_x = origin + l - c_l + dx
        else:
            start_t_x = origin
            end_t_x = origin + l
            
        res += GeometryScene.ax_2d.plot([start_t_x, end_t_x], [t, t], '-', color='r', linewidth=0.5, zorder=3)
        
        # Oś symetrii
        res += GeometryScene.ax_2d.plot([origin-1, origin+l+1], [0, 0], linestyle=(0, (25, 10, 2, 10)), color='k', linewidth=0.5, zorder=3)
        return res

    def _plot_2d_section(self, language='en'):
        """Dół: Przekrój - maskowanie pod fazą, naprawiony schodek, czarny obrys (gr. 1)"""
        origin, r, l = self.origin / 5, self.diameter / 2 / 5, self.height / 5
        c_l = self.chamfer_length / 5
        c_h = c_l * np.tan(np.radians(self.chamfer_angle))
        t = 1.1 * r

        # Odsunięcie opisu
        max_d = self.diameter
        curr = getattr(self, 'prev_elem', None)
        while curr is not None:
            if getattr(curr, 'diameter', 0) > max_d: max_d = curr.diameter
            curr = getattr(curr, 'prev_elem', None)
            
        curr = getattr(self, 'next_elem', None)
        while curr is not None:
            if getattr(curr, 'diameter', 0) > max_d: max_d = curr.diameter
            curr = getattr(curr, 'next_elem', None)
            
        max_r = max_d / 2 / 5

        # 1. Dokładna biała maska
        GeometryScene.ax_2d.fill_between(
            [origin, origin + c_l, origin + l - c_l, origin + l], 
            [0, 0, 0, 0], 
            [-(r + c_h), -r, -r, -(r + c_h)], 
            facecolor='white', edgecolor='none', zorder=2
        )

        # --- BEZPIECZNE OBLICZENIE STYKU Z SĄSIADEM ---
        prev_r = 0
        if getattr(self, 'prev_elem', None) is not None:
            prev_r = getattr(self.prev_elem, 'diameter', 0) / 10
            if hasattr(self.prev_elem, 'chamfer_pos') and getattr(self.prev_elem, 'chamfer_pos') in ['right', 'both']:
                n_cl = getattr(self.prev_elem, 'chamfer_length', 0) / 5
                n_ca = getattr(self.prev_elem, 'chamfer_angle', 45)
                n_ch = n_cl * np.tan(np.radians(n_ca))
                prev_r += n_ch

        # 2. Widoczny kontur otworu ze schodkami i fazą
        x_pts, y_pts = [], []
        
        # POPRAWKA: Schodek pionowy od promienia sąsiada w dół do początku skosu!
        x_pts.extend([origin, origin])
        y_pts.extend([-prev_r, -(r + c_h)])
        
        # Lewy skos
        x_pts.append(origin + c_l)
        y_pts.append(-r)
        GeometryScene.ax_2d.plot([origin + c_l, origin + c_l], [-r, 0], color='k', linewidth=1, zorder=3)
        
        # Prawy skos
        x_pts.append(origin + l - c_l)
        y_pts.append(-r)
        x_pts.append(origin + l)
        y_pts.append(-(r + c_h))
        GeometryScene.ax_2d.plot([origin + l - c_l, origin + l - c_l], [-r, 0], color='k', linewidth=1, zorder=3)

        # Obrys główny czarny (brak pionowej kreski zamykającej profil po prawej!)
        res = GeometryScene.ax_2d.plot(x_pts, y_pts, linestyle='-', color='k', linewidth=1, zorder=3)

        # Czerwona linia dna gwintu w przekroju
        if c_h >= (t - r):
            dx = c_l * (t - r) / c_h
            start_t_x = origin + c_l - dx
            end_t_x = origin + l - c_l + dx
        else:
            start_t_x = origin
            end_t_x = origin + l
            
        res += GeometryScene.ax_2d.plot([start_t_x, end_t_x], [-t, -t], '-', color='r', linewidth=0.5, zorder=3)

        # 3. Dynamiczny opis
        label = self.str_pl() if language == 'pl' else self.str_en()
        GeometryScene.ax_2d.text(origin + l/2, -max_r - 5, label, 
                                 rotation='vertical', multialignment='center', 
                                 va='top', ha='center', color='k')
        return res

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

    def __init__(self,
                 height,
                 teeth_no,
                 module,
                 chamfer_length=1,
                 chamfer_angle=45):
        num_of_lines_view = self.__class__.num_of_lines_view
        num_of_lines_sec = self.__class__.num_of_lines_sec
        num_of_lines_half_sec = self.__class__.num_of_lines_half_sec
        num_of_lines_front = self.__class__.num_of_lines_front

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

    def _plot_2d(self, language='en'):

        #         print(f'self.origin property is {self.origin()}')
        #         print(f'self.end property is {self.end()}')

        class_name = self.__class__.__name__

        span = np.linspace(0, len(class_name), 100)
        #         print(f'plot_2d is called for {class_name}')

        r = round(self.module * (self.teeth_no + 2)) / 10 / 2
        rp = round(self.module * (self.teeth_no)) / 10 / 2
        l = self.height / 10
        origin = self.origin / 10
        end = self.end / 10

        t_l = origin + l / 4
        t_r = (r + 2.5)

        res = GeometryScene.ax_2d.plot(
            [origin + 0, origin + 0, origin + l, origin + l, origin + 0],
            [-r, r, r, -r, -r],
            color='tab:pink') + GeometryScene.ax_2d.plot(
                [origin - 0.5, origin + l + 0.5], [0, 0],
                '-.',
                color='k',
                linewidth=1) + GeometryScene.ax_2d.plot(
                    [origin - 0.5, origin + l + 0.5], [-rp, -rp],
                    '-.',
                    color='k',
                    linewidth=1) + GeometryScene.ax_2d.plot(
                        [origin - 0.5, origin + l + 0.5], [rp, rp],
                        '-.',
                        color='k',
                        linewidth=1)  #Jaś Fasola

        if language == 'pl':
            text = GeometryScene.ax_2d.text(t_l,
                                            t_r,
                                            self.str_pl(),
                                            rotation='vertical',
                                            multialignment='center')
        else:
            text = GeometryScene.ax_2d.text(t_l,
                                            t_r,
                                            self.str_en(),
                                            rotation='vertical',
                                            multialignment='center')

        ShaftPreview(0,0, origin / 2,
                     [2 * r / 2, l / 2, "bez fazy", 0.2, '#6b7aa1'])

        print(res)


class HexagonalPrism(Solid):

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

    def __init__(self, height, indiameter):

        num_of_lines_view = self.__class__.num_of_lines_view
        num_of_lines_sec = self.__class__.num_of_lines_sec
        num_of_lines_half_sec = self.__class__.num_of_lines_half_sec
        num_of_lines_front = self.__class__.num_of_lines_front

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

    def _plot_2d(self, language='en'):

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
                [origin - 0.5, origin + l + 0.5], [0, 0],
                '-.',
                color='g',
                linewidth=1)

        if language == 'pl':
            text = GeometryScene.ax_2d.text(t_l,
                                            t_r,
                                            self.str_pl(),
                                            rotation='vertical',
                                            multialignment='center')
        else:
            text = GeometryScene.ax_2d.text(t_l,
                                            t_r,
                                            self.str_en(),
                                            rotation='vertical',
                                            multialignment='center')

        HexPreview(0,0, origin / 2,
                   [2 * r / 2, l / 2, "bez fazy", 0.6, '#6b7aa1'])

        print(res)


class ChamferedHexagonalPrism(HexagonalPrism):

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

    def __init__(self,
                 height,
                 indiameter,
                 chamfer_length=1,
                 chamfer_angle=45,
                 chamfer_pos='left'):

        super().__init__(height=height, indiameter=indiameter)

        num_of_lines_view = self.__class__.num_of_lines_view

        num_of_lines_sec = self.__class__.num_of_lines_sec
        num_of_lines_half_sec = self.__class__.num_of_lines_half_sec

        num_of_lines_front = self.__class__.num_of_lines_front

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

    def _plot_2d(self, language='en'):

        #         print(f'self.origin property is {self.origin()}')
        #         print(f'self.end property is {self.end()}')

        class_name = self.__class__.__name__

        span = np.linspace(0, len(class_name), 100)
        #         print(f'plot_2d is called for {class_name}')

        r = self.indiameter / 2 / 10
        l = self.height / 10
        origin = self.origin / 10
        end = self.end / 10

        t_l = origin  # + l / 9
        t_r = (r + 0.5)

        res = GeometryScene.ax_2d.plot(
            [origin + 0, origin + 0, origin + l, origin + l, origin + 0],
            [-r, r, r, -r, -r],
            color='g') + GeometryScene.ax_2d.plot(
                [origin - 0.5, origin + l + 0.5], [0, 0],
                '-.',
                color='g',
                linewidth=1) + GeometryScene.ax_2d.plot(
                    [origin + 0, origin + l], [r * 0.6, r * 0.6],
                    color='g') + GeometryScene.ax_2d.plot(
                        [origin + 0, origin + l], [-r * 0.6, -r * 0.6],
                        color='g')

        if language == 'pl':
            text = GeometryScene.ax_2d.text(t_l,
                                            t_r,
                                            self.str_pl(),
                                            rotation='vertical',
                                            multialignment='center')
        else:
            text = GeometryScene.ax_2d.text(t_l,
                                            t_r,
                                            self.str_en(),
                                            rotation='vertical',
                                            multialignment='center')

        #ShaftPreview(5,5,origin/2 ,[2*r/2, l/2, "bez fazy", 0.2, '#6b7aa1'])
        HexPreview(0,0, origin / 2,
                   [2 * r / 2, l / 2, "bez fazy", 0.2, '#6b7aa1'])

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

    def _plot_2d(self, language='en'):

        class_name = self.__class__.__name__
        span = np.linspace(0, len(class_name), 100)

        # --- Zmiana skali na / 5 ---
        origin = self.origin / 5
        r = self.diameter / 2 / 5
        l = self.height / 5
        r_h = self.hole_diameter / 2 / 5
        r_r = self.reference_diameter / 2 / 5
        holes_no = self.holes_no
        end = self.end / 5
        
        # Poprawiona trygonometria fazy
        c_l = self.chamfer_length / 5
        c_a = self.chamfer_angle
        c_h = c_l * np.tan(np.radians(c_a))

        # Zabezpieczenie przed uciekającym tekstem
        t_l = origin - 5
        t_r = (-r - 5)

        # --- 1. KRESKOWANIE (DÓŁ) ---
        GeometryScene.ax_2d.fill_between(
            [origin, origin + l], 
            [0, 0], 
            [-r, -r], 
            facecolor='none', hatch='//', edgecolor='k', alpha=0.5, zorder=1
        )

        # --- 2. BIAŁA MASKA DLA OTWORU NA DOLE (aby usunąć kreskowanie w świetle otworu) ---
        GeometryScene.ax_2d.fill_between(
            [origin, origin + l],
            [-r_r + r_h, -r_r + r_h],
            [-r_r - r_h, -r_r - r_h],
            facecolor='white', edgecolor='none', zorder=2
        )

        # --- 3. OBRYSY I OSIE (ZORDER=3) ---
        # Zmieniłem color='m' (magenta) na 'k' (czarny), aby wyglądało to profesjonalnie
        res = GeometryScene.ax_2d.plot(
            [origin - 0.5, origin + l + 0.5], [0, 0], # Główna oś symetrii
            '-.', color='k', linewidth=1, zorder=3
        ) + GeometryScene.ax_2d.plot(
            [origin, origin, origin + l, origin + l, origin], # Główny zewnętrzny obrys kołnierza
            [-r, r, r, -r, -r],
            color='k', zorder=3 
        ) + GeometryScene.ax_2d.plot(
            [origin - 0.5, origin + l + 0.5], [r_r, r_r], # Oś górnego otworu
            '-.', color='k', linewidth=1, zorder=3
        ) + GeometryScene.ax_2d.plot(
            [origin, origin, origin + l, origin + l, origin], # Dolny otwór (PRZEKRÓJ - ciągłe linie '-')
            [-r_r - r_h, -r_r + r_h, -r_r + r_h, -r_r - r_h, -r_r - r_h],
            '-', color='k', linewidth=1, zorder=3
        ) + GeometryScene.ax_2d.plot(
            [origin - 0.5, origin + l + 0.5], [-r_r, -r_r], # Oś dolnego otworu
            '-.', color='k', linewidth=1, zorder=3
        )

        if language == 'pl':
            text = GeometryScene.ax_2d.text(t_l, t_r, self.str_pl(), rotation='vertical', multialignment='center')
        else:
            text = GeometryScene.ax_2d.text(t_l, t_r, self.str_en(), rotation='vertical', multialignment='center')

        ShaftPreview(0,0, origin / 2, [2 * r / 2, l / 2, "bez fazy", 0.2, '#6b7aa1'])

        for hole_no in range(holes_no):
            xh = r_r * np.cos(hole_no * 2 * np.pi / holes_no)
            yh = r_r * np.sin(hole_no * 2 * np.pi / holes_no)
            ShaftPreview(5 + xh, 5 + yh, origin / 2, [2 * r_h / 2, l / 2, "bez fazy", 0.2, '#6b7aa1'])


class BlockBearingHolder(Solid):
    """
    Block with hole in every corner and bearing place on the top. It's drawn in the horizontal position (symmetry axis is horizontal line).
    """
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

    def __init__(self, height, width, length):

        self.height = height
        self.width = width
        self.length = length
        self._parameters = height, width, length

        num_of_lines_view = self.__class__.num_of_lines_view
        num_of_lines_sec = self.__class__.num_of_lines_sec
        num_of_lines_half_sec = self.__class__.num_of_lines_half_sec
        num_of_lines_front = self.__class__.num_of_lines_front

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
            'vertical_dimensions': 0,
            'angular_dimensions': 0,
        }

        num_of_lines_sec = {
            'horizontal_lines': 4,  #axis included
            'vertical_lines': 2,  #axis excluded
            'inclined_lines': 0,
            'horizontal_dimensions': 1,
            'vertical_dimensions': 0,
            'angular_dimensions': 0,
        }

        num_of_lines_half_sec = {
            'horizontal_lines': 3,  #axis included
            'vertical_lines': 2,  #axis excluded
            'inclined_lines': 0,
            'horizontal_dimensions': 1,
            'vertical_dimensions': 0,
            'angular_dimensions': 0,
        }

        num_of_lines_front = {
            'horizontal_lines': 4,  #axis excluded
            'vertical_lines': 4,  #axis excluede
            'inclined_lines': 0,
            'horizontal_dimensions': 3,
            'vertical_dimensions': 3, #height, base, hole position included
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

    def __init__(self,
                 height,
                 indiameter,
                 chamfer_length=1,
                 chamfer_angle=45,
                 chamfer_pos='left'):

        num_of_lines_front = {'circles': 1, 'phi_dimensions': 0}  # to improve

        super().__init__(height=height, indiameter=indiameter)

        num_of_lines_view = self.__class__.num_of_lines_view
        num_of_lines_sec = self.__class__.num_of_lines_sec
        num_of_lines_half_sec = self.__class__.num_of_lines_half_sec

        num_of_lines_front = self.__class__.num_of_lines_front

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

    def _plot_2d(self, language='en'):

        #         print(f'self.origin property is {self.origin()}')
        #         print(f'self.end property is {self.end()}')

        class_name = self.__class__.__name__

        span = np.linspace(0, len(class_name), 100)
        #         print(f'plot_2d is called for {class_name}')

        r = self.indiameter / 2 / 10
        l = self.height / 10
        origin = self.origin / 10
        end = self.end / 10

        t_l = origin + l / 2
        t_r = (r + 0.5)

        res = GeometryScene.ax_2d.plot(
            [origin + 0, origin + 0, origin + l, origin + l, origin + 0],
            [-r, r, r, -r, -r],
            color='tab:purple') + GeometryScene.ax_2d.plot(
                [origin - 0.5, origin + l + 0.5], [0, 0],
                '-.',
                color='k',
                linewidth=1) + GeometryScene.ax_2d.plot(
                    [origin + 0, origin + l], [r * 0.6, r * 0.6],
                    color='tab:purple') + GeometryScene.ax_2d.plot(
                        [origin + 0, origin + l], [-r * 0.6, -r * 0.6],
                        color='tab:purple')

        if language == 'pl':
            text = GeometryScene.ax_2d.text(t_l,
                                            t_r,
                                            self.str_pl(),
                                            rotation='vertical',
                                            multialignment='center')
        else:
            text = GeometryScene.ax_2d.text(t_l,
                                            t_r,
                                            self.str_en(),
                                            rotation='vertical',
                                            multialignment='center')

        #ShaftPreview(5,5,origin/2 ,[2*r/2, l/2, "bez fazy", 0.2, '#6b7aa1'])
        HexPreview(0,0, origin / 2,
                   [2 * r / 2, l / 2, "bez fazy", 0.2, '#6b7aa1'])

        print(res)


class Washer(Cylinder):
    """This object represents washer solid.
    
    The washer object has predefined numbers of lines and dimensions that are needed make a engineering drawing. Also it stores information about height and diameter.
    
    Parameters
    ==========
    
    height : int
        The value of height of washer
        
    diameter : int
        The value of diameter of washer
    
    Examples
    ========
    
    >>> from solids import washer
    >>> wsh = washer(5,2)
    >>> wsh._parameters
    (5, 2)
    
    >>> wsh._class_description
    'with L=5mm and diameter =2mm'
    
    >>> wsh._class_description_pl
    'o L=5mm i średnicy =2mm'
    
    >>> wsh._name
    {'pl': 'Podkładka'}
    
    """
    num_of_lines_sec = {
        'horizontal_lines': 3,
        'vertical_lines': 1,
        'horizontal_dimensions': 1,
        'vertical_dimensions': 1,
        'inclined_lines': 0,
    }
    num_of_lines_half_sec = {
            'horizontal_lines': 3,
            'vertical_lines': 0,
            'inclined_lines': 2,
            'horizontal_dimensions': 2,
            'vertical_dimensions': 1,
            'angular_dimensions': 1,
        }
    def _plot_2d(self, language='en'):

        #         print(f'self.origin property is {self.origin()}')
        #         print(f'self.end property is {self.end()}')

        class_name = self.__class__.__name__

        span = np.linspace(0, len(class_name), 100)
        #         print(f'plot_2d is called for {class_name}')

        r = self.diameter / 2 / 10
        l = self.height / 10
        origin = self.origin / 10
        end = self.end / 10

        t_l = origin - l * 1 / 2
        t_r = (r + 7)

        line_type = self.line_type
        color = self.color

        res = GeometryScene.ax_2d.plot(
            [origin + 0, origin + 0, origin + l, origin + l, origin + 0],
            [-r, r, r, -r, -r],
            line_type,
            color=color) + GeometryScene.ax_2d.plot(
                [origin - 0.5, origin + l + 0.5], [0, 0],
                '-.',
                color='k',
                linewidth=1)

        if language == 'pl':
            text = GeometryScene.ax_2d.text(t_l,
                                            t_r,
                                            self.str_pl(),
                                            rotation='vertical',
                                            multialignment='center')
        else:
            text = GeometryScene.ax_2d.text(t_l,
                                            t_r,
                                            self.str_en(),
                                            rotation='vertical',
                                            multialignment='center')

        ShaftPreview(0,0, origin / 2,
                     [2 * r / 2, l / 2, "bez fazy", 0.2, '#6b7aa1'])

        print(res)

    def str_en(self):
        return 'Washer \n with L={length}mm \n and diameter={d}mm'.format(
            length=self.height, d=self.diameter)

    def str_pl(self):
        return 'Podkładka \n o  grubości g={length}mm \n i średnicy d={d}mm'.format(
            length=self.height,
            d=self.diameter).replace('right',
                                     'prawej').replace('left', 'lewej')


class StandarizedNut(DoubleChamferedHexagonalPrism):

    num_of_lines_view = {
        'horizontal_lines': 5,
        'vertical_lines': 2,
        'inclined_lines': 2,
        'arcs': 6,
        'horizontal_dimensions': 2,
        'vertical_dimensions': 1,
        'angular_dimensions': 1,
    }

    num_of_lines_sec = {
        'horizontal_lines': 5,
        'vertical_lines': 2,
        'inclined_lines': 2,
        'arcs': 6,
        'horizontal_dimensions': 2,
        'vertical_dimensions': 1,
        'angular_dimensions': 1,
    }

    num_of_lines_half_sec = {
        'horizontal_lines': 5,
        'vertical_lines': 2,
        'inclined_lines': 2,
        'arcs': 6,
        'horizontal_dimensions': 2,
        'vertical_dimensions': 1,
        'angular_dimensions': 1,
    }

    num_of_lines_front = {'circles': 1, 'phi_dimensions': 0}  # to improve

    def _plot_2d(self, language='en'):

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
                [origin - 0.5, origin + l + 0.5], [0, 0],
                '-.',
                color='k',
                linewidth=1) + GeometryScene.ax_2d.plot(
                    [origin + 0, origin + l], [r * 0.6, r * 0.6],
                    color='tab:purple') + GeometryScene.ax_2d.plot(
                        [origin + 0, origin + l], [-r * 0.6, -r * 0.6],
                        color='tab:purple')

        if language == 'pl':
            text = GeometryScene.ax_2d.text(t_l,
                                            t_r,
                                            self.str_pl(),
                                            rotation='vertical',
                                            multialignment='center')
        else:
            text = GeometryScene.ax_2d.text(t_l,
                                            t_r,
                                            self.str_en(),
                                            rotation='vertical',
                                            multialignment='center')

        #ShaftPreview(5,5,origin/2 ,[2*r/2, l/2, "bez fazy", 0.2, '#6b7aa1'])
        HexPreview(0,0, origin / 2,
                   [2 * r / 2, l / 2, "bez fazy", 0.2, '#6b7aa1'])

        print(res)

    def str_en(self):
        return 'Standarized nut \n with L={length}mm, wrench size S={d} \n and chamfer {l_ch}x{angle} \n on the both sides'.format(
            length=self.height,
            d=self.indiameter,
            angle=self.chamfer_angle,
            l_ch=self.chamfer_length,
        )

    def str_pl(self):
        return 'Znormalizowana nakrętka \n o L={length}mm, wymiarze pod klucz S={d}mm \n i fazie {l_ch}x{angle} \n po oby stronach'.format(
            length=self.height,
            d=self.indiameter,
            angle=self.chamfer_angle,
            l_ch=self.chamfer_length,
        )


class HexagonalHeadOfScrew(ChamferedHexagonalPrism):

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
        'horizontal_lines': 5,
        'vertical_lines': 0,
        'inclined_lines': 2,
        'arcs': 3,
        'horizontal_dimensions': 2,
        'vertical_dimensions': 1,
        'angular_dimensions': 1,
    }

    num_of_lines_half_sec = {
        'horizontal_lines': 5,
        'vertical_lines': 0,
        'inclined_lines': 2,
        'arcs': 3,
        'horizontal_dimensions': 2,
        'vertical_dimensions': 1,
        'angular_dimensions': 1,
    }

    num_of_lines_front = {'circles': 1, 'phi_dimensions': 0}  # to improve

    def str_en(self):
        return 'Hexagonal head of screw \n with L={length}mm \n wrench size S={d}mm and chamfer {l_ch}x{angle}'.format(
            length=self.height,
            d=self.indiameter,
            angle=self.chamfer_angle,
            l_ch=self.chamfer_length,
        )

    def str_pl(self):
        return 'Łeb sześciokątny śruby \n o L={length}mm  \n i wymiarze pod klucz {d}mm'.format(
            length=self.height,
            d=self.indiameter,)

    
class ThreadOfScrew(Thread):
    
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
            'vertical_lines': 1,
            'inclined_lines': 2,
            'horizontal_dimensions': 2,
            'vertical_dimensions': 1,
            'angular_dimensions': 1,
        }


        num_of_lines_half_sec = {
            'horizontal_lines': 5,
            'vertical_lines': 1,
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
        self._class_description = "{} with L={}mm and chamfer {}x{}".format(*(self._parameters))

        self._name['pl'] = 'Gwint'
        self._class_description_pl = "{} o L={}mm i fazie {}x{}".format(*self._parameters)
        
        
    def str_en(self):
        return 'Part (free) of screw thread  M{d} \n with chamfer {l_ch}x{angle} \n being L={length}mm outside the nut'.format(
            length=self.height,
            d=self.diameter,
            angle=self.chamfer_angle,
            l_ch=self.chamfer_length,
            )

    def str_pl(self):
        return 'Część gwintu (swobodna) M{d} \n o fazie {l_ch}x{angle} \n wysunięta poza nakrętkę na L={length}mm'.format(
            length=self.height,
            d=self.diameter,
            angle=self.chamfer_angle,
            l_ch=self.chamfer_length,
            )
    

        
class BodyBlock(Solid):
    """This object represents cylinder solid.
    
    The cylinder object has predefined numbers of lines and dimensions that 
    are needed make a engineering drawing. Also it stores information about 
    height and diameter.
    
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
    color = 'k'

    num_of_lines_view = {
        'horizontal_lines': 3,
        'vertical_lines': 2,
        'horizontal_dimensions': 1,
        'vertical_dimensions': 0,
        'inclined_lines': 0,
    }
    num_of_lines_sec = {
        'horizontal_lines': 3,
        'vertical_lines': 2,
        'horizontal_dimensions': 1,
        'vertical_dimensions': 0, # including the axis position (it doesn't make any sense for holes lack)
        'inclined_lines': 0,
    }

    num_of_lines_half_sec = {
        'horizontal_lines': 3,
        'vertical_lines': 2,
        'horizontal_dimensions': 1,
        'vertical_dimensions': 0, # including the axis position (it doesn't make any sense for holes lack)
        'inclined_lines': 0,
    }

    num_of_lines_front = {'circles': 1, 'phi_dimensions': 0}

    @classmethod
    def num_of_lines(cls,type_of_view):
        
        if type_of_view == 'view':
            return cls.num_of_lines_view
        elif type_of_view == 'section':
            return cls.num_of_lines_sec
        elif type_of_view == 'halfsection':
            return cls.num_of_lines_half_sec
        else:
            return {}

    def __init__(self,
             height,
             length,
             width,
             axis_height,
             holes_diameter=None,
             holes_no=4 ):

        num_of_lines_view = self.num_of_lines('view') #test of class methdo
        num_of_lines_view = self.__class__.num_of_lines_view
        num_of_lines_sec = self.__class__.num_of_lines_sec
        num_of_lines_half_sec = self.__class__.num_of_lines_half_sec
        num_of_lines_front = self.__class__.num_of_lines_front

        super().__init__(View(**num_of_lines_view),
                         Section(**num_of_lines_sec),
                         HalfSection(**num_of_lines_half_sec),
                         FrontView(**num_of_lines_front))

        self.length = length
        self.height = height
 
        self.width = width
        self.axis_height=axis_height
        self.holes_no = holes_no
        self._holes_diameter=holes_diameter

        
    @property
    def holes_diameter(self):
        if self._holes_diameter:
            return self._holes_diameter
        else:
            return round(self.length*0.15)

    def str_en(self):
        return 'Simple bearing block with length={l}mm, \n height={h}mm, width={w}mm \n and {no} fixing holes d={hole_d}mm \n placed on the body edge'.format(
            l=self.length,
            h=self.height,
            w=self.width,
            no=self.holes_no,
            hole_d= self.holes_diameter)

    def str_pl(self):
        return 'Podpora łożyskowa o grubości g={l}mm \n wysokości={h}mm, zerokości={w}mm \n i {no} otworach montażowych d={hole_d}mm \n umiejscowionych na brzegu'.format(
            l=self.length,
            h=self.height,
            w=self.width,
            no=self.holes_no,
            hole_d= self.holes_diameter).replace('right',
                                     'prawej').replace('left', 'lewej')

    @property
    def space_btwn(self):
        return SPACE_BTW
    
    @property
    def height_upper(self):
        return self.height -self.axis_height

    @property
    def height_lower(self):
        return -self.axis_height
    
    @property    
    def _front_view_outline(self):
        
        origin = self.origin / 10
        l = self.length / 10
        h_up = self.height_upper / 10
        h_lw = self.height_lower / 10
        w = self.width / 10
        
        t_l = origin + l 
        t_r = (-l - 25)
        
        
        x_coords=np.array([0, 0, w,  w, 0])-w/2
        y_coords=np.array([h_lw, h_up, h_up, h_lw, h_lw])
        
        
        return np.array([[x,y]  for x,y in zip(x_coords,y_coords)])
    
    
    def _plot_2d(self, language='en'):

        #         print(f'self.origin property is {self.origin()}')
        #         print(f'self.end property is {self.end()}')



        origin = self.origin / 10
        l = self.length / 10
        h_up = self.height_upper / 10
        h_lw = self.height_lower / 10
        w = self.width / 10
        
        s = self.space_btwn/10

        t_l = origin + l 
        t_r = (+h_up +1)

        line_type = self.line_type
        color = self.color
        
        front_view=self._front_view_outline
        
        

        res = GeometryScene.ax_2d.plot(
            origin +np.array([0, 0,  l,  l,  0]),
            [h_lw, h_up, h_up, h_lw, h_lw],
            line_type,
            color=color) + GeometryScene.ax_2d.plot(
                front_view[:,0]+s, 
                front_view[:,1],
                '-',
                color='k',
                linewidth=1) + GeometryScene.ax_2d.plot(
            s - w/2 + 0.15*l +np.array([0, 0,  l,  l,  0])*0.15,
            [h_lw, h_up, h_up, h_lw, h_lw],
            '--',
            color='b')  + GeometryScene.ax_2d.plot(
            s + w/2 - 0.3*l +np.array([0, 0,  l,  l,  0])*0.15,
            [h_lw, h_up, h_up, h_lw, h_lw],
            '--',
            color='b')

        if language == 'pl':
            text = GeometryScene.ax_2d.text(t_l,
                                            t_r,
                                            self.str_pl(),
                                            rotation='vertical',
                                            multialignment='center')
        else:
            text = GeometryScene.ax_2d.text(t_l,
                                            t_r,
                                            self.str_en(),
                                            rotation='vertical',
                                            multialignment='center')

        BlockPreview(0,0, origin/2,
                     self._front_view_outline, l / 2, "bez fazy", 0.2, '#6b7aa1')


class BodyBlockShapeT(BodyBlock):
    
    line_type = '-'
    color = 'k'

    line_type = '-'
    color = 'k'

    num_of_lines_view = {
        'horizontal_lines': 4,
        'vertical_lines': 2,
        'horizontal_dimensions': 1,
        'vertical_dimensions': 0,
        'inclined_lines': 0,
    }
    num_of_lines_sec = {
        'horizontal_lines': 3,
        'vertical_lines': 2,
        'horizontal_dimensions': 1,
        'vertical_dimensions': 0, # including the axis position (it doesn't make any sense for holes lack)
        'inclined_lines': 0,
    }

    num_of_lines_half_sec = {
        'horizontal_lines': 3,
        'vertical_lines': 2,
        'horizontal_dimensions': 1,
        'vertical_dimensions': 0, # including the axis position (it doesn't make any sense for holes lack)
        'inclined_lines': 0,
    }

    num_of_lines_front = {'circles': 1, 'phi_dimensions': 0}


    
    @property
    def height_wider(self):
        return round(self.height*0.2)
    
    @property
    def indentation_wider(self):
        return round(self.width * 0.55)
    
    @property
    def _front_view_outline(self):
        
        origin = self.origin / 10
        l = self.length / 10
        h_up = self.height_upper / 10
        h_lw = self.height_lower / 10
        w = self.width / 10
        w_w = self.indentation_wider /10
        h_w = self.height_wider /10

        t_l = origin + l 
        t_r = (-l - 25)
        
        
        x_coords=np.array([0, 0,  w/2 - w_w/2 ,  w/2 - w_w/2 ,  w/2 + w_w/2,  w/2 + w_w/2,  w,   w,  0])-w/2
        y_coords=np.array([h_lw, h_lw + h_w, h_lw + h_w, h_up, h_up, h_lw + h_w, h_lw + h_w, h_lw, h_lw])
        
        
        return np.array([[x,y]  for x,y in zip(x_coords,y_coords)])
    
    def _plot_2d(self, language='en'):



        origin = self.origin / 10
        l = self.length / 10
        h_up = self.height_upper / 10
        h_lw = self.height_lower / 10
        w = self.width / 10
        w_w = self.indentation_wider /10
        h_w = self.height_wider /10
        
        s = self.space_btwn /10
        

        t_l = origin + l 
        t_r = (+h_up +1)

        line_type = self.line_type
        color = self.color
        
        front_view=self._front_view_outline
        
        

        res = GeometryScene.ax_2d.plot(
            origin +np.array([0, 0,  l,  l,  0]),
            [h_lw, h_up, h_up, h_lw, h_lw],
            line_type,
            color=color) + GeometryScene.ax_2d.plot(
                front_view[:,0]+s, 
                front_view[:,1],
                '-',
                color='k',
                linewidth=1) + GeometryScene.ax_2d.plot(
            s - w/2 + 0.1*l +np.array([0, 0,  l,  l,  0])*0.15,
            [h_lw, h_lw + h_w, h_lw + h_w, h_lw, h_lw],
            '--',
            color='b') + GeometryScene.ax_2d.plot(
            s + w/2 - 0.25*l +np.array([0, 0,  l,  l,  0])*0.15,
            [h_lw, h_lw + h_w, h_lw + h_w, h_lw, h_lw],
            '--',
            color='b')

        if language == 'pl':
            text = GeometryScene.ax_2d.text(t_l,
                                            t_r,
                                            self.str_pl(),
                                            rotation='vertical',
                                            multialignment='center')
        else:
            text = GeometryScene.ax_2d.text(t_l,
                                            t_r,
                                            self.str_en(),
                                            rotation='vertical',
                                            multialignment='center')

        BlockPreview(0,0, origin/2,
                     self._front_view_outline, l / 2, "bez fazy", 0.2, '#6b7aa1')

        
        
    def str_en(self):
        return 'Bearing block (type T - light) with length={l}mm, \n height={h}mm, width={w}mm \n and {no} fixing holes d={hole_d}mm \n placed on the body edge'.format(
            l=self.length,
            h=self.height,
            w=self.width,
            no=self.holes_no,
            hole_d= self.holes_diameter)

    def str_pl(self):
        return 'Podpora łożyskowa (typ T - lekka) o grubości g={l}mm \n wysokości={h}mm, zerokości={w}mm \n i {no} otworach montażowych d={hole_d}mm \n umiejscowionych na brzegu'.format(
            l=self.length,
            h=self.height,
            w=self.width,
            no=self.holes_no,
            hole_d= self.holes_diameter).replace('right',
                                     'prawej').replace('left', 'lewej')

    
class MediumBodyBlockShapeT(BodyBlockShapeT):
    
    
    @property
    def height_wider(self):
        return round(self.height*0.35)
    


    
    def str_en(self):
        return 'Bearing block (type T - medium) with length={l}mm, \n height={h}mm, width={w}mm \n and {no} fixing holes d={hole_d}mm \n placed on the body edge'.format(
            l=self.length,
            h=self.height,
            w=self.width,
            no=self.holes_no,
            hole_d= self.holes_diameter)

    def str_pl(self):
        return 'Podpora łożyskowa (typ T - średnia) o grubości g={l}mm \n wysokości={h}mm, zerokości={w}mm \n i {no} otworach montażowych d={hole_d}mm \n umiejscowionych na brzegu'.format(
            l=self.length,
            h=self.height,
            w=self.width,
            no=self.holes_no,
            hole_d= self.holes_diameter).replace('right',
                                     'prawej').replace('left', 'lewej')
    

    
class HeavyBodyBlockShapeT(BodyBlockShapeT):
    
    
    @property
    def height_wider(self):
        return round(self.height*0.9)
    


    
    def str_en(self):
        return 'Bearing block (type T - heavy) with length={l}mm, \n height={h}mm, width={w}mm \n and {no} fixing holes d={hole_d}mm \n placed on the body edge'.format(
            l=self.length,
            h=self.height,
            w=self.width,
            no=self.holes_no,
            hole_d= self.holes_diameter)

    def str_pl(self):
        return 'Podpora łożyskowa (typ T - ciężka) o grubości g={l}mm \n wysokości={h}mm, zerokości={w}mm \n i {no} otworach montażowych d={hole_d}mm \n umiejscowionych na brzegu'.format(
            l=self.length,
            h=self.height,
            w=self.width,
            no=self.holes_no,
            hole_d= self.holes_diameter).replace('right',
                                     'prawej').replace('left', 'lewej')    
    
    
    
    
class BodyBlockShapeC(BodyBlock):
    
    line_type = '-'
    color = 'k'

    num_of_lines_view = {
        'horizontal_lines': 3,
        'vertical_lines': 2,
        'horizontal_dimensions': 1,
        'vertical_dimensions': 0,
        'inclined_lines': 0,
    }
    num_of_lines_sec = {
        'horizontal_lines': 3,
        'vertical_lines': 2,
        'horizontal_dimensions': 1,
        'vertical_dimensions': 0,
        'inclined_lines': 0,
    }

    num_of_lines_half_sec = {
        'horizontal_lines': 3,
        'vertical_lines': 2,
        'horizontal_dimensions': 1,
        'vertical_dimensions': 0,
        'inclined_lines': 0,
    }

    num_of_lines_front = {'circles': 1, 'phi_dimensions': 0}

    @classmethod
    def num_of_lines(cls,type_of_view):
        
        if type_of_view == 'view':
            return cls.num_of_lines_view
        elif type_of_view == 'section':
            return cls.num_of_lines_sec
        elif type_of_view == 'halfsection':
            return cls.num_of_lines_half_sec
        else:
            return {}

    
    @property
    def height_upper(self):
        return self.height -self.axis_height

    @property
    def height_lower(self):
        return -self.axis_height
    
    @property
    def height_wider(self):
        return 20
    
    @property
    def indentation_wider(self):
        return self.width * 1/5
    
    @property    
    def _front_view_outline(self):

        origin = self.origin / 10
        l = self.length / 10
        h_up = self.height_upper / 10
        h_lw = self.height_lower / 10
        w = self.width / 10
        w_w = self.indentation_wider /10
        h_w = self.height_wider /10
        
        t_l = origin + l / 4
        t_r = (-l - 20)
        
        x_coords=np.array([0, 0, w_w, w_w, 0, 0, w, w, 0])-w*3/5
        y_coords=np.array([h_lw, h_lw + h_w, h_lw + h_w, h_up - h_w, h_up - h_w, h_up, h_up, h_lw, h_lw])

        return np.array([[x,y]  for x,y in zip(x_coords,y_coords)])
    
    def _plot_2d(self, language='en'):

        #         print(f'self.origin property is {self.origin()}')
        #         print(f'self.end property is {self.end()}')

        class_name = self.__class__.__name__

        span = np.linspace(0, len(class_name), 100)
        #         print(f'plot_2d is called for {class_name}')

        origin = self.origin / 10
        l = self.length / 10
        h_up = self.height_upper / 10
        h_lw = self.height_lower / 10
        w = self.width / 10
        w_w = self.indentation_wider /10
        h_w = self.height_wider /10
        
        s = self.space_btwn /10
        
        t_l = origin + l 
        t_r = (-l - 25)
        
        front_view=self._front_view_outline
        
        line_type = self.line_type
        color = self.color

        res = GeometryScene.ax_2d.plot(
            origin +np.array([0, 0, l, l, 0]),
            [h_lw, h_up, h_up, h_lw, h_lw],
            line_type,
            color=color,
            linewidth = 1) + GeometryScene.ax_2d.plot(
                origin +np.array([0, l]),
                [h_up - h_w, h_up - h_w],
                line_type,
                color=color,
                linewidth = 1) + GeometryScene.ax_2d.plot(
                    origin +np.array([0, l]),
                    [h_lw + h_w, h_lw + h_w],
                    line_type,
                    color=color,
                    linewidth = 1) + GeometryScene.ax_2d.plot(
                        front_view[:,0]+s, 
                        front_view[:,1],
                        '-',
                        color='k',
                        linewidth=1) + GeometryScene.ax_2d.plot(
            s - w/2 - 0.07*l +np.array([0, 0,  l,  l,  0])*0.15,
            [h_lw, h_lw + h_w, h_lw + h_w, h_lw, h_lw],
            '--',
            color='b')  + GeometryScene.ax_2d.plot(
            s - w/2 - 0.07*l +np.array([0, 0,  l,  l,  0])*0.15,
            [h_up, h_up - h_w, h_up - h_w, h_up, h_up],
            '--',
            color='b') 

        if language == 'pl':
            text = GeometryScene.ax_2d.text(t_l,
                                            t_r,
                                            self.str_pl(),
                                            rotation='vertical',
                                            multialignment='center')
        else:
            text = GeometryScene.ax_2d.text(t_l,
                                            t_r,
                                            self.str_en(),
                                            rotation='vertical',
                                            multialignment='center')

#         BlockPreview(0,0, origin/2,
#         self._front_view_outline, l / 2, "bez fazy", 0.2, '#6b7aa1')
        BlockPreview(0,0, origin/2,
        self._front_view_outline, l / 2, "bez fazy", 0.2, '#6b7aa1')
#         ShaftPreview(0,0, origin / 2,
#                      [2 * l / 2, l / 2, "bez fazy", 0.2, '#6b7aa1'])

        print(res)

class BodyBlockCutType(BodyBlock):
    
    line_type = '-'
    color = 'k'

    num_of_lines_view = {
        'horizontal_lines': 3,
        'vertical_lines': 2,
        'horizontal_dimensions': 1,
        'vertical_dimensions': 0,
        'inclined_lines': 0,
    }
    num_of_lines_sec = {
        'horizontal_lines': 3,
        'vertical_lines': 2,
        'horizontal_dimensions': 1,
        'vertical_dimensions': 0,
        'inclined_lines': 0,
    }

    num_of_lines_half_sec = {
        'horizontal_lines': 3,
        'vertical_lines': 2,
        'horizontal_dimensions': 1,
        'vertical_dimensions': 0,
        'inclined_lines': 0,
    }

    num_of_lines_front = {'circles': 1, 'phi_dimensions': 0}

    @classmethod
    def num_of_lines(cls,type_of_view):
        
        if type_of_view == 'view':
            return cls.num_of_lines_view
        elif type_of_view == 'section':
            return cls.num_of_lines_sec
        elif type_of_view == 'halfsection':
            return cls.num_of_lines_half_sec
        else:
            return {}

    
    @property
    def height_upper(self):
        return self.height -self.axis_height

    @property
    def height_lower(self):
        return -self.axis_height
    
    @property
    def height_wider(self):
        return 20
    
    @property
    def indentation_wider(self):
        return self.width * 1/5
    
    @property    
    def _front_view_outline(self):

        origin = self.origin / 10
        l = self.length / 10
        h_up = self.height_upper / 10
        h_lw = self.height_lower / 10
        w = self.width / 10
        w_w = self.indentation_wider /10
        h_w = self.height_wider /10
        

        x_coords=np.array([0, 0, w_w, w_w, 2*w_w, w, w, 0])-w*3/5
        y_coords=np.array([h_lw, h_lw + h_w, h_lw + h_w, h_up - h_w, h_up, h_up, h_lw, h_lw])

        return np.array([[x,y]  for x,y in zip(x_coords,y_coords)])
    
    def _plot_2d(self, language='en'):

        #         print(f'self.origin property is {self.origin()}')
        #         print(f'self.end property is {self.end()}')

        class_name = self.__class__.__name__

        span = np.linspace(0, len(class_name), 100)
        #         print(f'plot_2d is called for {class_name}')

        origin = self.origin / 10
        l = self.length / 10
        h_up = self.height_upper / 10
        h_lw = self.height_lower / 10
        w = self.width / 10
        w_w = self.indentation_wider /10
        h_w = self.height_wider /10
        
        s = self.space_btwn /10
        front_view=self._front_view_outline
        t_l = origin - 1 / 10
        t_r = (-l - 22)
        
        line_type = self.line_type
        color = self.color

        res = GeometryScene.ax_2d.plot(
            origin +np.array([0, 0, l, l, 0]),
            [h_lw, h_up, h_up, h_lw, h_lw],
            line_type,
            color=color,
            linewidth = 1) + GeometryScene.ax_2d.plot(
                origin +np.array([0, l]),
                [h_up - h_w, h_up - h_w],
                line_type,
                color=color,
                linewidth = 1) + GeometryScene.ax_2d.plot(
                    origin +np.array([0, l]),
                    [h_lw + h_w, h_lw + h_w],
                    line_type,
                    color=color,
                    linewidth = 1) + GeometryScene.ax_2d.plot(
                        front_view[:,0]+s, 
                        front_view[:,1],
                        '-',
                        color='k',
                        linewidth=1)  + GeometryScene.ax_2d.plot(
            s - w/2 - 0.07*l +np.array([0, 0,  l,  l,  0])*0.15,
            [h_lw, h_lw + h_w, h_lw + h_w, h_lw, h_lw],
            '--',
            color='b') 

        if language == 'pl':
            text = GeometryScene.ax_2d.text(t_l,
                                            t_r,
                                            self.str_pl(),
                                            rotation='vertical',
                                            multialignment='center')
        else:
            text = GeometryScene.ax_2d.text(t_l,
                                            t_r,
                                            self.str_en(),
                                            rotation='vertical',
                                            multialignment='center')

        BlockPreview(0,0, origin/2,
        self._front_view_outline, l / 2, "bez fazy", 0.2, '#6b7aa1')

        print(res)
        
class RoundedBodyBlock(Solid):
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
    color = 'k'

    num_of_lines_view = {
        'horizontal_lines': 3,
        'vertical_lines': 2,
        'horizontal_dimensions': 1,
        'vertical_dimensions': 1,
        'inclined_lines': 0,
    }
    num_of_lines_sec = {
        'horizontal_lines': 3,
        'vertical_lines': 2,
        'horizontal_dimensions': 1,
        'vertical_dimensions': 2, # including the axis position (it doesn't make any sense for holes lack)
        'inclined_lines': 0,
    }

    num_of_lines_half_sec = {
        'horizontal_lines': 3,
        'vertical_lines': 2,
        'horizontal_dimensions': 1,
        'vertical_dimensions': 2, # including the axis position (it doesn't make any sense for holes lack)
        'inclined_lines': 0,
    }

    num_of_lines_front = {'circles': 1, 'phi_dimensions': 0}

    @classmethod
    def num_of_lines(cls,type_of_view):
        
        if type_of_view == 'view':
            return cls.num_of_lines_view
        elif type_of_view == 'section':
            return cls.num_of_lines_sec
        elif type_of_view == 'halfsection':
            return cls.num_of_lines_half_sec
        else:
            return {}

    def __init__(self,
             height,
             length,
             width,
             axis_height,
             holes_diameter=None,
             holes_no=4 ):

        num_of_lines_view = self.num_of_lines('view')
        num_of_lines_sec = self.__class__.num_of_lines_sec
        num_of_lines_half_sec = self.__class__.num_of_lines_half_sec
        num_of_lines_front = self.__class__.num_of_lines_front

        super().__init__(View(**num_of_lines_view),
                         Section(**num_of_lines_sec),
                         HalfSection(**num_of_lines_half_sec),
                         FrontView(**num_of_lines_front))

        self.length = length
        self.height = height
 
        self.width = width
        self.axis_height=axis_height
        self.holes_no = holes_no
        self._holes_diameter=holes_diameter

        
    @property
    def holes_diameter(self):
        if self._holes_diameter:
            return self._holes_diameter
        else:
            return round(self.length*0.15)

    def str_en(self):
        return 'Simple rounded bearing block with length={l}mm, \n height={h}mm, width={w}mm \n and {no} fixing holes d={hole_d}mm \n placed on the body edge'.format(
            l=self.length,
            h=self.height,
            w=self.width,
            no=self.holes_no,
            hole_d= self.holes_diameter)

    def str_pl(self):
        return 'Zaokrąglona podpora łożyskowa o grubości g={l}mm \n wysokości={h}mm, zerokości={w}mm \n i {no} otworach montażowych d={hole_d}mm \n umiejscowionych na brzegu'.format(
            l=self.length,
            h=self.height,
            w=self.width,
            no=self.holes_no,
            hole_d= self.holes_diameter).replace('right',
                                     'prawej').replace('left', 'lewej')

    @property
    def space_btwn(self):
        return SPACE_BTW
    
    @property
    def height_upper(self):
        return self.height -self.axis_height

    @property
    def height_lower(self):
        return -self.axis_height
    
    @property    
    def _front_view_outline(self):
        
        origin = self.origin / 10
        l = self.length / 10
        h_up = self.height_upper / 10
        h_lw = self.height_lower / 10
        w = self.width / 10
        
        t_l = origin + l 
        t_r = (-l - 25)
        
        
        x_coords=np.array([0, 0, w,  w, 0])-w/2
        y_coords=np.array([h_lw, h_up, h_up, h_lw, h_lw])
        
        
        return np.array([[x,y]  for x,y in zip(x_coords,y_coords)])
    
    
    def _plot_2d(self, language='en'):

        #         print(f'self.origin property is {self.origin()}')
        #         print(f'self.end property is {self.end()}')



        origin = self.origin / 10
        l = self.length / 10
        h_up = self.height_upper / 10
        h_lw = self.height_lower / 10
        w = self.width / 10
        
        s = self.space_btwn/10

        t_l = origin + l 
        t_r = (+h_up +1)

        line_type = self.line_type
        color = self.color
        
        front_view=self._front_view_outline
        
        

        res = GeometryScene.ax_2d.plot(
            origin +np.array([0, 0,  l,  l,  0]),
            [h_lw, h_up, h_up, h_lw, h_lw],
            line_type,
            color=color) + GeometryScene.ax_2d.plot(
                front_view[:,0]+s, 
                front_view[:,1],
                '-',
                color='k',
                linewidth=1) + GeometryScene.ax_2d.plot(
            s - w/2 + 0.15*l +np.array([0, 0,  l,  l,  0])*0.15,
            [h_lw, h_up, h_up, h_lw, h_lw],
            '--',
            color='b')  + GeometryScene.ax_2d.plot(
            s + w/2 - 0.3*l +np.array([0, 0,  l,  l,  0])*0.15,
            [h_lw, h_up, h_up, h_lw, h_lw],
            '--',
            color='b')

        if language == 'pl':
            text = GeometryScene.ax_2d.text(t_l,
                                            t_r,
                                            self.str_pl(),
                                            rotation='vertical',
                                            multialignment='center')
        else:
            text = GeometryScene.ax_2d.text(t_l,
                                            t_r,
                                            self.str_en(),
                                            rotation='vertical',
                                            multialignment='center')

        BlockPreview(0,0, origin/2,
                     self._front_view_outline, l / 2, "bez fazy", 0.2, '#6b7aa1')


class RoundedBodyBlockShapeT(RoundedBodyBlock):
    
    line_type = '-'
    color = 'k'

    line_type = '-'
    color = 'k'

    num_of_lines_view = {
        'horizontal_lines': 4,
        'vertical_lines': 2,
        'horizontal_dimensions': 1,
        'vertical_dimensions': 0,
        'inclined_lines': 0,
    }
    num_of_lines_sec = {
        'horizontal_lines': 3,
        'vertical_lines': 2,
        'horizontal_dimensions': 1,
        'vertical_dimensions': 0, # including the axis position (it doesn't make any sense for holes lack)
        'inclined_lines': 0,
    }

    num_of_lines_half_sec = {
        'horizontal_lines': 4,
        'vertical_lines': 2,
        'horizontal_dimensions': 1,
        'vertical_dimensions': 0, # including the axis position (it doesn't make any sense for holes lack)
        'inclined_lines': 0,
    }

    num_of_lines_front = {'circles': 1, 'phi_dimensions': 0}


    
    @property
    def height_wider(self):
        return round(self.height*0.2)
    
    @property
    def indentation_wider(self):
        return round(self.width * 0.55)
    
    @property
    def _front_view_outline(self):
        
        origin = self.origin / 10
        l = self.length / 10
        h_up = self.height_upper / 10
        h_lw = self.height_lower / 10
        w = self.width / 10
        w_w = self.indentation_wider /10
        h_w = self.height_wider /10

        t_l = origin + l 
        t_r = (-l - 25)
        
        
        x_coords=np.array([0, 0,  w/2 - w_w/2 ,  w/2 - w_w/2 ,  w/2 + w_w/2,  w/2 + w_w/2,  w,   w,  0])-w/2
        y_coords=np.array([h_lw, h_lw + h_w, h_lw + h_w, h_up, h_up, h_lw + h_w, h_lw + h_w, h_lw, h_lw])
        
        
        return np.array([[x,y]  for x,y in zip(x_coords,y_coords)])
    
    def _plot_2d(self, language='en'):



        origin = self.origin / 10
        l = self.length / 10
        h_up = self.height_upper / 10
        h_lw = self.height_lower / 10
        w = self.width / 10
        w_w = self.indentation_wider /10
        h_w = self.height_wider /10
        
        s = self.space_btwn /10
        

        t_l = origin + l 
        t_r = (+h_up +1)

        line_type = self.line_type
        color = self.color
        
        front_view=self._front_view_outline
        
        

        res = GeometryScene.ax_2d.plot(
            origin +np.array([0, 0,  l,  l,  0]),
            [h_lw, h_up, h_up, h_lw, h_lw],
            line_type,
            color=color) + GeometryScene.ax_2d.plot(
                front_view[:,0]+s, 
                front_view[:,1],
                '-',
                color='k',
                linewidth=1) + GeometryScene.ax_2d.plot(
            s - w/2 + 0.1*l +np.array([0, 0,  l,  l,  0])*0.15,
            [h_lw, h_lw + h_w, h_lw + h_w, h_lw, h_lw],
            '--',
            color='b')  + GeometryScene.ax_2d.plot(
            s + w/2 - 0.25*l +np.array([0, 0,  l,  l,  0])*0.15,
            [h_lw, h_lw + h_w, h_lw + h_w, h_lw, h_lw],
            '--',
            color='b')

        if language == 'pl':
            text = GeometryScene.ax_2d.text(t_l,
                                            t_r,
                                            self.str_pl(),
                                            rotation='vertical',
                                            multialignment='center')
        else:
            text = GeometryScene.ax_2d.text(t_l,
                                            t_r,
                                            self.str_en(),
                                            rotation='vertical',
                                            multialignment='center')

        BlockPreview(0,0, origin/2,
                     self._front_view_outline, l / 2, "bez fazy", 0.2, '#6b7aa1')

        
        
    def str_en(self):
        return 'Bearing rounded block (type T - light) with length={l}mm, \n height={h}mm, width={w}mm \n and {no} fixing holes d={hole_d}mm \n placed on the body edge'.format(
            l=self.length,
            h=self.height,
            w=self.width,
            no=self.holes_no,
            hole_d= self.holes_diameter)

    def str_pl(self):
        return 'Zaokrąglona podpora łożyskowa (typ T - lekka) o grubości g={l}mm \n wysokości={h}mm, zerokości={w}mm \n i {no} otworach montażowych d={hole_d}mm \n umiejscowionych na brzegu'.format(
            l=self.length,
            h=self.height,
            w=self.width,
            no=self.holes_no,
            hole_d= self.holes_diameter).replace('right',
                                     'prawej').replace('left', 'lewej')

    
class RoundedMediumBodyBlockShapeT(RoundedBodyBlockShapeT):
    
    
    @property
    def height_wider(self):
        return round(self.height*0.35)
    


    
    def str_en(self):
        return 'Bearing rounded block (type T - medium) with length={l}mm, \n height={h}mm, width={w}mm \n and {no} fixing holes d={hole_d}mm \n placed on the body edge'.format(
            l=self.length,
            h=self.height,
            w=self.width,
            no=self.holes_no,
            hole_d= self.holes_diameter)

    def str_pl(self):
        return 'Zaokrąglona podpora łożyskowa (typ T - średnia) o grubości g={l}mm \n wysokości={h}mm, zerokości={w}mm \n i {no} otworach montażowych d={hole_d}mm \n umiejscowionych na brzegu'.format(
            l=self.length,
            h=self.height,
            w=self.width,
            no=self.holes_no,
            hole_d= self.holes_diameter).replace('right',
                                     'prawej').replace('left', 'lewej')
    

    
class RoundedHeavyBodyBlockShapeT(RoundedBodyBlockShapeT):
    
    
    @property
    def height_wider(self):
        return round(self.height*0.6)
    


    
    def str_en(self):
        return 'Bearing rounded block (type T - heavy) with length={l}mm, \n height={h}mm, width={w}mm \n and {no} fixing holes d={hole_d}mm \n placed on the body edge'.format(
            l=self.length,
            h=self.height,
            w=self.width,
            no=self.holes_no,
            hole_d= self.holes_diameter)

    def str_pl(self):
        return 'Zaokrąglona podpora łożyskowa (typ T - ciężka) o grubości g={l}mm \n wysokości={h}mm, zerokości={w}mm \n i {no} otworach montażowych d={hole_d}mm \n umiejscowionych na brzegu'.format(
            l=self.length,
            h=self.height,
            w=self.width,
            no=self.holes_no,
            hole_d= self.holes_diameter).replace('right',
                                     'prawej').replace('left', 'lewej')    
    
    
    
    
class RoundedBodyBlockShapeC(RoundedBodyBlock):
    
    line_type = '-'
    color = 'k'

    num_of_lines_view = {
        'horizontal_lines': 3,
        'vertical_lines': 2,
        'horizontal_dimensions': 1,
        'vertical_dimensions': 2,
        'inclined_lines': 0,
    }
    num_of_lines_sec = {
        'horizontal_lines': 3,
        'vertical_lines': 2,
        'horizontal_dimensions': 1,
        'vertical_dimensions': 1,
        'inclined_lines': 0,
    }

    num_of_lines_half_sec = {
        'horizontal_lines': 3,
        'vertical_lines': 2,
        'horizontal_dimensions': 1,
        'vertical_dimensions': 1,
        'inclined_lines': 0,
    }

    num_of_lines_front = {'circles': 1, 'phi_dimensions': 0}

    @classmethod
    def num_of_lines(cls,type_of_view):
        
        if type_of_view == 'view':
            return cls.num_of_lines_view
        elif type_of_view == 'section':
            return cls.num_of_lines_sec
        elif type_of_view == 'halfsection':
            return cls.num_of_lines_half_sec
        else:
            return {}
    
    @property
    def height_upper(self):
        return self.height -self.axis_height

    @property
    def height_lower(self):
        return -self.axis_height
    
    @property
    def height_wider(self):
        return 20
    
    @property
    def indentation_wider(self):
        return self.width * 1/5
    
    @property
    def _front_view_outline(self):

        origin = self.origin / 10
        l = self.length / 10
        h_up = self.height_upper / 10
        h_lw = self.height_lower / 10
        w = self.width / 10
        w_w = self.indentation_wider /10
        h_w = self.height_wider /10
        
        t_l = origin + l / 4
        t_r = (-l - 20)
        
        x_coords=np.array([0, 0, w_w, w_w, 0, 0, w, w, 0])-w*3/5
        y_coords=np.array([h_lw, h_lw + h_w, h_lw + h_w, h_up - h_w, h_up - h_w, h_up, h_up, h_lw, h_lw])

        return np.array([[x,y]  for x,y in zip(x_coords,y_coords)])
    
    def _plot_2d(self, language='en'):

        #         print(f'self.origin property is {self.origin()}')
        #         print(f'self.end property is {self.end()}')

        class_name = self.__class__.__name__

        span = np.linspace(0, len(class_name), 100)
        #         print(f'plot_2d is called for {class_name}')

        origin = self.origin / 10
        l = self.length / 10
        h_up = self.height_upper / 10
        h_lw = self.height_lower / 10
        w = self.width / 10
        w_w = self.indentation_wider /10
        h_w = self.height_wider /10
        
        s = self.space_btwn /10
        
        t_l = origin + l 
        t_r = (-l - 25)
        
        front_view=self._front_view_outline
        
        line_type = self.line_type
        color = self.color

        res = GeometryScene.ax_2d.plot(
            origin +np.array([0, 0, l, l, 0]),
            [h_lw, h_up, h_up, h_lw, h_lw],
            line_type,
            color=color,
            linewidth = 1) + GeometryScene.ax_2d.plot(
                origin +np.array([0, l]),
                [h_up - h_w, h_up - h_w],
                line_type,
                color=color,
                linewidth = 1) + GeometryScene.ax_2d.plot(
                    origin +np.array([0, l]),
                    [h_lw + h_w, h_lw + h_w],
                    line_type,
                    color=color,
                    linewidth = 1) + GeometryScene.ax_2d.plot(
                        front_view[:,0]+s, 
                        front_view[:,1],
                        '-',
                        color='k',
                        linewidth=1) + GeometryScene.ax_2d.plot(
            s - w/2 - 0.07*l +np.array([0, 0,  l,  l,  0])*0.15,
            [h_lw, h_lw + h_w, h_lw + h_w, h_lw, h_lw],
            '--',
            color='b')  + GeometryScene.ax_2d.plot(
            s - w/2 - 0.07*l +np.array([0, 0,  l,  l,  0])*0.15,
            [h_up, h_up - h_w, h_up - h_w, h_up, h_up],
            '--',
            color='b') 

        if language == 'pl':
            text = GeometryScene.ax_2d.text(t_l,
                                            t_r,
                                            self.str_pl(),
                                            rotation='vertical',
                                            multialignment='center')
        else:
            text = GeometryScene.ax_2d.text(t_l,
                                            t_r,
                                            self.str_en(),
                                            rotation='vertical',
                                            multialignment='center')

#         BlockPreview(0,0, origin/2,
#         self._front_view_outline, l / 2, "bez fazy", 0.2, '#6b7aa1')
        BlockPreview(0,0, origin/2,
        self._front_view_outline, l / 2, "bez fazy", 0.2, '#6b7aa1')
#         ShaftPreview(0,0, origin / 2,
#                      [2 * l / 2, l / 2, "bez fazy", 0.2, '#6b7aa1'])

        print(res)

class RoundedBodyBlockCutType(RoundedBodyBlock):
    
    line_type = '-'
    color = 'k'

    num_of_lines_view = {
        'horizontal_lines': 3,
        'vertical_lines': 2,
        'horizontal_dimensions': 1,
        'vertical_dimensions': 2,
        'inclined_lines': 0,
    }
    num_of_lines_sec = {
        'horizontal_lines': 3,
        'vertical_lines': 2,
        'horizontal_dimensions': 1,
        'vertical_dimensions': 1,
        'inclined_lines': 0,
    }

    num_of_lines_half_sec = {
        'horizontal_lines': 3,
        'vertical_lines': 2,
        'horizontal_dimensions': 1,
        'vertical_dimensions': 1,
        'inclined_lines': 0,
    }

    num_of_lines_front = {'circles': 1, 'phi_dimensions': 0}

    @classmethod
    def num_of_lines(cls,type_of_view):
        
        if type_of_view == 'view':
            return cls.num_of_lines_view
        elif type_of_view == 'section':
            return cls.num_of_lines_sec
        elif type_of_view == 'halfsection':
            return cls.num_of_lines_half_sec
        else:
            return {}
    
    @property
    def height_upper(self):
        return self.height -self.axis_height

    @property
    def height_lower(self):
        return -self.axis_height
    
    @property
    def height_wider(self):
        return 20
    
    @property
    def indentation_wider(self):
        return self.width * 1/5
    
    @property    
    def _front_view_outline(self):

        origin = self.origin / 10
        l = self.length / 10
        h_up = self.height_upper / 10
        h_lw = self.height_lower / 10
        w = self.width / 10
        w_w = self.indentation_wider /10
        h_w = self.height_wider /10
        

        x_coords=np.array([0, 0, w_w, w_w, 2*w_w, w, w, 0])-w*3/5
        y_coords=np.array([h_lw, h_lw + h_w, h_lw + h_w, h_up - h_w, h_up, h_up, h_lw, h_lw])

        return np.array([[x,y]  for x,y in zip(x_coords,y_coords)])
    
    def _plot_2d(self, language='en'):

        #         print(f'self.origin property is {self.origin()}')
        #         print(f'self.end property is {self.end()}')

        class_name = self.__class__.__name__

        span = np.linspace(0, len(class_name), 100)
        #         print(f'plot_2d is called for {class_name}')

        origin = self.origin / 10
        l = self.length / 10
        h_up = self.height_upper / 10
        h_lw = self.height_lower / 10
        w = self.width / 10
        w_w = self.indentation_wider /10
        h_w = self.height_wider /10
        
        s = self.space_btwn /10
        front_view=self._front_view_outline
        t_l = origin - 1 / 10
        t_r = (-l - 22)
        
        line_type = self.line_type
        color = self.color

        res = GeometryScene.ax_2d.plot(
            origin +np.array([0, 0, l, l, 0]),
            [h_lw, h_up, h_up, h_lw, h_lw],
            line_type,
            color=color,
            linewidth = 1) + GeometryScene.ax_2d.plot(
                origin +np.array([0, l]),
                [h_up - h_w, h_up - h_w],
                line_type,
                color=color,
                linewidth = 1) + GeometryScene.ax_2d.plot(
                    origin +np.array([0, l]),
                    [h_lw + h_w, h_lw + h_w],
                    line_type,
                    color=color,
                    linewidth = 1) + GeometryScene.ax_2d.plot(
                        front_view[:,0]+s, 
                        front_view[:,1],
                        '-',
                        color='k',
                        linewidth=1) + GeometryScene.ax_2d.plot(
            s - w/2 - 0.07*l +np.array([0, 0,  l,  l,  0])*0.15,
            [h_lw, h_lw + h_w, h_lw + h_w, h_lw, h_lw],
            '--',
            color='b') 

        if language == 'pl':
            text = GeometryScene.ax_2d.text(t_l,
                                            t_r,
                                            self.str_pl(),
                                            rotation='vertical',
                                            multialignment='center')
        else:
            text = GeometryScene.ax_2d.text(t_l,
                                            t_r,
                                            self.str_en(),
                                            rotation='vertical',
                                            multialignment='center')

        BlockPreview(0,0, origin/2,
        self._front_view_outline, l / 2, "bez fazy", 0.2, '#6b7aa1')

        print(res)

class BlockHole(Hole):
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

    def str_en(self):
        return 'Hole \n with diameter={d}mm \n and length L={length}mm'.format(length=self.height,
                                                         d=self.diameter)

    def str_pl(self):
        return 'Otwór \n o średnicy D={d}mm i długości L={length}mm'.format(
            length=self.height,
            d=self.diameter).replace('right',
                                     'prawej').replace('left', 'lewej')

    @property
    def shift_vertical(self):
        return 0
    
    @property
    def space_btwn(self):
        return SPACE_BTW
    
    @property    
    def _front_view_outline(self):
        
        origin = self.origin / 10
        r = self.diameter / 2 / 10
        l = self.height / 10
        end = self.end / 10

        h_p = l * 2
        v_p = self.shift_vertical
        v_p = self.shift_vertical
        
        t_l = origin + l 
        t_r = (-l - 25)
        
        angle = np.linspace(0,2*np.pi,100)
        x_c = r * np.cos(angle)
        y_c = r * np.sin(angle)
        
        x_coords=x_c
        y_coords=y_c # np.cos zwraca array, czyli taką listę, tylko bardzo wydajną
       
        
        return np.array([[x,y]  for x,y in zip(x_coords,y_coords)])

    def _plot_2d(self, language='en'):

        origin = self.origin / 10
        r = self.diameter / 2 / 10
        l = self.height / 10
        end = self.end / 10

        s_v = 0
        s = self.space_btwn / 10
        
        front_view = self._front_view_outline
        
        t_l = origin + l / 3
        t_r = (-r - 23)

        res = GeometryScene.ax_2d.plot(
            [origin + 0, origin + 0, origin + l, origin + l, origin + 0],
            [-r + s_v, r + s_v, r + s_v, -r + s_v, -r + s_v],
            '--',
            color='b') + GeometryScene.ax_2d.plot(
                [origin - 0.5, origin + l + 0.5],
                [0 + s_v, 0 + s_v],
                '-.',
                color='k',
                linewidth=1) + GeometryScene.ax_2d.plot(
                    front_view[:,0] + s , 
                    front_view[:,1] ,
                    '-',
                    color='b',
                    linewidth=1)


        if language == 'pl':
            text = GeometryScene.ax_2d.text(t_l,
                                            t_r,
                                            self.str_pl(),
                                            rotation='vertical',
                                            multialignment='center')
        else:
            text = GeometryScene.ax_2d.text(t_l,
                                            t_r,
                                            self.str_en(),
                                            rotation='vertical',
                                            multialignment='center')

        BlockPreview(0,0, origin/2,
        self._front_view_outline, l / 2, "bez fazy", 0.2, '#6b7aa1')

class BlockHiddenHole(OpenHole):
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
    num_of_lines_view = {
        'horizontal_lines': 1,
        'vertical_lines': 1,
        'horizontal_dimensions': 0,
        'vertical_dimensions': 0,
        'inclined_lines': 0,
    }
    num_of_lines_sec = {
        'horizontal_lines': 3,
        'vertical_lines': 0,
        'horizontal_dimensions': 0,
        'vertical_dimensions': 1,
        'inclined_lines': 0,
    }

    num_of_lines_half_sec = {
        'horizontal_lines': 2,
        'vertical_lines': 0,
        'horizontal_dimensions': 0,
        'vertical_dimensions': 1,
        'inclined_lines': 0,
    }

    def str_en(self):
        return 'Open hole \n with diameter={d}mm'.format(length=self.height,
                                                         d=self.diameter)

    def str_pl(self):
        return 'Otwór przelotowy \n o średnicy={d}mm'.format(
            length=self.height,
            d=self.diameter).replace('right',
                                     'prawej').replace('left', 'lewej')

    @property
    def shift_vertical(self):
        return 0
    
    @property
    def space_btwn(self):
        return SPACE_BTW
    
    @property    
    def _front_view_outline(self):
        
        origin = self.origin / 10
        r = self.diameter / 2 / 10
        l = self.height / 10
        end = self.end / 10

        h_p = l * 2
        v_p = self.shift_vertical
        v_p = self.shift_vertical
        
        t_l = origin + l 
        t_r = (-l - 25)
        
        angle = np.linspace(0,2*np.pi,100)
        x_c = r * np.cos(angle)
        y_c = r * np.sin(angle)
        
        x_coords=x_c
        y_coords=y_c # np.cos zwraca array, czyli taką listę, tylko bardzo wydajną
       
        
        return np.array([[x,y]  for x,y in zip(x_coords,y_coords)])

    def _plot_2d(self, language='en'):

        origin = self.origin / 10
        r = self.diameter / 2 / 10
        l = self.height / 10
        end = self.end / 10

        s_v = self.shift_vertical /10
        s = self.space_btwn / 10
        
        front_view = self._front_view_outline
        
        t_l = origin + l / 2
        t_r = (-r - 21)

        res = GeometryScene.ax_2d.plot(
            [origin + 0, origin + 0, origin + l, origin + l, origin + 0],
            [-r + s_v, r + s_v, r + s_v, -r + s_v, -r + s_v],
            '--',
            color='b') + GeometryScene.ax_2d.plot(
                [origin - 0.5, origin + l + 0.5],
                [0 + s_v, 0 + s_v],
                '-.',
                color='k',
                linewidth=1) + GeometryScene.ax_2d.plot(
                    front_view[:,0] + s, 
                    front_view[:,1],
                    '--',
                    color='b',
                    linewidth=1)


        if language == 'pl':
            text = GeometryScene.ax_2d.text(t_l,
                                            t_r,
                                            self.str_pl(),
                                            rotation='vertical',
                                            multialignment='center')
        else:
            text = GeometryScene.ax_2d.text(t_l,
                                            t_r,
                                            self.str_en(),
                                            rotation='vertical',
                                            multialignment='center')

        BlockPreview(0,0, origin/2,
        self._front_view_outline, l / 2, "bez fazy", 0.2, '#6b7aa1')
class ShaftWithKeyseatsSketch(Solid):
    line_type = '-'
    color = 'k'

    # Zaktualizowane limity linii dla lepszej czytelności rysunku
    num_of_lines_view = {'horizontal_lines': 5, 'vertical_lines': 4, 'inclined_lines': 2}
    num_of_lines_sec = {'horizontal_lines': 5, 'vertical_lines': 2, 'inclined_lines': 2}
    num_of_lines_half_sec = {'horizontal_lines': 5, 'vertical_lines': 4, 'inclined_lines': 2}
    num_of_lines_front = {'circles': 1, 'phi_dimensions': 0}

    def __init__(self, height, diameter, chamfer_length=1, chamfer_angle=45, chamfer_pos='left'):
        super().__init__(View(**self.num_of_lines_view),
                         Section(**self.num_of_lines_sec),
                         HalfSection(**self.num_of_lines_half_sec),
                         FrontView(**self.num_of_lines_front))

        self.height = height
        self.diameter = diameter
        self.chamfer_length = chamfer_length
        self.chamfer_angle = chamfer_angle
        self.chamfer_pos = chamfer_pos

    def str_en(self):
        return f'Cylinder with Keyseat\nL={self.height}mm, d={self.diameter}mm\nChamfer: {self.chamfer_length}x{self.chamfer_angle}'

    def str_pl(self):
        return f'Walec z rowkiem wpustowym\nL={self.height}mm, d={self.diameter}mm\nFaza: {self.chamfer_length}x{self.chamfer_angle}'

    def _plot_2d(self, language='en'):
        # Skala 1/5 zgodnie z nowym standardem
        origin = self.origin / 5
        r = self.diameter / 2 / 5
        l = self.height / 5
        
        c_l = self.chamfer_length / 5
        c_h = c_l * np.tan(np.radians(self.chamfer_angle))
        
        t_l = origin + l / 2
        t_r = (r + 7) # Pozycja tekstu nad wałkiem

        # --- LOGIKA WSPÓŁRZĘDNYCH DLA FAZ ---
        if self.chamfer_pos == 'left':
            x_obrys = [origin, origin + c_l, origin + l, origin + l, origin + c_l, origin, origin]
            y_obrys = [-r + c_h, -r, -r, r, r, r - c_h, -r + c_h]
            x_hatch = [origin, origin + c_l, origin + l]
            y_hatch = [-r + c_h, -r, -r]
        elif self.chamfer_pos == 'right':
            x_obrys = [origin, origin + l - c_l, origin + l, origin + l, origin + l - c_l, origin, origin]
            y_obrys = [-r, -r, -r + c_h, r - c_h, r, r, -r]
            x_hatch = [origin, origin + l - c_l, origin + l]
            y_hatch = [-r, -r, -r + c_h]
        elif self.chamfer_pos == 'both':
            x_obrys = [origin, origin + c_l, origin + l - c_l, origin + l, origin + l, origin + l - c_l, origin + c_l, origin, origin]
            y_obrys = [-r + c_h, -r, -r, -r + c_h, r - c_h, r, r, r - c_h, -r + c_h]
            x_hatch = [origin, origin + c_l, origin + l - c_l, origin + l]
            y_hatch = [-r + c_h, -r, -r, -r + c_h]
        else: # none
            x_obrys = [origin, origin + l, origin + l, origin, origin]
            y_obrys = [-r, -r, r, r, -r]
            x_hatch = [origin, origin + l]
            y_hatch = [-r, -r]

        # 1. KRESKOWANIE (Dolna połowa dla półprzekroju)
        GeometryScene.ax_2d.fill_between(x_hatch, [0]*len(x_hatch), y_hatch, 
                                        facecolor='none', hatch='//', edgecolor='k', alpha=0.5)

        # 2. OBRYS GŁÓWNY
        res = GeometryScene.ax_2d.plot(x_obrys, y_obrys, color='k', linewidth=1.5, zorder=3)

        # 3. ROWEK WPUSTOWY (Keyseat)
        # Rysujemy go centralnie na górnej części wałka
        kw_l = l * 0.6  # długość rowka (60% długości wałka)
        kw_r = r * 0.4  # "głębokość" wizualna rowka
        kw_x_start = origin + (l - kw_l) / 2
        
        # Geometria zaokrągleń wpustu (Twoja oryginalna logika, ale w nowej skali)
        angle = np.linspace(0.5*np.pi, 1.5*np.pi, 50)
        cx_l = (r*0.2) * np.cos(angle) + kw_x_start
        cy_l = (r*0.2) * np.sin(angle) + r*0.6
        cx_r = (r*0.2) * -np.cos(angle) + (kw_x_start + kw_l)
        cy_r = (r*0.2) * np.sin(angle) + r*0.6
        
        res += GeometryScene.ax_2d.plot(cx_l, cy_l, 'k-', linewidth=1)
        res += GeometryScene.ax_2d.plot(cx_r, cy_r, 'k-', linewidth=1)
        res += GeometryScene.ax_2d.plot([kw_x_start, kw_x_start + kw_l], [r*0.8, r*0.8], 'k-', linewidth=1)
        res += GeometryScene.ax_2d.plot([kw_x_start, kw_x_start + kw_l], [r*0.4, r*0.4], 'k-', linewidth=1)

        # 4. PIONOWE LINIE FAZY (jeśli występują)
        if self.chamfer_pos in ['left', 'both']:
            res += GeometryScene.ax_2d.plot([origin + c_l, origin + c_l], [-r, r], 'k-', linewidth=1)
        if self.chamfer_pos in ['right', 'both']:
            res += GeometryScene.ax_2d.plot([origin + l - c_l, origin + l - c_l], [-r, r], 'k-', linewidth=1)

        # 5. OŚ SYMETRII
        res += GeometryScene.ax_2d.plot([origin - 1, origin + l + 1], [0, 0], '-.', color='k', linewidth=1)

        # 6. TEKST
        label = self.str_pl() if language == 'pl' else self.str_en()
        GeometryScene.ax_2d.text(t_l, t_r, label, rotation='vertical', multialignment='center', va='bottom')

        # Podgląd (ShaftPreview)
        ShaftPreview(0, 0, origin / 2, [r, l, "wpust", 0.2, '#6b7aa1'])

class CylinderWithKeyseat(Cylinder):
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
    color = 'k'

    num_of_lines_view = {
        'horizontal_lines': 5,
        'vertical_lines': 2,
        'horizontal_dimensions': 3,
        'vertical_dimensions': 1,
        'inclined_lines': 0,
    }
    num_of_lines_sec = {
        'horizontal_lines': 3,
        'vertical_lines': 2,
        'horizontal_dimensions': 1,
        'vertical_dimensions': 1,
        'inclined_lines': 0,
    }

    num_of_lines_half_sec = {
        'horizontal_lines': 4,
        'vertical_lines': 2,
        'horizontal_dimensions': 3,
        'vertical_dimensions': 1,
        'inclined_lines': 0,
    }

    num_of_lines_front = {'circles': 1, 'phi_dimensions': 0}

    def str_en(self):
        return 'Cylinder with Keyseat\n with L={length}mm and diameter={d}mm'.format(
            length=self.height,
            d=self.diameter)

    def str_pl(self):
        return 'Walec z rowkiem na wpust \n o L={length}mm i średnicy={d}mm'.format(
            length=self.height,
            d=self.diameter).replace('right',
                                          'prawej').replace('left', 'lewej')
    
    
    def _plot_2d(self, language='en'):

        #         print(f'self.origin property is {self.origin()}')
        #         print(f'self.end property is {self.end()}')

        class_name = self.__class__.__name__

        span = np.linspace(0, len(class_name), 100)
        #         print(f'plot_2d is called for {class_name}')

        r = self.diameter / 2 / 10
        l = self.height / 10
        origin = self.origin / 10
        end = self.end / 10

        t_l = origin - 3
        t_r = (r + 5.5)

        line_type = self.line_type
        color = self.color
        
        angle = np.linspace(1/2*np.pi,3/2*np.pi,100)
        
        x_c_l = r*2/9 * np.cos(angle)
        y_c_l = r*2/9 * np.sin(angle)
        x_c_r = r*2/9 * -np.cos(angle)
        y_c_r = r*2/9 * -np.sin(angle)
        
        x_coords_l=x_c_l
        y_coords_l=y_c_l
        x_coords_r=x_c_r
        y_coords_r=y_c_r
        
        circle_l = np.array([[x,y]  for x,y in zip(x_coords_l,y_coords_l)])
        circle_r = np.array([[x,y]  for x,y in zip(x_coords_r,y_coords_r)])

        res = GeometryScene.ax_2d.plot(
            [origin + 0, origin + 0, origin + l, origin + l, origin + 0],
            [-r, r, r, -r, -r],
            line_type,
            color=color) + GeometryScene.ax_2d.plot(
                [origin - 0.5, origin + l + 0.5], [0, 0],
                '-.',
                color='k',
                linewidth=1) + GeometryScene.ax_2d.plot(
                    [origin + l/3, origin + l*2/3], 
                    [r*2/9, r*2/9],
                    '-',
                    color='k',
                        linewidth=1) + GeometryScene.ax_2d.plot(
                        [origin + l*2/3, origin + l/3], 
                        [-r*2/9, -r*2/9],
                        '-',
                        color='k',
                        linewidth=1) + GeometryScene.ax_2d.plot(
                            circle_l[:,0] + origin + l/3, 
                            circle_l[:,1],
                            '-',
                            color='k',
                            linewidth=1) + GeometryScene.ax_2d.plot(
                                circle_r[:,0] + origin + l*2/3, 
                                circle_r[:,1],
                                '-',
                                color='k',
                                linewidth=1)

        if language == 'pl':
            text = GeometryScene.ax_2d.text(t_l,
                                            t_r,
                                            self.str_pl(),
                                            rotation='vertical',
                                            multialignment='center')
        else:
            text = GeometryScene.ax_2d.text(t_l,
                                            t_r,
                                            self.str_en(),
                                            rotation='vertical',
                                            multialignment='center')

        ShaftPreview(0,0, origin / 2,
                     [2 * r / 2, l / 2, "bez fazy", 0.2, '#6b7aa1'])

        print(res)
    
    
class ChamferedCylinderWithKeyseat(ChamferedCylinder):
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
    num_of_lines_view = {
        'horizontal_lines': 5,
        'vertical_lines': 3,
        'horizontal_dimensions': 4,
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
        'horizontal_lines': 4,
        'vertical_lines': 3,
        'horizontal_dimensions': 4,
        'vertical_dimensions': 1,
        'inclined_lines': 2,
        'angular_dimensions': 1,
    }

    num_of_lines_front = {'circles': 2, 'phi_dimensions': 0}
    line_type = '-'
    color = 'k'
    
    def __init__(self,
                 height,
                 diameter,
                 chamfer_length=1,
                 chamfer_angle=45,
                 chamfer_pos='left'):

        num_of_lines_view = self.__class__.num_of_lines_view
        num_of_lines_sec = self.__class__.num_of_lines_sec
        num_of_lines_half_sec = self.__class__.num_of_lines_half_sec
        num_of_lines_front = self.__class__.num_of_lines_front

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
        return 'Chamfered Cylinder with Keyseat\n with L={length}mm, diameter={d}mm \n and {l_ch}x{angle} chamfer on the {pos} side'.format(
            length=self.height,
            d=self.diameter,
            angle=self.chamfer_angle,
            l_ch=self.chamfer_length,
            pos=self.chamfer_pos)

    def str_pl(self):
        return 'Walec z rowkiem na wpust \n o L={length}mm, średnicy={d}mm \n i fazie {l_ch}x{angle} znajdującej się po {pos} stronie'.format(
            length=self.height,
            d=self.diameter,
            angle=self.chamfer_angle,
            l_ch=self.chamfer_length,
            pos=self.chamfer_pos).replace('right',
                                          'prawej').replace('left', 'lewej')

    def _plot_2d(self, language='en'):

        #         print(f'self.origin property is {self.origin()}')
        #         print(f'self.end property is {self.end()}')

        class_name = self.__class__.__name__

        span = np.linspace(0, len(class_name), 100)
        #         print(f'plot_2d is called for {class_name}')

        r = self.diameter / 2 / 10
        l = self.height / 10
        origin = self.origin / 10
        end = self.end / 10

        t_l = origin - 3
        t_r = (r + 5.5)

        line_type = self.line_type
        color = self.color
        
        angle = np.linspace(1/2*np.pi,3/2*np.pi,100)
        
        x_c_l = r*2/9 * np.cos(angle)
        y_c_l = r*2/9 * np.sin(angle)
        x_c_r = r*2/9 * -np.cos(angle)
        y_c_r = r*2/9 * -np.sin(angle)
        
        x_coords_l=x_c_l
        y_coords_l=y_c_l
        x_coords_r=x_c_r
        y_coords_r=y_c_r
        
        circle_l = np.array([[x,y]  for x,y in zip(x_coords_l,y_coords_l)])
        circle_r = np.array([[x,y]  for x,y in zip(x_coords_r,y_coords_r)])

        res = GeometryScene.ax_2d.plot(
            [origin + 0, origin + 0, origin + l, origin + l, origin + 0],
            [-r, r, r, -r, -r],
            line_type,
            color=color) + GeometryScene.ax_2d.plot(
                [origin - 0.5, origin + l + 0.5], [0, 0],
                '-.',
                color='k',
                linewidth=1) + GeometryScene.ax_2d.plot(
                    [origin + l/3, origin + l*2/3], 
                    [r*2/9, r*2/9],
                    '-',
                    color='k',
                        linewidth=1) + GeometryScene.ax_2d.plot(
                        [origin + l*2/3, origin + l/3], 
                        [-r*2/9, -r*2/9],
                        '-',
                        color='k',
                        linewidth=1) + GeometryScene.ax_2d.plot(
                            circle_l[:,0] + origin + l/3, 
                            circle_l[:,1],
                            '-',
                            color='k',
                            linewidth=1) + GeometryScene.ax_2d.plot(
                                circle_r[:,0] + origin + l*2/3, 
                                circle_r[:,1],
                                '-',
                                color='k',
                                linewidth=1)

        if language == 'pl':
            text = GeometryScene.ax_2d.text(t_l,
                                            t_r,
                                            self.str_pl(),
                                            rotation='vertical',
                                            multialignment='center')
        else:
            text = GeometryScene.ax_2d.text(t_l,
                                            t_r,
                                            self.str_en(),
                                            rotation='vertical',
                                            multialignment='center')

        ShaftPreview(0,0, origin / 2,
                     [2 * r / 2, l / 2, "bez fazy", 0.2, '#6b7aa1'])

        print(res)
        
################################################## Complex Solids aka podziemie ################################################
class CylinderWithHole(Cylinder):

    line_type = '-'
    color = 'k'

    num_of_lines_view = {
        'horizontal_lines': 5,
        'vertical_lines': 2,
        'horizontal_dimensions': 3,
        'vertical_dimensions': 1,
        'inclined_lines': 0,
    }
    num_of_lines_sec = {
        'horizontal_lines': 3,
        'vertical_lines': 2,
        'horizontal_dimensions': 1,
        'vertical_dimensions': 1,
        'inclined_lines': 0,
    }

    num_of_lines_half_sec = {
        'horizontal_lines': 4,
        'vertical_lines': 2,
        'horizontal_dimensions': 3,
        'vertical_dimensions': 1,
        'inclined_lines': 0,
    }

    num_of_lines_front = {'circles': 1, 'phi_dimensions': 0}
    
    

    def str_en(self):
        return 'Cylinder with Hole\n with L={length}mm and diameter={d}mm'.format(
            length=self.height,
            d=self.diameter)

    def str_pl(self):
        return 'Walec z otworem \n o L={length}mm i średnicy={d}mm'.format(
            length=self.height,
            d=self.diameter).replace('right',
                                          'prawej').replace('left', 'lewej')
    
    
    def _plot_2d(self, language='en'):

        #         print(f'self.origin property is {self.origin()}')
        #         print(f'self.end property is {self.end()}')

        class_name = self.__class__.__name__

        span = np.linspace(0, len(class_name), 100)
        #         print(f'plot_2d is called for {class_name}')

        r = self.diameter / 2 / 10
        l = self.height / 10
        origin = self.origin / 10
        end = self.end / 10
       #r_h = self.hole_diameter / 2 / 10
        
        t_l = origin - 3
        t_r = (r + 5.5)

        line_type = self.line_type
        color = self.color
        
        #angle = np.linspace(1/2*np.pi,3/2*np.pi,100)
        
        #x_c_l = r*2/9 * np.cos(angle)
        #y_c_l = r*2/9 * np.sin(angle)
        #x_c_r = r*2/9 * -np.cos(angle)
        #y_c_r = r*2/9 * -np.sin(angle)
        
        #x_coords_l=x_c_l
        #y_coords_l=y_c_l
        #x_coords_r=x_c_r
        #y_coords_r=y_c_r
        
        #circle_l = np.array([[x,y]  for x,y in zip(x_coords_l,y_coords_l)])
        #circle_r = np.array([[x,y]  for x,y in zip(x_coords_r,y_coords_r)])

        res = GeometryScene.ax_2d.plot(
            [origin + 0, origin + 0, origin + l, origin + l, origin + 0],
            [-r, r, r, -r, -r],
            line_type,
            color=color) + GeometryScene.ax_2d.plot(
                [origin - 0.5, origin + l + 0.5], [0, 0],
                '-.',
                color='k',
                linewidth=1) + GeometryScene.ax_2d.plot(
                    [origin + 0, origin + l], 
                    [r*2/9, r*2/9],
                    '--',
                    color='b',
                        linewidth=1) + GeometryScene.ax_2d.plot(
                        [origin + l, origin + 0], 
                        [-r*2/9, -r*2/9],
                        '--',
                        color='b',
                        linewidth=1)+ GeometryScene.ax_2d.plot(
                            [origin + 0, origin + 0],
                            [-r*2/9, r*2/9],
                            '--',
                            color='b',
                            linewidth=3) + GeometryScene.ax_2d.plot(
                                [origin + l, origin + l],
                                [-r*2/9, r*2/9],
                                '--',
                                color='b',
                                linewidth=3)

        if language == 'pl':
            text = GeometryScene.ax_2d.text(t_l,
                                            t_r,
                                            self.str_pl(),
                                            rotation='vertical',
                                            multialignment='center')
        else:
            text = GeometryScene.ax_2d.text(t_l,
                                            t_r,
                                            self.str_en(),
                                            rotation='vertical',
                                            multialignment='center')

        ShaftPreview(0,0, origin / 2,
                     [2 * r / 2, l / 2, "bez fazy", 0.2, '#6b7aa1'])

        print(res)