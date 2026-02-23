"""
    . Soma de Dígitos
Escreva um programa que peça um número inteiro e calcule a soma de todos os seus dígitos usando while.
Exemplo de saída:
Digite um número: 1234
A soma dos dígitos de 1234 é 10
Explicação: 1 + 2 + 3 + 4 = 10
"""
n = int(input('Digite um número inteiro: '))
final = 0
soma = 0
while n > 0:
    final = n % 10
    soma += final
    n = n // 10

print(soma)