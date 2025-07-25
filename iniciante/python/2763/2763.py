# beecrowd | 2763
# Entrada e Saída CPF
# Por Roberto A. Costa Jr, UNIFEI BR Brazil

# Timelimit: 1

while True:
    try:
        cpf = input().strip()
        # Remove os pontos e o hífen do CPF
        cpf_numeros = cpf.replace('.', '').replace('-', '')
        # Divide o CPF em partes
        partes = [cpf_numeros[i:i+3] for i in range(0, 9, 3)] + [cpf_numeros[9:]]
        for parte in partes:
            print(parte)
    except EOFError:
        break
