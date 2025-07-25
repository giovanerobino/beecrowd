"""
beecrowd | 2760
Entrada e Saída de String

O seu professor gostaria de fazer um programa com as seguintes características:
1. Crie 3 variáveis para armazenar uma frase de no máximo 100 caracteres;
2. Leia uma frase para a primeira variável;
3. Leia uma frase para a segunda variável;
4. Leia uma frase para a terceira variável;
5. Imprima a primeira variável lida no passo 2, a segunda variável lida no passo 3, 
a terceira variável lida no passo 4. Não esqueça de pular linha;
6. Imprima a primeira variável lida no passo 3, a segunda variável lida no passo 4, 
a terceira variável lida no passo 2. Não esqueça de pular linha;
7. Imprima a primeira variável lida no passo 4, a segunda variável lida no passo 2, 
a terceira variável lida no passo 3. Não esqueça de pular linha;
8.Repita o procedimento 5, imprimindo só 10 caracteres de cada variável.

Entrada
A entrada consiste vários arquivos de teste. Em cada arquivo de teste tem três linhas. 
Na primeira linha tem uma variável A que armazena uma frase de no máximo 100 caracteres. 
Na segunda linha tem uma variável B que armazena uma frase de no máximo 100 caracteres. 
Na terceira linha tem uma variável C que armazena uma frase de no máximo 100 caracteres. 
Conforme mostrado no exemplo de entrada a seguir.

Saída
Para cada arquivo da entrada, terá um arquivo de saída. O arquivo de saída tem quatro 
linhas da forma descrita nos itens 5, 6, 7 e 8. Conforme mostra o exemplo de saída a seguir.

ExemplodeEntrada    ExemplodeSaída
Roberto             RobertoCarlosAldo
Carlos              CarlosAldoRoberto
Aldo                AldoRobertoCarlos
                    RobertoCarlosAldo

aaaa bbbb cccc      aaaa bbbb ccccccccxxxxx xxxx xx
cccc                ccccxxxxx xxxx xxaaaa bbbb cccc
xxxxx xxxx xx       xxxxx xxxx xxaaaa bbbb cccccccc
                    aaaa bbbb ccccxxxxx xxxx

"""
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
