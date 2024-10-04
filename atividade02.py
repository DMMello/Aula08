import os
# os.system('cls')
import random

def limpa_tela():
    os.system('cls')

def decoracao():
    print(15*'-')

def calcula_peso(peso,REG):
    max = peso - REG
    pgto = max * MULTA
    return pgto
    
#Inicio do programa
print('Inicio do programa')

limpa_tela()
REG = 100
MULTA = 4

peso = float(input('Informe o peso do peixe :'))

limpa_tela()
decoracao()
if peso >= REG:
    x = calcula_peso(peso,REG)
    print(f'Limite de Peso Excedido: {peso}kg')
    print(f'Valor da multa: R${x}')
else:
    print(f'Valor dentro do Regulamento: {peso}kg')
decoracao()