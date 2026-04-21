"""
CadQuery-based solid elements for 3D modeling.

This module provides solid primitives (Cylinder, ChamferedCylinder, Hole, etc.)
that use CadQuery for proper 3D model generation instead of matplotlib.

The design allows for easy composition of solids and reuse across different
drawing classes.
"""

import sys
import os

# Ensure we import the pip-installed cadquery, not the local folder
_repo_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
_local_cq = os.path.join(_repo_root, 'cadquery')
_original_path = sys.path.copy()
sys.path = [p for p in sys.path if os.path.abspath(p) != _repo_root]

import cadquery as cq

sys.path = _original_path  # Restore original path

from typing import List, Optional, Union, Tuple
from abc import ABC, abstractmethod
import random
import copy


class CQSolid(ABC):
    """
    Abstract base class for all CadQuery-based solid elements.
    
    Each solid knows its height, diameter, and position (origin).
    Solids can be chained together via _ref_elem to create composed parts.
    """
    
    def __init__(self, height: float, diameter: float):
        self.height = height
        self.diameter = diameter
        self._origin: float = 0
        self._ref_elem: Optional['CQSolid'] = None
        self._name = {'en': 'Solid', 'pl': 'Bryła'}
    
    @property
    def origin(self) -> float:
        """Get the origin position, considering reference element if set."""
        if self._ref_elem is not None:
            return self._ref_elem.end
        return self._origin
    
    @property
    def end(self) -> float:
        """Get the end position (origin + height)."""
        return self.origin + self.height
    
    @property
    def radius(self) -> float:
        """Get the radius (diameter / 2)."""
        return self.diameter / 2
    
    @abstractmethod
    def to_cq(self, workplane: Optional[cq.Workplane] = None) -> cq.Workplane:
        """
        Generate CadQuery geometry for this solid.
        
        Args:
            workplane: Optional existing workplane to build upon.
                      If None, creates a new workplane.
        
        Returns:
            CadQuery Workplane with the solid geometry.
        """
        pass
    
    def str_en(self) -> str:
        """English description of the solid."""
        return f"{self._name['en']} L={self.height}mm, D={self.diameter}mm"
    
    def str_pl(self) -> str:
        """Polish description of the solid."""
        return f"{self._name['pl']} L={self.height}mm, D={self.diameter}mm"
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(height={self.height}, diameter={self.diameter})"


class CQCylinder(CQSolid):
    """
    A simple cylinder solid.
    
    Creates a cylinder along the X axis (for shaft-like parts).
    """
    
    def __init__(self, height: float, diameter: float):
        super().__init__(height, diameter)
        self._name = {'en': 'Cylinder', 'pl': 'Walec'}
    
    def to_cq(self, workplane: Optional[cq.Workplane] = None) -> cq.Workplane:
        """Create a cylinder centered on the axis."""
        if workplane is None:
            workplane = cq.Workplane("YZ")
        
        # Create cylinder along X axis, starting at origin
        result = (
            workplane
            .center(0, 0)
            .circle(self.radius)
            .extrude(self.height)
            .translate((self.origin, 0, 0))
        )
        return result


class CQChamferedCylinder(CQSolid):
    """
    A cylinder with chamfered edges.
    
    Parameters:
        height: Length of the cylinder
        diameter: Diameter of the cylinder  
        chamfer_length: Length of the chamfer
        chamfer_angle: Angle of the chamfer (degrees)
        chamfer_pos: 'left', 'right', or 'both'
    """
    
    def __init__(self, height: float, diameter: float, 
                 chamfer_length: float = 1, chamfer_angle: float = 45,
                 chamfer_pos: str = 'left'):
        super().__init__(height, diameter)
        self.chamfer_length = chamfer_length
        self.chamfer_angle = chamfer_angle
        self.chamfer_pos = chamfer_pos
        self._name = {'en': 'Chamfered Cylinder', 'pl': 'Walec z fazą'}
    
    def to_cq(self, workplane: Optional[cq.Workplane] = None) -> cq.Workplane:
        """Create a chamfered cylinder."""
        if workplane is None:
            workplane = cq.Workplane("YZ")
        
        # Create base cylinder
        result = (
            workplane
            .center(0, 0)
            .circle(self.radius)
            .extrude(self.height)
            .translate((self.origin, 0, 0))
        )
        
        # Apply chamfers based on position
        try:
            if self.chamfer_pos in ('left', 'both'):
                result = result.faces("<X").chamfer(self.chamfer_length)
            if self.chamfer_pos in ('right', 'both'):
                result = result.faces(">X").chamfer(self.chamfer_length)
        except Exception:
            # Chamfer may fail if geometry doesn't allow it
            pass
            
        return result
    
    def str_en(self) -> str:
        return f"Chamfered Cylinder L={self.height}mm, D={self.diameter}mm, chamfer {self.chamfer_length}x{self.chamfer_angle}° ({self.chamfer_pos})"
    
    def str_pl(self) -> str:
        pos_pl = {'left': 'lewa', 'right': 'prawa', 'both': 'obie'}
        return f"Walec z fazą L={self.height}mm, D={self.diameter}mm, faza {self.chamfer_length}x{self.chamfer_angle}° ({pos_pl.get(self.chamfer_pos, self.chamfer_pos)})"


