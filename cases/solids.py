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
                         HalfSection(**num_of_lines),FrontView(**num_of_lines_front))
        self.height = height
        self.top_diameter = top_diameter
        self.bottom_diameter = bottom_diameter

        self._parameters = height, top_diameter, bottom_diameter
        self._class_description = "with L={}mm, top diameter = {}mm and bottom diameter={}mm".format(
            *self._parameters)

        self._name['pl'] = 'Stożek'
        self._class_description_pl = "o L={}mm, średnicy górnej podstawy = {}mm i średnicy dolnej podstawy={}mm".format(
            *self._parameters)


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
                         HalfSection(**num_of_lines),FrontView(**num_of_lines_front))
        self.height = height
        self.diameter = diameter

        self._parameters = height, diameter
        self._class_description = "with L={}mm and diameter ={}mm".format(
            *self._parameters)

        self._name['pl'] = 'Walec'
        self._class_description_pl = "o L={}mm i średnicy ={}mm".format(
            *self._parameters)


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
        return 'Hole with L={length}mm, diameter={d}mm and {l_ch}x{angle} chamfer on the {pos} side'.format(
            length=self.height,
            d=self.diameter,
            angle=self.chamfer_angle,
            l_ch=self.chamfer_length,
            pos=self.chamfer_pos)

    def str_pl(self):
        return 'Otwór o L={length}mm, średnicy={d}mm i fazie {l_ch}x{angle} znajdującej się po {pos} stronie'.format(
            length=self.height,
            d=self.diameter,
            angle=self.chamfer_angle,
            l_ch=self.chamfer_length,
            pos=self.chamfer_pos).replace('right',
                                          'prawej').replace('left', 'lewej')


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
        return 'Cylinder with L={length}mm, diameter={d}mm and {l_ch}x{angle} chamfer on the {pos} side'.format(
            length=self.height,
            d=self.diameter,
            angle=self.chamfer_angle,
            l_ch=self.chamfer_length,
            pos=self.chamfer_pos)

    def str_pl(self):
        return 'Walec o L={length}mm, średnicy={d}mm i fazie {l_ch}x{angle} znajdującej się po {pos} stronie'.format(
            length=self.height,
            d=self.diameter,
            angle=self.chamfer_angle,
            l_ch=self.chamfer_length,
            pos=self.chamfer_pos).replace('right',
                                          'prawej').replace('left', 'lewej')


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
                         FrontView(**num_of_lines_front) )
        
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
        self.chamfer_length = chamfer_length
        self.chamfer_angle = chamfer_angle
        self.thread = thread
        self._parameters = thread,diameter,
        self._class_description = "Threaded open hole {}{}".format(
            *self._parameters)

    def str_en(self):
        return 'Open threaded hole (to the end of solid) {thread}{d} with {l_ch}x{angle} chamfers on both sides'.format(
             thread=self.thread,
            d=self.diameter,
            angle=self.chamfer_angle,
            l_ch=self.chamfer_length)

    def str_pl(self):
        return 'Gwintowany otwór przelotowy {thread}{d} z fazą {l_ch}x{angle} po obu stronach'.format(
            thread=self.thread,
            d=self.diameter,
            angle=self.chamfer_angle,
            l_ch=self.chamfer_length)
        
        

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
        self.diameter = round(module * (teeth_no + 2) / 2)
        self.chamfer_length = chamfer_length
        self.chamfer_angle = chamfer_angle
        self._parameters = height, teeth_no, module, chamfer_length, chamfer_angle,
        self._class_description = "with L={}mm, z={}, m={} and chamfer {}x{}".format(
            *(self._parameters))

        self._name['pl'] = 'Koło zębate'
        self._class_description_pl = "o  L={}mm, z={}, m={} i fazie {}x{}".format(
            *self._parameters)
        
    def str_en(self):
        return f'Gear with outside diameter {self.height}, module {self.module} and {self.chamfer_length}x{self.chamfer_angle} chamfers on both sides'


