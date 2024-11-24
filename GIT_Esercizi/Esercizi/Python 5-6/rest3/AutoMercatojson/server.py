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
    try:
        response = request.json
        marca = response.get("Marca")
        modello = response.get("Modello")
        cilindrata = response.get("Cilindrata")
        disponibilità = bool
        query= db.write_in_db(mydb, f"insert into AutoMercato(Marca, Modello, Cilindrata, Disponibilità) values ('{nome}', '{cognome}', '{dataNascita}', '{codicefiscale}')")
        
        if query == 0:
            print("Andato a buon fine")
            return jsonify({"Esito": "200", "msg": "Andato a buon fine"}), 200
        else:
            print("Errore")
            return jsonify({"Esito": "404", "msg": "Non andato a buon fine"}), 404
        db.close(mydb)
    except Exception as e:
        print(str(e))
        return jsonify({"Esito": "500", "msg": "Errore di Connessione al Server"}), 500
    db.close(mydb)
    
api.run(host="127.0.0.1", port=8080, ssl_context="adhoc", debug=True)
