import json

with open('Python 6\server\json\quiz.json') as f:
    data = json.load(f)
domande = 0
matematica=0
opzioni = 0
for cat, questions in data['quiz'].items():
    for key, info in questions.items():
        domande += 1
        opzioni += len(info['options'])

        if cat == 'maths':
            matematica += 1
    
media= opzioni/domande
print(f"Domande totali:{domande}")
print(f"Domande media del numero di riposte:{media}")
print(f"Domande sulla matematica:{matematica}")