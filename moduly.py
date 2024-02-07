# import time

# print("Tekst")
# time.sleep(2)
# print("Kolejny tekst")

import pygame

pygame.init()
WIELKOŚĆ_EKRANU = (800, 600)
ekran = pygame.display.set_mode(WIELKOŚĆ_EKRANU)
x = 400
y = 300

while True:
  	for event in pygame.event.get():
  		if event.type == pygame.QUIT:
  			pygame.quit()
  		if event.type == pygame.KEYDOWN:
  			if event.key == pygame.K_RIGHT:
  				x += 5
  	ekran.fill((255,0,0))
  	pygame.draw.circle(ekran, (0,0,0), (x,y), 20, 2)
  	print(event)
  	pygame.display.update()


