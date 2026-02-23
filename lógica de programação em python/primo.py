a = int(input('Digite o início do intervalo: '))
b = int(input('Digite o fim do intervalo: '))

primos = []

for n in range(a, b + 1):
    if n > 1:
        eh_primo = True

        for divisor in range(2, n):
            if n % divisor == 0:
                eh_primo = False
                break

        if eh_primo:
            primos.append(n)

print(f'Números primos no intervalo [{a}, {b}]:')
print(primos)
