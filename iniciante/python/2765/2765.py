# beecrowd | 2765
# Entrada e Saída com Virgula
# Por Roberto A. Costa Jr, UNIFEI BR Brazil

# Timelimit: 1

while True:
    try:
        frase = input()
        partes = frase.split(',', 1)  # Divide a frase em duas partes na primeira vírgula
        print(partes[0])
        print(partes[1])
    except EOFError:
        break
