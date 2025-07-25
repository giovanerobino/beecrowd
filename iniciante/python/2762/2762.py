# beecrowd | 2762
# Entrada e Saída 6
# Por Roberto A. Costa Jr, UNIFEI BR Brazil

# Timelimit: 1

while True:
    try:
        entrada = input().strip()
        parte_inteira, parte_decimal = entrada.split('.')
        parte_inteira = parte_inteira.lstrip('0')
        parte_decimal = parte_decimal.lstrip('0')
        print(f"{parte_decimal}.{parte_inteira}")
    except EOFError:
        break
