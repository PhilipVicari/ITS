class Solution:
    def two_sum(self, nums, target):
        # Creiamo un dizionario per memorizzare il numero e il suo indice
        num_to_index = {}
        
        # Iteriamo attraverso la lista nums usando enumerate per ottenere anche l'indice
        for index, num in enumerate(nums):
            # Calcoliamo il complemento che serve a raggiungere il target
            complement = target - num
            
            # Controlliamo se il complemento è già stato visto
            if complement in num_to_index:
                # Se trovato, restituiamo l'indice del complemento e l'indice corrente
                return [num_to_index[complement], index]
            
            # Altrimenti, aggiungiamo il numero e il suo indice al dizionario
            num_to_index[num] = index
        
        # Se non troviamo nessuna coppia, restituiamo una lista vuota
        return []
# Example usage:
es=Solution()
nums = [2, 7, 11, 15]
target = 9
result = es.two_sum(nums, target)
print(result)  # Output: [0, 1] since nums[0] + nums[1] = 2 + 7 = 9