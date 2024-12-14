from flask import Flask, json, request, render_template, jsonify
import random
import os
import dbclient as db
import sys

api = Flask(__name__)

####################################################################################################################################################

@api.route("/crea_veicolo", methods = ["POST"])
def Gestione_Crea_Veicolo():
    mydb = db.connect()

    if mydb is None:
        print("Errore connessione al DB")
        sys.exit()
    
    try:
        response = request.json
        tipo= response.get("tipo")
        marca= response.get("marca")
        modello= response.get("modello")
        disponibilità= response.get("disponibilità")
        numero_telaio= response.get("numero telaio")
        
        query = db.write_in_db(mydb, f"INSERT INTO {tipo} (marca, modello, disponibilità, numero_telaio) VALUES ('{marca}', '{modello}', '{disponibilità}', '{numero_telaio}')")

        if query == 0:
            print("Andato a buon fine")
            
            return jsonify({"Esito": "200", "msg": "Andato a buon fine"}), 200
        else:
            
            print("Errore")
            return jsonify({"Esito": "404", "msg": "Non andato a buon fine"}), 404
    except Exception as e:
        print(str(e))
        
        return jsonify({"Esito": "500", "msg": "Errore di Connessione al Server"}), 500
    finally:
        db.close(mydb)
####################################################################################################################################################

@api.route("/richiesta_veicolo", methods = ["POST"])
def Gestione_Richiedi_Veicolo():
    mydb = db.connect()

    if mydb is None:
        print("Errore connessione al DB")
        sys.exit()
    
    try:
        response = request.json
        tipo= response.get("tipo")
        numero_telaio= response.get("numero telaio")
        
        query = db.read_next_row(mydb, f"SELECT * FROM {tipo} WHERE numero_telaio = {numero_telaio}")

        if query == -1:
            print("Errore")
            return jsonify({"Esito": "404", "msg": "Non andato a buon fine"}), 404
        else:
            print(query)
            print("Andato a buon fine")
            return jsonify({"Esito": "200", "msg": "Andato a buon fine"}), 200

    except Exception as e:
        print(str(e))
        return jsonify({"Esito": "500", "msg": "Errore di Connessione al Server"}), 500
    finally:
        db.close(mydb)

####################################################################################################################################################

@api.route("/update_veicolo", methods = ["PUT"])
def Gestione_Update_Veicolo():
    mydb = db.connect()

    if mydb is None:
        print("Errore connessione al DB")
        sys.exit()
    
    try:
        response = request.json
        tipo= response.get("tipo")
        marca= response.get("marca")
        modello= response.get("modello")
        disponibilità= response.get("disponibilità")
        numero_telaio= response.get("numero telaio")
                
        if marca:
            N_query = db.write_in_db(mydb, f"UPDATE {tipo} SET marca = '{marca}' AND numero_telaio = '{numero_telaio}'")
        elif modello:
            N_query = db.write_in_db(mydb, f"UPDATE {tipo} SET modello = '{modello}' AND numero_telaio = '{numero_telaio}'")
        elif marca:
            N_query = db.write_in_db(mydb, f"UPDATE {tipo} SET disponibilità = '{disponibilità}' AND numero_telaio = '{numero_telaio}'")
            
        if N_query == 0:
            print("Andato a buon fine")
            return jsonify({"Esito": "200", "msg": "Andato a buon fine"}), 200
        else:
            print("Errore")
            return jsonify({"Esito": "404", "msg": "Non andato a buon fine"}), 404
    except Exception as e:
        print(str(e))
        
        return jsonify({"Esito": "500", "msg": "Errore di Connessione al Server"}), 500
    finally:
        db.close(mydb)
####################################################################################################################################################

@api.route("/elimina_veicolo", methods = ["DELETE"])
def Gestione_Elimina_Veicolo():
    mydb = db.connect()

    if mydb is None:
        print("Errore connessione al DB")
        sys.exit()
    
    try:
        response = request.json
        tipo= response.get("tipo")
        numero_telaio= response.get("numero telaio")
        
        query = db.write_in_db(mydb, f"DELETE FROM {tipo} WHERE numero_telaio = {numero_telaio}")

        if query == 0:
            print("Andato a buon fine")
            
            return jsonify({"Esito": "200", "msg": "Andato a buon fine"}), 200
        else:
            
            print("Errore")
            return jsonify({"Esito": "404", "msg": "Non andato a buon fine"}), 404
    except Exception as e:
        print(str(e))
        
        return jsonify({"Esito": "500", "msg": "Errore di Connessione al Server"}), 500
    finally:
        db.close(mydb)
####################################################################################################################################################

api.run(host="127.0.0.1", port=8080, debug=True)
