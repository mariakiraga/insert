# importujemy moduły, z których będziemy korzystac
import pygame
import random

# inicjujemy pygame
pygame.init()

# przygotowujemy ekran
WIELKOŚĆ_EKRANU = (800, 600)
ekran = pygame.display.set_mode(WIELKOŚĆ_EKRANU)

####################### KLASA KULKI #######################

# Kulki to nazwa klasy, którą będziemy posługiwa się później, aby narysowac kulkę na naszym ekranie
class Kulki: 
	# W nawiasie podajemy wybrane przez nas wlasnosci kazdej kulki
	# dla naszej klasy Kulki są to: x, y (pozycja na ekranie), promien (czyli rozmiar kulki), kolor
	def __init__(self,x,y,promien,kolor): 
		self.x = x
		self.y = y
		self.promien = promien
		self.kolor = kolor

	def rysuj(self):
		# Zauważcie, że w funkcji pygame do rysowania kulki wlasnosci sa w innej kolejnosci niz przy tworzeniu naszych kulek
	 	pygame.draw.circle(ekran, self.kolor, (self.x, self.y), self.promien) 

###########################################################


# tworzymy pierwsza kulkę
# na naszym ekranie powinna pojawic się w
# x:
# y:
# rozmiarze:
# kolorze:
kulka1 = Kulki(20, 30, 10, (0,0,0))

# druga kulka, którą tworzymy pojawi się obok pierwszej kuli, ale losowym kolorze
losowy_kolor = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
# na naszym ekranie powinna pojawic się w
# x:
# y:
# rozmiarze:
kulka2 = Kulki(60, 30, 10, losowy_kolor)

# stwórzcie kulkę w losowym x, losowym y, losowym rozmiarze i losowym kolorze

# LISTA KULEK

#################### GŁÓWNA PĘTLA GRY ####################
while True:

	###
	# pętla odpowiedzialna za różne wydarzenia w okienku (ekranie) i na klawiaturze
	for event in pygame.event.get():
  		if event.type == pygame.QUIT:
  			pygame.quit()
  			quit()

  	###

  	# wypełniamy tło ekranu
	ekran.fill((255,255,255))
	
	# po stworzeniu kulek tak jak to zrobiliśmy wyżej jeszcze nie zostaną narysowane w nasyzm okienku
	# musimy wywoła funkcję rysuj() dla każdej z nich
	kulka1.rysuj()
	kulka2.rysuj()

	# na koniec głównej pętli odświeżamy ekran
	pygame.display.update()
###########################################################