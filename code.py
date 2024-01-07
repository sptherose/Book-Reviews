
from dataclasses import dataclass

@dataclass
class Rating:
    Stars: float
    Review: str
@dataclass
class Book:
    Title: str
    Author: str
    Rating: Rating

books = []

def add_book() -> [Book]:
    title = input("What is the title of the book?")
    author = input ("Who wrote the book?")
    stars = float(input("How many stars do you give the book out of 5?"))
    review = input("How do you feel about the book?")
    book = Book(title,author,Rating(stars,review))
    books.append(book)

def find_title(title:str) -> Book:
    if not books:
        return Book("You did not read this book","",Rating(0,"No review"))
    else:
        found = Book("You did not read this book","",Rating(0,"No review"))
        for book in books:
            if title == book.Title:
                found = book
    return found

search_or_add = input("Do you want to search for a book or add a book to your finished books?")
if search_or_add == "search":
    action = input("What are you filtering by?")
    if action == "title":
        title = input("What is the title?")
        find_title(title)
if search_or_add == "add":
    add_book()

