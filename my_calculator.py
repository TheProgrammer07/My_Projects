import pygame,sys
pygame.init()

weight = 800
height = 600
win_size = (800,600)

window = pygame.display.set_mode(win_size)

while True:
  for i in pygame.event.get():
    if i.type == pygame.QUIT:
      sys.exit()
      
  pygame.display.update()
