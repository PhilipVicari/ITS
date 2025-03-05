#Sviluppa un sistema in Python per la gestione di un catalogo film che permetta di aggiungere, rimuovere e cercare film di un particolare regista. 
# Il sistema dovrebbe consentire anche di visualizzare tutti i registi e i loro film.
#Classe:
#- MovieCatalog: Gestisce tutte le operazioni legate al catalogo dei film.
#Metodi:
#- add_movie(director_name, movies): Aggiunge uno o più film a un regista specifico nel catalogo. Se il regista non esiste, viene creato un nuovo record. 
# Se il regista esiste, la sua lista di film viene aggiornata.
#- remove_movie(director_name, movie_name): Rimuove un film specifico dall'elenco dei film di un regista. 
# Se tutti i film sono rimossi, il regista può essere opzionalmente rimosso dal catalogo.
#- list_directors(): Elenca tutti i registi presenti nel catalogo.
#- get_movies_by_director(director_name): Restituisce tutti i film di un regista specifico.
#- search_movies_by_title(title): Trova tutti i film che contengono una certa parola nel titolo. 
# Restituisce un elenco dei registi e dei rispettivi film che contengono la parola cercata o un messaggio di errore se nessun film contiene la parola cercata nel titolo.
class MovieCatalog():
    def __init__(self) -> None:
        self.catalogo= {}
    def __str__(self) -> str:
        return str (self.catalogo)
    
    def add_movie(self, director_name:str, movies):
        if director_name not in self.catalogo:
            self.catalogo[director_name]= [movies]
        else:
            self.catalogo[director_name].append(movies)
        return self.catalogo
    
    
    def remove_movie(self, director_name, movie_name):
        if movie_name in self.catalogo[director_name]:
            self.catalogo[director_name].remove(movie_name)
            if self.catalogo[director_name]== []:
                del self.catalogo[director_name]
        return self.catalogo
    
    
    def list_directors(self):
        list_directors=[self.catalogo.keys()]
        return list_directors
    
    
    def get_movies_by_director(self, director_name):
        return self.catalogo.get(director_name)
    
    
    def search_movies_by_title(self, title):
        result={}
        for dir, movies in self.catalogo.items():
            Same_word_films=[]
            for movie in movies:
                if title in movie:
                    Same_word_films.append(movie)
            if Same_word_films:
                result[dir] = Same_word_films
        if result:
            return result
        else:
            return "Nessun film trovato"
        

    def Tutti_film(self):
        for dir, movies in self.catalogo.items():
            print("\n", dir)
            for movie in movies:
                print("\n", movie)
catalog= MovieCatalog()
catalog.add_movie("Spielberg", "The Wolf of Wall Street")
print("\n",catalog)

catalog.add_movie("Quentin Tarantino", "Django")
print("\n",catalog)

catalog.add_movie("Christopher Nolan", ["Oppenheimer", "Batman Begins"])
print("\n",catalog)

catalog.list_directors()
print("\n","I registi sono:", catalog.list_directors())

catalog.get_movies_by_director("Christopher Nolan")
print("\n","I film di Nolan sono:", catalog.get_movies_by_director("Christopher Nolan"))

catalog.search_movies_by_title("Django")
print("\n", "Film trovati:", catalog.search_movies_by_title("Django"))

catalog.Tutti_film()
