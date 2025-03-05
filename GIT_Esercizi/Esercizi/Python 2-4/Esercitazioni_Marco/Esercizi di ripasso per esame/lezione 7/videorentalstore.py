class Movie():
    def __init__(self, movie_id: str, title: str, director: str, is_rented: bool) -> None:
        self.movie_id = movie_id
        self.title = title
        self.director = director
        self.is_rented = is_rented
    def rent(self):
        if self.is_rented == False:
            self.is_rented==True
        else:
            print(f"Il film {self.title} è già noleggiato")
    def return_movie(self):
        if self.is_rented == True:
            self.is_rented==False
        else:
            print(f"Il film {self.title} non attualmente noleggiato")
class Customer():
    def __init__(self, customer_id:str, name:str, rented_movies=[]) -> None:
        self.customer_id=customer_id
        self.name= name
        self.rented_movies= rented_movies
    def rent(self, movie:Movie):
        if self.is_rented == False:
            self.rented_movies.append(movie)
        else:
            print(f"Il film {self.title} è già noleggiato")
    def return_movie(self, movie:Movie):
        if self.is_rented == True:
            self.is_rented==False
        else:
            print(f"Il film {self.title} non attualmente noleggiato")
class VideoRentalStore():
    def __init__(self, movies:dict[{str, Movie}], customers:dict[str, Customer]) -> None:
        self.movies= movies
        self.customers= customers
    def add_movie(self, movie_id:str, title:str, director:str):
        movie= Movie(movie_id, title, director)
        if movie not in self.movies:
            self.movies[movie_id]= movie
        else:
            return f"Il film con ID {movie_id} esiste già."
    def register_customer(self, customers_id: str, name:str):
        customer= Customer(customers_id, name)
        if customer not in self.customers:
            self.customers[customers_id] = customer
        else:
            return f"Il cliente con ID {customers_id} è già registrato."
    
    def rent_movie(self, customers_id: str, movie_id:str):
        if customers_id in self.customers and movie_id in self.movies:
            movie = self.movies[movie_id]
            movie.is_rented == True
        else:
            return f"Cliente o film non trovato."

    def return_movie(self, customers_id: str, movie_id:str):
        if customers_id in self.customers and movie_id in self.movies:
            movie = self.movies[movie_id]
            movie.is_rented == False
        else:
            return f"Cliente o film non trovato."
    def get_rented_movies(self, customers_id: str) -> list [Movie]:
        if customers_id in self.customers:
            customer= self.customers[customers_id]
            return customer.rented_movies()
             
