# beecrowd | 2764
# Entrada e Saída de Data
# Por Roberto A. Costa Jr, UNIFEI BR Brazil

# Timelimit: 1

while True:
    try:
        data = input().strip()
        if not data:
            break
        dia, mes, ano = data.split('/')
        print(f"{mes}/{dia}/{ano}")
        print(f"{ano}/{mes}/{dia}")
        print(f"{dia}-{mes}-{ano}")
    except EOFError:
        break
