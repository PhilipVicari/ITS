import json

with open('Esercizi/Python 5-6/server/Json/quiz.json') as f:
    data = json.load(f)
    
risposte_medie = 0
domande= 0
matematica=0
for cat, question in data['quiz'].items():
    for e in question:
        domande += 1
    print(domande)
    

print(data)