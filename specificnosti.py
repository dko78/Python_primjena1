lista = [1, 2, 3, 4, 5]

#print(lista.reverse())  # Ispisuje None jer metoda reverse() ne vraća novu listu, već mijenja originalnu listu
#lista.reverse()  # Mijenja originalnu listu tako da je obrnuta
#print("Lista:", lista)  # Ispisuje obrnutu verziju originalne liste
lista2 = lista[::-1]  # 
print("lista2", lista2)  # Ispisuje novu listu koja je obrnuta verzija originalne liste


# 1) Napišite program unutar kojeg ćete u varijablu inicijalizirati listu proizvoljnog
# sadržaja (lista od barem 3 vrijednosti). Elemente liste spremite u pojedinačne
# varijable u jednoj liniji. Nakon što elemente liste imate spremljene u
# zasebnim varijablama, ispišite vrijednosti tih varijabli.

lista = [10, "Python", 3.14]

a, b, c = lista  # spremanje elemenata liste u varijable u jednoj liniji

print(a)
print(b)
print(c)

# 2) U dvije varijable inicijalizirajte dva različita proizvoljna broja. Nakon
# inicijalizacije ispišite vrijednosti varijabli na zaslon. Zamijenite vrijednosti
# tih dviju varijabli te ponovo ispišite njihove nove vrijednosti.
# 
a = 5
b = 12

print("Prije zamjene:")
print("a =", a)
print("b =", b)

a, b = b, a  # zamjena vrijednosti

print("Nakon zamjene:")
print("a =", a)
print("b =", b)

# 3) S tipkovnice učitajte broj proizvoljne vrijednosti. Za tako učitan broj
# provjerite zadovoljava li on uvjet: 10 < broj < 30 , ako je uvjet
# zadovoljen, ispišite na ekran: "Zadovoljava!", ako pak uvjet nije
# zadovoljen, ispišite na ekran: "Ne zadovoljava!". Ovaj zadatak potrebno je
# riješiti korištenjem operatora usporedbe, bez korištenja logičkih operatora i
# logičkih izraza.
broj = float(input("Unesite broj: "))

if broj > 10:
    if broj < 30:
        print("Zadovoljava!")
    else:
        print("Ne zadovoljava!")
else:
    print("Ne zadovoljava!")

# 4) Kreirajte listu te ju popunite s 5 proizvoljnih vrijednosti ( brojeva). Potom
# učitajte proizvoljan broj s tipkovnice. Unutar petlje for provjerite nalazi li
# se učitana vrijednost unutar liste. Ako tražena vrijednost (broj) postoji u
# listi, ispišite na ekran "Postoji!", u suprotnom ispišite na ekran "Ne
# postoji !". U ovom zadatku iskoristite for/else konstrukt.    
lista4 = [4, 8, 15, 16, 23]

trazeni_broj = float(input("Unesite broj: "))

for broj in lista4:
    if broj == trazeni_broj:
        print("Postoji!")
        break
else:
    print("Ne postoji!")

# 5)    S tipkovnice učitajte broj proizvoljne vrijednosti. Pomoću ternarnog
# operatora detektirajte je li učitani broj paran ili neparan. Ako je učitani broj
# paran, ispišite na ekran: "Paran!", ako pak je neparan, ispišite na ekran:
# "
broj = int(input("Unesite broj: "))

rezultat = "Paran!" if broj % 2 == 0 else "Neparan!"
print(rezultat)

# 6) Implementirajte dvije funkcije. Prva funkcija neka se zove paran() i ona
# neka ispisuje na ekran: "Paran!", druga funkcija neka se zove neparan()
# i ona neka ispisuje na ekran: "Neparan!". S tipkovnice učitajte broj
# proizvoljne vrijednosti te pomoću ternarnog operatora detektirajte je li
# učitana vrijednost parna ili neparna te ovisno o parnosti pozovite jednu od
# dviju funkcija koje ste prethodno kreirali.

def paran():
    print("Paran!")

def neparan():
    print("Neparan!")

broj = int(input("Unesite broj: "))

(paran if broj % 2 == 0 else neparan)()

# 7) Implementirajte funkciju prototipa rezultat(var1, var2), funkcija može
# primiti dvije vrijednosti. Tako kreirana funkcija neka u pozivajući dio
# programa vraća tri vrijednosti dobivene sljedećim aritmetičkim
# operacijama: var1*var2, var1+var2, 10*var1+var2. U glavnom dijelu
# programa pozovite prethodno implementiranu funkciju te njene povratne
# vrijednosti spremite u tri zasebne varijable proizvoljnog imena i ispišite
# ih.

def rezultat(var1, var2):
    return var1 * var2, var1 + var2, 10 * var1 + var2


a = int(input("Unesite prvu vrijednost: "))
b = int(input("Unesite drugu vrijednost: "))

umnozak, zbroj, kombinacija = rezultat(a, b)# to je tupple?

print("var1 * var2 =", umnozak)
print("var1 + var2 =", zbroj)
print("10 * var1 + var2 =", kombinacija)

#8
niz = ["Hello World"]
print(niz[0], niz[::-1])