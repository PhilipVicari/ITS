#9-1. Restaurant: Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type. 
#Make a method called describe_restaurant() that prints these two pieces of information, and a method called open_restaurant() that prints a message indicating that the restaurant is open. 
#Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.

#9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three different instances from the class, and call describe_restaurant() for each instance.
class restaurant:
    def __init__(self, name, cuisine_type) -> None:
        self.name= name
        self.cuisine_type= cuisine_type
    def describe_restaurant(self):
        print("\n", self.name)
        print(self.cuisine_type)
    def open_restaurant(self):
        print(f"The", self.name, "is open!")
restaurant1=restaurant("La Parolaccia", "Roman cuisine")
restaurant2=restaurant("Da Vittorio","Roman cuisine")
restaurant3=restaurant("Zi teresa","Roman cuisine")
restaurant4=restaurant("Fratini","Roman cuisine")

restaurant1.describe_restaurant()
restaurant1.open_restaurant()

restaurant2.describe_restaurant()
restaurant2.open_restaurant()

restaurant3.describe_restaurant()
restaurant3.open_restaurant()

restaurant4.describe_restaurant()
restaurant4.open_restaurant()
#9-3. Users: Make a class called User. 
#Create two attributes called first_name and last_name, and then create several other attributes that are typically stored in a user profile. 
#Make a method called describe_user() that prints a summary of the user’s information. 
#Make another method called greet_user() that prints a personalized greeting to the user. 
#Create several instances representing different users, and call both methods for each user.
class User:
    def __init__(self, first_name, last_name, age, hair, eyes) -> None:
        self.first_name= first_name
        self.last_name= last_name
        self.age= age
        self.hair= hair
        self.eyes= eyes
    def describe_user(self):
        summary= self.first_name, self.last_name, self.age, self.hair, self.eyes
        return summary
    def greet_user(self):
        print("\n", "hi", self.first_name, "nice to meet you")

person1= User("Mattia", "Massimi", 33, "Brown", "Brown")

person1.describe_user()
person1.greet_user()
#9-4. Number Served: Start with your program from Exercise 9-1. Add an attribute called number_served with a default value of 0. 
#Create an instance called restaurant from this class. Print the number of customers the restaurant has served, and then change this value and print it again. 
#Add a method called set_number_served() that lets you set the number of customers that have been served. Call this method with a new number and print the value again.
# Add a method called increment_number_served() that lets you increment the number of customers who’ve been served. 
#Call this method with any number you like that could represent how many customers were served in, say, a day of business. 
class restaurant:
    def __init__(self, name, cuisine_type) -> None:
        self.name= name
        self.cuisine_type= cuisine_type
    def describe_restaurant(self):
        print("\n", self.name)
        print(self.cuisine_type)
    def open_restaurant(self):
        print(f"The", self.name, "is open!")
restaurant1=restaurant("La Parolaccia", "Roman cuisine")
