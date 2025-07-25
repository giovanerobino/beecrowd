Beecrowd | 2759

# Entrada e Saída de Carácter

## Descrição

O seu professor gostaria de fazer um programa com as seguintes características:

1. Crie 3 variáveis para armazenar um único carácter;
2. Leia um valor carácter para a primeira variável;
3. Leia um valor carácter para a segunda variável;
4. Leia um valor carácter para a terceira variável;
5. Imprima a letra A, um espaço em branco, o sinal de igual, um espaço em branco, o carácter armazenado na primeira variável lida no passo 2, uma virgula, um espaço em branco, a letra B, um espaço em branco, o sinal de igual, um espaço em branco, o carácter armazenado na segunda variável lida no passo 3, a letra C, um espaço em branco, o sinal de igual, um espaço em branco, o carácter armazenado na terceira variável lida no passo 4. Não esqueça de pular linha;
6. Imprima a letra A, um espaço em branco, o sinal de igual, um espaço em branco, o carácter armazenado na primeira variável lida no passo 3, uma virgula, um espaço em branco, a letra B, um espaço em branco, o sinal de igual, um espaço em branco, o carácter armazenado na segunda variável lida no passo 4, a letra C, um espaço em branco, o sinal de igual, um espaço em branco, o carácter armazenado na terceira variável lida no passo 2. Não esqueça de pular linha;
7. Imprima a letra A, um espaço em branco, o sinal de igual, um espaço em branco, o carácter armazenado na primeira variável lida no passo 4, uma virgula, um espaço em branco, a letra B, um espaço em branco, o sinal de igual, um espaço em branco, o carácter armazenado na segunda variável lida no passo 2, a letra C, um espaço em branco, o sinal de igual, um espaço em branco, o carácter armazenado na terceira variável lida no passo 3. Não esqueça de pular linha.

## Entrada

A entrada consiste vários arquivos de teste. Em cada arquivo de teste tem três linhas. Na primeira linha tem uma variável **A** que armazena um valor carácter. Na segunda linha tem uma variável **B** que armazena um valor carácter. Na terceira linha tem uma variável **C** que armazena um valor carácter. Conforme mostrado no exemplo de entrada a seguir.

## Saída

Para cada arquivo da entrada, terá um arquivo de saída. O arquivo de saída tem três linhas da forma descrita nos itens 5, 6 e 7. Conforme mostra o exemplo de saída a seguir.

## Exemplos

```
Entrada 1:
a
b
c

Saída 1:
A = a, B = b, C = c
A = b, B = c, C = a
A = c, B = a, C = b

Entrada 2:
0
1
2

Saída 2:
A = 0, B = 1, C = 2
A = 1, B = 2, C = 0
A = 2, B = 0, C = 1
```

## Para testar

```bash
python 2759.py < input1.txt
```

## Links

- Problema: https://resources.beecrowd.com/repository/UOJ_2759.html
- Site principal: https://judge.beecrowd.com/pt/problems/view/2759
