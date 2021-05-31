n1 = float(input('Digite um número:'))
n2 = float(input('Digitou outro número:'))
n3 = float(input('Digite um último número:'))
lista = [n1, n2, n3]
print('O menor número dos que você digitou é o {:.0f}.'.format(min(lista)))
print('O maior número dos que você digitou é o {:.0f}.'.format(max(lista)))
