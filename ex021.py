import pygame 

#iniciando o pygame
pygame.init() 

#escolhendo a música
pygame.mixer.music.load('FreshPastries.mp3') 

#play na música
pygame.mixer.music.play()
input()

#espera o evento (a música) terminar para encerrar o programa
pygame.event.wait