class CQThread(CQSolid):
    """
    A threaded cylinder section.
    
    Visually represented as a cylinder (threads are not geometrically modeled).
    """
    
    def __init__(self, height: float, diameter: float,
                 chamfer_length: float = 1, chamfer_angle: float = 45,
                 thread: str = 'M'):
        super().__init__(height, diameter)
        self.chamfer_length = chamfer_length
        self.chamfer_angle = chamfer_angle
        self.thread = thread
        self._name = {'en': 'Thread', 'pl': 'Gwint'}
    
    def to_cq(self, workplane: Optional[cq.Workplane] = None) -> cq.Workplane:
        """Create thread representation (simplified as cylinder)."""
        if workplane is None:
            workplane = cq.Workplane("YZ")
        
        result = (
            workplane
            .center(0, 0)
            .circle(self.radius)
            .extrude(self.height)
            .translate((self.origin, 0, 0))
        )
        
        # Add chamfer on left side
        try:
            result = result.faces("<X").chamfer(self.chamfer_length)
        except Exception:
            pass
            
        return result
    
    def str_en(self) -> str:
        return f"Thread {self.thread}{self.diameter} L={self.height}mm"
    
    def str_pl(self) -> str:
        return f"Gwint {self.thread}{self.diameter} L={self.height}mm"


class CQHole(CQSolid):
    """
    A hole (negative cylinder) to be subtracted from other solids.
    """
    
    def __init__(self, height: float, diameter: float):
        super().__init__(height, diameter)
        self._name = {'en': 'Hole', 'pl': 'Otwór'}
        self._is_hole = True
    
    def to_cq(self, workplane: Optional[cq.Workplane] = None) -> cq.Workplane:
        """Create a hole (cylinder to be subtracted)."""
        if workplane is None:
            workplane = cq.Workplane("YZ")
        
        result = (
            workplane
            .center(0, 0)
            .circle(self.radius)
            .extrude(self.height)
            .translate((self.origin, 0, 0))
        )
        return result


class CQChamferedHole(CQHole):
    """
    A hole with chamfered edges.
    """
    
    def __init__(self, height: float, diameter: float,
                 chamfer_length: float = 1.2, chamfer_angle: float = 45,
                 chamfer_pos: str = 'left'):
        super().__init__(height, diameter)
        self.chamfer_length = chamfer_length
        self.chamfer_angle = chamfer_angle
        self.chamfer_pos = chamfer_pos
        self._name = {'en': 'Chamfered Hole', 'pl': 'Otwór z fazą'}
    
    def to_cq(self, workplane: Optional[cq.Workplane] = None) -> cq.Workplane:
        """Create a chamfered hole."""
        if workplane is None:
            workplane = cq.Workplane("YZ")
        
        result = (
            workplane
            .center(0, 0)
            .circle(self.radius)
            .extrude(self.height)
            .translate((self.origin, 0, 0))
        )
        
        # Chamfer the appropriate face
        try:
            if self.chamfer_pos in ('left', 'both'):
                result = result.faces("<X").chamfer(self.chamfer_length)
            if self.chamfer_pos in ('right', 'both'):
                result = result.faces(">X").chamfer(self.chamfer_length)
        except Exception:
            pass
            
        return result


class CQOpenHole(CQHole):
    """
    An open hole (through hole) - negative cylinder.
    """
    
    def __init__(self, height: float, diameter: float):
        super().__init__(height, diameter)
        self._name = {'en': 'Open Hole', 'pl': 'Otwór przelotowy'}


class CQThreadedOpenHole(CQOpenHole):
    """
    A threaded open hole.
    """
    
    def __init__(self, height: float, diameter: float):
        super().__init__(height, diameter)
        self._name = {'en': 'Threaded Hole', 'pl': 'Otwór gwintowany'}


