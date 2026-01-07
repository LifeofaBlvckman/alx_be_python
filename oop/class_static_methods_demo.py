"""Demonstrate class methods and static methods"""

class Calculator:
    """Calculator class demonstrating static and class methods"""
    
    # Class attribute
    calculation_type = "Arithmetic Operations"
    
    @staticmethod
    def add(a: float, b: float) -> float:
        """Static method to add two numbers
        
        Args:
            a (float): First number
            b (float): Second number
            
        Returns:
            float: Sum of a and b
        """
        return a + b
    
    @classmethod
    def multiply(cls, a: float, b: float) -> float:
        """Class method to multiply two numbers
        
        Prints the calculation type from class attribute before multiplying
        
        Args:
            cls: Reference to the class
            a (float): First number
            b (float): Second number
            
        Returns:
            float: Product of a and b
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
