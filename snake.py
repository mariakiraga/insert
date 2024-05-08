import pygame


pygame.init()

# przygotowujemy ekran
SZEROKOSC_EKRANU = 800
WYSOKOSC_EKRANU = 600
WIELKOŚĆ_EKRANU = (SZEROKOSC_EKRANU, WYSOKOSC_EKRANU)
ekran = pygame.display.set_mode(WIELKOŚĆ_EKRANU)

FPS = 60
zegar = pygame.time.Clock()


font = pygame.font.Font('freesansbold.ttf', 32)
tekst = font.render('GAME OVER', True, (0,0,255), (255,0,0))
tekstRect = tekst.get_rect(center = (SZEROKOSC_EKRANU/2, WYSOKOSC_EKRANU/2-200))

# tekst2
# tekstRect2

# tekst3
# tekstRect3

szer = 20
x = [100, 100-szer, 100-2*szer, 100-3*szer]
y = [100, 100, 100, 100]
kierunek = "prawo"

sciezka = "jablko.png"
jablko = pygame.image.load(sciezka)
xj = SZEROKOSC_EKRANU/2
yj = WYSOKOSC_EKRANU/2

def jedzenie():
	global xj, yj

	zla_pozycja = True

	while zla_pozycja:
		xj = random.randint(0, SZEROKOSC_EKRANU / szer - 1) * szer
		yj = random.randint(0, WYSOKOSC_EKRANU / szer - 1) * szer

		zla_pozycja = False

		for i in range(len(x)-1):
			if x[i] == xj and y[i] == yj:
				zla_pozycja = True

def kolizja():
	global x, y, xj, yj

	if x[0] == xj and y[0] == yj:
		jedzenie()


gramy = True
game_over = False

klatki = 0
szybkosc = 3

while gramy:
	for event in pygame.event.get():
  		if event.type == pygame.QUIT:
  			pygame.quit()
  			quit()

  

	ekran.fill((255,255,255))
	ekran.blit(jablko, (xj,yj))

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


	


	if x[0] <= 0 or x[0]+50 >= SZEROKOSC_EKRANU or y[0] <= 0 or y[0]+50 >= WYSOKOSC_EKRANU:
		gramy = False
		game_over = True

	if klatki == szybkosc:
		for i in range(len(x)-1, 0, -1):
			x[i] = x[i-1]
			y[i] = y[i-1]

		if kierunek == "prawo":
			x[0] = x[0] + 30
		if kierunek == "lewo":
			x[0] = x[0] - 30
		if kierunek == "góra":
			y[0] = y[0] - 30
		if kierunek == "dół":
			y[0] = y[0] + 30

		klatki = 0

	for i in range(len(x)):

		pygame.draw.rect(ekran, (0,0,255), (x[i], y[i], 30, 30)) # (ekran, (kolor), (x, y, dlugosc, szerokosc))
		


	klatki += 1
	print(klatki)
	
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