"""
. Conversão Decimal para Binário
Escreva um programa que converta um número decimal para binário usando apenas estruturas de repetição (sem usar bin()).
O algoritmo consiste em dividir sucessivamente por 2 e guardar os restos.
Exemplo de saída:
Digite um número decimal: 13
O número 13 em binário é 1101
Dica: 13 ÷ 2 = 6 resto 1, 6 ÷ 2 = 3 resto 0, 3 ÷ 2 = 1 resto 1, 1 ÷ 2 = 0 resto 1
"""
n = int(input('Digite um número em decimal: '))
binario = []
while n > 0:
    resto = n % 2
    binario.append(resto)
    n = n//2

binario.reverse()
print(binario)
    