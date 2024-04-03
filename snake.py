import pygame


pygame.init()

# przygotowujemy ekran
WIELKOŚĆ_EKRANU = (800, 600)
ekran = pygame.display.set_mode(WIELKOŚĆ_EKRANU)

FPS = 5
zegar = pygame.time.Clock()

x = 100
y = 100
kierunek = "prawo"

gramy = True
game_over = False

while gramy:
	for event in pygame.event.get():
  		if event.type == pygame.QUIT:
  			pygame.quit()
  			quit()

  

	ekran.fill((255,255,255))

	klawisz = pygame.key.get_pressed()
	print(klawisz)


	if klawisz[pygame.K_UP]:
		kierunek = "góra"

	if klawisz[pygame.K_DOWN]:
		kierunek = "dół"

	if klawisz[pygame.K_LEFT]:
		kierunek = "lewo"

	if klawisz[pygame.K_RIGHT]:
		kierunek = "prawo"


	if kierunek == "prawo":
		x = x + 30
	if kierunek == "lewo":
		x = x - 30
	if kierunek == "góra":
		y = y - 30
	if kierunek == "dół":
		y = y + 30


	if x <= 0 or x+50 >= 800 or y <= 0 or y+50 >= 600:
		gramy = False
		game_over = True





	pygame.draw.rect(ekran, (0,0,255), (x, y, 30, 30)) # (ekran, (kolor), (x, y, dlugosc, szerokosc))



	pygame.display.update()
	zegar.tick(FPS)


while game_over:
	for event in pygame.event.get():
  		if event.type == pygame.QUIT:
  			pygame.quit()
  			quit()

	ekran.fill((255,0,0))

	pygame.display.update()
	zegar.tick(FPS)