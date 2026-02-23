"""
. Pares Ordenados de Função
Solicite ao usuário dois valores (a e b) que representam um intervalo [a, b]. Use for e range() para calcular e exibir os pares (x, f(x))
onde f(x) = 2x² - 3x + 1.
Exemplo com a = 0 e b = 4:
Extremo esquerdo: 0
Extremo direito: 4
(0, 1)
(1, 0)
(2, 3)
(3, 10)
(4, 21)
"""
def f(x):
    return 2 * x**2 - 3 * x + 1
a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))
for i in range(a, b+1):
    resul = f(i)
    print(f'({i}, {resul})')
    
