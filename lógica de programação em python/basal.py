"""Homens
TMB = 66,5 + (13,75 × peso em kg) + (5,0 × altura em cm) − (6,75 × idade em anos)

Mulheres
TMB = 655 + (9,56 × peso em kg) + (1,85 × altura em cm) − (4,67 × idade em anos) """
def basalMan(peso, altura, idade):
    return 66.5 + (13.75 * peso) + (5 * altura) - (6.75 * idade)

def basalWoman(peso, altura, idade):
    return 665 + (9.56 * peso) + (1.85 * altura) - (4.67 * idade)
validador = False
while (not validador):
    try:
        peso = float(input('Digite seu peso kg.g: '))
        validador = True
    except ValueError:
        print('Digite somente números.')
validador = False
while(not validador):
    try:
        metros = float(input('Digite sua altura m.cm: '))
        validador = True
    except ValueError:
        print('Somente números')
idade = int(input('Digite sua idade: '))
sexo = input('Digite seu sexo m ou f: ').lower()
altura = metros * 100
if sexo == 'm':
   resul = basalMan(peso, altura, idade)
   print(resul)


    