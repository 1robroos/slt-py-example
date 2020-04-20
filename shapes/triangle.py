#!/usr/bin/env python

"""
Author: Rob Roos
File: triangle.py
Purpose: Defines a Triangle object, inherited from the abstract class Shape.
Formule Oppervlakte driehoek =  = 1/2 x basis x hoogte  = 1/2*lengthA*height
Formule Omtrek driehoek = lengthA+lengthB+lengthC
Mandatory: lengthA+lengthB+lengthC and height.
"""

from shapes.shape import Shape
"""
- shapes is the package
- shape is the module
- Shape is the class
"""

class Triangle(Shape):
    """
    Represents a Triangle shape, and contains a base value and height value.
    """

    def __init__(self, lengthA, lengthB, lengthC,height):
        self.lengthA = lengthA
        self.lengthB = lengthB
        self.lengthC = lengthC
        self.height = height

    def area(self):
        """
        Compute the area using the formula 1/2*base*height
        """
        return self.lengthA * self.height * 0.5

    def perimeter(self):
        """
        Compute the perimeter using the formula lengthA+lengthB+lengthC
        """
        return (self.lengthA+self.lengthB+self.lengthC)