from flask import Flask, json, request, render_template, jsonify
import random
import os
import sys

api = Flask(__name__)

@api.route('/', methods= ['GET'])
def index():
    answer = "Ciao a tutti"
    return render_template("send.html", answer = "Ciao")

@api.route('/mansendfile', methods= ['POST'])
def ricevidati():
    domanda= request.form.get("question")
    image = request.files.get("image")
    length= len(image)
    mioanswer = "Ciao a tutti MA ADESSO NON TI RISPONDO alla domanda" + domanda + "con file " + str(length)
    return render_template("send.html", answer=mioanswer)



api.run(host="127.0.0.1", port=8085, debug=True)
