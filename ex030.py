import math

n = int(input('Digite um número inteiro.'))
d = n % 2
if d == 1:
    print('\nO número {}, que você digitou, é um número \033[31mímpar!\033[m'.format(n))
else:
    print('\nO número {}, que você digitou, é um número \033[32mpar!\033[m'.format(n))
