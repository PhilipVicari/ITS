from flask import json
import requests
import sys

base_url = "https://127.0.0.1:8080"

def AddDatiCittadino():
    nome = input("Qual'è il nome?")
    cognome = input("Qual'è il cognome")
    dataN = input("Qual'è la data di nascita?")
    codF = input("Qual'è il codice fiscale?")
    """
    {
        "nome": "Mario",
        "cognome":"Retti",
        "data nascita": "22/05/2010",
        "codice fiscale": "dfrcde23t44h501u"
    }
    
    """
    datiCittadino = {"nomeutente":nome, "cognomeutente": cognome, "datanascita":dataN, "codicefiscale":codF}
    return datiCittadino


def RichiediCittadino():
    codF= input("Inserisci il codice fiscale:")
    datiCittadino={'codicefiscale': codF}
    return datiCittadino

def ModificaCittadino():
    codF = input("Qual'è il codice fiscale?")
    datiCittadino={'codicefiscale': codF}
    Msg= input("Quale elemento vuoi cambiare?")
    if Msg == "nome":
        nome = input("Qual'è il nome?")
        nome_nuovo = nome
        datiCittadino = {"nomeutente":nome_nuovo}
        return datiCittadino
    elif Msg == "cognome":
        cognome = input("Qual'è il cognome?")
        cognome_nuovo = cognome
        datiCittadino = {"cognomeutente": cognome_nuovo}
        return datiCittadino
    elif Msg == "data nascita":
        dataN = input("Qual'è la data di nascita?")
        dataN_nuovo = dataN
        datiCittadino = {"datanascita":dataN_nuovo}
        return datiCittadino
    elif Msg == "Codice fiscale":
        codF = input("Qual'è il codice fiscale?")
        codF_Nuovo = codF
        datiCittadino = {"codicefiscale":codF_Nuovo}
        return datiCittadino
    else:
        return "Errore nell'inserimento"

def EliminaCittadino():
    codF = input("Qual'è il codice fiscale?")
    datiCittadino={'codicefiscale': codF}
    
print("Operazioni disponibili:")
print("1. Inserisci cittadino (es. atto di nascita)")
print("2. Richiedi cittadino (es. cert. residenza)")
print("3. Modifica cittadino (es. cambio residenza)")
print("4. Elimina cittadino (es. trasferim altro comune)")
print("5. Esci")
comando = input("Cosa vuoi fare?")

while(True):
    
    if comando == "1":
    
        print("Aggiungi Cittadino")
        datiCittadino = AddDatiCittadino()
        api_url = base_url + '/add_cittadino'
        try:
            request = requests.post(api_url, json=datiCittadino, verify = False)
            if request.status_code == 200:
                print("Andato a buon fine")
        except:
            print("Errore di Connessione al Server")
    
    
    elif comando == "2":
    
        print("Richiesta Cittadino")
        datiCittadino = RichiediCittadino()
        api_url = base_url + '/richiedi_cittadino'
        try:
            request = requests.get(api_url, json=datiCittadino, verify = False)
            if request.status_code == 200:
                print("Andato a buon fine")
        except:
            print("Errore di Connessione al Server")
    
    elif comando == "3":
    
        print("Modifica Cittadino")
        datiCittadino = AddDatiCittadino()
        api_url = base_url + '/modifica_cittadino'
        try:
            request = requests.put(api_url, json=datiCittadino, verify = False)
            if request.status_code == 200:
                print("Andato a buon fine")
        except:
            print("Errore di Connessione al Server")
    
    
    elif comando == "4":
    
        print("Elimina Cittadino")
        datiCittadino = AddDatiCittadino()
        api_url = base_url + '/elimina_cittadino'
        try:
            request = requests.delete(api_url, json=datiCittadino, verify = False)
            if request.status_code == 200:
                print("Andato a buon fine")
        except:
            print("Errore di Connessione al Server")
    
    
    if comando=="5":
    
        print("Buona giornata!")
        sys.exit()
    
    print("Operazioni disponibili:")
    print("1. Inserisci cittadino (es. atto di nascita)")
    print("2. Richiedi cittadino (es. cert. residenza)")
    print("3. Modifica cittadino (es. cambio residenza)")
    print("4. Elimina cittadino (es. trasferim altro comune)")
    print("5. Esci")
    comando = input("Cosa vuoi fare?")