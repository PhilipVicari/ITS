class RecipeManager:
    def __init__(self) -> None:
            self.recipe= {}

    def __str__(self) -> str:
        return str (self.recipe)
    
    def create_recipe(self, name, ingredients):
        if name in self.recipe:
            return f"La ricetta esiste già"
        else:
            self.recipe[name]=ingredients
            return self.recipe

    def add_ingredient(self, recipe_name, ingredient):
        if ingredient in self.recipe:
            return f"l'ingrediente inserito esiste già oppure la ricetta non esiste"
        else:
            self.recipe[recipe_name].append(ingredient)
            return self.recipe

    def remove_ingredient(self, recipe_name, ingredient):
        if ingredient not in self.recipe or recipe_name in self.recipe:
            return f"l'ingrediente inserito esiste già oppure la ricetta non esiste"
        else:
            self.recipe[recipe_name].remove(ingredient)
            return self.recipe
    def update_ingredient(self, recipe_name, old_ingredient, new_ingredient):

        if old_ingredient not in self.recipe or recipe_name in self.recipe:
            return f"l'ingrediente inserito esiste già oppure la ricetta non esiste"
        else:
            self.recipe.replace(old_ingredient, new_ingredient)
            return self.recipe
    def list_recipes(self):
        return self.recipe.keys()
    
    def list_ingredients(self, recipe_name):
        return self.recipe.values()
    
    def search_recipe_by_ingredient(self, ingredient):
        for i in self.recipe:
            if ingredient in self.recipe.values():
                return self.recipe(ingredient)
        else:
            return"Errore"


  
manager = RecipeManager()
print(manager.create_recipe("Torta di mele", ["Farina", "Uova", "Mele"]))
print(manager.add_ingredient("Torta di mele", "Zucchero"))
print(manager.list_recipes()) # ['Torta di mele']
print(manager.list_ingredients("Torta di mele"))
print(manager.search_recipe_by_ingredient("Uova"))
