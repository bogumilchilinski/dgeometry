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

import IPython as IP
import numpy as np
from sympy import Symbol, symbols
import copy
import sympy

import itertools as it
from ..dgeometry import *
from . import solids as sol
import gc


class DrawingSheets(GeometricalCase):

    _case_no = plots_no()
    scheme_name = 'absxyz'
    real_name = 'abs'

    paper_size_dict = {
        'A4': (210, 297),
        'A3': (420, 297),
        'A2': (594, 420),
        'A1': (841, 594),
        'A0': (1189, 841)
    }

    borders_extented = {
        'left': 20,
        'right': 10,
        'top': 10,
        'bottom': 10,
    }

    drawing_area_dict = {
        'A4': (190, 277),
        'A3': (400, 277),
        'A2': (574, 400),
        'A1': (821, 574),
        'A0': (1169, 821)
    }

    @classmethod
    def from_random_data(cls):
        new_obj = cls()
        data_set = new_obj.get_random_parameters()
        print(data_set)
        entities = [elem for label, elem in data_set.items()]
        print(entities)
        return cls(*entities)

    def __init__(self, *assumptions, **kwargs):
        super().__init__()
        self._solution_step = []
        self._solution3d_step = []

        self._label = None

        self._given_data = {
            str(no + 1): val
            for no, val in enumerate(assumptions)
        }

        self._cached_solution = None

    @property
    def _cube_size(self):
        return (self._given_data['a'])

    @property
    def _ref_paper(self):
        return list(self._given_data.values())[0]

    @property
    def _extra_paper(self):
        return list(self._given_data.values())[1]

    @property
    def paper_size(self):

        papers = self.__class__.paper_size_dict

        return papers[self._ref_paper]

    @property
    def extra_paper_size(self):

        papers = self.__class__.paper_size_dict

        return papers[self._extra_paper]

    @property
    def paper_area(self):

        papers = self.__class__.paper_size_dict

        width, height = papers[self._ref_paper]

        return width * height

    @property
    def extra_paper_area(self):

        papers = self.__class__.paper_size_dict

        width, height = papers[self._extra_paper]

        return width * height

    @property
    def paper_drawing_area_size(self):

        papers = self.__class__.drawing_area_dict

        return papers[self._ref_paper]

    @property
    def extra_paper_drawing_area_size(self):

        papers = self.__class__.drawing_area_dict

        return papers[self._extra_paper]

    def _solution(self, solved_case=None):


        new_obj = copy.deepcopy(self)

        return new_obj

    def get_default_data(self):

        papers = self.__class__.paper_size_dict

        default_data_dict = {
            '1': list(papers.keys()),
            '2': list(papers.keys()),
        }

        return default_data_dict

    def get_random_parameters(self):

        parameters_dict = super().get_random_parameters()

        if parameters_dict['1'] == parameters_dict['2']:
            #print('lock action')
            parameters_dict = self.get_random_parameters()

        return parameters_dict

    def subs(self, *args, **kwargs):
        if len(args) > 0 and isinstance(args[0], dict):
            data_set = args[0]
            entities = [point for label, point in data_set.items()]

            new_obj = self.__class__(*entities)
            new_obj._given_data = args[0]

        else:
            new_obj = copy.deepcopy(self)
            #new_obj._cached_solution=None

        return new_obj


class CubeDrawing(DrawingSheets):

    cube_sizes = [50, 75, 100, 125, 150]

    def get_default_data(self):

        papers = self.__class__.paper_size_dict
        cube_side = self.__class__.cube_sizes

        default_data_dict = {
            '1': list(papers.keys()),
            '2': list(papers.keys()),
            'a': cube_side,
        }

        return default_data_dict


step_mod_inc_flange = lambda step: random.choice([
#     step,
#     sol.ChamferedCylinder(
#         step.height, step.diameter, chamfer_angle=45, chamfer_length=1),
#     sol.Thread(step.height, step.diameter),
    [
        sol.Thread(step.height, step.diameter),
        sol.FlangeWithHoles(height=step.height,
                            diameter=step.diameter * 3,
                            hole_diameter=12,
                            reference_diameter=step.diameter * 3 - 2 * 12,
                            holes_no=4), copy.copy(step)
    ],
    [
        copy.copy(step),
        sol.FlangeWithHoles(height=step.height,
                            diameter=step.diameter * 3,
                            hole_diameter=16,
                            reference_diameter=step.diameter * 3 - 2 * 16,
                            holes_no=6), copy.copy(step)
    ],
    [
        copy.copy(step),
        sol.FlangeWithHoles(height=step.height,
                            diameter=step.diameter * 3,
                            hole_diameter=14,
                            reference_diameter=step.diameter * 3 - 2 * 14,
                            holes_no=8), copy.copy(step)
    ],
])
step_mod_dec_flange = lambda step: random.choice([
    copy.copy(step),
    sol.ChamferedCylinder(step.height,
                          step.diameter,
                          chamfer_angle=45,
                          chamfer_length=1,
                          chamfer_pos='right'),
    [
        copy.copy(step),
        sol.FlangeWithHoles(height=step.height,
                            diameter=step.diameter * 3,
                            hole_diameter=12,
                            reference_diameter=step.diameter * 3 - 2 * 12,
                            holes_no=4), copy.copy(step)
    ],
    [
        copy.copy(step),
        sol.FlangeWithHoles(height=step.height,
                            diameter=step.diameter * 3,
                            hole_diameter=16,
                            reference_diameter=step.diameter * 3 - 2 * 16,
                            holes_no=6), copy.copy(step)
    ],
    [
        copy.copy(step),
        sol.FlangeWithHoles(height=step.height,
                            diameter=step.diameter * 3,
                            hole_diameter=14,
                            reference_diameter=step.diameter * 3 - 2 * 14,
                            holes_no=8), copy.copy(step)
    ],
])

step_mod_inc_threads = lambda step: random.choice([
    #step,
    sol.ChamferedCylinder(
        step.height, step.diameter, chamfer_angle=45, chamfer_length=1),
    sol.Thread(step.height, step.diameter),
])

step_mod_dec_screw = lambda step: random.choice([

    [sol.Cylinder(4, round(step.diameter*0.85)),
            sol.Thread(step.height, step.diameter),sol.ChamferedCylinder(round(step.height*0.3),
                              round(step.diameter*0.85),
                              chamfer_angle=45,
                              chamfer_length=1,
                              chamfer_pos='right')],
        
    [sol.ChamferedCylinder(10,
                              round(step.diameter*1.3),
                              chamfer_angle=45,
                              chamfer_length=1,
                              chamfer_pos='right'),
            sol.Thread(step.height, step.diameter),sol.ChamferedCylinder(round(step.height*0.3),
                              round(step.diameter*0.85),
                              chamfer_angle=45,
                              chamfer_length=1,
                              chamfer_pos='right')],
    sol.Thread(step.height, step.diameter),
    [sol.Thread(step.height, step.diameter),sol.ChamferedCylinder(round(step.height*0.3),
                              round(step.diameter*0.85),
                              chamfer_angle=45,
                              chamfer_length=1,
                              chamfer_pos='right')],
        
])


step_mod_dec_threads = lambda step: random.choice([
    copy.copy(step),
    #     sol.ChamferedCylinder(step.height,
    #                           step.diameter,
    #                           chamfer_angle=45,
    #                           chamfer_length=1,
    #                           chamfer_pos='right'),
    sol.Thread(step.height, step.diameter),
])

step_mod_inc_chamfer = lambda step: random.choice([
    copy.copy(step),
    sol.ChamferedCylinder(
        step.height, step.diameter, chamfer_angle=45, chamfer_length=1),
])



step_mod_dec_hole_chamfer = lambda step: random.choice([
    copy.copy(step),
    sol.ChamferedHole(
        step.height, step.diameter, chamfer_angle=45, chamfer_length=1.2),
])

step_mod_dec_chamfer = lambda step: random.choice([
    copy.copy(step),
    sol.ChamferedCylinder(step.height,
                          step.diameter,
                          chamfer_angle=45,
                          chamfer_length=1,
                          chamfer_pos='right'),
])


step_mod_inc_keyseat = lambda step: random.choice([
    copy.copy(step),
    sol.ChamferedCylinder(
        step.height, step.diameter, chamfer_angle=45, chamfer_length=1),
    sol.ChamferedCylinderWithKeyseat(
        step.height, step.diameter, chamfer_angle=45, chamfer_length=1),
])


step_mod_dec_keyseat = lambda step: random.choice([
    copy.copy(step),
    sol.ChamferedCylinderWithKeyseat(step.height,
                          step.diameter,
                          chamfer_angle=45,
                          chamfer_length=1,
                          chamfer_pos='right'),
    sol.ChamferedCylinder(step.height,
                          step.diameter,
                          chamfer_angle=45,
                          chamfer_length=1,
                          chamfer_pos='right'),
    sol.CylinderWithKeyseat(step.height,
                          step.diameter),
])



step_mod_chamfer_hex_prism = lambda step: random.choice([
    copy.copy(step),
    sol.ChamferedHexagonalPrism(step.height,
                          step.diameter,
                          chamfer_angle=45,
                          chamfer_length=1,
                          chamfer_pos='left'),
])

step_mod_inc_gear = lambda step: random.choice([
    copy.copy(step),
    *[[
        step,
        sol.Gear(step.height,
                 round(2 * step.diameter / module),
                 module,
                 chamfer_angle=45,
                 chamfer_length=1)
    ] for module in [2, 3, 4]],
])

step_mod_dec_gear = lambda step: random.choice([
    copy.copy(step),
    *[[
        sol.Gear(step.height,
                 round(2 * step.diameter / module),
                 module,
                 chamfer_angle=45,
                 chamfer_length=1),
        step,
    ] for module in [2, 3, 4]],
])

