from flask import json
import requests
import sys

base_url = "http://127.0.0.1:8080"

def GetDatiCittadino():
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
    datiCittadino = {"nome":nome, "cognome": cognome, "data nascita":dataN, "codice fiscale":codF}
    return datiCittadino


def RichiediCittadino():
    codF= input("Inserisci il codice fiscale:")
    datiCittadino={'codice fiscale': codF}
    return datiCittadino

def ModificaCittadino():
    codF = input("Qual'è il codice fiscale?")
    datiCittadino={'codice fiscale': codF}
    Msg= input("Quale elemento vuoi cambiare?")
    if Msg == "nome":
        nome = input("Qual'è il nome?")
        nome_nuovo = nome
        datiCittadino = {"nome":nome_nuovo}
        return datiCittadino
    elif Msg == "cognome":
        cognome = input("Qual'è il cognome?")
        cognome_nuovo = cognome
        datiCittadino = {"cognome": cognome_nuovo}
        return datiCittadino
    elif Msg == "data nascita":
        dataN = input("Qual'è la data di nascita?")
        dataN_nuovo = dataN
        datiCittadino = {"data nascita":dataN_nuovo}
        return datiCittadino
    elif Msg == "Codice fiscale":
        codF = input("Qual'è il codice fiscale?")
        codF_Nuovo = codF
        datiCittadino = {"codice fiscale":codF_Nuovo}
        return datiCittadino
    else:
        return "Errore nell'inserimento"

def EliminaCittadino():
    codF = input("Qual'è il codice fiscale?")
    datiCittadino={'codice fiscale': codF}
print("Operazioni disponibili:")
print("1. Inserisci cittadino (es. atto di nascita)")
print("2. Richiedi cittadino (es. cert. residenza)")
print("3. Modifica cittadino (es. cambio residenza)")
print("4. Elimina cittadino (es. trasferim altro comune)")
print("5. Esci")
sOper = input("Cosa vuoi fare?")
while(True):
    if sOper == "1":
        print("Inserimento nuovo cittadino")
        api_url = base_url + "/add_cittadino"
        jsonDataRequest = GetDatiCittadino()
        try:
            response = requests.post(api_url,json=jsonDataRequest)
        
            #print(response.json())
            print(response.status_code)
            print(response.headers["Content-Type"])
            data1 = response.json()
            print(data1)
        except:
            print("Problemi di comunicazione con il server, riprova più tardi")
            
    elif sOper == "2":
        print("Richiesta Cittadino")
        api_url = base_url + "/richiedi_cittadino"
        jsonDataRequest = RichiediCittadino()
        try:
            response = requests.get(api_url,json=jsonDataRequest)
        
            #print(response.json())
            print(response.status_code)
            print(response.headers["Content-Type"])
            data2 = response.json()
            print(data2)
        except:
            print("Problemi di comunicazione con il server, riprova più tardi")
    
    elif sOper == "3":
        print("Modifica Cittadino")
        api_url = base_url + "/modifica_cittadino"
        jsonDataRequest = ModificaCittadino()
        try:
            response = requests.get(api_url,json=jsonDataRequest)
        
            #print(response.json())
            print(response.status_code)
            print(response.headers["Content-Type"])
            data2 = response.json()
            print(data2)
        except:
            print("Problemi di comunicazione con il server, riprova più tardi")
            
    elif sOper == "4":
        print("Modifica Cittadino")
        api_url = base_url + "/modifica_cittadino"
        jsonDataRequest = ModificaCittadino()
        try:
            response = requests.get(api_url,json=jsonDataRequest)
        
            #print(response.json())
            print(response.status_code)
            print(response.headers["Content-Type"])
            data2 = response.json()
            print(data2)
        except:
            print("Problemi di comunicazione con il server, riprova più tardi")      
              
    if sOper=="5":
        print("Buona giornata!")
        sys.exit()
    print("Operazioni disponibili:")
    print("1. Inserisci cittadino (es. atto di nascita)")
    print("2. Richiedi cittadino (es. cert. residenza)")
    print("3. Modifica cittadino (es. cambio residenza)")
    print("4. Elimina cittadino (es. trasferim altro comune)")
    print("5. Esci")
    sOper = input("Cosa vuoi fare?")    