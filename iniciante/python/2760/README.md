Beecrowd | 2760

# Entrada e Saída de String

## Descrição

O seu professor gostaria de fazer um programa com as seguintes características:

1. Crie 3 variáveis para armazenar uma frase de no máximo 100 caracteres;
2. Leia uma frase para a primeira variável;
3. Leia uma frase para a segunda variável;
4. Leia uma frase para a terceira variável;
5. Imprima a primeira variável lida no passo 2, a segunda variável lida no passo 3, a terceira variável lida no passo 4. Não esqueça de pular linha;
6. Imprima a primeira variável lida no passo 3, a segunda variável lida no passo 4, a terceira variável lida no passo 2. Não esqueça de pular linha;
7. Imprima a primeira variável lida no passo 4, a segunda variável lida no passo 2, a terceira variável lida no passo 3. Não esqueça de pular linha;
8.Repita o procedimento 5, imprimindo só 10 caracteres de cada variável.

## Entrada

A entrada consiste vários arquivos de teste. Em cada arquivo de teste tem três linhas. Na primeira linha tem uma variável **A** que armazena uma frase de no máximo 100 caracteres. Na segunda linha tem uma variável **B** que armazena uma frase de no máximo 100 caracteres. Na terceira linha tem uma variável **C** que armazena uma frase de no máximo 100 caracteres. Conforme mostrado no exemplo de entrada a seguir.

## Saída

Para cada arquivo da entrada, terá um arquivo de saída. O arquivo de saída tem quatro linhas da forma descrita nos itens 5, 6, 7 e 8. Conforme mostra o exemplo de saída a seguir.

## Exemplos

```
Entrada 1:
Roberto
Carlos
Aldo

Saída 1:
RobertoCarlosAldo
CarlosAldoRoberto
AldoRobertoCarlos
RobertoCarlosAldo

Entrada 2:
aaaa bbbb cccc
cccc
xxxxx xxxx xx

Saída 2:
aaaa bbbb ccccccccxxxxx xxxx xx
ccccxxxxx xxxx xxaaaa bbbb cccc
xxxxx xxxx xxaaaa bbbb cccccccc
aaaa bbbb ccccxxxxx xxxx
```

## Para testar

```bash
python 2760.py < input1.txt
```

## Links

- Problema: https://resources.beecrowd.com/repository/UOJ_2760.html
- Site principal: https://judge.beecrowd.com/pt/problems/view/2760
