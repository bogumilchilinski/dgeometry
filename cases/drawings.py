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

    def solution(self, solved_case=None):

        if self._cached_solution is None:

            new_obj = copy.deepcopy(self)
            self._cached_solution = new_obj

        else:
            new_obj = self._cached_solution

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
    step,
    sol.ChamferedCylinder(
        step.height, step.diameter, chamfer_angle=45, chamfer_length=1),
    sol.Thread(step.height, step.diameter),
    [
        step,
        sol.FlangeWithHoles(height=step.height,
                            diameter=step.diameter * 3,
                            hole_diameter=12,
                            reference_diameter=step.diameter * 3 - 2 * 12,
                            holes_no=4), step
    ],
    [
        step,
        sol.FlangeWithHoles(height=step.height,
                            diameter=step.diameter * 3,
                            hole_diameter=16,
                            reference_diameter=step.diameter * 3 - 2 * 16,
                            holes_no=6), step
    ],
    [
        step,
        sol.FlangeWithHoles(height=step.height,
                            diameter=step.diameter * 3,
                            hole_diameter=14,
                            reference_diameter=step.diameter * 3 - 2 * 14,
                            holes_no=8), step
    ],
])
step_mod_dec_flange = lambda step: random.choice([
    step,
    sol.ChamferedCylinder(step.height,
                          step.diameter,
                          chamfer_angle=45,
                          chamfer_length=1,
                          chamfer_pos='right'),
    [
        step,
        sol.FlangeWithHoles(height=step.height,
                            diameter=step.diameter * 3,
                            hole_diameter=12,
                            reference_diameter=step.diameter * 3 - 2 * 12,
                            holes_no=4), step
    ],
    [
        step,
        sol.FlangeWithHoles(height=step.height,
                            diameter=step.diameter * 3,
                            hole_diameter=16,
                            reference_diameter=step.diameter * 3 - 2 * 16,
                            holes_no=6), step
    ],
    [
        step,
        sol.FlangeWithHoles(height=step.height,
                            diameter=step.diameter * 3,
                            hole_diameter=14,
                            reference_diameter=step.diameter * 3 - 2 * 14,
                            holes_no=8), step
    ],
])

step_mod_inc_threads = lambda step: random.choice([
    step,
    sol.ChamferedCylinder(
        step.height, step.diameter, chamfer_angle=45, chamfer_length=1),
    sol.Thread(step.height, step.diameter),
])
step_mod_dec_threads = lambda step: random.choice([
    step,
    sol.ChamferedCylinder(step.height,
                          step.diameter,
                          chamfer_angle=45,
                          chamfer_length=1,
                          chamfer_pos='right'),
])

step_mod_inc_chamfer = lambda step: random.choice([
    step,
    sol.ChamferedCylinder(
        step.height, step.diameter, chamfer_angle=45, chamfer_length=1),
])

step_mod_dec_hole_chamfer = lambda step: random.choice([
    step,
    sol.ChamferedHole(
        step.height, step.diameter, chamfer_angle=45, chamfer_length=1.2),
])

step_mod_dec_chamfer = lambda step: random.choice([
    step,
    sol.ChamferedCylinder(step.height,
                          step.diameter,
                          chamfer_angle=45,
                          chamfer_length=1,
                          chamfer_pos='right'),
])

step_mod_inc_gear = lambda step: random.choice([
    step,
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
    step,
    *[[
        sol.Gear(step.height,
                 round(2 * step.diameter / module),
                 module,
                 chamfer_angle=45,
                 chamfer_length=1),
        step,
    ] for module in [2, 3, 4]],
])


def create_random_profile(max_steps_no,
                          min_steps_no=4,
                          initial_diameter=[40,45,50],
                          increase_values=[2, 3, 4, 5],
                          step_lengths=[40,45,50],
                          step_type=sol.Cylinder,
                          step_modificator=lambda step: step):
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

    return sympy.flatten([step_modificator(step) for step in base_geometry])


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

    steps_no={'max':4,'min':1}
    
    shafts = [ create_random_profile(
        4,
        1,
        increase_values=[
            4,
            5,
            6,
        ]) + create_random_profile(
            2,
            1,
            increase_values=[
                -4,
                -5,
                -6,
            ]) for i in range(50)]
    
    
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
        
        steps_no=self.steps_no



        shaft = assumptions

        self._label = None

        
        self._solid_structure = sol.ComposedPart(*assumptions)
        
        if len(assumptions)!=0:
            self._solid_structure = sol.ComposedPart(*assumptions[0])
        
        self._given_data = {
            str(no + 1): val
            for no, val in enumerate(assumptions)
        }

        
        
        self._cached_solution = None

    def get_default_data(self):

        shafts = self.__class__.shafts

        #default_data_dict = {no:step.str_pl()    for no,step  in enumerate(shaft) }
        default_data_dict = {'shaft':shafts }
        

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
    
#     def get_random_parameters(self):

#         parameters_dict = super().get_random_parameters()

#         if parameters_dict['1'] == parameters_dict['2']:
#             #print('lock action')
#             parameters_dict = self.get_random_parameters()

#         return parameters_dict