step_mod_dec_plate = lambda step: random.choice([
    copy.copy(step),
    sol.Plate(step.height,
              step.diameter*3),
])

def create_random_profile(max_steps_no,
                          min_steps_no=4,
                          initial_diameter=[50,55,60,65],
                          increase_values=[2, 3, 4, 5],
                          step_lengths=[50,55,60],
                          step_type=sol.Cylinder,
                          step_modificator=lambda step: step,
                          origin=0):
    steps_no = random.randint(min_steps_no, max_steps_no - 1)

    #boundary_node=random.randint(0,steps_no)

    first_d = random.choice(initial_diameter)

    profile_changes = [
        random.choice(increase_values) for node in range(steps_no)
    ]  #+[-random.choice(increase_values)  for node in range(boundary_node,steps_no)]

    profile = [first_d] + [
        first_d + sum(profile_changes[0:step_no + 1])
        for step_no in range(len(profile_changes))
    ]

    base_geometry = [
        step_type(random.choice(step_lengths), diameter)
        for diameter in profile
    ]

    steps_list=sympy.flatten([step_modificator(step) for step in base_geometry])
    
    steps_list[0]._origin = origin
    
    for no,step in enumerate(steps_list):
        step._ref_elem = steps_list[no-1]
        
    steps_list[0]._origin = origin
    steps_list[0]._ref_elem = None
    
    return steps_list


names_dict = {
    'view': 'view',
    'section': 'section view',
    'halfsection': 'half-section view',
    'front_view': 'front view'
}
names_dict_pl = {
    'view': 'widok',
    'section': 'przekrój',
    'halfsection': 'półwidok-półprzekrój',
    'horizontal_lines': 'linii poziomych',
    'vertical_lines': 'linii pionowych',
    'horizontal_dimensions': 'wymiarów poziomych',
    'vertical_dimensions': 'wymiarów pionowych',
    'angular_dimensions': 'wymiarów kątowych',
    'inclined_lines': 'linii ukośnych'
}

geometry_view_product = [{
    'view_type': view_type,
    'element_type': element_key.replace('_', ' '),
    'element_type_pl': names_dict_pl[element_key],
    'element_key': element_key
} for view_type, element_key in (
    it.product(['view', 'section', 'halfsection'], [
        'horizontal_lines', 'vertical_lines', 'horizontal_dimensions',
        'vertical_dimensions', 'angular_dimensions', 'inclined_lines'
    ]))]


