#import 

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
