def mappa_parole_a_lunghezza(words: list) -> dict:
    contaparole={}
    for w in words:
        contaparole=[w]
        words.count(w)
    return contaparole

print(mappa_parole_a_lunghezza(["apple", "banana", "cherry"]))