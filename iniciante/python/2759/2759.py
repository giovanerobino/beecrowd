# beecrowd | 2759
# Entrada e Saída de Carácter
# Por Roberto A. Costa Jr, UNIFEI BR Brazil

# Timelimit: 1

def main():
    a = input().strip()
    b = input().strip()
    c = input().strip()

    print(f"A = {a}, B = {b}, C = {c}")
    print(f"A = {b}, B = {c}, C = {a}")
    print(f"A = {c}, B = {a}, C = {b}")


if __name__ == "__main__":
    main()
