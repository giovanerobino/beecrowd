# beecrowd | 2760
# Entrada e Saída de String
# Por Roberto A. Costa Jr, UNIFEI BR Brazil

# Timelimit: 1

while True:
    try:
        A = input()
        B = input()
        C = input()

        print(A + B + C)
        print(B + C + A)
        print(C + A + B)
        print(A[:10] + B[:10] + C[:10])
    except EOFError:
        break
