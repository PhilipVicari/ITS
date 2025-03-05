"""Si creino tre classi chiamate Azione, Commedia e Drama, tutte derivanti dalla classe Film. 
Ognuna di queste classi ha un attributo privato di tipo string chiamato genere, 
che equivale al genere di film (genere="Azione", nella classe Azione) ed un attributo privato di tipo float chiamato penale. 
I film di azione hanno una penalità di 3 euro al giorno, le commedie hanno una penale di 2.50 euro al giorno, i film drammatici hanno una penale di 2 euro al giorno.

- Per ognuna di queste classi si implementi un metodo chiamato:

    getGenere(), che ritorna il genere di film
    getPenale(), che ritorna il valore della penale
    calcolaPenaleRitardo(), che prende in ingresso il numero dei giorni di ritardo per un film e restituisce la penale da pagare per quel film.

Le tre classi Azione, Commedia e Drama devono essere contenute nel file "movie_genre.py"."""
from Esercitazioni_Marco.film import Film 
class Azione(Film):
    __Genere="Azione"
    __penale:float= 3
    def getGenere(self):
        return self.__Genere
    def getPenale(self):
        return self.__penale
    def calcola_penale_Ritardo(self, N_giorni):
        penaletot= self.__penale*N_giorni
        return penaletot
class Commedia(Film):
    __Genere="Commedia"
    __penale:float= 2.50
    def getGenere(self):
        return self.__Genere
    def getPenale(self):
        return self.__penale
    def calcola_penale_Ritardo(self, N_giorni):
        penaletot= self.__penale*N_giorni
        return penaletot
class Drama(Film):
    __Genere= "Drama"
    __penale:float= 2
    def getGenere(self):
        return self.__Genere
    def getPenale(self):
        return self.__penale
    def calcola_penale_Ritardo(self, N_giorni):
        penaletot= self.__penale*N_giorni
        return penaletot
