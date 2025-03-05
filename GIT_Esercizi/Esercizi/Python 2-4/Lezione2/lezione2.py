# Philip Vicari
# 18/04/2024
#2-3 Personal Message: use a variable to represent a person's name, and print a message to that person. 
#your message should be simple like this: "Hello Eric, would you like to learn some python today?"
name = "Mario"
print(f"Hello", (name), ", would you like to learn some python today?")
#2-4 Use a variable to represent a person's name, and then print tht person's name in uppercase, lowercase and titlecase
name : str= "Federico"
uppername= name.upper()
lowername= name.lower()
titlename= name.title()
print(uppername, lowername, titlename)
#2-5.Famous Quote: Find a quote from a famous person you admire. Print the quote and the name of its author. Your output should look something like the following, including the quotation marks:
#    Albert Einstein once said, “A person who never made a mistake never tried anything new.”
name = "Albert_Einstein once said,"
print(name, "'Only a life lived for others is a life worthless'")
#2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the famous person’s name using a variable called famous_person. 
#Then compose your message and represent it with a new variable called message. Print your message.
famous_person = "Albert_Einstein"
message = "once said: 'Only a life lived for others is a life worthless'"
print(famous_person, message)
#2-8 Assign the value "python_notes.txt" to a variables called filename. 
#Then used the remoesuffix() method to display the filename without the file extension, like some file browsers do
filename : str= "python_notes.txt"
print(filename.removesuffix(".txt"))
#3-1. Names: Store the names of a few of your friends in a list called names. 
#     Print each person’s name by accessing each element in the list, one at a time.
names=["Damiano", "Gioia", "Riccardo"]
print(names[0])
print(names[1])
print(names[2])

#3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, print a message to them. The text of each message should be the same, but each message should be personalized with the person’s name.
print(f"ciao", (names[0]), "!")
print(f"ciao", (names[1]), "!")
print(f"ciao", (names[2]), "!")
#3-3. Your Own List: Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. 
#Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”
cars=["Ferrari", "Mclaren", "BMW"]
print(f"I would like to drive a", (cars[0]))
print(f"I would like to drive a", (cars[1]))
print(f"I would like to drive a", (cars[2]))

#3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you’d like to invite to dinner. 
#Then use your list to print a message to each person, inviting them to dinner.

#3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
#• Start with your program from Exercise 3-4. Add a print() call at the end of your program, stating the name of the guest who can’t make it.
#• Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
#• Print a second set of invitation messages, one for each person who is still in your list.

#3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
#• Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, informing people that you found a bigger table.
#• Use insert() to add one new guest to the beginning of your list.
#• Use insert() to add one new guest to the middle of your list.
#• Use append() to add one new guest to the end of your list.
#• Print a new set of invitation messages, one for each person in your list.

#3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and now you have space for only two guests.
#• Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
#• Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
#• Print a message to each of the two people still on your list, letting them know they’re still invited.
#• Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.
Person=[ "Batman", "Brad Pitt", "Mike Tyson"]
print(f"Hello", (Person[0]), ", I would like to invite you in a dinner")
print(f"Hello", (Person[1]), ", I would like to invite you in a dinner")
print(f"Hello", (Person[2]), ", I would like to invite you in a dinner")

print(f"unfortunately", (Person[2]), "can't be here")
del Person[2]
Person.append("Margot Robbie")
print(f"Hello", (Person[0]), ", I would like to invite you in a dinner")
print(f"Hello", (Person[1]), ", I would like to invite you in a dinner")
print(f"Hello", (Person[2]), ", I would like to invite you in a dinner")
Person.insert(0, "Sylvester Stallone")
Person.insert(1, "Arnold Schwarzenegger")
Person.append("Cillian Murphy")
print(f"Hello", (Person[0]), ", I would like to invite you in a dinner")
print(f"Hello", (Person[1]), ", I would like to invite you in a dinner")
print(f"Hello", (Person[2]), ", I would like to invite you in a dinner")
print(f"Hello", (Person[3]), ", I would like to invite you in a dinner")
print(f"Hello", (Person[4]), ", I would like to invite you in a dinner")
print(f"Hello", (Person[5]), ", I would like to invite you in a dinner")

print("This is the number of people that are invited:", len(Person))

