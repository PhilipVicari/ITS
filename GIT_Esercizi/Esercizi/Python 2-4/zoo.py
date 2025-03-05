class Zoo:
    class fences:
        def __init__(self, area, temperature, habitat):
            self.area = area
            self.temperature = temperature
            self.habitat = habitat
    class zoo_keepers:
        def __init__(self, name, surname, id):
            self.name = name
            self.surname = surname
            self.id = id
        def add_animal():
            pass
        def remove_animal():
            pass
        def feed():
            pass
        def clean():
            pass
class Animale:
    def __init__(self, name, species, age, height, width, preferred_habitat, health):
        self.name = name
        self.species = species
        self.age = age
        self.height = height
        self.width = width
        self.preferred_habitat = preferred_habitat
        self.health = health