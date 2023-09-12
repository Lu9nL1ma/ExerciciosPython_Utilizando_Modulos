# Exercício Python 01: Crie um programa que leia um número Real qualquer pelo teclado
# E mostre na tela a sua porção Inteira.

import math

numero = float(input('Digite um número real: '))
real = math.trunc(numero)

print('O valor digitado foi {} e sua porção inteira é: {}'.format(numero, real))
