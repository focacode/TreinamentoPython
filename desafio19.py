'''import random
lista = str(input('digite o nome do 1º aluno:')), str(input('digite o nome do 2º aluno:')), str(input('digite o nome do 3º aluno:')), str(input('digite o nome do 4º aluno:'))

print('os alunos que serão sorteados são:', lista)

print(' o aluno {} foi o sorteado'.format(random.choice(lista)))'''

'''import random
a1 = str(input('nome do 1º aluno: '))
a2 = str(input('nome do 2º aluno: '))
a3 = str(input('nome do 3º aluno: '))
a4 = str(input('nome do 4º aluno: '))
lista = [a1, a2, a3, a4]
escolha = random.choice(lista)

print('o aluno escolhido foi {}' .format(escolha))'''

from random import choice

a1 = str(input('nome do 1º aluno:'))
a2 = str(input('nome do 2º aluno:'))
a3 = str(input('nome do 3º aluno:'))
a4 = str(input('nome do 4º aluno:'))
lista = [a1, a2, a3, a4]
escolha = choice(lista)

print('o escolhido foi {}' .format(escolha))