print("I'm sorry but i can invite only two people for tonight")
print("I'm sorry", (Person[5]), "but i cannot let you come anymore")
popped_item = Person.pop(5)
print("I'm sorry", (Person[4]), "but i cannot let you come anymore")
popped_item = Person.pop(4)
print("I'm sorry", (Person[3]), "but i cannot let you come anymore")
popped_item = Person.pop(3)
print("I'm sorry", (Person[2]), "but i cannot let you come anymore")
popped_item = Person.pop(2)
print((Person[0]), "," ,(Person[1]), "you are invited to the dinner")
del Person[0]
del Person[0]
print(Person)
#3-8. Seeing the World: Think of at least five places in the world you’d like to visit.
#• Store the locations in a list. Make sure the list is not in alphabetical order.
#• Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list.
#• Use sorted() to print your list in alphabetical order without modifying the actual list.
#• Show that your list is still in its original order by printing it.
#• Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
#• Show that your list is still in its original order by printing it again.
#• Use reverse()  to change the order of your list. Print the list to show that its order has changed.
#• Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
#• Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
#• Use sort() to change your list so it’s stored in reverse-alphabetical order.
#Print the list to show that its order has changed.
city=["Milan", "Turin", "Bologna", "L.A", "New York"]
print(city)
ordered= sorted(city)
print(ordered)
print(city)
city.reverse()
print(city)
city.reverse()
print(city)
city.sort()
print(city)
city.reverse()
print(city)
#3-9. Dinner Guests: Working with one of the programs from Exercises 3, use len() to print a message indicating the number of people you’re inviting to dinner.

#3-10. Every Function: Think of things you could store in a list. For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. 
#Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.
L=["uno", "due", "tre", "quattro", "cinque", "sei", "sette"]
ordered= sorted(L)
print(ordered)
L.reverse()
print(L)
L.pop(0)
print(L)
L.reverse()
print(L)
del L[0]
print(L)
L.insert(3, "Quattordici")
print(L)
L.append("Dieci")
print(L)
#6-1. Person: Use a dictionary to store information about a person you know. Store their first name, last name, age, and the city in which they live.
# You should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.
Amico={"first_name":"Damiano", "last_name": "Muni", "age":19, "city":"Rome"}
print(Amico["first_name"])
print(Amico["last_name"])
print(Amico["age"])
print(Amico["city"])
#6-2. Favorite Numbers: Use a dictionary to store people�s favorite numbers. Think of five names, and use them as keys in your dictionary. 
#Think of a favorite number for each person, and store each as a value in your dictionary. Print each person�s name and their favorite number. 
#For even more fun, poll a few friends and get some actual data for your program.
People_num={"Marco":2, "Lorenzo": 10, "Paolo": 5, "Luca": 78}
print(People_num)
#6-3. Glossary: A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let�s call it a glossary.
#� Think of five programming words you�ve learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.
#� Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, 
#  or print the word on one line and then print its meaning indented on a second line. 
#  Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.

#[6-7. People: Start with the program you wrote for Exercise 6-1. 
#Make two new dictionaries representing different people, and store all three dictionaries in a list called people. Loop through your list of people. 
#As you loop through the list, print everything you know about each person.
dict1={"first_name":"Lorenza", "last_name": "Verdi", "age":19, "city":"Rome", "first_name":"Mario", "last_name": "Rossi", "age":25, "city":"Rome"}
dict2={"first_name":"Riccardo", "last_name": "Malizia", "age":20, "city":"Rome", "first_name":"Gabriele", "last_name": "Mancini", "age":17, "city":"Rome"}
People=[dict1, dict2, Amico]
print(People)
#6-8. Pets: Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner�s name. 
#Store these dictionaries in a list called pets. Next, loop through your list and as you do, print everything you know about each pet.
pet1={"Pet:": "cat", "owner:": "Mario"}
pet2={"Pet:": "bunny", "owner:": "Gabriele"}
pet3={"Pet:": "dog", "owner:": "Damiano"}
pets=[pet1, pet2, pet3]
for elem in pets:
    print(elem)
#6-9. Favorite Places: Make a dictionary called favorite_places. Think of three names to use as keys in the dictionary, and store one to three favorite places for each person. 
#To make this exercise a bit more interesting, ask some friends to name a few of their favorite places. Loop through the dictionary, and print each person�s name and their favorite places.
favorite_places={"Valerio": "Villa Borghese", "Mario": "Colosseo", "Gioia": "Via Del Corso"}
for keys, values in favorite_places.items():
    print(keys, values)

#6-10. Favorite Numbers: Modify your program from Exercise 6-2 so each person can have more than one favorite number. Then print each person�s name along with their favorite numbers.
People_num={"Marco":"2, 5, 6, 7", "Lorenzo": "10, 3, 6, 2", "Paolo": "5, 18, 45", "Luca": "78, 23, 44"}
print(People_num)
#6-11. Cities: Make a dictionary called cities. Use the names of three cities as keys in your dictionary. 
#Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city. 
#The keys for each city�s dictionary should be something like country, population, and fact. Print the name of each city and all of the information you have stored about it.
cities={"Roma", "Bologna", "Venezia"}
information={"Country:" :"Italy", "Population:": "2.800.000", "Country:" :"Italy", "Population:": "388.000", "Country:" :"Italy", "Population:": "260.000"}
#6-12. Extensions: We�re now working with examples that are complex enough that they can be extended in any number of ways. 
#Use one of the example programs from this chapter, and extend it by adding new keys and values, changing the context of the program, or improving the formatting of the output.
