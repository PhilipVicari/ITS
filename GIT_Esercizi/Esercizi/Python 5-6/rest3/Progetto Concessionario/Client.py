import requests,json
import sys

base_url = "http://127.0.0.1:8080"

def Login():
    pass

def Registrazione():
    pass

def Crea_veicolo():
    tipo = input("Inserire il tipo di veicolo: (automobile o motocicletta) ")
    marca = input("Inserire la marca del veicolo: ")
    modello = input("Inserire il modello del veicolo: ")
    disponibilità = True
    numero_telaio= input("Inserire il numero del telaio: ")
    datiVeicolo = {"tipo": tipo, "marca": marca, "modello": modello, "disponibilità": disponibilità, "numero telaio": numero_telaio}
    return datiVeicolo

def Richiedi_Veicolo():
    tipo = input("Inserire il tipo di veicolo: (automobile o motocicletta) ")
    numero_telaio= input("Inserire il numero del telaio: ")
    datiVeicolo = {"tipo": tipo, "numero telaio": numero_telaio}
    return datiVeicolo

def Update_Veicolo():
    tipo = input("Inserire il tipo di veicolo: (automobile o motocicletta) ")
    numero_telaio = input("Inserisci il numero di telaio del veicolo a cui vuoi modificare i dati: ")
    marca = input("Inserisci la marca modificata (Lascia vuoto per non cambiare): ")
    modello = input("Inserisci il modello modificato (Lascia vuoto per non cambiare): ")
    disponibilità = input("Inserisci la disponibilità modificata (Lascia vuoto per non cambiare): ")
    
    dati_da_modificare = {
        "tipo": tipo,
        "numero_telaio": numero_telaio,
        "marca": marca if marca else None,
        "modello": modello if modello else None,
        "disponibilità": True if disponibilità.lower() == "si" else False if disponibilità.lower() == "no" else None
    }
    return dati_da_modificare


def Elimina_Veicolo():
    tipo = input("Inserire il tipo di veicolo: (automobile o motocicletta) ")
    numero_telaio= input("Inserire il numero del telaio: ")
    datiVeicolo = {"tipo": tipo, "numero telaio": numero_telaio}
    return datiVeicolo

while True:
    print("\nOperazioni disponibili:")
    print("1. Inserisci Veicolo ")
    print("2. Richiedi Veicolo ")
    print("3. Modifica Veicolo ")
    print("4. Elimina Veicolo ")
    print("5. Esci")
    
    comando = input("Cosa vuoi fare? ")
    if comando == "1":
        api_url = base_url + "/crea_veicolo"
        datiVeicolo = Crea_veicolo()
        try:
            richiesta = requests.post(api_url, json = datiVeicolo, verify= False)
            if richiesta.status_code == 200:
                print("Andato a buon fine")
        except:
            print("Errore di Connessione al Server")
    
    if comando == "2":
        print("Richiesta Veicolo")
        api_url = base_url + "/richiesta_veicolo"
        datiVeicolo = Richiedi_Veicolo()
        try:
            richiesta = requests.post(api_url, json = datiVeicolo, verify= False)
            if richiesta.status_code == 200:
                print("Andato a buon fine")

        except:
            print("Errore di Connessione al Server")
    
    if comando == "3":
        api_url = base_url + "/update_veicolo"
        datiVeicolo = Update_Veicolo()
        try:
            richiesta = requests.put(api_url, json = datiVeicolo, verify= False)
            if richiesta.status_code == 200:
                print("Andato a buon fine")
        except:
            print("Errore di Connessione al Server")
    
    if comando == "4":
        api_url = base_url + "/elimina_veicolo"
        datiVeicolo = Elimina_Veicolo()
        try:
            richiesta = requests.delete(api_url, json = datiVeicolo, verify= False)
            if richiesta.status_code == 200:
                print("Andato a buon fine")
        except:
            print("Errore di Connessione al Server")
    
    if comando == "5":
        print("Buona giornata!")
        sys.exit()