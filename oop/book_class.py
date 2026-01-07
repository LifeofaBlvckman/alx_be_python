#!/usr/bin/python3
"""Book class implementation with magic methods"""


class Book:
    """A class to represent a book with magic methods"""
    
    def __init__(self, title: str, author: str, year: int):
        """Constructor to initialize Book instance
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            year (int): The publication year of the book
        """
        self.title = title
        self.author = author
        self.year = year
    
    def __str__(self):
        """Returns a user-friendly string representation
        
        Returns:
            str: String in format "(title) by (author), published in (year)"
        """
        return f"{self.title} by {self.author}, published in {self.year}"
    
    def __repr__(self):
        """Returns an official string representation that can recreate the object
        
        Returns:
            str: String that looks like a constructor call
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"
    
    def __del__(self):
        """Destructor that prints a message when object is deleted"""
        print(f"Deleting {self.title}")
