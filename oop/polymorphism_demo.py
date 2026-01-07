"""Demonstrate polymorphism through method overriding"""

import math


class Shape:
    """Base class representing a geometric shape"""
    
    def area(self) -> float:
        """Calculate the area of the shape
        
        This method should be overridden by derived classes
        
        Raises:
            NotImplementedError: If not overridden by subclass
        """
        raise NotImplementedError("Subclasses must implement area() method")


class Rectangle(Shape):
    """Derived class representing a rectangle"""
    
    def __init__(self, length: float, width: float):
        """Initialize a rectangle with length and width
        
        Args:
            length (float): The length of the rectangle
            width (float): The width of the rectangle
        """
        self.length = length
        self.width = width
    
    def area(self) -> float:
        """Calculate the area of the rectangle
        
        Overrides the area() method from Shape class
        
        Returns:
            float: Area of the rectangle (length × width)
        """
        return self.length * self.width


class Circle(Shape):
    """Derived class representing a circle"""
    
    def __init__(self, radius: float):
        """Initialize a circle with radius
        
        Args:
            radius (float): The radius of the circle
        """
        self.radius = radius
    
    def area(self) -> float:
        """Calculate the area of the circle
        
        Overrides the area() method from Shape class
        
        Returns:
            float: Area of the circle (π × radius²)
        """
        return math.pi * (self.radius ** 2)
