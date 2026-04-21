"""
CadQuery-based drawing classes for 3D modeling.

This module provides sketch classes (SimpleShaftSketchCQ, SimpleSleeveSketchCQ)
that use CadQuery for proper 3D model generation. The 2D preview still uses
matplotlib for compatibility, while 3D models are generated using CadQuery.

Usage:
    sketch = SimpleShaftSketchCQ.from_random_data()
    sketch.preview()           # Shows matplotlib 2D preview  
    sketch.export_step("model.step")  # Exports CadQuery 3D model
    sketch.show_3d()           # Interactive 3D view (requires jupyter-cadquery or similar)
"""

from typing import List, Optional, Dict, Any
import numpy as np
import copy
import random
import base64
import gc
import os

import matplotlib.pyplot as plt
import IPython as IP

# Import cq from cq_solids which handles the path correctly
from . import cq_solids as cqs
from .cq_solids import cq

from ..dgeometry import GeometryScene, GeometricalCase, plots_no


class CQShaftSketchBase(GeometricalCase):
    """
    Base class for CadQuery-based shaft sketches.
    
    Provides common functionality for generating and previewing shaft-like parts
    with both matplotlib 2D visualization and CadQuery 3D models.
    """
    
    _case_no = plots_no()
    scheme_name = 'absxyz'
    real_name = 'abs'
    
    # Configuration for profile generation - override in subclasses
    steps_no = {'max': 3, 'min': 1}
    holes_no = {'max': 3, 'min': 2}
    
    # Class-level cache for generated structures
    _cached_structures: Optional[List] = None
    
    @classmethod
    def _reset_cache(cls):
        """Reset the cached structures."""
        cls._cached_structures = None
    
    @classmethod
    def _solids(cls) -> List:
        """Get or generate the list of possible shaft configurations."""
        if cls._cached_structures is None:
            cls._cached_structures = cls._structure_generator()
        return cls._cached_structures
    
    @classmethod
    def _structure_generator(cls) -> List:
        """
        Generate random shaft structures.
        
        Override this method in subclasses to customize the geometry generation.
        """
        steps = cls.steps_no
        
        shafts = []
        for _ in range(50):
            # Create increasing profile (left side)
            shaft = cqs.create_cq_random_profile(
                steps['max'], steps['min'],
                increase_values=[4, 5, 6],
                step_modificator=cqs.cq_step_mod_inc_chamfer,
                origin=0
            )
            
            if shaft:
                d_end = shaft[-1].diameter
                
                # Create decreasing profile (right side)
                shaft += cqs.create_cq_random_profile(
                    steps['max'], steps['min'],
                    initial_diameter=[d_end + 8, d_end + 10],
                    increase_values=[-4, -5, -6],
                    step_modificator=cqs.cq_step_mod_dec_chamfer,
                    origin=shaft[-1].end
                )
            
            shafts.append(shaft)
        
        return shafts
    
    @classmethod
    def from_random_data(cls) -> 'CQShaftSketchBase':
        """Create an instance with randomly generated data."""
        new_obj = cls()
        data_set = new_obj.get_random_parameters()
        entities = [elem for label, elem in data_set.items()]
        return cls(*entities)
    
    def __init__(self, *assumptions, **kwargs):
        super().__init__()
        self._solution_step = []
        self._solution3d_step = []
        self._label = None
        self._path = None
        self._cached_solution = None
        
        # Store the shaft elements
        self._solid_structure = cqs.CQComposedPart()
        
        if len(assumptions) != 0:
            if isinstance(assumptions[0], list):
                self._solid_structure = cqs.CQComposedPart(*assumptions[0])
            else:
                self._solid_structure = cqs.CQComposedPart(*assumptions)
        
        self._given_data = {
            str(no + 1): val
            for no, val in enumerate(assumptions)
        }
    
    def get_default_data(self) -> Dict[str, Any]:
        """Get default data dictionary for random generation."""
        shafts = self._solids()
        return {'shaft': shafts}
    
    def subs(self, *args, **kwargs) -> 'CQShaftSketchBase':
        """Substitute data with new values."""
        if len(args) > 0 and isinstance(args[0], dict):
            data_set = args[0]
            entities = [point for label, point in data_set.items()]
            new_obj = self.__class__(*entities)
            new_obj._given_data = args[0]
        else:
            new_obj = copy.deepcopy(self)
        return new_obj
    
    def _scheme(self) -> str:
        """Get path to scheme image."""
        if self._path is None:
            self.preview()
        return self._path
    
    def _real_example(self) -> str:
        """Get path to real example image."""
        if self._path is None:
            self.preview()
        return self._path
    
    def _scheme_pl(self) -> str:
        """Get path to Polish scheme image."""
        if self._path is None:
            self.preview(language='pl')
        return self._path
    
    def preview(self, example: bool = False, language: str = 'en'):
        """
        Generate and display 2D preview using matplotlib.
        
        Args:
            example: Whether this is an example preview
            language: Language for labels ('en' or 'pl')
        
        Returns:
            IPython Image object for display
        """
        GeometryScene(30, 60, figsize=(14, 7))
        
        # Draw 2D representation using matplotlib
        self._plot_2d(language=language)
        
        # Generate file path
        images_dir = os.path.dirname(__file__).replace('cases', 'images')
        os.makedirs(images_dir, exist_ok=True)
        path = os.path.join(
            images_dir,
            f"{self.__class__.__name__}{next(self.__class__._case_no)}.png"
        )
        
        plt.savefig(path)
        
        # Clean up matplotlib
        plt.cla()
        plt.clf()
        plt.close('all')
        gc.collect()
        
        self._path = path
        
        # Return displayable image
        with open(path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        
        return IP.display.Image(base64.b64decode(encoded_string))
    
    def _plot_2d(self, language: str = 'en'):
        """
        Plot 2D representation of the shaft using matplotlib.
        
        Creates a cross-section view showing all elements.
        """
        ax = GeometryScene.ax_2d
        
        if not self._solid_structure.elements:
            return
        
        for elem in self._solid_structure.elements:
            self._draw_element_2d(ax, elem, language)
        
        # Draw center axis
        if self._solid_structure.elements:
            total_length = self._solid_structure.total_length / 10
            ax.plot([-0.5, total_length + 0.5], [0, 0], '-.', color='k', linewidth=1)
    
    def _draw_element_2d(self, ax, elem: cqs.CQSolid, language: str = 'en'):
        """Draw a single element in 2D."""
        r = elem.diameter / 2 / 10  # Scale for display
        l = elem.height / 10
        origin = elem.origin / 10
        
        # Determine if this is a hole
        is_hole = hasattr(elem, '_is_hole') and elem._is_hole
        
        if is_hole:
            # Draw hole as dashed lines
            ax.plot(
                [origin, origin, origin + l, origin + l],
                [r, r, r, r],
                '--', color='k', linewidth=1
            )
            ax.plot(
                [origin, origin, origin + l, origin + l],
                [-r, -r, -r, -r],
                '--', color='k', linewidth=1
            )
        else:
            # Draw solid outline
            ax.plot(
                [origin, origin, origin + l, origin + l, origin],
                [-r, r, r, -r, -r],
                '-', color='k', linewidth=1.5
            )
        
        # Add label
        label = elem.str_pl() if language == 'pl' else elem.str_en()
        t_l = origin + l / 2
        t_r = r + 2 if not is_hole else -r - 4
        ax.text(t_l, t_r, label, rotation='vertical', 
                multialignment='center', fontsize=8)
    
    # =========================================================================
    # CadQuery 3D Model Methods
    # =========================================================================
    
    def to_cq(self) -> cq.Workplane:
        """
        Generate the CadQuery 3D model.
        
        Returns:
            CadQuery Workplane containing the 3D model
        """
        return self._solid_structure.to_cq()
    
    def export_step(self, filename: str) -> None:
        """
        Export the 3D model to a STEP file.
        
        Args:
            filename: Path to the output STEP file
        """
        self._solid_structure.export_step(filename)
    
    def export_stl(self, filename: str, tolerance: float = 0.1) -> None:
        """
        Export the 3D model to an STL file.
        
        Args:
            filename: Path to the output STL file
            tolerance: Mesh tolerance (smaller = finer mesh)
        """
        self._solid_structure.export_stl(filename, tolerance)
    
    def show_3d(self):
        """
        Show interactive 3D view.
        
        Requires jupyter-cadquery or CQ-editor for visualization.
        Returns the CadQuery model for display in compatible environments.
        """
        return self.to_cq()
    
    def get_cq_assembly(self) -> cq.Assembly:
        """
        Get the model as a CadQuery Assembly.
        
        Useful for more complex visualization and export options.
        """
        assy = cq.Assembly()
        model = self.to_cq()
        assy.add(model, name=self.__class__.__name__)
        return assy


class SimpleShaftSketchCQ(CQShaftSketchBase):
    """
    Simple shaft sketch using CadQuery for 3D modeling.
    
    Creates a shaft with minimal stepped profile (0-1 steps on each side).
    
    Example:
        >>> sketch = SimpleShaftSketchCQ.from_random_data()
        >>> sketch.preview()  # 2D matplotlib preview
        >>> sketch.export_step("shaft.step")  # Export 3D model
    """
    
    steps_no = {'max': 1, 'min': 0}
    _cached_structures = None
    
    @classmethod
    def _structure_generator(cls) -> List:
        """Generate simple shaft structures with minimal steps."""
        steps = cls.steps_no
        
        shafts = []
        for _ in range(50):
            # Create simple increasing profile
            shaft = cqs.create_cq_random_profile(
                steps['max'], steps['min'],
                initial_diameter=[50, 55, 60, 65],
                increase_values=[4, 5, 6],
                step_lengths=[50, 55, 60],
                step_modificator=cqs.cq_step_mod_inc_chamfer,
                origin=0
            )
            
            if shaft:
                d_end = shaft[-1].diameter
                
                # Create simple decreasing profile
                shaft += cqs.create_cq_random_profile(
                    steps['max'], steps['min'],
                    initial_diameter=[d_end + 8, d_end + 10],
                    increase_values=[-4, -5, -6],
                    step_lengths=[50, 55, 60],
                    step_modificator=cqs.cq_step_mod_dec_chamfer,
                    origin=shaft[-1].end
                )
            
            shafts.append(shaft)
        
        return shafts


class SimpleSleeveSketchCQ(CQShaftSketchBase):
    """
    Simple sleeve sketch (shaft with central hole) using CadQuery for 3D modeling.
    
    Creates a sleeve with stepped outer profile and internal bore.
    
    Example:
        >>> sketch = SimpleSleeveSketchCQ.from_random_data()
        >>> sketch.preview()  # 2D matplotlib preview
        >>> sketch.export_step("sleeve.step")  # Export 3D model
    """
    
    steps_no = {'max': 2, 'min': 0}
    holes_no = {'max': 2, 'min': 1}
    _cached_structures = None
    
    @classmethod
    def _structure_generator(cls) -> List:
        """Generate sleeve structures with central holes."""
        steps = cls.steps_no
        holes = cls.holes_no
        
        shafts = []
        for _ in range(50):
            # Create outer profile - increasing side
            shaft = cqs.create_cq_random_profile(
                steps['max'], steps['min'],
                initial_diameter=[50, 55, 60, 65],
                increase_values=[4, 5, 6],
                step_lengths=[50, 55, 60],
                step_modificator=cqs.cq_step_mod_inc_chamfer,
                origin=0
            )
            
            if shaft:
                d_end = shaft[-1].diameter
                d_height = shaft[-1].height
                
                # Create outer profile - decreasing side
                right_profile = cqs.create_cq_random_profile(
                    steps['max'], steps['min'],
                    initial_diameter=[d_end + 8, d_end + 10],
                    increase_values=[-4, -5, -6],
                    step_lengths=[50, 55, 60],
                    step_modificator=cqs.cq_step_mod_dec_chamfer,
                    origin=shaft[-1].end
                )
                shaft += right_profile
                
                # Calculate total length for hole
                total_length = right_profile[-1].end if right_profile else shaft[-1].end
                
                # Create internal hole profile
                hole_profile = cqs.create_cq_random_profile(
                    holes['max'], holes['min'],
                    initial_diameter=[25, 30],
                    increase_values=[-2, -3, -4],
                    step_lengths=[round(total_length / 3)],
                    step_type=cqs.CQHole,
                    step_modificator=cqs.cq_step_mod_dec_hole_chamfer,
                    origin=0
                )
                shaft += hole_profile
                
                # Add through hole for remaining length
                if hole_profile:
                    remaining_length = total_length - hole_profile[-1].end
                    if remaining_length > 0:
                        open_hole = cqs.CQOpenHole(
                            remaining_length, 
                            hole_profile[-1].diameter + 5
                        )
                        open_hole._origin = hole_profile[-1].end
                        shaft.append(open_hole)
            
            shafts.append(shaft)
        
        return shafts


# =============================================================================
# Utility functions for working with CQ sketches
# =============================================================================

def export_sketch_to_step(sketch: CQShaftSketchBase, filename: str) -> None:
    """
    Export a sketch to STEP format.
    
    Args:
        sketch: The sketch instance to export
        filename: Output filename
    """
    sketch.export_step(filename)


def export_sketch_to_stl(sketch: CQShaftSketchBase, filename: str, 
                         tolerance: float = 0.1) -> None:
    """
    Export a sketch to STL format.
    
    Args:
        sketch: The sketch instance to export
        filename: Output filename
        tolerance: Mesh tolerance
    """
    sketch.export_stl(filename, tolerance)


def batch_generate_models(sketch_class: type, count: int = 10, 
                          output_dir: str = "./models") -> List[str]:
    """
    Generate multiple random models and export them.
    
    Args:
        sketch_class: The sketch class to instantiate
        count: Number of models to generate
        output_dir: Directory for output files
    
    Returns:
        List of generated file paths
    """
    import os
    os.makedirs(output_dir, exist_ok=True)
    
    paths = []
    for i in range(count):
        sketch = sketch_class.from_random_data()
        filename = os.path.join(output_dir, f"{sketch_class.__name__}_{i:03d}.step")
        sketch.export_step(filename)
        paths.append(filename)
    
    return paths
