"""
2. Tabuada do 3
Crie um programa que imprima a tabuada do 3, de 3×1 até 3×10, usando while.
Saída esperada:
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
...
3 x 10 = 30
"""
print('Tabuada do 3')
t = 3
i = 0
while i <= 10:
    print(f'{t} X {i} = {t*i}')
    i = i +1