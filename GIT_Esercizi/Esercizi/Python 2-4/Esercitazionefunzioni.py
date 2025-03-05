"""
from collections import Counter


def frequency_dict(elements: list) -> dict:
    a = dict(Counter(elements))
    print(a)
frequency_dict(['mela', 'banana', 'mela'])
"""

"""
def rounded_average(numbers: list[int]) -> int:
    Sum = sum(numbers)
    Sum=Sum//len(numbers)
    if Sum==1:
        Sum+=1
    print(Sum)

rounded_average([1,1,2,2])
"""

"""
def create_contact(name: str, email: str, telefono: int) -> dict:
    contact={'profile':name, 'email':email, 'telefono':telefono}
    return contact
create_contact('Paolo', 'Paolo@gmail.com', 3333456)


def update_contact(dictionary: dict, name: str, email: str =None, telefono: int=None) -> dict:

"""

"""

def rimuovi_elementi(lista: list[int], da_rimuovere: dict[int:int]) -> list  
    for i in lista:
        if da_rimuovere.keys in lista:
            while da_rimuovere.values                
                listanuova=[lista.remove(da_rimuovere.key)]            
                return listanuova
print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 2}))

"""

"""
def aggregavoti(voti: list[dict]) -> dict:
    result={}
    for students in voti:
        nome = students['name']
        voto = students['voto']
        if nome in result:
                        result = students['name']
                        result = students['voto']
        else:
            result[nome]= [voto]
            return result
aggregavoti([{'nome': 'Alice', 'voto': 90}, {'nome': 'Bob', 'voto': 75}, {'nome': 'Alice', 'voto': 85}])

"""
