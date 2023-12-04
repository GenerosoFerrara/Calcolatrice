def calcola(num1, num2, operatore):
    if operatore == '+':
        return num1 + num2
    elif operatore == '-':
        return num1 - num2
    elif operatore == '*':
        return num1 * num2
    elif operatore == '/':
        if num2 != 0:  # Assicurati di non dividere per zero
            return num1 / num2
        else:
            return "Impossibile dividere per zero"
    else:
        return "Operatore non valido"

# Esempi di utilizzo della funzione:
risultato = calcola(5, 3, '+')
print("Risultato:", risultato)

risultato = calcola(10, 2, '/')
print("Risultato:", risultato)