# DOWNLOAD ex028.mp3 and ex028B.mp3
from random import randint
from time import sleep
import pygame
print('\033[1;30;41m-=-\033[m' * 4)
print('\033[1;30;41mO Mentalista\033[m')
print('\033[1;30;41m-=-\033[m' * 4)

n = randint(0, 5)
sleep(1)
print("\nEstou pensando em um número...")
sleep(1)
print("\nSerá que você consegue adivinhar em qual número eu pensei?")
sleep(1)
print("\n\033[1;32mVou lhe dar uma dica: É um número entre 0 e 5!\033[m")
nj = int(input('\n\033[7mVamos lá! Tente acertar meu pensamento:\033[m'))
sleep(2)
if nj == n:
    print('\n\033[1;42mUAAAAU! Você conseguiu ler os pensamentos de uma máquina! Parabéns!\033[m')
    pygame.mixer.init()
    pygame.mixer.music.load('ex028.mp3')
    pygame.mixer.music.play()
    sleep(6)
else:
    print('\033[1;30;41mNão, você falhou, como qualquer outro ser humano.\033[m'
          '\n\033[1;30;41mO número que eu pensei foi o {}.\033[m'.format(n))
    pygame.mixer.init()
    pygame.mixer.music.load('ex028B.mp3')
    pygame.mixer.music.play()
    sleep(6)
