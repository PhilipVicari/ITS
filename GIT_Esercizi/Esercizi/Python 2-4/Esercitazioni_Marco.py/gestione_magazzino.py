class Prodotto:
    def __init__(self, nome:str, quantità:int) -> None:
        self.nome= nome
        self.quantità= quantità
class Magazzino:
    def __init__(self) -> None:
        self.magazzino = []
    def aggiungi_prodotto(self, prodotto: Prodotto):
        self.magazzino.append(prodotto)
        return self.magazzino
    def cerca_prodotto(self, nome:str):
        for prod in self.magazzino:
            if prod.nome == nome:
                return nome
        return None      
    def verifica_disponibilità(self, nome:str):
        for prod in self.magazzino:
            if prod.nome == nome:
                return f"il prodotto {prod.nome} è disponibile in negozio"
        return f"Questo prodotto non esiste"

oggetto_1 = Prodotto("Bottiglia", 6)

magazzino = Magazzino()

print(magazzino.aggiungi_prodotto(oggetto_1))

print(magazzino.verifica_disponibilità("Bottiglia"))

#chiedere a davide del perchè di questo output