class ShaftSketch(GeometricalCase):

    _case_no = plots_no()
    scheme_name = 'absxyz'
    real_name = 'abs'

    steps_no = {'max': 3, 'min': 1}
    holes_no = {'max': 3, 'min': 2}
    
    shafts=None

    @classmethod
    def set_steps_number(cls,steps=None,holes=None):
        if steps is not None and isinstance(steps,dict):
            cls.steps_no = step
        else:
            raise TypeError(f'obj steps of {type(steps)} is not a dict')
            
        if holes is not None and isinstance(holes,dict):
            cls.holes_no = holes
        else:
            raise TypeError(f'obj holes of {type(holes)} is not a dict')
        
        return cls
    
    @classmethod
    def _solids(cls):

        if cls.shafts is None:
            cls.shafts = cls._structure_generator()

        return cls.shafts

    @classmethod
    def _structure_generator(cls):
        
        steps = cls.steps_no
        holes = cls.holes_no
        
        shafts =  []
        for i in range(50):
            shaft = create_random_profile(steps['max'],steps['min'],
                                  increase_values=[
                                      4,
                                      5,
                                      6,
                                  ],
                                  step_modificator=step_mod_inc_chamfer,origin=0) 
            
            d_end=shaft[-1].diameter
            
            shaft +=create_random_profile(steps['max'],steps['min'],
                                  initial_diameter=[d_end+8, d_end+10 ],
                                  increase_values=[
                                      -4,
                                      -5,
                                      -6,
                                  ],
                                  step_modificator=step_mod_dec_chamfer,origin = shaft[-1].end)
            

            
            shafts.append(shaft)
        return shafts

    @classmethod
    def from_random_data(cls):
        new_obj = cls()
        data_set = new_obj.get_random_parameters()
        print(data_set)
        entities = [elem for label, elem in data_set.items()]
        print(entities)
        return cls(*entities)



        
    def _scheme(self):

        if self._path is None:
            self.preview()


        return self._path

    def _real_example(self):

        if self._path is None:
            self.preview()

        return self._path


    def _scheme_pl(self):

        if self._path is None:
            self.preview(language='pl')

        return self._path



    
    def preview(self, example=False,language='en'):
        GeometryScene(30,60,figsize=(14,7))

        self._solid_structure.preview(language=language)

        
        
        path = __file__.replace('cases/drawings.py', 'images/') + self.__class__.__name__ + str(next(self.__class__._case_no)) + '.png'

        
        
        plt.savefig(path)


        # Clear the current axes.
        plt.cla() 
        # Clear the current figure.
        plt.clf() 
        # Closes all the figure windows.
        plt.close('all')

        gc.collect()


        self._path = path


     



        with open(f"{path}", "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        image_file.close()

        return IP.display.Image(base64.b64decode(encoded_string))
    
    
    def __init__(self, *assumptions, **kwargs):
        super().__init__()
        self._solution_step = []
        self._solution3d_step = []

        steps_no = self.steps_no

        shaft = assumptions

        self._label = None


        
        self._solid_structure = sol.ComposedPart(*assumptions)

        if len(assumptions) != 0:
            self._solid_structure = sol.ComposedPart(*assumptions[0])

        self._given_data = {
            str(no + 1): val
            for no, val in enumerate(assumptions)
        }

        self._cached_solution = None
        self._path = None

    def get_default_data(self):

        shafts = self._solids()

        #default_data_dict = {no:step.str_pl()    for no,step  in enumerate(shaft) }
        default_data_dict = {'shaft': shafts}

        return default_data_dict

    def subs(self, *args, **kwargs):
        if len(args) > 0 and isinstance(args[0], dict):
            data_set = args[0]
            entities = [point for label, point in data_set.items()]

            new_obj = self.__class__(*entities)
            new_obj._given_data = args[0]

        else:
            new_obj = copy.deepcopy(self)
            #new_obj._cached_solution=None

        return new_obj

class SimpleShaftSketch(ShaftSketch):



    steps_no = {'max': 1, 'min': 0}

    
    shafts=None
    
    
class SleeveSketch(ShaftSketch
                   #GeometricalCase
                   ):

    steps_no = {'max': 4, 'min': 1}
    holes_no = {'max': 3, 'min': 2}
    
    @classmethod
    def _structure_generator(cls):
        
        
        print('struct gen for Sleeve')
        
        steps = cls.steps_no
        holes = cls.holes_no



        shafts =  []
        for i in range(50):
            shaft = create_random_profile(steps['max'],steps['min'],
                                  increase_values=[
                                      4,
                                      5,
                                      6,
                                  ],
                                  step_modificator=step_mod_inc_chamfer,origin=0) 

            d_end=shaft[-1].diameter
            d_height=shaft[-1].height
            

            right_profile =create_random_profile(steps['max'],steps['min'],
                                  initial_diameter=[d_end+8, d_end+10 ],
                                  increase_values=[
                                      -4,
                                      -5,
                                      -6,
                                  ],
                                  step_modificator=step_mod_dec_chamfer,origin = shaft[-1].end)
            shaft +=right_profile
            thread_length = right_profile[-1].end
            
            shaft +=create_random_profile(holes['max'],holes['min'],
                                       initial_diameter=[25, 30],
                                       increase_values=[
                                           -2,
                                           -3,
                                           -4,
                                       ],
                                       step_lengths=[thread_length/3],
                                       step_type=sol.Hole,origin=0)
            
            shafts.append(shaft)
            shaft[-1]._origin=0
        return shafts


class SimpleSleeveSketch(SleeveSketch
                   #GeometricalCase
                   ):

    steps_no = {'max': 2, 'min': 0}
    holes_no = {'max': 2, 'min': 1}


class SleeveWithThreadsSketch(ShaftSketch
                              #GeometricalCase
                              ):

    steps_no = {'max': 2, 'min': 1}

    @classmethod
    def _structure_generator(cls):

        steps = cls.steps_no
        holes = cls.holes_no

        shafts  = []
        for i in range(50):
            shaft = create_random_profile(steps['max'],steps['min'],
                                  increase_values=[
                                      4,
                                      5,
                                      6,
                                  ],
                                  step_modificator=step_mod_inc_threads,origin=0)
            shaft += create_random_profile(steps['max'],steps['min'],
                                  increase_values=[
                                      -4,
                                      -5,
                                      -6,
                                  ],
                                  step_modificator=step_mod_dec_threads,origin=shaft[-1].end)
            shaft += create_random_profile(2,
                                  1,
                                  initial_diameter=[25, 22],
                                  increase_values=[
                                      -2,
                                      -3,
                                  ],
                                  step_lengths=[62, 65],
                                  step_modificator=step_mod_dec_hole_chamfer,
                                  step_type=sol.Hole, origin=0)
             
            shafts.append(shaft)
        return shafts

class SimpleSleeveWithThreadsSketch(SleeveWithThreadsSketch):

    steps_no = {'max': 2, 'min': 0}
    holes_no = {'max': 2, 'min': 1}
    
class SleeveWithFlangeSketch(ShaftSketch
                              #GeometricalCase
                              ):

    steps_no = {'max': 1, 'min': 0}

    @classmethod
    def _structure_generator(cls):

        steps = cls.steps_no
        holes = cls.holes_no

        shafts  = []
        for i in range(50):
            shaft = create_random_profile(steps['max'],steps['min'],
                                  increase_values=[
                                      4,
                                      5,
                                      6,
                                  ],
                                  step_modificator=step_mod_inc_flange,origin=0)
            shaft += create_random_profile(steps['max'],steps['min'],
                                  increase_values=[
                                      -4,
                                      -5,
                                      -6,
                                  ],
                                  step_modificator=step_mod_dec_threads,
                                           origin=shaft[-1].end)
            shaft += create_random_profile(2,
                                  1,
                                  initial_diameter=[25, 22],
                                  increase_values=[
                                      -2,
                                      -3,
                                  ],
                                  step_lengths=[62, 65],
                                  step_modificator=step_mod_dec_hole_chamfer,
                                  step_type=sol.Hole, origin=0)
                                  
            
            shafts.append(shaft)
        return shafts

class SimpleSleeveWithFlangeSketch(SleeveWithFlangeSketch):

    steps_no = {'max': 1, 'min': 0}
    holes_no = {'max': 1, 'min': 0}
    
class SleeveWithThreadedHoleSketch(ShaftSketch
                                   #GeometricalCase
                                   ):

    steps_no = {'max': 2, 'min': 1}

    @classmethod
    def _structure_generator(cls):

        
        steps = cls.steps_no
        holes = cls.holes_no

        shafts =  []
        for i in range(50):
            shaft = create_random_profile(steps['max'],steps['min'],
                                  increase_values=[
                                      4,
                                      5,
                                      6,
                                  ],
                                  step_modificator=step_mod_inc_threads,origin=0) 
            
            shaft +=create_random_profile(steps['max'],steps['min'],
                                  increase_values=[
                                      -4,
                                      -5,
                                      -6,
                                  ],
                                  step_modificator=step_mod_dec_threads,origin = shaft[-1].end)
            
            shaft += create_random_profile(4,
                                  1,
                                  initial_diameter=[30,25,20],
                                  increase_values=[
                                      -2,
                                      -3,
                                      -4,
                                  ],
                                  step_lengths=[27, 29],
                                  step_modificator=step_mod_dec_hole_chamfer,
                                  step_type=sol.Hole,origin=0) 
            shaft += [sol.ThreadedOpenHole(shaft[-1].diameter-5,1.4)]
            shaft[-1]._ref_elem=shaft[-2].end
            
            shafts.append(shaft)
        
        
        return shafts


class SleeveWithGrearsSketch(ShaftSketch
                             #GeometricalCase
                             ):

    steps_no = {'max': 1, 'min': 0}

    @classmethod
    def _structure_generator(cls):
        
        steps = cls.steps_no
        holes = cls.holes_no
        
        shafts =  []
        for i in range(50):
            shaft = [sol.Cylinder(25, 40)]
            shaft[0]._origin = 0
            
            shaft += create_random_profile(steps['max'],steps['min'],
                                  increase_values=[
                                      4,
                                      5,
                                      6,
                                  ],
                                  step_modificator=step_mod_inc_gear,origin=shaft[-1].end) 
            
            shaft +=create_random_profile(steps['max'],steps['min'],
                                  increase_values=[
                                      -4,
                                      -5,
                                      -6,
                                  ],
                                  step_modificator=step_mod_inc_gear,origin = shaft[-1].end)
            
            shaft += create_random_profile(4,
                                  2,
                                  initial_diameter=[30,25,20],
                                  increase_values=[
                                      -2,
                                      -3,
                                      -4,
                                  ],
                                  step_lengths=[27, 29],
                                  step_modificator=step_mod_dec_hole_chamfer,
                                  step_type=sol.Hole,origin=0) 
            shaft += [sol.ThreadedOpenHole(shaft[-1].diameter-5,14)]
            shaft[-1]._origin=shaft[-2].end
            
            shafts.append(shaft)
        

        return shafts

    
class SimpleGearSketch(ShaftSketch
                             #GeometricalCase
                             ):

    steps_no = {'max': 1, 'min': 0}

    @classmethod
    def _structure_generator(cls):
        
        steps = cls.steps_no
        holes = cls.holes_no
        
        shafts =  []
        for i in range(50):
            
            shaft = [sol.Cylinder(25, 55)]
            shaft[0]._origin = 0
    
            shaft += [sol.Gear(25, 40, 2)]
            shaft[-1]._origin = shaft[-2].end
            
            shaft += create_random_profile(1,
                                  0,
                                  initial_diameter=[25,15,10],
                                  increase_values=[
                                      -2,
                                      -3,
                                      -4,
                                  ],
                                  step_lengths=[27, 29],
                                  step_modificator=step_mod_dec_hole_chamfer,
                                  step_type=sol.Hole,origin=0) 
            
            shafts.append(shaft)
        

        return shafts

class MultipleGearSketch(ShaftSketch
                             #GeometricalCase
                             ):

    steps_no = {'max': 1, 'min': 0}

    @classmethod
    def _structure_generator(cls):
        
        steps = cls.steps_no
        holes = cls.holes_no
        
        shafts =  []
        for i in range(50):
            shaft = [sol.Cylinder(60, 40)]
            shaft[0]._origin = 0
            
            shaft += [sol.Gear(25, 40, 2)]
            shaft[-1]._origin = shaft[-2].end
            
            shaft += create_random_profile(steps['max'],steps['min'],
                                  increase_values=[
                                      4,
                                      5,
                                      6,
                                  ],
                                  step_modificator=step_mod_inc_gear,origin=shaft[-1].end) 
            
            shaft +=create_random_profile(steps['max'],steps['min'],
                                  increase_values=[
                                      -4,
                                      -5,
                                      -6,
                                  ],
                                  step_modificator=step_mod_inc_gear,origin = shaft[-1].end)
            
            shaft += create_random_profile(3,
                                  0,
                                  initial_diameter=[30,25,20],
                                  increase_values=[
                                      -2,
                                      -3,
                                      -4,
                                  ],
                                  step_lengths=[27, 29],
                                  step_modificator=step_mod_dec_hole_chamfer,
                                  step_type=sol.Hole,origin=0) 
            shaft += [sol.ThreadedOpenHole(shaft[-1].diameter-5,14)]
            shaft[-1]._origin=shaft[-2].end
            
            shafts.append(shaft)
        

        return shafts


class DoubleGearSketch(ShaftSketch
                             #GeometricalCase
                             ):

    steps_no = {'max': 1, 'min': 0}

    @classmethod
    def _structure_generator(cls):
        
        steps = cls.steps_no
        holes = cls.holes_no
        
        shafts =  []
        for i in range(50):
            shaft = [sol.Cylinder(60, 40)]
            shaft[0]._origin = 0
            
            #shaft += [sol.Gear(25, 40, 2)]
            #shaft[-1]._origin = shaft[-2].end
            
            shaft += create_random_profile(steps['max'],steps['min'],
                                  increase_values=[
                                      4,
                                      5,
                                      6,
                                  ],
                                  step_modificator=step_mod_inc_gear,origin=shaft[-1].end) 
            
            shaft +=create_random_profile(steps['max'],steps['min'],
                                  increase_values=[
                                      -4,
                                      -5,
                                      -6,
                                  ],
                                  step_modificator=step_mod_inc_gear,origin = shaft[-1].end)
            
            #shaft = [sol.Cylinder(60, 40)]
            #shaft += [sol.ThreadedOpenHole(shaft[-1].diameter-5,14)]
            #shaft[-1]._origin=shaft[-2].end
            
            shafts.append(shaft)
        

        return shafts

class SingleShaftGearSketch(ShaftSketch
                             #GeometricalCase
                             ):

    steps_no = {'max': 1, 'min': 0}

    @classmethod
    def _structure_generator(cls):
        
        steps = cls.steps_no
        holes = cls.holes_no
        
        shafts =  []
        for i in range(50):
            shaft = [sol.Cylinder(60, 40)]
            shaft[0]._origin = 0
            
#             shaft += [sol.Gear(25, 40, 2)]
#             shaft[-1]._origin = shaft[-2].end
            
            shaft += create_random_profile(steps['max'],steps['min'],
                                  increase_values=[
                                      4,
                                      5,
                                      6,
                                  ],
                                  step_modificator=step_mod_inc_chamfer,origin=shaft[-1].end) 

            shaft += [sol.Gear(25, 40, 3)]
            shaft[-1]._origin = shaft[-2].end
            
            shaft +=create_random_profile(steps['max'],steps['min'],
                                  increase_values=[
                                      -4,
                                      -5,
                                      -6,
                                  ],
                                  step_modificator=step_mod_dec_chamfer,origin = shaft[-1].end)
            
            #shaft = [sol.Cylinder(60, 40)]
            #shaft += [sol.ThreadedOpenHole(shaft[-1].diameter-5,14)]
            #shaft[-1]._origin=shaft[-2].end
            
            shafts.append(shaft)
        

        return shafts
    
    
class SimpleHollowSleeveSketch(ShaftSketch
                             #GeometricalCase
                             ):

    steps_no = {'max': 2, 'min': 1}

    @classmethod
    def _structure_generator(cls):
        
        steps = cls.steps_no
        holes = cls.holes_no
        
        shafts =  []
        for i in range(50):
 
            
            shaft = create_random_profile(steps['max'],steps['min'],
                                  increase_values=[
                                      4,
                                      5,
                                      6,
                                  ],
                                  step_modificator=step_mod_inc_chamfer,origin=0) 
            
            
            d_end=shaft[-1].diameter

            right_profile  =create_random_profile(steps['max'],steps['min'],
                                  initial_diameter=[d_end+8, d_end+10 ],
                                  increase_values=[
                                      -4,
                                      -5,
                                      -6,
                                  ],
                                  step_modificator=step_mod_dec_chamfer,origin = shaft[-1].end)

            shaft +=  right_profile
            

            
            thread_length = right_profile[-1].end #- shaft[-1].end
            
            shaft += [sol.ThreadedOpenHole(thread_length,round(shaft[0].diameter*0.4))]
            shafts.append(shaft)
            shaft[-1]._origin=0
        

        return shafts
    
class HollowSleeveWithGrearsSketch(ShaftSketch
                             #GeometricalCase
                             ):

    steps_no = {'max': 1, 'min': 0}

    @classmethod
    def _structure_generator(cls):
        
        steps = cls.steps_no
        holes = cls.holes_no
        
        shafts =  []
        for i in range(50):
            shaft = [sol.Gear(25, 40, 2)]
            shaft[0]._origin = 0
            
            shaft += create_random_profile(steps['max'],steps['min'],
                                  increase_values=[
                                      4,
                                      5,
                                      6,
                                  ],
                                  step_modificator=step_mod_inc_gear,origin=shaft[-1].end) 
            
            
            

            right_profile =create_random_profile(steps['max'],steps['min'],
                                  increase_values=[
                                      -4,
                                      -5,
                                      -6,
                                  ],
                                  step_modificator=step_mod_inc_gear,origin=shaft[-1].end)

            shaft +=  right_profile
            
            shaft += create_random_profile(4,
                                  2,
                                  initial_diameter=[30,25,20],
                                  increase_values=[
                                      -2,
                                      -3,
                                      -4,
                                  ],
                                  step_lengths=[27, 29],
                                  step_modificator=step_mod_dec_hole_chamfer,
                                  step_type=sol.Hole,origin=0) 
            
            thread_length = right_profile[-1].end - shaft[-1].end
            
            shaft += [sol.ThreadedOpenHole(thread_length,shaft[-1].diameter-5)]
            shafts.append(shaft)
            shaft[-1]._origin=shaft[-2].end
        

        return shafts
    
class ThreadedSleeveWithGrearsSketch(ShaftSketch
                             #GeometricalCase
                             ):

    steps_no = {'max': 1, 'min': 0}

    @classmethod
    def _structure_generator(cls):
        
        steps = cls.steps_no
        holes = cls.holes_no
        
        shafts =  []
        for i in range(50):
            shaft =  create_random_profile(steps['max'],steps['min'],
                                  increase_values=[
                                      4,
                                      5,
                                      6,
                                  ],
                                  step_modificator= step_mod_inc_threads,origin = 0)
            
            shaft +=  [sol.Gear(25, 40, 3)]
            shaft[-1]._origin = shaft[-2].end
            
            shaft +=create_random_profile(steps['max'],steps['min'],
                                  increase_values=[
                                      -4,
                                      -5,
                                      -6,
                                  ],
                                  step_modificator=step_mod_inc_gear,origin = shaft[-1].end)
            
            shaft += create_random_profile(4,
                                  2,
                                  initial_diameter=[30,25,20],
                                  increase_values=[
                                      -2,
                                      -3,
                                      -4,
                                  ],
                                  step_lengths=[27, 29],
                                  step_modificator=step_mod_dec_hole_chamfer,
                                  step_type=sol.Hole,origin=0)
            shaft += [sol.ThreadedOpenHole(shaft[-1].diameter-5,14)]
            shaft[-1]._origin=shaft[-2].end
            
            shafts.append(shaft)
        

        return shafts
    
    
class ComplexBoltWithHole(ShaftSketch
                             #GeometricalCase
                             ):

    steps_no = {'max': 1, 'min': 0}
    holes_no = {'max': 2, 'min': 0}    

    @classmethod
    def _structure_generator(cls):
        
        steps = cls.steps_no
        holes = cls.holes_no

        shafts =  []
        for i in range(50):
            indiameter = random.randint( 60,70)
            height=round(1.2*0.5*indiameter)
            
            shaft = [sol.ChamferedHexagonalPrism(height,indiameter, random.randint(3,4))]
            shaft[-1]._origin=0
            #shaft += [sol.ThreadedOpenHole(shaft[-1].height,shaft[-1].diameter-5)]
            shaft[-1]._origin = 0

#             shaft =  create_random_profile(steps['max'],steps['min'],
#                                   increase_values=[
#                                       4,
#                                       5,
#                                       6,
#                                   ],
#                                   step_modificator= step_mod_chamfer_hex_prism, origin = 0) 
            
            shaft +=create_random_profile(steps['max'],steps['min'],
                                  initial_diameter=[40,35,30],
                                  increase_values=[
                                      -4,
                                      -5,
                                      -6,
                                  ],
                                  step_lengths=[60, 70],
                                  step_modificator=step_mod_dec_screw,origin = shaft[-1].end)
            
            shaft += create_random_profile(2,
                                  1,
                                  initial_diameter=[23,20],
                                  increase_values=[
                                      -5,
                                      -7,
                    
                                  ],
                                  step_lengths=[31, 33,37],
                                  step_modificator=step_mod_dec_hole_chamfer,
                                  step_type=sol.Hole,origin=0) 
            
            
            shafts.append(shaft)
        

        return shafts
    
class HexNutSketch(ShaftSketch
                             #GeometricalCase
                             ):

    steps_no = {'max': 2, 'min': 1}
    holes_no = {'max': 2, 'min': 0}    

    @classmethod
    def _structure_generator(cls):
        
        steps = cls.steps_no
        holes = cls.holes_no

        shafts =  []
        for i in range(50):
            indiameter = random.randint( 70,80)
            height=round(0.8*0.5*indiameter)
            
            shaft = [sol.ChamferedHexagonalPrism(height,indiameter, random.randint(3,4))]
            shaft[0]._origin = 0
            shaft += [sol.Cylinder(round(shaft[-1].height*0.2),round(shaft[-1].indiameter*0.9))]
            shaft[-1]._origin= shaft[-2].end
            shaft += [sol.ThreadedOpenHole(shaft[-2].height+shaft[-1].height,shaft[-2].diameter-5)]
            shaft[-1]._origin = 0
            
            shafts.append(shaft)
            
        for i in range(50):
            
            
            indiameter = random.randint( 70,80)
            height=round(1.2*0.5*indiameter)
            
            shaft = [sol.ChamferedHexagonalPrism(height,indiameter, random.randint(3,4))]
            shaft[0]._origin = 0
            shaft += [sol.Cylinder(round(shaft[-1].height*0.3),round(shaft[-1].indiameter*0.9))]
            shaft[-1]._origin= shaft[-2].end
            shaft  += [sol.ChamferedHexagonalPrism(shaft[-2].height, shaft[-2].indiameter, shaft[-2].chamfer_length)]
            shaft[-1]._origin = shaft[-2].end
            shaft += [sol.ThreadedOpenHole(shaft[-3].height+shaft[-2].height+shaft[-1].height,shaft[-3].diameter-5)]
            shaft[-1]._origin = 0
            
            shafts.append(shaft)
            
        for i in range(50):
            indiameter = random.randint( 70,80)
            height=round(1.2*0.5*indiameter)
            
            shaft = [sol.DoubleChamferedHexagonalPrism(height,indiameter, random.randint(3,4))]
            shaft[0]._origin = 0
            shaft += [sol.ThreadedOpenHole(shaft[-1].height,shaft[-1].diameter-5)]
            shaft[-1]._origin = 0
            
            shafts.append(shaft)

        for i in range(50):
            indiameter = random.randint( 70,80)
            height=round(1.2*0.5*indiameter)
            
            shaft = [sol.ChamferedHexagonalPrism(height,indiameter, random.randint(3,4))]
            shaft[0]._origin = 0
            shaft += [sol.Cylinder(round(shaft[-1].height*0.2),round(shaft[-1].indiameter*1.2))]
            shaft[-1]._origin= shaft[-2].end
            shaft += [sol.ThreadedOpenHole(shaft[-2].height+shaft[-1].height,shaft[-2].diameter-5)]
            shaft[-1]._origin = 0
            
            shafts.append(shaft)

        return shafts
    
class BasicGearSketch(ShaftSketch
                             #GeometricalCase
                             ):

    steps_no = {'max': 4, 'min': 2}

    @classmethod
    def _structure_generator(cls):
        
        steps = cls.steps_no
        holes = cls.holes_no
        
        shafts =  []
#         for i in range(50): # Git

#             shaft = [sol.Cylinder(random.randint(20,40),random.randint(50,60))] + [sol.Gear(random.randint(30,60), random.randint(40,50), random.randint(3,4))]
#             shaft[-1]._origin=0
#             shaft[-2]._origin=shaft[-1].end
            
#             shaft +=[sol.ChamferedOpenHoleWithKeyway(shaft[-2].end,random.randint(20,40))]
#             shaft[-1]._origin=shaft[-2].origin
#             shaft[-1]._end=shaft[-3].end
            
#             shafts.append(shaft)
            
              
#         for i in range(50): # Git
#             shaft =[sol.Cylinder(random.randint(20,40),random.randint(50,60))] + [sol.Gear(random.randint(30,60), random.randint(40,50), random.randint(3,4))] + [sol.Cylinder(random.randint(20,40),random.randint(50,60))]
#             shaft[-3]._origin = 0
#             shaft[-2]._origin=shaft[-3].end
#             shaft[-1]._origin = shaft[-2].end
            
#             shaft +=[sol.ChamferedOpenHoleWithKeyway(shaft[-1].end,random.randint(20,40))]
#             shaft[-1]._origin=shaft[-4].origin
#             shaft[-1]._end=shaft[-2].end
              
#             shafts.append(shaft)
            
#         for i in range(50): # Git

#             shaft = [sol.Gear(random.randint(30,60), random.randint(40,50), random.randint(3,4))] + [sol.Cylinder(random.randint(20,40),random.randint(50,60))]
#             shaft[-1]._origin =0
#             shaft[-2]._origin = shaft[-1].end
#             shaft +=[sol.ChamferedHole(shaft[-2].end,random.randint(20,40))]
#             shaft[-1]._origin=shaft[-2].origin
#             shaft[-1]._end=shaft[-3].end
            
            
#             shafts.append(shaft)
        for i in range(50): # Git
            shaft =[sol.Cylinder(random.randint(20,40),random.randint(50,60))] +[sol.Cylinder(random.randint(20,40),random.randint(50,60))]+[sol.Cylinder(random.randint(20,40),random.randint(50,60))]
            shaft[-3]._origin = 0
            shaft[-2]._origin=shaft[-3].end
            shaft[-1]._origin = shaft[-2].end
          
              
           
            shafts.append(shaft)
  
            
        return shafts
    
class ScrewConnectionSketch(ShaftSketch
                             #GeometricalCase
                             ):

    steps_no = {'max': 4, 'min': 2}

    @classmethod
    def _structure_generator(cls):
        
        steps = cls.steps_no
        holes = cls.holes_no
        shafts = []
        for i in range(50): # 2 płytki
            
            screw_diameter = random.randint(40,60)
            
            shaft =  [sol.HexagonalHeadOfScrew(round(0.7 * screw_diameter), 2 * screw_diameter)]
            shaft += [sol.ScrewCore(round(screw_diameter*3), screw_diameter)] 
            shaft += [sol.Washer(round(0.15 * screw_diameter), round(2.2 * screw_diameter))]
            shaft += [sol.StandarizedNut(round(0.8 * screw_diameter), 2 * screw_diameter)]
            shaft += [sol.ThreadOfScrew(round(0.3 * screw_diameter), screw_diameter)]
            
            shaft += [sol.Plate(random.randint(70,80),random.randint(100,110))]
            shaft += [sol.Plate((shaft[-5].end-shaft[-1].end),random.randint(120,130))]

            shaft[-7]._origin = 0
            shaft[-6]._origin = shaft[-7].end
            shaft[-5]._origin = shaft[-6].end
            shaft[-4]._origin = shaft[-5].end
            shaft[-3]._origin = shaft[-4].end
            
            shaft[-2]._origin = shaft[-7].end
            shaft[-1]._origin = shaft[-2].end
            
            shaft += [sol.OpenHole(shaft[-2].end-shaft[-7].end,round(screw_diameter*1.2))]
            shaft += [sol.OpenHole(shaft[-2].end-shaft[-8].end-shaft[-1].end,round(screw_diameter*1.2)+2)]
            
            shaft[-2]._origin = shaft[-9].end
            shaft[-1]._origin = shaft[-2].end
            
            shafts.append(shaft)
            
        for i in range(50): # 3 płytki
            
            screw_diameter = random.randint(40,60)
            
            shaft =  [sol.HexagonalHeadOfScrew(round(0.7 * screw_diameter), 2 * screw_diameter)]
            shaft += [sol.ScrewCore(round(screw_diameter*3), screw_diameter)] 
            shaft += [sol.Washer(round(0.15 * screw_diameter), round(2.2 * screw_diameter))]
            shaft += [sol.StandarizedNut(round(0.8 * screw_diameter), 2 * screw_diameter)]
            shaft += [sol.ThreadOfScrew(round(0.3 * screw_diameter), screw_diameter)]
            
            shaft += [sol.Plate(random.randint(40,60),random.randint(100,110))]
            shaft += [sol.Plate((round(0.7*shaft[-5].end)-shaft[-1].end),random.randint(120,130))]

            shaft[-7]._origin = 0
            shaft[-6]._origin = shaft[-7].end
            shaft[-5]._origin = shaft[-6].end
            shaft[-4]._origin = shaft[-5].end
            shaft[-3]._origin = shaft[-4].end
            
            shaft[-2]._origin = shaft[-7].end
            shaft[-1]._origin = shaft[-2].end
            
            shaft += [sol.Plate((shaft[-6].end-shaft[-1].end),random.randint(100,110))]
            
            shaft[-1]._origin = shaft[-2].end
            
            shaft += [sol.OpenHole(shaft[-3].end-shaft[-8].end,round(screw_diameter*1.2))]
            shaft += [sol.OpenHole(shaft[-3].end-shaft[-9].end-shaft[-1].end,round(screw_diameter*1.2)+2)]
            shaft += [sol.OpenHole(shaft[-3].end-shaft[-10].end-shaft[-2].end-shaft[-1].end,round(screw_diameter*1.2))]
            
            shaft[-3]._origin = shaft[-11].end
            shaft[-2]._origin = shaft[-3].end
            shaft[-1]._origin = shaft[-2].end
            
            shafts.append(shaft)

        for i in range(50): # 4 płytki
            
            screw_diameter = random.randint(40,60)
            
            shaft =  [sol.HexagonalHeadOfScrew(round(0.7 * screw_diameter), 2 * screw_diameter)]
            shaft += [sol.ScrewCore(round(screw_diameter*3), screw_diameter)] 
            shaft += [sol.Washer(round(0.15 * screw_diameter), round(2.2 * screw_diameter))]
            shaft += [sol.StandarizedNut(round(0.8 * screw_diameter), 2 * screw_diameter)]
            shaft += [sol.ThreadOfScrew(round(0.3 * screw_diameter), screw_diameter)]
            
            shaft += [sol.Plate(random.randint(40,60),random.randint(100,110))]
            shaft += [sol.Plate((round(0.6*shaft[-5].end)-shaft[-1].end),random.randint(120,130))]

            shaft[-7]._origin = 0
            shaft[-6]._origin = shaft[-7].end
            shaft[-5]._origin = shaft[-6].end
            shaft[-4]._origin = shaft[-5].end
            shaft[-3]._origin = shaft[-4].end
            
            shaft[-2]._origin = shaft[-7].end
            shaft[-1]._origin = shaft[-2].end
            
            shaft += [sol.Plate((round(0.9*shaft[-6].end)-shaft[-1].end),random.randint(100,110))]
            
            shaft[-1]._origin = shaft[-2].end
            
            shaft += [sol.Plate((shaft[-7].end-shaft[-1].end),random.randint(120,130))]
            
            shaft[-1]._origin = shaft[-2].end
            
            shaft += [sol.OpenHole(shaft[-4].end-shaft[-9].end,round(screw_diameter*1.2))]
            shaft += [sol.OpenHole(shaft[-4].end-shaft[-10].end-shaft[-1].end,round(screw_diameter*1.2)+2  )]
            shaft += [sol.OpenHole(shaft[-4].end-shaft[-11].end-shaft[-2].end-shaft[-1].end,round(screw_diameter*1.2)+4)]
            shaft += [sol.OpenHole(shaft[-4].end-shaft[-12].end-shaft[-3].end-shaft[-2].end-shaft[-1].end,round(screw_diameter*1.2))]
            
            shaft[-4]._origin = shaft[-13].end
            shaft[-3]._origin = shaft[-4].end
            shaft[-2]._origin = shaft[-3].end
            shaft[-1]._origin = shaft[-2].end
            
            shafts.append(shaft)
            
        return shafts
    

class BodyBlockView(ShaftSketch
                              #GeometricalCase
                              ):


    @classmethod
    def _structure_generator(cls):
        
        steps = cls.steps_no
        holes = cls.holes_no
        
        shafts  = []
        for i in range(50):
            body_height=random.randint(120,150)
            body_width=random.randint(140,170)
            
            body_length = round(0.7*body_width)
            
            axis_pos= round(0.01*random.randint(50,70) * body_height)
            
            body_type = random.choice([
                                       sol.BodyBlock,
                                       sol.BodyBlockShapeT,
                                       sol.HeavyBodyBlockShapeT,
                                       sol.MediumBodyBlockShapeT,
                                       sol.BodyBlockShapeC,
                                       sol.BodyBlockCutType,
                                      ])
            
            shaft = [body_type(body_height,body_length,body_width,axis_pos)]
            shaft[-1]._origin = 0
            
            step_length = random.randint(10,20)
            
            shaft += [sol.BlockHole(step_length,round(0.35*body_width))]
            shaft[-1]._origin = 0
            
            
            shaft += [sol.BlockHiddenHole(body_length-step_length,round(0.4*body_width))]
            shaft[-1]._origin =step_length
            #shaft[-1]._end = shaft[-2].end
            
            
            shafts.append(shaft)
            
            

        for i in range(50):
            body_height=random.randint(120,150)
            body_width=random.randint(140,170)
            
            body_length = round(0.7*body_width)
            
            axis_pos= round(0.01*random.randint(50,70) * body_height)
            
            body_type = random.choice([
                                       sol.BodyBlock,
                                       sol.BodyBlockShapeT,
                                       sol.HeavyBodyBlockShapeT,
                                       sol.MediumBodyBlockShapeT,
                                       #sol.BodyBlockShapeC,
                                       #sol.BodyBlockCutType,
                                      ])
            
            shaft = [body_type(body_height,body_length,body_width,axis_pos)]
            shaft[-1]._origin = 0
            shaft += [sol.BlockHole(round(body_length*0.4),round(0.4*body_width))]
            shaft[-1]._origin = 0


            step_length = random.randint(10,30)
            
            shaft += [sol.BlockHole(step_length,round(0.3*body_width))]
            shaft[-1]._origin = shaft[-2].end
            
            
            shaft += [sol.BlockHiddenHole(body_length-(round(body_length*0.4) + step_length ) ,round(0.4*body_width))]
            shaft[-1]._origin = shaft[-2].end
            #shaft[-1]._end = shaft[-2].end
            
            
            shafts.append(shaft)
            

            
        return shafts
    
    
class BearingBlockView(ShaftSketch
                              #GeometricalCase
                              ):


    @classmethod
    def _structure_generator(cls):
        
        steps = cls.steps_no
        holes = cls.holes_no
        
        shafts  = []



        for i in range(50):
            body_height=random.randint(120,150)
            body_width=random.randint(140,170)
            
            body_length = round(0.7*body_width)
            
            axis_pos= round(0.01*random.randint(50,70) * body_height)
            
            body_type = random.choice([sol.BodyBlock,
                                       sol.BodyBlockShapeT,
                                       sol.HeavyBodyBlockShapeT,
                                       sol.MediumBodyBlockShapeT,
                                      ])
            
            shaft = [body_type(body_height,body_length,body_width,axis_pos)]
            shaft[-1]._origin = 0
            shaft += [sol.BlockHole(round(body_length*0.3),round(0.4*body_width))]
            shaft[-1]._origin = 0


            step_length = random.randint(10,30)
            
            shaft += [sol.BlockHole(step_length,round(0.35*body_width))]
            shaft[-1]._origin = shaft[-2].end

            shaft += [sol.BlockHole(step_length,round(0.3*body_width))]
            shaft[-1]._origin = shaft[-2].end
            
            shaft += [sol.BlockHiddenHole(body_length-(round(body_length*0.3) + 2*step_length ) ,round(0.4*body_width))]
            shaft[-1]._origin = shaft[-2].end
            #shaft[-1]._end = shaft[-2].end
            
            
            shafts.append(shaft)
            
        for i in range(50):
            body_height=random.randint(120,150)
            body_width=random.randint(140,170)
            
            body_length = round(0.7*body_width)
            
            axis_pos= round(0.01*random.randint(50,70) * body_height)
            
            body_type = random.choice([sol.BodyBlock,
                                       sol.BodyBlockShapeT,
                                       sol.HeavyBodyBlockShapeT,
                                       sol.MediumBodyBlockShapeT,
                                       sol.BodyBlockShapeC,
                                       sol.BodyBlockCutType,
                                      ])
            
            shaft = [body_type(body_height,body_length,body_width,axis_pos)]
            shaft[-1]._origin = 0
            shaft += [sol.BlockHole(round(body_length*0.3),round(0.35*body_width))]
            shaft[-1]._origin = 0


            step_length = random.randint(10,30)
            
            shaft += [sol.BlockHole(step_length,round(0.3*body_width))]
            shaft[-1]._origin = shaft[-2].end

            shaft += [sol.BlockHole(step_length,round(0.25*body_width))]
            shaft[-1]._origin = shaft[-2].end
            
            shaft += [sol.BlockHiddenHole(body_length-(round(body_length*0.3) + 2*step_length ) ,round(0.4*body_width))]
            shaft[-1]._origin = shaft[-2].end
            #shaft[-1]._end = shaft[-2].end
            
            
            shafts.append(shaft)

        for i in range(50):
            body_height=random.randint(120,150)
            body_width=random.randint(140,170)
            
            body_length = round(0.7*body_width)
            
            axis_pos= round(0.01*random.randint(50,70) * body_height)
            
            body_type = random.choice([sol.BodyBlock,
                                       sol.BodyBlockShapeT,
                                       sol.HeavyBodyBlockShapeT,
                                       sol.MediumBodyBlockShapeT,
                                       sol.BodyBlockShapeC,
                                       sol.BodyBlockCutType,
                                      ])
            
            shaft = [body_type(body_height,body_length,body_width,axis_pos)]
            shaft[-1]._origin = 0
            shaft += [sol.BlockHole(round(body_length*0.4),round(0.4*body_width))]
            shaft[-1]._origin = 0


            step_length = random.randint(10,30)
            
            shaft += [sol.BlockHole(step_length,round(0.35*body_width))]
            shaft[-1]._origin = shaft[-2].end

            shaft += [sol.BlockHole(step_length,round(0.3*body_width))]
            shaft[-1]._origin = shaft[-2].end
            
            shaft += [sol.BlockHiddenHole(body_length-(round(body_length*0.4) + 2*step_length ) ,round(0.35*body_width))]
            shaft[-1]._origin = shaft[-2].end
            #shaft[-1]._end = shaft[-2].end
            
            
            shafts.append(shaft)
            
            
        return shafts    
    
    
class BodyBlockRoundedView(ShaftSketch
                              #GeometricalCase
                              ):
    @classmethod
    def _structure_generator(cls):
        
        steps = cls.steps_no
        holes = cls.holes_no
        
        shafts  = []
        for i in range(50):
            body_height=random.randint(120,150)
            body_width=random.randint(140,170)
            
            body_length = round(0.7*body_width)
            
            axis_pos= round(0.01*random.randint(50,70) * body_height)
            
            body_type = random.choice([sol.RoundedBodyBlock,
                                       sol.RoundedBodyBlockShapeT,
                                       sol.RoundedHeavyBodyBlockShapeT,
                                       sol.RoundedMediumBodyBlockShapeT,
                                       sol.RoundedBodyBlockShapeC,
                                       sol.RoundedBodyBlockCutType,
                                      ])
            
            shaft = [body_type(body_height,body_length,body_width,axis_pos)]
            shaft[-1]._origin = 0
            
            step_length = random.randint(10,20)
            
            shaft += [sol.BlockHole(step_length,round(0.35*body_width))]
            shaft[-1]._origin = 0
            
            
            shaft += [sol.BlockHiddenHole(body_length-step_length,round(0.4*body_width))]
            shaft[-1]._origin =step_length
            #shaft[-1]._end = shaft[-2].end
            
            
            shafts.append(shaft)
            
            

        for i in range(50):
            body_height=random.randint(120,150)
            body_width=random.randint(140,170)
            
            body_length = round(0.7*body_width)
            
            axis_pos= round(0.01*random.randint(50,70) * body_height)
            
            body_type = random.choice([sol.RoundedBodyBlock,
                                       sol.RoundedBodyBlockShapeT,
                                       sol.RoundedHeavyBodyBlockShapeT,
                                       sol.RoundedMediumBodyBlockShapeT,
                                       sol.RoundedBodyBlockShapeC,
                                       sol.RoundedBodyBlockCutType,
                                      ])
            
            shaft = [body_type(body_height,body_length,body_width,axis_pos)]
            shaft[-1]._origin = 0
            shaft += [sol.BlockHole(round(body_length*0.4),round(0.4*body_width))]
            shaft[-1]._origin = 0


            step_length = random.randint(10,30)
            
            shaft += [sol.BlockHole(step_length,round(0.3*body_width))]
            shaft[-1]._origin = shaft[-2].end
            
            
            shaft += [sol.BlockHiddenHole(body_length-(round(body_length*0.4) + step_length ) ,round(0.4*body_width))]
            shaft[-1]._origin = shaft[-2].end
            #shaft[-1]._end = shaft[-2].end
            
            
            shafts.append(shaft)
            

            
        return shafts

    
    
class ShaftWithKeyseats(ShaftSketch
                              #GeometricalCase
                              ):
    



    @classmethod
    def _structure_generator(cls):
        
        steps = cls.steps_no
        holes = cls.holes_no
        
        shafts  = []
#         for i in range(50):
#             body_length=random.randint(30,50)
            
#             shaft = [sol.ChamferedCylinderWithKeyseat(0.7*body_length,1.2*body_length)]
#             shaft[-1]._origin = 0
#             #shaft += [sol.ShaftWithKeyseatsSketch(2*body_length,1.3*body_length)]
#             #shaft[-1]._origin = shaft[-2].end
#             shaft += [sol.CylinderWithKeyseat(0.2*body_length,1.45*body_length)]
#             shaft[-1]._origin = shaft[-2].end
# #             shaft += [sol.Gear(0.9*body_length,0.8*body_length,random.randint(2,3))] 
# #             shaft[-1]._origin = shaft[-2].end
# #             shaft += [sol.CylinderWithKeyseat(0.2*body_length,1.45*body_length)]
# #             shaft[-1]._origin = shaft[-2].end
# #             shaft += [sol.ShaftWithKeyseatsSketch(3*body_length,1.3*body_length)]
# #             shaft[-1]._origin = shaft[-2].end
# #             shaft += [sol.CylinderWithKeyseat(0.6*body_length,1.2*body_length)]
# #             shaft[-1]._origin = shaft[-2].end
# #             shaft += [sol.ShaftWithKeyseatsSketch(3*body_length,1.1*body_length)]
# #             shaft[-1]._origin = shaft[-2].end
# #             shaft += [sol.ChamferedCylinderWithKeyseat(0.7*body_length,1*body_length)]
# #             shaft[-1]._origin = shaft[-2].end
            

            
#             shafts.append(shaft)
            
        for i in range(50):
            shaft = [sol.CylinderWithKeyseat(60, 40)]
            shaft[0]._origin = 0
            

            
            shaft += create_random_profile(steps['max'],steps['min'],
                                  increase_values=[
                                      4,
                                      5,
                                      6,
                                  ],
                                  step_modificator=step_mod_inc_keyseat,origin=shaft[-1].end) 
            
            shaft +=create_random_profile(steps['max'],steps['min'],
                                  increase_values=[
                                      -4,
                                      -5,
                                      -6,
                                  ],
                                  step_modificator=step_mod_dec_keyseat,origin = shaft[-1].end)
            
            shaft += create_random_profile(holes['max'],holes['min'],
                                  initial_diameter=[30,25,20],
                                  increase_values=[
                                      -2,
                                      -3,
                                      -4,
                                  ],
                                  step_lengths=[27, 29],
                                  step_modificator=step_mod_dec_hole_chamfer,
                                  step_type=sol.Hole,origin=0) 
            #shaft += [sol.ThreadedOpenHole(shaft[-1].diameter-5,14)]
            #shaft[-1]._origin=shaft[-2].end
            
            shafts.append(shaft)
        

        return shafts            
            
class SimpleShaftWithKeyseats(ShaftWithKeyseats
                              #GeometricalCase
                              ):
    
    steps_no = {'max': 2, 'min': 0}
    holes_no = {'max': 1, 'min': 0}
    
class BodyBlockSimpleView(ShaftSketch
                              #GeometricalCase
                              ):


    @classmethod
    def _structure_generator(cls):
        
        steps = cls.steps_no
        holes = cls.holes_no
        
        shafts  = []

        for i in range(50):
            body_height=random.randint(120,150)
            body_width=random.randint(140,170)
            
            body_length = round(0.7*body_width)
            
            axis_pos= round(0.01*random.randint(50,70) * body_height)
            
            shaft = [sol.BodyBlock(body_height,body_length,body_width,axis_pos)]
            shaft[-1]._origin = 0
            shaft += [sol.BlockHole(round(body_length*0.3),round(0.4*body_width))]
            shaft[-1]._origin = 0


            step_length = random.randint(10,30)
            
            shaft += [sol.BlockHole(step_length,round(0.35*body_width))]
            shaft[-1]._origin = shaft[-2].end

            shaft += [sol.BlockHole(step_length,round(0.3*body_width))]
            shaft[-1]._origin = shaft[-2].end
            
            shaft += [sol.BlockHiddenHole(body_length-(round(body_length*0.3) + 2*step_length ) ,round(0.4*body_width))]
            shaft[-1]._origin = shaft[-2].end
            
            
            shafts.append(shaft)
            
        return shafts    
    
class BodyBlockShapeTView(ShaftSketch
                              #GeometricalCase
                              ):


    @classmethod
    def _structure_generator(cls):
        
        steps = cls.steps_no
        holes = cls.holes_no
        
        shafts  = []



        for i in range(50):
            body_height=random.randint(120,150)
            body_width=random.randint(140,170)
            
            body_length = round(0.7*body_width)
            
            axis_pos= round(0.01*random.randint(50,70) * body_height)
            
            body_type = random.choice([
                                       sol.BodyBlockShapeT,
                                       sol.HeavyBodyBlockShapeT,
                                       sol.MediumBodyBlockShapeT,
                                      ])
            
            shaft = [body_type(body_height,body_length,body_width,axis_pos)]
            shaft[-1]._origin = 0
            shaft += [sol.BlockHole(round(body_length*0.3),round(0.4*body_width))]
            shaft[-1]._origin = 0


            step_length = random.randint(10,30)
            
            shaft += [sol.BlockHole(step_length,round(0.35*body_width))]
            shaft[-1]._origin = shaft[-2].end

            shaft += [sol.BlockHole(step_length,round(0.3*body_width))]
            shaft[-1]._origin = shaft[-2].end
            
            shaft += [sol.BlockHiddenHole(body_length-(round(body_length*0.3) + 2*step_length ) ,round(0.4*body_width))]
            shaft[-1]._origin = shaft[-2].end
            #shaft[-1]._end = shaft[-2].end
            
            
            shafts.append(shaft)
            
        return shafts
        
class BodyBlockShapeCView(ShaftSketch
                              #GeometricalCase
                              ):


    @classmethod
    def _structure_generator(cls):
        
        steps = cls.steps_no
        holes = cls.holes_no
        
        shafts  = []

        for i in range(50):
            body_height=random.randint(120,150)
            body_width=random.randint(140,170)
            
            body_length = round(0.7*body_width)
            
            axis_pos= round(0.01*random.randint(50,70) * body_height)
            
            shaft = [sol.BodyBlockShapeC(body_height,body_length,body_width,axis_pos)]
            shaft[-1]._origin = 0
            shaft += [sol.BlockHole(round(body_length*0.3),round(0.4*body_width))]
            shaft[-1]._origin = 0


            step_length = random.randint(10,30)
            
            shaft += [sol.BlockHole(step_length,round(0.35*body_width))]
            shaft[-1]._origin = shaft[-2].end

            shaft += [sol.BlockHole(step_length,round(0.3*body_width))]
            shaft[-1]._origin = shaft[-2].end
            
            shaft += [sol.BlockHiddenHole(body_length-(round(body_length*0.3) + 2*step_length ) ,round(0.4*body_width))]
            shaft[-1]._origin = shaft[-2].end
            
            
            shafts.append(shaft)
            
        return shafts    
    
class BodyBlockCutTypeView(ShaftSketch
                              #GeometricalCase
                              ):


    @classmethod
    def _structure_generator(cls):
        
        steps = cls.steps_no
        holes = cls.holes_no
        
        shafts  = []

        for i in range(50):
            body_height=random.randint(120,150)
            body_width=random.randint(140,170)
            
            body_length = round(0.7*body_width)
            
            axis_pos= round(0.01*random.randint(50,70) * body_height)
            
            shaft = [sol.BodyBlockCutType(body_height,body_length,body_width,axis_pos)]
            shaft[-1]._origin = 0
            shaft += [sol.BlockHole(round(body_length*0.3),round(0.4*body_width))]
            shaft[-1]._origin = 0


            step_length = random.randint(10,30)
            
            shaft += [sol.BlockHole(step_length,round(0.35*body_width))]
            shaft[-1]._origin = shaft[-2].end

            shaft += [sol.BlockHole(step_length,round(0.3*body_width))]
            shaft[-1]._origin = shaft[-2].end
            
            shaft += [sol.BlockHiddenHole(body_length-(round(body_length*0.3) + 2*step_length ) ,round(0.4*body_width))]
            shaft[-1]._origin = shaft[-2].end
            
            
            shafts.append(shaft)
            
        return shafts    
    
class RoundedBodyBlockSimpleView(ShaftSketch
                              #GeometricalCase
                              ):


    @classmethod
    def _structure_generator(cls):
        
        steps = cls.steps_no
        holes = cls.holes_no
        
        shafts  = []

        for i in range(50):
            body_height=random.randint(120,150)
            body_width=random.randint(140,170)
            
            body_length = round(0.7*body_width)
            
            axis_pos= round(0.01*random.randint(50,70) * body_height)
            
            shaft = [sol.RoundedBodyBlock(body_height,body_length,body_width,axis_pos)]
            shaft[-1]._origin = 0
            shaft += [sol.BlockHole(round(body_length*0.3),round(0.4*body_width))]
            shaft[-1]._origin = 0


            step_length = random.randint(10,30)
            
            shaft += [sol.BlockHole(step_length,round(0.35*body_width))]
            shaft[-1]._origin = shaft[-2].end

            shaft += [sol.BlockHole(step_length,round(0.3*body_width))]
            shaft[-1]._origin = shaft[-2].end
            
            shaft += [sol.BlockHiddenHole(body_length-(round(body_length*0.3) + 2*step_length ) ,round(0.4*body_width))]
            shaft[-1]._origin = shaft[-2].end
            
            
            shafts.append(shaft)
            
        return shafts    
    
class RoundedBodyBlockShapeTView(ShaftSketch
                              #GeometricalCase
                              ):


    @classmethod
    def _structure_generator(cls):
        
        steps = cls.steps_no
        holes = cls.holes_no
        
        shafts  = []



        for i in range(50):
            body_height=random.randint(120,150)
            body_width=random.randint(140,170)
            
            body_length = round(0.7*body_width)
            
            axis_pos= round(0.01*random.randint(50,70) * body_height)
            
            body_type = random.choice([
                                       sol.RoundedBodyBlockShapeT,
                                       sol.RoundedHeavyBodyBlockShapeT,
                                       sol.RoundedMediumBodyBlockShapeT,
                                      ])
            
            shaft = [body_type(body_height,body_length,body_width,axis_pos)]
            shaft[-1]._origin = 0
            shaft += [sol.BlockHole(round(body_length*0.3),round(0.4*body_width))]
            shaft[-1]._origin = 0


            step_length = random.randint(10,30)
            
            shaft += [sol.BlockHole(step_length,round(0.35*body_width))]
            shaft[-1]._origin = shaft[-2].end

            shaft += [sol.BlockHole(step_length,round(0.3*body_width))]
            shaft[-1]._origin = shaft[-2].end
            
            shaft += [sol.BlockHiddenHole(body_length-(round(body_length*0.3) + 2*step_length ) ,round(0.4*body_width))]
            shaft[-1]._origin = shaft[-2].end
            #shaft[-1]._end = shaft[-2].end
            
            
            shafts.append(shaft)
            
        return shafts
        
class RoundedBodyBlockShapeCView(ShaftSketch
                              #GeometricalCase
                              ):


    @classmethod
    def _structure_generator(cls):
        
        steps = cls.steps_no
        holes = cls.holes_no
        
        shafts  = []

        for i in range(50):
            body_height=random.randint(120,150)
            body_width=random.randint(140,170)
            
            body_length = round(0.7*body_width)
            
            axis_pos= round(0.01*random.randint(50,70) * body_height)
            
            shaft = [sol.RoundedBodyBlockShapeC(body_height,body_length,body_width,axis_pos)]
            shaft[-1]._origin = 0
            shaft += [sol.BlockHole(round(body_length*0.3),round(0.4*body_width))]
            shaft[-1]._origin = 0


            step_length = random.randint(10,30)
            
            shaft += [sol.BlockHole(step_length,round(0.35*body_width))]
            shaft[-1]._origin = shaft[-2].end

            shaft += [sol.BlockHole(step_length,round(0.3*body_width))]
            shaft[-1]._origin = shaft[-2].end
            
            shaft += [sol.BlockHiddenHole(body_length-(round(body_length*0.3) + 2*step_length ) ,round(0.4*body_width))]
            shaft[-1]._origin = shaft[-2].end
            
            
            shafts.append(shaft)
            
        return shafts    
    
class RoundedBodyBlockCutTypeView(ShaftSketch
                              #GeometricalCase
                              ):


    @classmethod
    def _structure_generator(cls):
        
        steps = cls.steps_no
        holes = cls.holes_no
        
        shafts  = []

        for i in range(50):
            body_height=random.randint(120,150)
            body_width=random.randint(140,170)
            
            body_length = round(0.7*body_width)
            
            axis_pos= round(0.01*random.randint(50,70) * body_height)
            
            shaft = [sol.RoundedBodyBlockCutType(body_height,body_length,body_width,axis_pos)]
            shaft[-1]._origin = 0
            shaft += [sol.BlockHole(round(body_length*0.3),round(0.4*body_width))]
            shaft[-1]._origin = 0


            step_length = random.randint(10,30)
            
            shaft += [sol.BlockHole(step_length,round(0.35*body_width))]
            shaft[-1]._origin = shaft[-2].end

            shaft += [sol.BlockHole(step_length,round(0.3*body_width))]
            shaft[-1]._origin = shaft[-2].end
            
            shaft += [sol.BlockHiddenHole(body_length-(round(body_length*0.3) + 2*step_length ) ,round(0.4*body_width))]
            shaft[-1]._origin = shaft[-2].end
            
            
            shafts.append(shaft)
            
        return shafts    
    
class ShortSleeve(ShaftSketch
                             #GeometricalCase
                             ):

    steps_no = {'max': 4, 'min': 2}

    @classmethod
    def _structure_generator(cls):
        
        steps = cls.steps_no
        holes = cls.holes_no
        
        shafts =  []
        
        for i in range(50): #Najprostsza wersja 2 stopnie i 3 stopnie otwór
            body_type1 = random.choice([sol.Cylinder,
                                       sol.ChamferedCylinder,
                                      ])
            body_type2 = random.choice([sol.Cylinder,
                                       sol.ChamferedCylinder,
                                      ])
            hole_type1 = random.choice([sol.OpenHole,
                                       sol.ChamferedHole,
                                      ])
            hole_type2 = random.choice([sol.OpenHole,
                                       sol.ChamferedHole,
                                      ])
            hole_type3 = random.choice([sol.OpenHole,
                                       sol.ChamferedHole,
                                      ])
            shaft =[body_type1(random.randint(50,70),random.randint(50,90))] +[body_type2(random.randint(45,60),random.randint(40,80))]
            shaft[-2]._origin=0
            shaft[-1]._origin = shaft[-2].end
            shaft += [hole_type1(random.randint(20,45),random.randint(15,32))]
            shaft[-1]._origin = 0
            shaft += [hole_type2(random.randint(10,35),random.randint(15,32))]
            shaft[-1]._origin = shaft[-2].end
            shaft += [hole_type3(shaft[-3].end-shaft[-1].end,random.randint(15,32))]
            shaft[-1]._origin = shaft[-2].end
              
           
            shafts.append(shaft)
        for i in range(50): #Najprostsza wersja 3 stopnie i 3 stopnie otwór
            body_type1 = random.choice([sol.Cylinder,
                                       sol.ChamferedCylinder,
                                      ])
            body_type2 = random.choice([sol.Cylinder,
                                       sol.ChamferedCylinder,
                                      ])
            body_type3 = random.choice([sol.Cylinder,
                                       sol.ChamferedCylinder,
                                      ])
            hole_type1 = random.choice([sol.OpenHole,
                                       sol.ChamferedHole,
                                      ])
            hole_type2 = random.choice([sol.OpenHole,
                                       sol.ChamferedHole,
                                      ])
            hole_type3 = random.choice([sol.OpenHole,
                                       sol.ChamferedHole,
                                      ])
            shaft =[body_type1(random.randint(50,70),random.randint(50,90))] +[body_type2(random.randint(45,60),random.randint(40,80))]+[body_type3(random.randint(45,70),random.randint(40,80))]
            shaft[-3]._origin = 0
            shaft[-2]._origin=shaft[-3].end
            shaft[-1]._origin = shaft[-2].end
            shaft += [hole_type1(random.randint(20,45),random.randint(15,32))]
            shaft[-1]._origin = 0
            shaft += [hole_type2(random.randint(10,35),random.randint(15,32))]
            shaft[-1]._origin = shaft[-2].end
            shaft += [hole_type3(shaft[-3].end-shaft[-1].end,random.randint(15,32))]
            shaft[-1]._origin = shaft[-2].end
              
           
            shafts.append(shaft)
        for i in range(50): #Najprostsza wersja 2 stopnie i 2 stopnie otwór
            body_type1 = random.choice([sol.Cylinder,
                                       sol.ChamferedCylinder,
                                      ])
            body_type2 = random.choice([sol.Cylinder,
                                       sol.ChamferedCylinder,
                                      ])
            hole_type1 = random.choice([sol.OpenHole,
                                       sol.ChamferedHole,
                                      ])
            hole_type2 = random.choice([sol.OpenHole,
                                       sol.ChamferedHole,
                                      ])
         
            shaft =[body_type1(random.randint(50,70),random.randint(50,90))] +[body_type2(random.randint(45,60),random.randint(40,80))]
            shaft[-2]._origin=0
            shaft[-1]._origin = shaft[-2].end
            shaft += [hole_type1(random.randint(20,70),random.randint(15,32))]
            shaft[-1]._origin = 0
            shaft += [hole_type2(shaft[-2].end-shaft[-1].end,random.randint(15,32))]
            shaft[-1]._origin = shaft[-2].end
              
           
            shafts.append(shaft)
        for i in range(50): #Najprostsza wersja 3 stopnie i 2 stopnie otwór
            body_type1 = random.choice([sol.Cylinder,
                                       sol.ChamferedCylinder,
                                      ])
            body_type2 = random.choice([sol.Cylinder,
                                       sol.ChamferedCylinder,
                                      ])
            body_type3 = random.choice([sol.Cylinder,
                                       sol.ChamferedCylinder,
                                      ])
            hole_type1 = random.choice([sol.OpenHole,
                                       sol.ChamferedHole,
                                      ])
            hole_type2 = random.choice([sol.OpenHole,
                                       sol.ChamferedHole,
                                      ])
         
            shaft =[body_type1(random.randint(50,70),random.randint(50,90))] +[body_type2(random.randint(45,60),random.randint(40,80))]+[body_type3(random.randint(45,70),random.randint(40,80))]
            shaft[-3]._origin = 0
            shaft[-2]._origin=shaft[-3].end
            shaft[-1]._origin = shaft[-2].end
            shaft += [hole_type1(random.randint(20,80),random.randint(15,32))]
            shaft[-1]._origin = 0
            shaft += [hole_type2(shaft[-2].end-shaft[-1].end,random.randint(15,32))]
            shaft[-1]._origin = shaft[-2].end
              
           
            shafts.append(shaft)

    
        for i in range(50): # 1 Stopień otwór
            body_type1 = random.choice([sol.Cylinder,
                                       sol.ChamferedCylinder,
                                      ])
            body_type2 = random.choice([sol.Cylinder,
                                       sol.ChamferedCylinder,
                                      ])
            body_type3 = random.choice([sol.Cylinder,
                                       sol.ChamferedCylinder,
                                      ])
            body_type4 = random.choice([sol.Cylinder,
                                       sol.ChamferedCylinder,
                                      ])
            body_type5 = random.choice([sol.Cylinder,
                                       sol.ChamferedCylinder,
                                      ])
            hole_type1 = random.choice([sol.OpenHole,
                                       sol.ChamferedHole,
                                      ])
            hole_type2 = random.choice([sol.OpenHole,
                                       sol.ChamferedHole,
                                      ])
         
            shaft =[body_type1(random.randint(50,70),random.randint(50,90))] +[body_type2(random.randint(45,60),random.randint(40,80))]+[body_type3(random.randint(45,70),random.randint(40,80))]+                          [body_type4(random.randint(30,50),random.randint(40,80))]+[body_type5(random.randint(35,90),random.randint(50,70))]
            shaft[-5]._origin = 0
            shaft[-4]._origin=shaft[-5].end
            shaft[-3]._origin = shaft[-4].end
            shaft[-2]._origin=shaft[-3].end
            shaft[-1]._origin = shaft[-2].end
            shaft += [hole_type1(random.randint(20,100),random.randint(15,32))]
            shaft[-1]._origin = 0
            shaft += [hole_type2(shaft[-2].end-shaft[-1].end,random.randint(15,32))]
            shaft[-1]._origin = shaft[-2].end
              
           
            shafts.append(shaft)

        for i in range(50): # 2 Stopnie otwór
            body_type1 = random.choice([sol.Cylinder,
                                       sol.ChamferedCylinder,
                                      ])
            body_type2 = random.choice([sol.Cylinder,
                                       sol.ChamferedCylinder,
                                      ])
            body_type3 = random.choice([sol.Cylinder,
                                       sol.ChamferedCylinder,
                                      ])
            body_type4 = random.choice([sol.Cylinder,
                                       sol.ChamferedCylinder,
                                      ])
            body_type5 = random.choice([sol.Cylinder,
                                       sol.ChamferedCylinder,
                                      ])
            hole_type1 = random.choice([sol.OpenHole,
                                       sol.ChamferedHole,
                                      ])
            hole_type2 = random.choice([sol.OpenHole,
                                       sol.ChamferedHole,
                                      ])
            hole_type3 = random.choice([sol.OpenHole,
                                       sol.ChamferedHole,
                                      ])
         
            shaft =[body_type1(random.randint(50,70),random.randint(50,90))] +[body_type2(random.randint(45,60),random.randint(40,80))]+[body_type3(random.randint(45,70),random.randint(40,80))]+                          [body_type4(random.randint(30,50),random.randint(40,80))]+[body_type5(random.randint(35,90),random.randint(50,70))]
            shaft[-5]._origin = 0
            shaft[-4]._origin=shaft[-5].end
            shaft[-3]._origin = shaft[-4].end
            shaft[-2]._origin=shaft[-3].end
            shaft[-1]._origin = shaft[-2].end
            shaft += [hole_type1(random.randint(20,100),random.randint(15,32))]
            shaft[-1]._origin = 0
            shaft += [hole_type2(random.randint(20,100),random.randint(15,32))]
            shaft[-1]._origin = shaft[-2].end
            shaft += [hole_type3(shaft[-3].end-shaft[-1].end,random.randint(15,32))]
            shaft[-1]._origin = shaft[-2].end
          
              
           
            shafts.append(shaft)
  
            
        return shafts