class Book():
    def __init__(self, book_id:str, title: str, author: str, is_borrowed: bool) -> None:
        self.book_id= book_id
        self.title= title
        self.author= author
        self.is_borrowed=is_borrowed
    
    def borrow(self):
        if self.is_borrowed== True:
            self.is_borrowed==False
            
    def return_book(self):
        self.is_borrowed==True
        
class Member():
    def __init__(self, member_id: str, name:str) -> None:
        self.member_id=member_id
        self.name=name
        self.borrowed_books=[]
        
    def borrow_book(self, book):
        if book not in self.borrowed_books:
            self.borrowed_books.append(book)
            
class Library():
    
    def __init__(self) -> None:
        self.books={}
        self.members={}
        
    def add_book(self, book_id:str, title:str, author:str):
        if book_id not in self.books:
            self.books[book_id]= [title]
        else:
            self.books[book_id].append(title)
            
    def register_member(self, member_id:str, name:str):
        if member_id not in self.members:
            self.members[member_id]=[name]
        else:
            self.members.update({member_id: name})
            
    def borrow_book(self, member_id:str, book_id:str):
        book = Book()
        if member_id in self.members and book_id in self.books:
            if book.is_borrowed == False:
                book.is_borrowed = True
        return self.books
    
    def return_book(self, member_id:str, book_id:str):
        book = Book()
        if member_id in self.members and book_id in self.books:
            if book.is_borrowed == True:
                book.is_borrowed = False
        return self.books
    
    def get_borrowed_books(self, member_id):
        lista_prestito=[]
        if member_id in self.members:
            for k in self.members:
                if k == member_id:
                    lista_prestito.append(self.members[k])
        return lista_prestito
                    
                    
                    
                    
library = Library()

library.add_book("B001", "The Great Gatsby", "F. Scott Fitzgerald")
library.add_book("B002", "1984", "George Orwell")
library.add_book("B003", "To Kill a Mockingbird", "Harper Lee")

# Register members
library.register_member("M001", "Alice")
library.register_member("M002", "Bob")
library.register_member("M003", "Charlie")

# Borrow books
library.borrow_book("M001", "B001")
library.borrow_book("M002", "B002")

print(library.get_borrowed_books("M001"))  # Expected output: ['The Great Gatsby']
print(library.get_borrowed_books("M002"))  # Expected output: ['1984']