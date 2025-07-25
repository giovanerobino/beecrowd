"""
beecrowd | 2761
Entrada e Saída de Vários Tipos

O seu professor gostaria de fazer um programa com as seguintes características:
1. Crie uma variável inteira;
2. Crie uma variável real de simples precisão;
3. Crie uma variável que armazene um carácter;
4. Crie uma variável que armazene uma frase de no máximo 50 caracteres;
5. Leia todas as variáveis na ordem da forma criada;
6. Imprima todas as variáveis como foram lidas;
7. Imprima as variáveis, separando-as por uma tabulação (8 espaços), na ordem que foram lidas;
8. Imprima as variáveis com exatos 10 espaços.

Entrada
A entrada consiste vários arquivos de teste. Em cada arquivo de teste tem uma linha. A linha 
tem uma variável A que armazena um número inteiro, uma variável B que armazena um 
número real, uma variável C com um carácter e uma variável D que armazena uma frase 
de no máximo 50 caracteres. Conforme mostrado no exemplo de entrada a seguir.

Saída
Para cada arquivo da entrada, terá um arquivo de saída. O arquivo de saída tem três linhas da 
forma descrita nos itens 6, 7 e 8. Conforme mostra o exemplo de saída a seguir. Imprima os 
valores de ponto flutuante com 6 casas decimais após a vírgula.

ExemplodeEntrada            ExemplodeSaída
12 3.141560 a Uri online    123.141560aUri online
                            12 3.141560 a Uri online
                            12 3.141560 a Uri online

791 123.141568 | aaa        791123.141571|aaa
                            791 123.141571 | aaa
                            791123.141571 | aaa

"""
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
