reta1 = float(input('Qual é a medida da primeira reta?'))
reta2 = float(input('Qual é a medida da segunda reta?'))
reta3 = float(input('Qual é a medida da terceira reta?'))
som1e2 = reta1 + reta2 > reta3
som2e3 = reta2 + reta3 > reta1
som3e1 = reta3 + reta1 > reta2
if som1e2 == True and som2e3 == True and som3e1 == True:
    print('Essas retas podem formar um triângulo!')
else:
    print('Essas retas não formam um triângulo!')
