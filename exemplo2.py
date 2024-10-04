import os
os.system('cls')
# biblioteca para numeros aleatorios
import random

def gera_num(inicio,final,quantidade):
    return [random.randint(inicio,final) for _ in range(quantidade)]
    
   
inicio = int(input('Informe o numero inicial :'))
final = int(input('Informe o numero final :'))
quantidade = int(input('Quantos números voce quer gerar :'))

numeros = gera_num(inicio,final,quantidade)

print("Números ordenados:", numeros)

