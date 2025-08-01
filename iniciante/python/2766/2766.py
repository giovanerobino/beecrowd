# beecrowd | 2766
# Entrada e Saída Lendo e Pulando Nomes
# Por Roberto A. Costa Jr, UNIFEI BR Brazil

# Timelimit: 1

while True:
    try:
        nomes = [input() for _ in range(10)]
        print(nomes[2])  # Terceiro nome
        print(nomes[6])  # Sétimo nome
        print(nomes[8])  # Nono nome
    except EOFError:
        break
