from flask import Flask, json, request, render_template
import random
import os
import sys
import dbclientPhi as db

api = Flask(__name__)
mydb = db.connect()
if mydb is None:
    print("Errore di connessione")
    sys.exit()
else:
    print("Connessione al db ok")

@api.route('/add_cittadino', methods=['POST'])
def GestisciAddCittadino():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
        accesso = request.json[1]
        dati = request.json[0]
        if login_interno(accesso) and controllo_privilegi_admin(accesso):
            with open("user.json") as json_file:
                cittadini = json.load(json_file)
            for key, vale in dati.items():
                if key in cittadini:
                    print("Errore codice fiscale già esistente")
                    return "True"
            with open("user.json", "w") as json_file:
                cittadini |= dati
                json.dump(cittadini, json_file)
            return "True"
        else:
            return "Dati errati"
    else:
        return 'Content-Type not supported!'
    
    
@api.route('/read_cittadino', methods=['POST'])
def GestisciReadCittadino():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
        accesso = request.json[1]
        dati = request.json[0]
        if login_interno(accesso):
            with open("user.json") as json_file:
                cittadini = json.load(json_file)
            for key, value in cittadini.items():
                if dati == key:
                    return cittadini[key]
            return "Cittadino non trovato"
        else:
            return "Dati errati"
    else:
        return 'Content-Type not supported!'
    
@api.route('/update_cittadino', methods=['POST'])
def GestisciUpdateCittadino():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
        accesso = request.json[1]
        dati = request.json[0]
        if login_interno(accesso) and controllo_privilegi_admin(accesso):
            with open("user.json") as json_file:
                cittadini = json.load(json_file)
        
            if dati[0] not in cittadini:
                return "Errore, codice fiscale non trovato"

            for i in range(len(dati) - 1):
                if dati[i+1]:
                    if i + 1 == 1:
                        cittadini[dati[0]]["cognome"] = dati[i+1]
                    elif i + 1 == 2:
                        cittadini[dati[0]]["dataNascita"] = dati[i+1]
                    elif i + 1 == 3:
                        cittadini[dati[0]]["nome"] = dati[i+1]
            with open("user.json", "w") as json_file:
                json.dump(cittadini, json_file)
            return "Modifica avvenuta con successo"   
        else:
            return "Dati errati"     
    else:
        return 'Content-Type not supported!'

@api.route('/delete_cittadino', methods=['POST'])
def GestisciDeleteCittadino():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
        accesso = request.json[1]
        dati = request.json[0]
        if login_interno(accesso) and controllo_privilegi_admin(accesso):
            with open("user.json") as json_file:
                cittadini = json.load(json_file)
        
            if dati not in cittadini:
                return "Errore, codice fiscale non trovato"
            cittadini.pop(dati)
            with open("user.json", "w") as json_file:
                json.dump(cittadini, json_file)
                
            return "Eliminazione avvenuta con successo"
        else:
            return "Dati errati"
    else:
        return 'Content-Type not supported!'
    
@api.route('/login', methods=['POST'])
def login():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
        for key, value in request.json.items():
            sQuery = f"select * from utenti where username = '{key}' and password = '{value[0]}'; "
            print(sQuery)
            INumRecord = db.read_in_db(mydb, sQuery)
            if INumRecord == 1:            
                print("Login Terminato Correttamente")
                lRecord = db.read_next_row(mydb)
                iStato = lRecord[1][0]
                return '{"Esito": "ok", "Stato": '+ str(iStato) + '}'
            elif INumRecord == 0:
                print("Credenziali Errate")
                return '{"Esito": "ko", "Stato": -1}'
            elif INumRecord <= -1:
                print("Dati Errati")
                return '{"Esito": "ko", "Stato": -1}'
            else:
                print("Attenzione: Attacco in Corso")
                return '{"Esito": "ko", "Stato": {iStato}}'
    else:
        return 'Content-Type not supported!'

@api.route('/registrazione', methods=['POST'])
def Registrazione():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
        #Dobbiamo intervenire qui
        #Dobbiamo verificare se username è già presente nella tabella utenti 
        #altrimenti facciamo la insert
        for key, value in request.json.items():
            sQuery = f"insert into utenti(username,password,privilegi) values ('{key}', '{value[0]}', {random.randint(0,1)});"
            print(sQuery)
            iRetValue = db.write_in_db(mydb, sQuery)
            if iRetValue == -2:
                return "Nome utente già in uso"
            elif iRetValue == 0:
                return "Registrazione avvenuta con successo"
            else:
                return "errore non gestito nella registrazione"
        return "Errore richiesta non conforme"
    else:
        return 'Content-Type not supported!'

api.run(host="127.0.0.1", port=8080, ssl_context='adhoc')
