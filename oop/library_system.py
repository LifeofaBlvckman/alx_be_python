"""Library system with inheritance and composition"""

class Book:
    """Base class representing a book"""
    
    def __init__(self, title: str, author: str):
        """Initialize a Book with title and author
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
        """
        self.title = title
        self.author = author


class EBook(Book):
    """Derived class representing an electronic book"""
    
    def __init__(self, title: str, author: str, file_size: int):
        """Initialize an EBook with title, author, and file size
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            file_size (int): The file size in KB
        """
        # Call the parent class constructor
        super().__init__(title, author)
        self.file_size = file_size


class PrintBook(Book):
    """Derived class representing a printed book"""
    
    def __init__(self, title: str, author: str, page_count: int):
        """Initialize a PrintBook with title, author, and page count
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            page_count (int): The number of pages
        """
        # Call the parent class constructor
        super().__init__(title, author)
        self.page_count = page_count

class Library:
    """Class representing a library that manages books (composition)"""
    
    def __init__(self):
        """Initialize an empty library"""
        self.books = []  # This is composition - Library "has" books
    
    def add_book(self, book):
        """Add a book to the library
        
        Args:
            book: Can be Book, EBook, or PrintBook instance
        """
        self.books.append(book)
    
    def list_books(self):
        """Print all books in the library with their details"""
        for book in self.books:
            if isinstance(book, EBook):
                print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB")
            elif isinstance(book, PrintBook):
                print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
            else:
                print(f"Book: {book.title} by {book.author}")
