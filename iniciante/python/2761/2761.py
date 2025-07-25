# beecrowd | 2761
# Entrada e Saída de Vários Tipos
# Por Roberto A. Costa Jr, UNIFEI BR Brazil

# Timelimit: 1
import struct

try:
    while True:
        linha = input().split(' ', 3)

        A = int(linha[0])
        # Converte para float, depois para single-precision e de volta para float
        B_double = float(linha[1])
        B = struct.unpack('f', struct.pack('f', B_double))[0]
        C = linha[2]
        D = linha[3]

        print(f"{A}{B:.6f}{C}{D}")

        print(f"{A}\t{B:.6f}\t{C}\t{D}")

        print(f"{A:>10}{B:>10.6f}{C:>10}{D:>10}")

except EOFError:
    pass
