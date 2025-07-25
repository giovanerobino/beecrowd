# beecrowd | 2758
# Entrada e Saída de Números Reais
# Por Roberto A. Costa Jr, UNIFEI BR Brazil

# Timelimit: 1

import struct

def to_float32(value):
    """Simula a conversão para float32 (precisão simples)"""
    # Converte para float, depois para bytes como float32, e volta para float
    return struct.unpack('f', struct.pack('f', float(value)))[0]

# Ler os números
line1 = input().split()
line2 = input().split()

# Precisão simples (float32) para A e B
a = to_float32(line1[0])
b = to_float32(line1[1])
# Precisão dupla (float64) para C e D
c = float(line2[0])
d = float(line2[1])

print(f"A = {a:.6f}, B = {b:.6f}")
print(f"C = {c:.6f}, D = {d:.6f}")
print(f"A = {a:.1f}, B = {b:.1f}")
print(f"C = {c:.1f}, D = {d:.1f}")
print(f"A = {a:.2f}, B = {b:.2f}")
print(f"C = {c:.2f}, D = {d:.2f}")
print(f"A = {a:.3f}, B = {b:.3f}")
print(f"C = {c:.3f}, D = {d:.3f}")
print(f"A = {a:.3E}, B = {b:.3E}")
print(f"C = {c:.3E}, D = {d:.3E}")
print(f"A = {int(round(a))}, B = {int(round(b))}")
print(f"C = {int(round(c))}, D = {int(round(d))}")
