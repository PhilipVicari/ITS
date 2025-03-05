class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Inizializziamo una lista vuota che conterrà le parti unite di word1 e word2
        Merged = []
        
        # Utilizziamo zip() per iterare attraverso i caratteri di entrambe le stringhe
        # zip() accoppierà i caratteri di word1 e word2 finché entrambe hanno caratteri
        for a, b in zip(word1, word2):
            # Aggiungiamo la coppia di caratteri (un carattere da word1 e uno da word2) alla lista Merged
            Merged.append(a + b)
        
        # Controlliamo quale delle due stringhe è più lunga
        if len(word1) > len(word2):
            # Se word1 è più lunga, aggiungiamo il resto di word1 alla lista Merged
            Merged.append(word1[len(word2):])
        else:
            # Se word2 è più lunga (o sono uguali), aggiungiamo il resto di word2 alla lista Merged
            Merged.append(word2[len(word1):])
        
        # Uniamo tutti gli elementi della lista Merged in una singola stringa e la restituiamo
        return "".join(Merged)
es_1768= Solution()
print(es_1768.mergeAlternately("ab", "pqrs"))