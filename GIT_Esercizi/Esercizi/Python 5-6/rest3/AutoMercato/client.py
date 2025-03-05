from flask import json
import requests
import sys

base_url = "https://127.0.0.1:8080"


def CreaVeicolo():
    tipo = input("Inserire il tipo di veicolo (automobili o motociclette): ")
    marca = input("Inserire la marca: ")
    modello = input("Inserire il modello: ")
    disponibilità = True
    datiVeicolo = {"tipo": tipo, "marca": marca, "modello": modello, "disponibilità": disponibilità}
    return datiVeicolo

def RichiediVeicolo():
    tipo = input("Inserire il tipo di veicolo (automobili o motociclette): ")
    id_veicolo = input("Inserire l'ID del veicolo: ")
    return {"tipo": tipo, "id": id_veicolo}

def ModificaVeicolo():
    tipo = input("Inserire il tipo di veicolo (automobili o motociclette): ")
    datiVeicolo = {"tipo": tipo}
    id_veicolo = input("Inserire l'ID del veicolo: ")
    datiVeicolo = {"id": id_veicolo}
    Msg= input("Quale elemento vuoi cambiare? (marca/modello/disponibilità)")
    if Msg == "marca":
        marca= input("Qual è il nome?: ")
        marca_nuova = marca
        datiVeicolo = {"marca": marca_nuova}
        return datiVeicolo
    elif Msg == "modello":
        modello= input("Qual è il modello?: ")
        modello_nuovo = modello
        datiVeicolo = {"modello": modello_nuovo}
        return datiVeicolo
    elif Msg == "disponibilità":
        disponibilità= input("Il veicolo è disponibile?: ")
        if disponibilità == "si":
            nuova_disponibilità = False
        else:
            nuova_disponibilità = True
        datiVeicolo = {"disponibilità": nuova_disponibilità}
        return datiVeicolo
    else:
        "Errore nell'inserimento"
    

def EliminaVeicolo():
    tipo = input("Inserire il tipo di veicolo (automobili o motociclette): ")
    id_veicolo = input("Inserire l'ID del veicolo: ")
    datiVeicolo = {"tipo": tipo, "id": id_veicolo}
    return datiVeicolo

# Menu principale
while True:
    print("\nOperazioni disponibili:")
    print("1. Inserisci Veicolo")
    print("2. Richiedi Veicolo")
    print("3. Modifica Veicolo")
    print("4. Elimina Veicolo")
    print("5. Esci")
    comando = input("Cosa vuoi fare? ")

    if comando == "1":
        datiVeicolo = CreaVeicolo()
        api_url = base_url + '/crea_Veicolo'
        try:
            risposta = requests.post(api_url, json=datiVeicolo, verify=False)
            print(risposta.json())
        except Exception as e:
            print(f"Errore: {str(e)}")

    elif comando == "2":
        datiVeicolo = RichiediVeicolo()
        api_url = base_url + '/richiedi_Veicolo'
        try:
            risposta = requests.post(api_url, json=datiVeicolo, verify=False)
            print(risposta.json())
        except Exception as e:
            print(f"Errore: {str(e)}")

    elif comando == "3":
        datiVeicolo = ModificaVeicolo()
        api_url = base_url + '/modifica_Veicolo'
        try:
            risposta = requests.post(api_url, json=datiVeicolo, verify=False)
            print(risposta.json())
        except Exception as e:
            print(f"Errore: {str(e)}")

    elif comando == "4":
        datiVeicolo = EliminaVeicolo()
        api_url = base_url + '/elimina_Veicolo'
        try:
            risposta = requests.delete(api_url, json=datiVeicolo, verify=False)
            print(risposta.json())
        except Exception as e:
            print(f"Errore: {str(e)}")

    elif comando == "5":
        print("Buona giornata!")
        sys.exit()

    else:
        print("Comando non valido.")
