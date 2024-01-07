
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
    return books

def find_title(title:str):
    if not books:
        print("You have not added any books")
    else:
        found = print("You have not read this book")
        for book in books:
            if title == book.Title:
                found = book
        print(found)

keep_going = True
while keep_going == True:
    command = input("Do you want to search for a book or add a book to your finished books or exit program?")
    if command == "search":
        action = input("What are you filtering by?")
        if action == "title":
            title = input("What is the title?")
            find_title(title)
    if command == "add":
        add_book()
    if command == "exit":
        keep_going = False
