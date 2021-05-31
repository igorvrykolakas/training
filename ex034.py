sal = int(input('Qual o seu salário?'))
if sal >= 1250:
    print('Seu aumento foi de 10%. Seu novo salário será: R${:.0f}.'.format((sal * 0.10) + sal))
else:
    print('Seu aumento de salário foi de 15%. Seu novo salário é R${:.1f}.'.format((sal * 0.15) + sal))
