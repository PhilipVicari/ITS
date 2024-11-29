from flask import Flask, json, request, render_template, jsonify
import random
import os
import sys
import dbclientPhi as db

api = Flask(__name__)

@api.route('/cerca_automobile', methods= ['POST'])
def Gestisci_Crea_Veicolo():
    mydb = db.connect()
    if mydb is None:
        return "Connessione Fallita"
    else:    
        try:
            response = request.json
            marca = response.get("Marca")
            modello = response.get("Modello")
            cilindrata = response.get("Cilindrata")
            disponibilità = response.get("Disponibilità")
            
            query= db.write_in_db(mydb, f"insert into AutoMercato(Marca, Modello, Cilindrata, Disponibilità) values ('{nome}', '{cognome}', '{dataNascita}', '{codicefiscale}')")
            
            if query == 0:
                print("Andato a buon fine")
                db.close(mydb)
                return jsonify({"Esito": "200", "msg": "Andato a buon fine"}), 200
            else:
                print("Errore")
                db.close(mydb)
                return jsonify({"Esito": "404", "msg": "Non andato a buon fine"}), 404
        except Exception as e:
            print(str(e))
            db.close(mydb)
            return jsonify({"Esito": "500", "msg": "Errore di Connessione al Server"}), 500


@api.route('/richiedi_veicolo', methods= ['GET'])
def Gestisci_Richiedi_Veicolo():
    mydb = db.connect()
    if mydb is None:
        return "Connessione Fallita"
    else:    
        try:
            response = request.json
            #Primarykey database = response.get("Primarykey database")
            query= db.read_next_row(mydb, f"SELECT * FROM utenti where codicefiscale = {codicefiscale}")
            
            if query == -1:
                print("Errore")
                db.close(mydb)
                return jsonify({"Esito": "404", "msg": "Non andato a buon fine"}), 404
            else:
                print("Andato a buon fine")
                db.close(mydb)
                return jsonify({"Esito": "200", "msg": "Andato a buon fine"}), 200

        except Exception as e:
            print(str(e))
            db.close(mydb)
            return jsonify({"Esito": "500", "msg": "Errore di Connessione al Server"}), 500

@api.route('/modifica_veicolo', methods= ['PUT'])
def Gestisci_Modifica_Veicolo():
    mydb = db.connect()
    if mydb is None:
        return "Connessione Fallita"
    else:    
        try:
            response = request.json
            nome = response.get("nome")
            cognome = response.get("cognome")
            dataNascita = response.get("data nascita")
            codicefiscale = response.get("codice fiscale")
            
            query= db.write_in_db(mydb, f"UPDATE *Nome Database* SET nome = '{nome}, cognome = '{cognome}, datanascita = '{dataNascita}, codicefiscale = '{codicefiscale}, ")
            
            if query == 0:
                print("Andato a buon fine")
                db.close(mydb)
                return jsonify({"Esito": "200", "msg": "Andato a buon fine"}), 200
            elif query == -1:
                print("Errore")
                db.close(mydb)
                return jsonify({"Esito": "404", "msg": "Non andato a buon fine"}), 404

        except Exception as e:
            print(str(e))
            db.close(mydb)
            return jsonify({"Esito": "500", "msg": "Errore di Connessione al Server"}), 500

@api.route('/elimina_veicolo', methods= ['DELETE'])
def Gestisci_Elimina_Veicolo():
    mydb = db.connect()
    if mydb is None:
        return "Connessione Fallita"
    else:    
        try:
            response = request.json
            codicefiscale = response.get("codice fiscale")
            
            query= db.write_in_db(mydb, f"DELETE FROM utenti where codicefiscale = '{codicefiscale}'")
            
            if query == 0:
                print("Andato a buon fine")
                db.close(mydb)
                return jsonify({"Esito": "200", "msg": "Andato a buon fine"}), 200
            elif query == -1:
                print("Errore")
                db.close(mydb)
                return jsonify({"Esito": "404", "msg": "Non andato a buon fine"}), 404

        except Exception as e:
            print(str(e))
            db.close(mydb)
            return jsonify({"Esito": "500", "msg": "Errore di Connessione al Server"}), 500

api.run(host="127.0.0.1", port=8080, ssl_context="adhoc", debug=True)
