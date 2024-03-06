import random

# tworzymy pustą listę, do której będziemy wrzuca losowe liczby
losowe_liczby = []


# ta pętla wykona się _____ razy
for i in range(20):
	# za każdym razem będzimy dodawa do pętli nową liczbę używając funkcji .append()
	losowe_liczby.append(random.randint(0,100))

# Zadanie: zmiencie kod w 10 linijce tak, aby losował liczbę nie od 0, ale od numeru liczby któą dodajemy
# czyli jeżeli do listy wrzucamy liczbę po raz pierwszy liczba będzie z przedziału random.randint(1,100)
# po raz drugi: random.randint(2, 100)
# po raz trzeci: random.randint(3, 100)
# po raz czwarty: random.randint(4, 100)
# itd...


# ta pętla będzie wypisywała kolejne liczby z listy pod sobą
for liczba in losowe_liczby:
	print(liczba)

# Zadanie: zmiencie druga petle tak, aby wypisywała liczby tylko, jezeli będą większe od 50