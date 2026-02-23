"""
    5. Filtrando Múltiplos
Crie um programa que, dada uma lista de números inteiros, crie uma nova lista contendo apenas os múltiplos de 3 da lista original. Imprima ambas as listas.
Exemplo com lista numeros = [12, 7, 9, 15, 4, 18, 22, 6]:
Lista original: [12, 7, 9, 15, 4, 18, 22, 6]
Múltiplos de 3: [12, 9, 15, 18, 6]
"""
lista = [12, 7, 9, 15, 4, 18, 22, 6]
multiplosDe3 = []
for valores in lista:
    if valores % 3 == 0:
        multiplosDe3.append(valores)
        
print(multiplosDe3)