km = int(input('Quantos km terá sua viagem?'))
if km <= 200:
    print('\nSua passagem de ônibus vai custar \033[7mR${}.\033[m'.format(km * 0.50))
else:
    print('\nSua passagem de ônibus vai custar \033[7mR${}.\033[m'.format((km * 0.45)))
