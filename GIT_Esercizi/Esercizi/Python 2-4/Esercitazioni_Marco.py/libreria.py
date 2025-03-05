#Si desidera sviluppare un sistema per la gestione di una biblioteca in Python. Il sistema deve permettere di gestire un inventario di libri e le operazioni di prestito e restituzione degli stessi. 
# Gli utenti del sistema devono essere in grado di aggiungere libri al catalogo, prestarli, restituirli e visualizzare quali libri sono disponibili in un dato momento.
#Classi:
#- Book: Rappresenta un libro con titolo, autore, stato del prestito. Il libro deve essere inizialmente disponibile (non prestato).

#- Library: Gestice tutte le operazioni legate alla gestione di una biblioteca.

#    Metodi:
#    - add_book(libro): Aggiunge un nuovo libro al catalogo della biblioteca. Restituisce un messaggio di conferma.
#
#    - borrow_book(titolo): Cerca un libro per titolo e, se disponibile e non già prestato, lo segna come disponibile. Restituisce un messaggio di stato.
#
#    - return_book(titolo): Cerca un libro per titolo e, se trovato e prestato, lo segna come disponibile. Restituisce un messaggio di stato.
#
#    - get_borrowed_books(): Restituisce una lista dei titoli dei libri attualmente disponibili. Se non ci sono libri disponibili, restituisce un messaggio di errore.
#
#Test Cases:
#- Un amministratore della biblioteca aggiunge alcuni libri all'inventario.
#- Un utente prende in prestito un libro, che viene quindi marcato come non disponibile.
#- L'utente restituisce il libro, che viene marcato di nuovo come disponibile.
#- In qualsiasi momento, un utente può visualizzare quali libri sono disponibili per il prestito.

class Book:
    def __init__(self, book_id, title, author, state_of_borrow=True) -> None:
        self.book_id=book_id
        self.title= title
        self.author= author
        self.state_of_borrow= state_of_borrow
    def borrow(self):
        pass
    def return_book():
        pass

class Member():
    pass
        
class Library():
    def __init__(self) -> None:
        self.catalogo=[]
    def add_book(self, libro: Book):
        self.catalogo.append(libro)
        return f"IL libro è stato aggiunto:{libro.title}"
    
    def borrow_book(self, title):
        for libro in self.catalogo:
            if libro.title == title:
                if libro.state_of_borrow:
                    libro.state_of_borrow = False
                    return "Il libro è stato prestato"
                else:
                    return "Il libro non è disponibile"
    def return_book(self, title):
        for libro in self.catalogo:
            if libro.title == title:
                if not libro.state_of_borrow:
                    libro.state_of_borrow = True
                    return "Il libro è tornato disponibile"
                else:
                    return "Il libro era già disponibile"
                    
    def get_borrowed_books(self):
        disponibili = []
        for libro in self.catalogo:
            if libro.state_of_borrow:
                disponibili.append(libro.title)
        return disponibili    
libro_1= Book("1984", "George Orwell")
libro_2= Book("Le barzellette di Francesco Totti", "Francesco Totti")
biblioteca_1= Library()
print(biblioteca_1.add_book(libro_1))
print(biblioteca_1.add_book(libro_2))

print(biblioteca_1.borrow_book("1984"))
print(biblioteca_1.borrow_book("Le barzellette di Francesco Totti"))

print(biblioteca_1.borrow_book("1984"))
print(biblioteca_1.borrow_book("Le barzellette di Francesco Totti"))

print(biblioteca_1.return_book("1984"))
print(biblioteca_1.return_book("Le barzellette di Francesco Totti"))
print(biblioteca_1.get_borrowed_books())