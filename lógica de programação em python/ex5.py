"""
    6. Progressão Geométrica (PG)
Escreva um programa que exiba os termos de uma PG dado o primeiro termo, a razão e o número de termos. Na PG, cada termo é: a_n = a_1 × r^(n-1)
Exemplo de saída:
Primeiro termo da PG: 2
Razão: 3
Número de termos: 5
2
6
18
54
162
"""
pg = 2
razao = 3
num_termos = 5
i = 1
while i <= num_termos:
    print(pg)
    pg*= razao
    i+=1