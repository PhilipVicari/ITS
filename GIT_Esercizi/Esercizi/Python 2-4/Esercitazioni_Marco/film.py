#In un file chiamato "film.py", si definisca la classe Film che rappresenta un film preso a nolleggio. 
# In tale classe, definire un codice identificativo (int) ed un titolo (string). Entrambi gli attributi sono da considerarsi privati.
 
#- Definire i seguenti metodi:

#    init(id, title): metodo costruttore.
#    setID(id): che consente di impostare il codice identificativo del film, modificando il valore del relativo attributo.
#    setTitle(title): che consente di impostare il codice identificativo del film, modificando il valore del relativo attributo.
#    getID(): che consente di ritornare il valore del codice identificativo di un film.
#    getTitle(): che consente di ritornare il valore del titolo di un film.
#    isEqual(otherFilm): che ritorna true se il codice identificativo di due film è uguale.  
class Film:
    def __init__(self, id, title):
        self.id=id
        self.title=title
    def setId(self, id):
        self. id = id
        return self.id
    def set_title(self, title):
        self.title=title
        return self.title
    def getId(self):
        return self.id
    def getTitle(self):
        return self.title
    def isEqual(self, otherFilm):
        if otherFilm == self.id:
            return True
        else:
            return False
film_1=Film(333, "Fight Club")
film_1.setId(333)
film_1.set_title("Fight Club")
print(film_1.getId())
print(film_1.getTitle())
print(film_1.isEqual())