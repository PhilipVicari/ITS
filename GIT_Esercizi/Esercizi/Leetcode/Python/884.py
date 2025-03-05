class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        # Inizializza una lista vuota per contenere le parole non comuni
        l:list = []  
        
        # Splitta le frasi s1 e s2 in liste di parole
        New_s1 = s1.split()  
        New_s2 = s2.split()  

        # Itera su ogni parola della prima lista (New_s1)
        for word in New_s1:
            # Conta quante volte la parola appare in New_s1
            lala = New_s1.count(word)  
            # Controlla se la parola appare solo una volta in New_s1
            if lala == 1:
                # Controlla se la parola non è presente in New_s2
                if word not in New_s2:
                    # Aggiungi la parola alla lista delle parole non comuni
                    l.append(word)  
        
        # Itera su ogni parola della seconda lista (New_s2)
        for words in New_s2:
            # Conta quante volte la parola appare in New_s2
            lalo = New_s2.count(words)  
            # Controlla se la parola appare solo una volta in New_s2
            if lalo == 1:
                # Controlla se la parola non è presente in New_s1
                if words not in New_s1:
                    # Aggiungi la parola alla lista delle parole non comuni
                    l.append(words)  
                    
        # Restituisce la lista delle parole non comuni
        return l


es884=Solution()
print(es884.uncommonFromSentences("apple apple", "banana"))