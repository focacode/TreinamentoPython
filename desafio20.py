'''import random

nome1 = str(input('  Digite o primeiro nome:     '))
nome2 = str(input('  Digiteo segundo nome:     '))
nome3 = str(input('  Digite o terceiro nome:     '))
nome4 = str(input('  Digite o quarto nome:     '))
lista = [nome1,nome2,nome3,nome4]
random.shuffle(lista)

print('a ordem que vão apresentar será ')
print(lista)'''

from random import shuffle
n1 = str(input('digite o primeiro nome: '))
n2 = str(input('digite o segundo nome: '))
n3 = str(input('digite o terceiro nome: '))
n4 = str(input('digite o quarto nome: '))

lista = [n1, n2, n3, n4]
shuffle(lista)

print('A ordem de apresentação é: ')
print(lista)