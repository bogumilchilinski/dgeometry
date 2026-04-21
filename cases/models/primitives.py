"""
Geometric tree structure with Node and Endpoint abstractions.
Supports compositing of Solid and Primitive geometric objects.
"""

from abc import ABC, abstractmethod
from typing import List, Union, Optional, Dict, Any




class Primitive:
    """
    Represents a primitive geometric object (basic geometric element).
    Acts as a leaf node in the geometric tree.
    
    Primitive cannot have children - it is a terminal element.
    
    Examples
    --------
    >>> cube = Primitive(name="Cube", shape_type="box", dimensions=(10, 10, 10))
    >>> sphere = Primitive(name="Sphere", shape_type="sphere", radius=5)
    """
    
    def __init__(
        self,
        name: str,
        shape_type: str,
        properties: Optional[Dict[str, Any]] = None
    ):
        """
        Initialize a Primitive geometric object.
        
        Parameters
        ----------
        name : str
            Name/identifier of the primitive
        shape_type : str
            Type of shape ('box', 'sphere', 'cylinder', etc.)
        properties : dict, optional
            Shape-specific properties (dimensions, radius, etc.)
        """
        self._name = name
        self._shape_type = shape_type
        self._properties = properties or {}
        self._parent: Optional['Solid'] = None
    
    def add_child(self, child: 'Node') -> None:
        """Primitive cannot have children."""
        raise TypeError(f"Primitive '{self._name}' cannot have children")
    
    def remove_child(self, child: 'Node') -> None:
        """Primitive has no children."""
        raise TypeError(f"Primitive '{self._name}' has no children")
    
    def get_children(self) -> List['Node']:
        """Return empty list - Primitive has no children."""
        return []
    
    def is_leaf(self) -> bool:
        """Primitive is always a leaf."""
        return True
    
    def get_type(self) -> NodeType:
        """Return PRIMITIVE type."""
        return NodeType.PRIMITIVE
    
    def get_bounds(self) -> Dict[str, Any]:
        """Return bounds of primitive based on shape type."""
        return {
            'name': self._name,
            'shape_type': self._shape_type,
            **self._properties
        }
    
    def get_volume(self) -> float:
        """Calculate volume of primitive."""
        # Implementation depends on shape_type
        if self._shape_type == 'box':
            dims = self._properties.get('dimensions', (1, 1, 1))
            return dims[0] * dims[1] * dims[2]
        elif self._shape_type == 'sphere':
            radius = self._properties.get('radius', 1)
            return (4/3) * 3.14159 * (radius ** 3)
        return 0.0
    
    def get_name(self) -> str:
        """Return name of primitive."""
        return self._name
    
    def set_parent(self, parent: Optional['Solid']) -> None:
        """Set parent Solid."""
        self._parent = parent
    
    def __repr__(self) -> str:
        return f"Primitive(name='{self._name}', type='{self._shape_type}')"


class Solid(Primitive):
    """
    Represents a composite geometric object that can contain Primitives and other Solids.
    Acts as a composite node in the geometric tree.
    
    A Solid is a container for geometric elements, enabling hierarchical composition.
    It can contain:
    - Primitive objects (basic geometric elements)
    - Other Solid objects (nested compositions)
    
    Examples
    --------
    >>> assembly = Solid(name="Assembly")
    >>> cube = Primitive(name="Cube", shape_type="box", dimensions=(10, 10, 10))
    >>> sphere = Primitive(name="Sphere", shape_type="sphere", radius=5)
    >>> assembly.add_child(cube)
    >>> assembly.add_child(sphere)
    
    >>> # Nested composition
    >>> sub_assembly = Solid(name="SubAssembly")
    >>> sub_assembly.add_child(Primitive(name="Cylinder", shape_type="cylinder"))
    >>> assembly.add_child(sub_assembly)
    """
    
    def __init__(self, name: str, properties: Optional[Dict[str, Any]] = None):
        """
        Initialize a Solid (composite) object.
        
        Parameters
        ----------
        name : str
            Name/identifier of the solid
        properties : dict, optional
            Additional properties
        """
        self._name = name
        self._properties = properties or {}
        self._children: List[Node] = []
        self._parent: Optional['Solid'] = None
    
    def add_child(self, child: Node) -> None:
        """
        Add a child node (Primitive or Solid).
        
        Parameters
        ----------
        child : Node
            Child node to add (Primitive or Solid)
        
        Raises
        ------
        TypeError
            If child is not a valid Node type
        """
        if not isinstance(child, Node):
            raise TypeError(f"Child must be a Node, got {type(child)}")
        
        if child not in self._children:
            self._children.append(child)
            if isinstance(child, (Primitive, Solid)):
                child.set_parent(self)
    
    def remove_child(self, child: Node) -> None:
        """
        Remove a child node.
        
        Parameters
        ----------
        child : Node
            Child node to remove
        """
        if child in self._children:
            self._children.remove(child)
            if isinstance(child, (Primitive, Solid)):
                child.set_parent(None)
    
    def get_children(self) -> List[Node]:
        """Return list of direct children."""
        return self._children.copy()
    
    def get_all_descendants(self) -> List[Node]:
        """Return all descendants (recursive)."""
        descendants = list(self._children)
        for child in self._children:
            if isinstance(child, Solid):
                descendants.extend(child.get_all_descendants())
        return descendants
    
    def is_leaf(self) -> bool:
        """Solid is a leaf only if it has no children."""
        return len(self._children) == 0
    
    def get_type(self) -> NodeType:
        """Return SOLID type."""
        return NodeType.SOLID
    
    def get_bounds(self) -> Dict[str, Any]:
        """
        Return aggregated bounds from all children.
        """
        children_bounds = [child.get_bounds() for child in self._children] if hasattr(self._children[0] if self._children else None, 'get_bounds') else []
        return {
            'name': self._name,
            'num_children': len(self._children),
            'children_bounds': children_bounds,
            **self._properties
        }
    
    def get_volume(self) -> float:
        """
        Calculate total volume of all contained elements.
        """
        total_volume = 0.0
        for child in self._children:
            if hasattr(child, 'get_volume'):
                total_volume += child.get_volume()
        return total_volume
    
    def get_name(self) -> str:
        """Return name of solid."""
        return self._name
    
    def set_parent(self, parent: Optional['Solid']) -> None:
        """Set parent Solid."""
        self._parent = parent
    
    def get_parent(self) -> Optional['Solid']:
        """Get parent Solid."""
        return self._parent
    
    def __repr__(self) -> str:
        return f"Solid(name='{self._name}', children={len(self._children)})"