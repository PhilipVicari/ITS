from flask import json
import requests
import sys

base_url = "https://127.0.0.1:8080"

def CreaVeicolo():
    tipo= input("Inserire il tipo di veicolo (automobili o motociclette): ")
    
    marca = input("Inserire la marca: ")
    modello = input("Inserire la modello: ")
    disponibilità = True
    datiVeicolo = {"tipo": tipo, "marca": marca, "modello": modello, "disponibilità": disponibilità}
    return datiVeicolo

def RichiediVeicolo():
    tipo = input("Quale è il tipo?: ")
    marca = input("Qual'è la marca?: ")
    modello = input("Qual è il modello?: ")
    datiVeicolo={'tipo': tipo, 'marca': marca, 'modello': modello}
    return datiVeicolo

def ModificaVeicolo():
    marca = input("Di quale marca si tratta?: ")
    datiVeicolo={'Marca': marca}
    Msg= input("Quale elemento vuoi cambiare?")
    if Msg == "marca":
        marca = input("Qual'è la marca?: ")
        marca_nuova = marca
        datiVeicolo = {"Marca":marca_nuova}
        return datiVeicolo
    elif Msg == "modello":
        modello = input("Qual'è il modello?: ")
        modello_nuovo = modello
        datiVeicolo = {"Modello": modello_nuovo}
        return datiVeicolo
    elif Msg == "disponibilità":
        disponibilità_nuovo = disponibilità
        datiVeicolo = {"disponibilità": disponibilità_nuovo}
        return datiVeicolo
    else:
        return "Errore nell'inserimento"

def EliminaVeicolo():
    tipo = input("Quale è il tipo?: ")
    marca = input("Qual'è la marca?: ")
    modello = input("Qual è il modello?: ")
    datiVeicolo={'tipo': tipo, 'marca': marca, 'modello': modello}
    return datiVeicolo

print("Operazioni disponibili:")
print("1. Inserisci Veicolo ")
print("2. Richiedi Veicolo")
print("3. Modifica Veicolo")
print("4. Elimina Veicolo")
print("5. Esci")
comando = input("Cosa vuoi fare?")

while(True):
    
    if comando == "1":
    
        print("Aggiungi Veicolo")
        datiVeicolo = CreaVeicolo()
        api_url = base_url + '/crea_Veicolo'
        try:
            richiesta = requests.post(api_url, json=datiVeicolo, verify = False)
            if richiesta.status_code == 200:
                print("Andato a buon fine")
        except:
            print("Errore di Connessione al Server")
    
    
    elif comando == "2":
    
        print("Richiesta Veicolo")
        datiVeicolo = RichiediVeicolo()
        api_url = base_url + '/richiedi_Veicolo'
        try:
            richiesta = requests.post(api_url, json=datiVeicolo, verify = False)
            if richiesta.status_code == 200:
                print("Andato a buon fine")
        except:
            print("Errore di Connessione al Server")
        
    elif comando == "3":
    
        print("Modifica veicolo")
        datiVeicolo = ModificaVeicolo()
        api_url = base_url + '/modifica_Veicolo'
        try:
            richiesta = requests.post(api_url, json=datiVeicolo, verify = False)
            if richiesta.status_code == 200:
                print("Andato a buon fine")
        except:
            print("Errore di Connessione al Server")
    
    elif comando == "4":
    
        print("Elimina veicolo")
        datiVeicolo = EliminaVeicolo()
        api_url = base_url + '/elimina_Veicolo'
        try:
            richiesta = requests.delete(api_url, json=datiVeicolo, verify = False)
            if richiesta.status_code == 200:
                print("Andato a buon fine")
        except:
            print("Errore di Connessione al Server")
    
    
    if comando=="5":
    
        print("Buona giornata!")
        sys.exit()
    
    print("Operazioni disponibili:")
    print("1. Inserisci Veicolo ")
    print("2. Richiedi Veicolo")
    print("3. Modifica Veicolo")
    print("4. Elimina Veicolo")
    print("5. Esci")
    comando = input("Cosa vuoi fare?")
