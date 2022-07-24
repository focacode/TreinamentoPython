#import math
#ang = float(input('digite um angulo: '))
#sen = math.cos(ang)
#cos = math.sin(ang)
#tan = math.tan(ang)

#print('Para o angulo de {}º, o sen é {}, o cos é {} e a tan é {}' .format(ang, sen, cos, tan))

'''from math import sin, cos, tan
ang = float(input('digite um angulo: '))
sen = sin(ang)
coseno = cos(ang)
tang = tan(ang)
print('para o angulo de {}º, temos um seno de {}, um cosseno de {} e uma tangente de {}' .format(ang, sen, coseno, tang))'''

'''aqui já começamos a usar a conversão para radianos
import math
ang = float(input(' digite um angulo: '))
sen = math.sin(math.radians(ang))
print('para o angulo {}º, o seno é {:.2f}' .format(ang, sen))
cos = math.cos(math.radians(ang))
print('o coseno é {:.2f}' .format(cos))
tang = math.tan(math.radians(ang))
print('a tangente é {:.2f}' .format(tang))'''

from math import radians, sin, cos, tan
ang = float(input('digite um angulo: '))
sen = sin(radians(ang))
print('para o angulo {}º, temos o seno {}' .format(ang, sen))
cos = cos(radians(ang))
print('o coseno é {}' .format(cos))
tang = tan(radians(ang))
print('a tangente é {}' .format(tang))

