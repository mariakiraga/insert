import pygame


pygame.init()

# przygotowujemy ekran
SZEROKOSC_EKRANU = 800
WYSOKOSC_EKRANU = 600
WIELKOŚĆ_EKRANU = (SZEROKOSC_EKRANU, WYSOKOSC_EKRANU)
ekran = pygame.display.set_mode(WIELKOŚĆ_EKRANU)

FPS = 5
zegar = pygame.time.Clock()


font = pygame.font.Font('freesansbold.ttf', 32)
tekst = font.render('GAME OVER', True, (0,0,255), (255,0,0))
tekstRect = tekst.get_rect(center = (SZEROKOSC_EKRANU/2, WYSOKOSC_EKRANU/2-200))

# tekst2
# tekstRect2

# tekst3
# tekstRect3


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
	#print(klawisz)


	if klawisz[pygame.K_UP] and kierunek != "dół":
		kierunek = "góra"

	if klawisz[pygame.K_DOWN] and kierunek != "góra":
		kierunek = "dół"

	if klawisz[pygame.K_LEFT] and kierunek != "prawo":
		kierunek = "lewo"

	if klawisz[pygame.K_RIGHT] and kierunek != "lewo":
		kierunek = "prawo"


	if kierunek == "prawo":
		x = x + 30
	if kierunek == "lewo":
		x = x - 30
	if kierunek == "góra":
		y = y - 30
	if kierunek == "dół":
		y = y + 30


	if x <= 0 or x+50 >= SZEROKOSC_EKRANU or y <= 0 or y+50 >= WYSOKOSC_EKRANU:
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
  		if event.type == pygame.MOUSEBUTTONDOWN:
  			pos = pygame.mouse.get_pos()
  			print(pos)


	ekran.fill((255,0,0))

	ekran.blit(tekst, tekstRect)

	pygame.display.update()
	zegar.tick(FPS)