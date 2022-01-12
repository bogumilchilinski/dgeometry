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


class DrawingSheets(GeometricalCase):

    _case_no = plots_no()
    scheme_name = 'absxyz'
    real_name = 'abs'

    paper_size_dict={'A4':(210,297),'A3':(420,297),'A2':(594,420),'A1':(841,594),'A0':(1189,841)  }

    borders_extented={'left':20,'right':10,'top':10,'bottom':10,}

    drawing_area_dict={'A4':(190,277),'A3':(400,277),'A2':(574,400),'A1':(821,574),'A0':(1169,821)  }
    
    


    @classmethod
    def from_random_data(cls):
        new_obj = cls()
        data_set=new_obj.get_random_parameters()
        print(data_set)
        entities = [elem  for label,elem in data_set.items()]
        print(entities)
        return cls(*entities)

    def __init__(self,*assumptions,**kwargs):
        super().__init__()
        self._solution_step=[]
        self._solution3d_step=[]
        
        
        self._label = None


        
        self._given_data={str(no+1):val   for no,val in enumerate(assumptions)}
        

        
        self._cached_solution=None
        

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
        
        width,height = papers[self._ref_paper]
        
        return width*height

    @property
    def extra_paper_area(self):
        
        papers = self.__class__.paper_size_dict
        
        width,height = papers[self._extra_paper]
        
        return width*height
    
    
    @property
    def paper_drawing_area_size(self):
        
        papers = self.__class__.drawing_area_dict
        
        return papers[self._ref_paper]

    @property
    def extra_paper_drawing_area_size(self):
        
        papers = self.__class__.drawing_area_dict
        
        return papers[self._extra_paper]    
    
    
    def solution(self,solved_case=None):

        if self._cached_solution is None:
        
            new_obj = copy.deepcopy(self)
            self._cached_solution=new_obj
            
        else:
            new_obj = self._cached_solution

        return new_obj

    

    
    
    def get_default_data(self):
        
        papers = self.__class__.paper_size_dict
        
        default_data_dict={
            '1':list(papers.keys()),
            '2':list(papers.keys()),
            
        }

        return default_data_dict

    def get_random_parameters(self):

        parameters_dict = super().get_random_parameters()

        if parameters_dict['1']==parameters_dict['2']:
            #print('lock action')
            parameters_dict = self.get_random_parameters()


        return parameters_dict
    
    def subs(self,*args,**kwargs):
        if len(args)>0 and isinstance(args[0],dict):
            data_set=args[0]
            entities = [point  for label,point in data_set.items()]

            new_obj=self.__class__(*entities)
            new_obj._given_data=args[0]

        else:
            new_obj = copy.deepcopy(self)
            #new_obj._cached_solution=None
            
        return new_obj
    
class CubeDrawing(DrawingSheets):
    
    cube_sizes=[50,75,100,125,150]
    
    def get_default_data(self):
        
        papers = self.__class__.paper_size_dict
        cube_side = self.__class__.cube_sizes
        
        default_data_dict={
            '1':list(papers.keys()),
            '2':list(papers.keys()),
            'a':cube_side,
            
        }

        return default_data_dict