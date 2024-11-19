from flask import Flask, json, request, render_template, jsonify
import random
import os
import sys
import dbclientPhi as db

api = Flask(__name__)

@api.route('/add_cittadino', methods=['POST'])
def GestisciAddCittadino():
    mydb = db.connect()
    if mydb is None:
        print("AHAHAHAH")
        sys.exit()
    try:
        response = request.json
        nome = response.get("nome")
        cognome = response.get("cognome")
        dataNascita = response.get("data nascita")
        codicefiscale = response.get("codice fiscale")
        
        query= db.write_in_db(mydb, f"insert into utenti(nomeutente, cognomeutente, datanascita, codicefiscale) values ('{nome}', '{cognome}', '{dataNascita}', '{codicefiscale}')")
        
        if query == 0:
            print("Andato a buon fine")
            return jsonify({"Esito": "200", "msg": "Andato a buon fine"}), 200
        else:
            print("Errore")
            return jsonify({"Esito": "404", "msg": "Non andato a buon fine"}), 404
    except Exception as e:
        print(str(e))
        return jsonify({"Esito": "500", "msg": "Errore di Connessione al Server"}), 500



@api.route('/richiedi_cittadino', methods= ['GET'])
def GestisciRichiediCIttadino():
    pass
@api.route('/modifica_cittadino', methods= ['PUT'])
def GestisciModificaCIttadino():
    pass
@api.route('/elimina_cittadino', methods= ['DELETE'])
def EliminaCittadino():
    pass
api.run(host="127.0.0.1", port=8080, ssl_context="adhoc", debug=True)


