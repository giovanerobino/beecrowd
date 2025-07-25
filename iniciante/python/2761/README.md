Beecrowd | 2761

# Entrada e Saída de Vários Tipos

## Descrição

O seu professor gostaria de fazer um programa com as seguintes características:
1. Crie uma variável inteira;
2. Crie uma variável real de simples precisão;
3. Crie uma variável que armazene um carácter;
4. Crie uma variável que armazene uma frase de no máximo 50 caracteres;
5. Leia todas as variáveis na ordem da forma criada;
6. Imprima todas as variáveis como foram lidas;
7. Imprima as variáveis, separando-as por uma tabulação (8 espaços), na ordem que foram lidas;
8. Imprima as variáveis com exatos 10 espaços.

## Entrada

A entrada consiste vários arquivos de teste. Em cada arquivo de teste tem uma linha. A linha tem uma variável **A** que armazena um número inteiro, uma variável **B** que armazena um número real, uma variável **C** com um carácter e uma variável **D** que armazena uma frase de no máximo 50 caracteres. Conforme mostrado no exemplo de entrada a seguir.

## Saída

Para cada arquivo da entrada, terá um arquivo de saída. O arquivo de saída tem três linhas da forma descrita nos itens 6, 7 e 8. Conforme mostra o exemplo de saída a seguir. Imprima os valores de ponto flutuante com 6 casas decimais após a vírgula.

## Exemplos

```
Entrada 1:
12 3.141560 a Uri online

Saída 1:
123.141560aUri online
12	3.141560	a	Uri online
        12  3.141560         aUri online

Entrada 2:
791 123.141568 | aaa

Saída 2:
791123.141571|aaa
791	123.141571	|	aaa
       791123.141571         |       aaa

```

## Para testar

```bash
python 2761.py < input1.txt
```

## Links

- Problema: https://resources.beecrowd.com/repository/UOJ_2761.html
- Site principal: https://judge.beecrowd.com/pt/problems/view/2761
