"""
    2. Elementos Maiores que 10
Dada a lista valores = [5, 12, 3, 18, 7, 25, 9], imprima apenas os elementos maiores que 10.
Saída esperada:
12
18
25
"""
lista = [5, 12, 3, 18, 7, 25, 9, 15, 44, 24, 9, 11, 0, 0 , 0, 11, 12, 111, 444]
for valor in lista:
    if valor > 10:
        print(valor)