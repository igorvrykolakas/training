km = int(input('Em qual velocidade o carro estava em km/h?'))
if km > 80:
    print('\033[1;41mVocê recebeu uma multa no valor de R${}.\033[m\n\033[1;41mDirija sempre com cuidado!\033[m'.format((km - 80) * 7))
else:
    print('\033[1;42mTudo bem, você não recebeu uma multa.\033[m\n\033[1;42mDirija sempre com cuidado!\033[m')