#         super().__init__(View(horizontal_lines,vertical_lines,diagonal_lines,horizontal_dimensions,vertical_dimensions,diagonal_dimensions))
    def str_pl(self):
        return f'Koło zębate o średnicy wierzchołkowej {self.height}, module {self.module} z fazą {self.chamfer_length}x{self.chamfer_angle} po obu stronach'


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
        
        num_of_lines_front = {'circles': 1, 'phi_dimensions': 0} # to improve

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
        
        num_of_lines_front = {'circles': 1, 'phi_dimensions': 0} # to improve

        super().__init__(height=height, indiameter=indiameter)

        self._views = {
            'view': View(**num_of_lines_view),
            'section': Section(**num_of_lines_sec),
            'halfsection': HalfSection(**num_of_lines_half_sec),
            'front_view':FrontView(**num_of_lines_front)
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
        
        num_of_lines_front = {'circles': 2+holes_no, 'phi_dimensions': 0}

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
        return "Flange with open holes with L={}mm, D={}, hole diameter={}, reference diameter of hole pattern={}, holes number={} and chamfers {}x{} on both sides".format(
            *(self._parameters))

    def str_pl(self):
        return "Kołnierz z przelotowymi otworami o  L={}mm, D={}, średnicy otworu={}, średnicy rozmieszczenia otworów={}, liczbie otworów={} i fazach {}x{} po obu stronach".format(
            *self._parameters)


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
            'horizontal_lines': 2+1, #axis included
            'vertical_lines': 2,  #axis excluded
            'inclined_lines': 0,
            'horizontal_dimensions': 1,
            'vertical_dimensions': 1,
            'angular_dimensions': 0,
        }

        num_of_lines_sec = {
            'horizontal_lines': 2+1, #axis included
            'vertical_lines': 2,  #axis excluded
            'inclined_lines': 0,
            'horizontal_dimensions': 1,
            'vertical_dimensions': 1,
            'angular_dimensions': 0,
        }

        num_of_lines_half_sec = {
            'horizontal_lines': 2+1, #axis included
            'vertical_lines': 2,  #axis excluded
            'inclined_lines': 0,
            'horizontal_dimensions': 1,
            'vertical_dimensions': 1,
            'angular_dimensions': 0,
        }
        
        
        num_of_lines_front = {
            'horizontal_lines': 2, #axis excluded
            'vertical_lines': 2, #axis exclueded
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
            'horizontal_lines': 3, #axis included
            'vertical_lines': 2,  #axis excluded
            'inclined_lines': 0,
            'horizontal_dimensions': 1,
            'vertical_dimensions': 1,
            'angular_dimensions': 0,
        }

        num_of_lines_sec = {
            'horizontal_lines': 3, #axis included
            'vertical_lines': 2,  #axis excluded
            'inclined_lines': 0,
            'horizontal_dimensions': 1,
            'vertical_dimensions': 1,
            'angular_dimensions': 0,
        }

        num_of_lines_half_sec = {
            'horizontal_lines': 3, #axis included
            'vertical_lines': 2,  #axis excluded
            'inclined_lines': 0,
            'horizontal_dimensions': 1,
            'vertical_dimensions': 1,
            'angular_dimensions': 0,
        }
        
        num_of_lines_front = {
            'horizontal_lines': 2, #axis excluded
            'vertical_lines': 2, #axis exclueded
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
            'horizontal_lines': 5, #axis included
            'vertical_lines': 2,  #axis excluded
            'inclined_lines': 0,
            'horizontal_dimensions': 1,
            'vertical_dimensions': 1,
            'angular_dimensions': 0,
        }

        num_of_lines_sec = {
            'horizontal_lines': 4, #axis included
            'vertical_lines': 2,  #axis excluded
            'inclined_lines': 0,
            'horizontal_dimensions': 1,
            'vertical_dimensions': 1,
            'angular_dimensions': 0,
        }

        num_of_lines_half_sec = {
            'horizontal_lines': 3, #axis included
            'vertical_lines': 2,  #axis excluded
            'inclined_lines': 0,
            'horizontal_dimensions': 1,
            'vertical_dimensions': 1,
            'angular_dimensions': 0,
        }
        
        num_of_lines_front = {
            'horizontal_lines': 4, #axis excluded
            'vertical_lines': 4, #axis excluede
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
    
    def __init__(self, height, indiameter, chamfer_length=1, chamfer_angle=45, chamfer_pos='left'):
        
        
        num_of_lines_view = {
            'horizontal_lines': 5, #axis included
            'vertical_lines': 2,
            'inclined_lines': 4,
            'arcs': 6,
            'horizontal_dimensions': 3,
            'vertical_dimensions': 1,
            'angular_dimensions': 2,
        }

        num_of_lines_sec = {
            'horizontal_lines': 3, #axis included
            'vertical_lines': 2,
            'inclined_lines': 4,
            'arcs': 0,
            'horizontal_dimensions': 3,
            'vertical_dimensions': 1,
            'angular_dimensions': 2,
        }

        num_of_lines_half_sec = {
            'horizontal_lines': 4, # axis included
            'vertical_lines': 2,
            'inclined_lines': 4,
            'arcs': 4,
            'horizontal_dimensions': 3,
            'vertical_dimensions': 1,
            'angular_dimensions': 2,
        }
        
        num_of_lines_front = {'circles': 1, 'phi_dimensions': 0} # to improve

        super().__init__(height=height, indiameter=indiameter)

        self._views = {
            'view': View(**num_of_lines_view),
            'section': Section(**num_of_lines_sec),
            'halfsection': HalfSection(**num_of_lines_half_sec),
            'front_view':FrontView(**num_of_lines_front)
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
    