class CQComposedPart:
    """
    A composed part made of multiple solid elements.
    
    Handles combining positive solids and subtracting holes to create
    the final 3D model.
    """
    
    def __init__(self, *elements: CQSolid):
        self.elements: List[CQSolid] = list(elements) if elements else []
    
    def add(self, element: CQSolid) -> 'CQComposedPart':
        """Add an element to the composed part."""
        new_elements = list(self.elements)
        new_elements.append(element)
        return CQComposedPart(*new_elements)
    
    def __add__(self, other: CQSolid) -> 'CQComposedPart':
        return self.add(other)
    
    def to_cq(self) -> cq.Workplane:
        """
        Generate the complete CadQuery model.
        
        Combines all positive solids and subtracts all holes.
        """
        if not self.elements:
            return cq.Workplane("YZ")
        
        # Separate positive solids from holes
        positive_solids = []
        holes = []
        
        for elem in self.elements:
            if hasattr(elem, '_is_hole') and elem._is_hole:
                holes.append(elem)
            else:
                positive_solids.append(elem)
        
        # Build the positive geometry
        if not positive_solids:
            return cq.Workplane("YZ")
        
        # Start with the first solid
        result = positive_solids[0].to_cq()
        
        # Union with remaining positive solids
        for solid in positive_solids[1:]:
            solid_cq = solid.to_cq()
            result = result.union(solid_cq)
        
        # Subtract all holes
        for hole in holes:
            hole_cq = hole.to_cq()
            result = result.cut(hole_cq)
        
        return result
    
    def export_step(self, filename: str) -> None:
        """Export the model to a STEP file."""
        model = self.to_cq()
        model.val().exportStep(filename)
    
    def export_stl(self, filename: str, tolerance: float = 0.1) -> None:
        """Export the model to an STL file."""
        model = self.to_cq()
        model.val().exportStl(filename, tolerance)
    
    @property
    def total_length(self) -> float:
        """Calculate the total length of the composed part."""
        if not self.elements:
            return 0
        
        # Find max end position among non-hole elements
        positive_ends = [
            elem.end for elem in self.elements 
            if not (hasattr(elem, '_is_hole') and elem._is_hole)
        ]
        return max(positive_ends) if positive_ends else 0


# =============================================================================
# Profile generation utilities
# =============================================================================

def create_cq_random_profile(
    max_steps_no: int,
    min_steps_no: int = 1,
    initial_diameter: List[int] = None,
    increase_values: List[int] = None,
    step_lengths: List[int] = None,
    step_type: type = CQCylinder,
    step_modificator=None,
    origin: float = 0
) -> List[CQSolid]:
    """
    Create a random stepped profile for shaft-like parts.
    
    Args:
        max_steps_no: Maximum number of steps
        min_steps_no: Minimum number of steps
        initial_diameter: List of possible initial diameters
        increase_values: List of diameter increase values between steps
        step_lengths: List of possible step lengths
        step_type: Type of solid to use for each step
        step_modificator: Optional function to modify each step
        origin: Starting position
    
    Returns:
        List of CQSolid elements forming the profile
    """
    if initial_diameter is None:
        initial_diameter = [50, 55, 60, 65]
    if increase_values is None:
        increase_values = [2, 3, 4, 5]
    if step_lengths is None:
        step_lengths = [50, 55, 60]
    if step_modificator is None:
        step_modificator = lambda step: step
    
    steps_no = random.randint(min_steps_no, max_steps_no)
    
    first_d = random.choice(initial_diameter)
    
    profile_changes = [
        random.choice(increase_values) for _ in range(steps_no)
    ]
    
    profile = [first_d] + [
        first_d + sum(profile_changes[0:step_no + 1])
        for step_no in range(len(profile_changes))
    ]
    
    base_geometry = [
        step_type(random.choice(step_lengths), diameter)
        for diameter in profile
    ]
    
    # Apply modificator and flatten
    steps_list = []
    for step in base_geometry:
        modified = step_modificator(step)
        if isinstance(modified, list):
            steps_list.extend(modified)
        else:
            steps_list.append(modified)
    
    # Set up origin chain
    if steps_list:
        steps_list[0]._origin = origin
        steps_list[0]._ref_elem = None
        
        for no in range(1, len(steps_list)):
            steps_list[no]._ref_elem = steps_list[no - 1]
    
    return steps_list


# =============================================================================
# Step modificators for profile generation
# =============================================================================

def cq_step_mod_inc_chamfer(step: CQSolid) -> CQSolid:
    """Modificator that may add chamfer to increasing step."""
    return random.choice([
        copy.copy(step),
        CQChamferedCylinder(
            step.height, step.diameter, 
            chamfer_angle=45, chamfer_length=1, chamfer_pos='left'
        ),
    ])


def cq_step_mod_dec_chamfer(step: CQSolid) -> CQSolid:
    """Modificator that may add chamfer to decreasing step."""
    return random.choice([
        copy.copy(step),
        CQChamferedCylinder(
            step.height, step.diameter,
            chamfer_angle=45, chamfer_length=1, chamfer_pos='right'
        ),
    ])


def cq_step_mod_dec_hole_chamfer(step: CQSolid) -> CQSolid:
    """Modificator that may add chamfer to hole."""
    return random.choice([
        copy.copy(step),
        CQChamferedHole(
            step.height, step.diameter,
            chamfer_angle=45, chamfer_length=1.2
        ),
    ])
