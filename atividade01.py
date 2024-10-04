import os
# os.system('cls')
import random

def limpa_tela():
    os.system('cls')

def decoracao():
    print(15*'-')

def num_aleat():
    n1 = random.randint(1,100)
    n2 = random.randint(1,100)
    return (n1,n2)

def somar(a, b):
    return a + b
    
def diminuir(a,b):
    return a - b

def mult(a,b):
    return a * b

def div(a,b):
    return float(a / b)

a, b = num_aleat() 

soma = somar(a,b)
dim = diminuir(a,b)
mul = mult(a,b)
di = div(a,b)


limpa_tela()
decoracao()
print(a,b)
print("Soma", soma)
print("Diminuir", dim)
print("Mult", mul)
print("Divisao", di)
decoracao()


# #inicio_do_programa
# limpa_tela()
# decoracao()
# print('calculadora')
