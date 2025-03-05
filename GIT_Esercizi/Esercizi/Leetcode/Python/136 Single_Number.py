class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        count = 0  # Inizializziamo un contatore a zero
        
        # Iteriamo attraverso ogni numero nella lista nums
        for number in nums:
            count += 1  # Incrementiamo il contatore ad ogni iterazione
            
            # Controlliamo se il numero è presente nella lista nums
            if number in nums:  # Questa condizione sarà sempre vera
                count += 1  # Incrementiamo il contatore se il numero è trovato

            # Se il contatore è uguale a 1, restituiamo il numero
            if count == 1:
                return number  # Questa condizione non verrà mai soddisfatta come previsto

es_136= Solution()
print(es_136.singleNumber([2,2,1]))