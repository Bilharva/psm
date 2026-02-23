"""
6. Maior e Menor Elemento
Escreva um programa que encontre e imprima o maior e o menor elemento de uma lista sem usar as funções max() e min(). Use apenas for.
Exemplo com lista valores = [34, 12, 67, 23, 89, 5, 45]:
Maior elemento: 89
Menor elemento: 5
"""
lista = [34, 12, 67, 23, 89, 5, 45]
maior = lista[0]
menor = lista[0]
for valor in lista:
    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor


print('Array com todos os valores: ', lista)
print(f'Maior número: {maior}')
print(f'Menor número: {menor}')
