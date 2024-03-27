import pygame


pygame.init()

# przygotowujemy ekran
WIELKOŚĆ_EKRANU = (800, 600)
ekran = pygame.display.set_mode(WIELKOŚĆ_EKRANU)

FPS = 5
zegar = pygame.time.Clock()

x = 100
y = 100

while True:
	for event in pygame.event.get():
  		if event.type == pygame.QUIT:
  			pygame.quit()
  			quit()

  

	ekran.fill((255,255,255))

	klawisz = pygame.key.get_pressed()
	print(klawisz)

	pygame.draw.rect(ekran, (0,0,255), (x, y, 30, 30)) # (ekran, (kolor), (x, y, dlugosc, szerokosc))
	x = x+30


	pygame.display.update()
	zegar.tick(FPS)