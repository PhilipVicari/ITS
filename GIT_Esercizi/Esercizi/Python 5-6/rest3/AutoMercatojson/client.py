from flask import json
import requests
import sys

base_url = "https://127.0.0.1:8080"

def CreaVeicolo():
    tipo= input("Inserire il tipo di veicolo (Automobile o Motocicletta): ")
    marca = input("Inserire la Marca: ")
    modello = input("Inserire la modello: ")
    cilindrata = input("Inserire la cilindrata: ")
    disponibilità = bool
    datiVeicolo = {"Marca": marca, "modello": modello, "cilindrata": cilindrata, "tipo": tipo, "Disponibilità": disponibilità}
    return datiVeicolo

def RichiediVeicolo():
    marca= input("Inserire la Marca: ")
    datiVeicolo={'Marca': marca}
    return datiVeicolo

def ModificaVeicolo():
    marca = input("Di quale marca si tratta?: ")
    datiVeicolo={'Marca': marca}
    Msg= input("Quale elemento vuoi cambiare?")
    if Msg == "Marca":
        marca = input("Qual'è la marca?: ")
        marca_nuova = marca
        datiVeicolo = {"Marca":marca_nuova}
        return datiVeicolo
    elif Msg == "Modello":
        cognome = input("Qual'è il modello?: ")
        modello_nuovo = modello
        datiVeicolo = {"Modello": modello_nuovo}
        return datiVeicolo
    elif Msg == "Cilindrata":
        dataN = input("Qual'è la cilindrata?: ")
        cilindrata_nuovo = cilindrata
        datiVeicolo = {"Cilindrata":cilindrata_nuovo}
        return datiVeicolo
    else:
        return "Errore nell'inserimento"

def EliminaVeicolo():
    marca = input("Qual'è la marca?: ")
    datiVeicolo={'Marca': marca}

def Disponibilità():
    marca = input("Inserire la Marca: ")
    if datiVeicolo.get("Marca") == marca:
        return datiVeicolo.get("Disponibilità")
    
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
            if request.status_code == 200:
                print("Andato a buon fine")
        except:
            print("Errore di Connessione al Server")
    
    
    elif comando == "2":
    
        print("Richiesta Veicolo")
        datiVeicolo = RichiediVeicolo()
        api_url = base_url + '/richiedi_Veicolo'
        try:
            richiesta = requests.post(api_url, json=datiVeicolo, verify = False)
            if request.status_code == 200:
                print("Andato a buon fine")
        except:
            print("Errore di Connessione al Server")
        
    elif comando == "3":
    
        print("Elimina veicolo")
        datiVeicolo = EliminaVeicolo()
        api_url = base_url + '/elimina_Veicolo'
        try:
            richiesta = requests.post(api_url, json=datiVeicolo, verify = False)
            if request.status_code == 200:
                print("Andato a buon fine")
        except:
            print("Errore di Connessione al Server")
    
    
    if comando=="4":
    
        print("Buona giornata!")
        sys.exit()
    
    print("Operazioni disponibili:")
    print("1. Inserisci Veicolo (es. atto di nascita)")
    print("2. Richiedi Veicolo (es. cert. residenza)")
    print("3. Elimina Veicolo (es. trasferim altro comune)")
    print("4. Esci")
    comando = input("Cosa vuoi fare?")
