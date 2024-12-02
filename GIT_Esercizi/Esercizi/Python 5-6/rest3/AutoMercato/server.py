from flask import Flask, json, request, render_template, jsonify
import random
import os
import sys
import dbclientPhi as db

api = Flask(__name__)

@api.route('/crea_Veicolo', methods= ['POST'])
def Gestisci_Crea_Veicolo():
    mydb = db.connect()
    if mydb is None:
        return "Connessione Fallita"
    try:
        response = request.json
        tipo = response.get("tipo")
        marca = response.get("marca")
        modello = response.get("modello")
        disponibilità = response.get("disponibilità")
        query= db.write_in_db(mydb, f"insert into {tipo}(marca, modello, disponibilità) values ('{marca}', '{modello}', {disponibilità})")
        
        if query == 0:
            print("Andato a buon fine")
            return jsonify({"Esito": "200", "msg": "Andato a buon fine"}), 200
        else:
            print("Errore")
            db.close(mydb)
            return jsonify({"Esito": "404", "msg": "Non andato a buon fine"}), 404
    except Exception as e:
        print(str(e))
        db.close(mydb)
        return jsonify({"Esito": "500", "msg": "Errore di Connessione al Server"}), 500
    
@api.route('/richiedi_Veicolo', methods= ['POST'])
def Gestisci_Richiedi_Veicolo():
    mydb = db.connect()
    if mydb is None:
        return "Connessione Fallita"
    try:
        response = request.json
        tipo = response.get("tipo")
        marca = response.get("marca")
        modello = response.get("modello")
        query= db.read_in_db(mydb, f"SELECT * from {tipo} where marca = '{marca}' and modello = '{modello}'")
        
        if query == -1:
            print("Errore")
            return jsonify({"Esito": "404", "msg": "Non andato a buon fine"}), 404
        else:
            print("Andato a buon fine")
            db.close(mydb)
            return jsonify({"Esito": "200", "msg": "Andato a buon fine"}), 200
    except Exception as e:
        print(str(e))
        db.close(mydb)
        return jsonify({"Esito": "500", "msg": "Errore di Connessione al Server"}), 500
    

@api.route('/modifica_Veicolo', methods= ['GET'])
def Gestisci_Modifica_Veicolo():
    mydb = db.connect()
    if mydb is None:
        return "Connessione Fallita"
    try:
        response = request.json
        tipo = response.get("tipo")
        marca = response.get("marca")
        modello = response.get("modello")
        disponibilità = response.get("disponibilità")
        query= db.write_in_db(mydb, f"UPDATE {tipo} SET marca = '{marca}', modello = '{modello}', disponibilità = '{disponibilità}'")
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
    

@api.route('/elimina_Veicolo', methods= ['DELETE'])
def Gestisci_Elimina_Veicolo():
    mydb = db.connect()
    if mydb is None:
        return "Connessione Fallita"
    try:
        response = request.json
        tipo = response.get("tipo")
        marca = response.get("marca")
        modello = response.get("modello")
        query= db.write_in_db(mydb, f"DELETE FROM {tipo} where marca = '{marca}' and modello = '{modello}'")
        
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
