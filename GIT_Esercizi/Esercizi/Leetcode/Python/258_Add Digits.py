class Solution:
    def addDigits(self, num: int) -> int:
        # Converte il numero in una stringa, poi in una lista di cifre intere
        digits = list(map(int, str(num))) 
        
        # Calcola la somma delle cifre
        somma = sum(digits)  
        
        # Continua a sommare le cifre finché la somma è maggiore di 9
        while somma > 9:
            # Converte la somma in una stringa e poi in una lista di cifre intere
            digits = list(map(int, str(somma)))  
            
            # Calcola la nuova somma delle cifre
            somma = sum(digits)  
        
        # Restituisce la somma finale, che sarà un numero compreso tra 0 e 9
        return somma  
es_258=Solution()
print(es_258.addDigits(199))