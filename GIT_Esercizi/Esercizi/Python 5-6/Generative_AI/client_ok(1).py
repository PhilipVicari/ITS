
# def GetDatiCittadino():
#     nome = input("Inserisci il nome: ")
#     cognome = input("Inserisci il cognome: ")
#     dataN = input("Inserisci la data di nascita (gg/mm/aaaa): ")
#     codF = input("Inserisci il codice fiscale: ")
#     datiCittadino = {
#         "nome": nome, 
#         "cognome": cognome, 
#         "dataNascita": dataN, 
#         "codFiscale": codF
#     }
#     return datiCittadino


# def GetCodicefiscale():
#     cod = input('Inserisci codice fiscale: ')
#     return {"codFiscale": cod}
# def GetCredenziali():    
#     username= input("Inserisci l'username")
#     password= input("Inserisci la password")
#     credenziali = {"username": username, "Password": password} 
#     return credenziali
# api_url = base_url + "/getcredenziali"
# jsonDataRequest = GetCredenziali()
# response = requests.post(api_url, json=jsonDataRequest)


    # elif sOper == 4:
    #     print("Eliminazione cittadino")
    #     api_url = base_url + "/elimina_cittadino"
    #     jsonDataRequest = GetCodicefiscale()
    #     response = requests.post(api_url, json=jsonDataRequest, verify= False)
    #     print(response.json())


    # elif sOper == 5:
    #     print("Buona giornata!")
    #     sys.exit()

    # else:
    #     print("Operazione non disponibile, riprova.")


#

import requests, json, sys

GoogleApiKey= "AIzaSyDJmjkZ-hM2UnviUOrJbwxbjEcFVcRVqJ4"

base_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key="

api_url = base_url + GoogleApiKey

print("Benvenuti nel mio GenerativeAI")


iFlag = 0
while True:
    print("\nOperazioni disponibili:")
    print("1. Inserisci una domanda")
    print("2. Richiedi una domanda su un immagine")
    print("3. Esci")


    try:
        sOper = int(input("Cosa vuoi fare? "))
    except ValueError:
        print("Inserisci un numero valido!")
        continue


    if sOper == 1:
        Domanda = input("inserisci domanda: ")
        jsonDataRequest = {"contents": [{"parts":[{"text": Domanda}]}]}
        response = requests.post(api_url, json=jsonDataRequest, verify = True)
        if response.status_code == 200:
            print(response.json())
            listaRisposte = response.json()["candidates"]
            for Risposta in listaRisposte:
                TestoRisposta = Risposta["content"]["parts"][0]["text"]
                print(TestoRisposta)
                
    elif sOper == 2:
        Image = input("Inserisci file img da analizzare: ")
        Domanda = input("inserisci domanda: ")
        jsonDataRequest = {"contents": [{"parts":[{"text": Domanda}]}]}
        

    elif sOper == 3:
        print("Modifica cittadino")