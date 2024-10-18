class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        # Crea una copia dell'elenco 'heights' e la ordina
        N_heights = sorted(heights)  
        
        # Inizializza un contatore per le posizioni diverse
        count = 0  

        # Itera su ogni indice dell'elenco 'heights'
        for i in range(len(heights)):
            # Confronta l'altezza originale con l'altezza ordinata
            if heights[i] != N_heights[i]:
                # Se sono diversi, incrementa il contatore
                count += 1
                
        # Restituisce il numero totale di posizioni in cui le altezze differiscono
        return count  

es1051=Solution()
print(es1051.heightChecker([1,1,4,2,1,3]))