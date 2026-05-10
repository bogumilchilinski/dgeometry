#import 


from random import random

from cases.models.primitives import *
from cases.models.primitives import Solid


class ChamferedSolid(Solid):
    """
    A solid with chamfered edges.
    
    Parameters:
        height: Length of the solid
        diameter: Diameter of the solid  
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
        self._name = {'en': 'Chamfered Solid', 'pl': 'Bryła z fazą'}


    



class ChamferedCylinder(Solid):
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



# =============================================================================
# Step modificators for profile generation
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
) -> List[Solid]:
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
        List of Solid elements forming the profile
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
# Profile generation utilities
# =============================================================================

def cq_step_mod_inc_chamfer(step: Solid) -> Solid:
    """Modificator that may add chamfer to increasing step."""
    return random.choice([
        copy.copy(step),
        ChamferedCylinder(
            step.height, step.diameter, 
            chamfer_angle=45, chamfer_length=1, chamfer_pos='left'
        ),
    ])


def cq_step_mod_dec_chamfer(step: Solid) -> Solid:
    """Modificator that may add chamfer to decreasing step."""
    return random.choice([
        copy.copy(step),
        ChamferedCylinder(
            step.height, step.diameter,
            chamfer_angle=45, chamfer_length=1, chamfer_pos='right'
        ),
    ])


def cq_step_mod_dec_hole_chamfer(step: Solid) -> Solid:
    """Modificator that may add chamfer to hole."""
    return random.choice([
        copy.copy(step),
        CQChamferedHole(
            step.height, step.diameter,
            chamfer_angle=45, chamfer_length=1.2
        ),
    ])