# Exercício Python 02: Faça um programa que leia o comprimento do cateto oposto
# E do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.

from math import hypot

cateto_op = float(input('Comprimento do cateto oposto: '))
cateto_adj = float(input('Comprimento do cateto adjacente: '))
hipot = hypot(cateto_op, cateto_adj)

print('A hipotenusa vai medir: {:.3f}'.format(hipot))
