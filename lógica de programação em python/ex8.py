"""
    9. Sequência de Fibonacci
Escreva um programa que gere os N primeiros termos da sequência de Fibonacci usando while.
Na sequência de Fibonacci, cada termo é a soma dos dois anteriores: 0, 1, 1, 2, 3, 5, 8, 13...
Exemplo de saída:
Quantos termos da sequência de Fibonacci? 8
0
1
1
2
3
5
8
13
"""
sequencia = 8
a = 0
b = 1
c = 0
while c <= sequencia:
    print(a) #0; 1;1;2
    prox = b + a #0+1; 1;2;2+1;;3+2
    a =  b # 1;1;2
    b = prox #1;2;3
    c+=1
    
    
