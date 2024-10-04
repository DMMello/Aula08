import os
os.system("cls")


def calcula(x):
    dobro = x * 2
    triplo = x * 3
    return dobro, triplo


# parte principal
num = float(input('Informe o número para ser calculado: '))
x2, x3 = calcula(num)

print(f'O dobro e {x2} e o triplo e {x3}')

