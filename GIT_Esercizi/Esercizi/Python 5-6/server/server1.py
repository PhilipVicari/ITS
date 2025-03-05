from flask import Flask, render_template, request

api = Flask("__name__")

utenti=[['mario','rossi', 'M', '0'], ['gianni','fumagalli', 'M', '0'], ['AnitaGaribaldi','proietti', 'F', '0'],]


@api.route('/', methods=['GET'])
def index():
    return render_template('y.html')


@api.route('/registrati', methods=['GET'])
def indexpippo():
    nome=request.args.get('name')
    cognome= request.args.get('cognome')
    for u in utenti:
    
        if u[0]== nome and u[1]==cognome:  
            return render_template('si.html', nome=nome, cognome = cognome)
    return render_template('no.html', nome=nome, cognome = cognome)

api.run(host="0.0.0.0", port=8085)
