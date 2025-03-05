stringa = "['mario', 'gino', 'lucrezia']"

mylist_2 = ['mario', 'gino','lucrezia']

def Serializza(mylist_2):
    Mystring= str(mylist_2)
    return Mystring

def Deserializza(stringa):
    mylist=list(stringa)
    return mylist

out1=Serializza(mylist_2)
if type(out1) == str:

    print(f"{mylist_2} è una stringa")

else:

    print(f"{mylist_2} non è una stringa")
    
out2= Deserializza(stringa)
if type(out2) == list:

    print(f"{stringa} è una lista")

else:

    print(f"{stringa} non è una lista")