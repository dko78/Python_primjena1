# Napišite programski kôd unutar kojeg postoji vjerojatnost da se podigne
# iznimka ValueError . Pokrenite program i namjestite ulazne vrijednosti
# koje će podići iznimku ValueError

# Programski kôd iz prethodnog zadatka nadogradite tako da uhvatite
# iznimku koja se dogodila (napravite da se hvataju sve iznimke, a ne
# selektivno) te na ekran ispišite poruku "Iznimka je uhvaćena!".

# Primjer koda koji MOŽE podići ValueError
# try:
#     unos = input("Unesite cijeli broj: ")
#     broj = int(unos)   # može baciti ValueError
#     print("Unijeli ste:", broj)
# except Exception:
#     print("Iznimka je uhvaćena!")


# Napišite proizvoljni programski kôd unutar kojeg se mogu dogoditi bar
# dvije vrste iznimaka. Selektivno uhvatite iznimke i ispišite koji tip
# iznimke je uhvaćen.    
# Nadogradite prethodni zadatak tako da uz ispis tipa uhvaćene iznimke
# ispišete i detalje (opis) iznimke generirane od strane Pythona

try:
    broj = int(input("Unesite cijeli broj: "))   # može ValueError
    rezultat = 10 / broj                         # može ZeroDivisionError
    print("Rezultat:", rezultat)

except ValueError as e:
    print("Uhvaćena je iznimka tipa ValueError.")
    print("Detalji iznimke:", e)

except ZeroDivisionError as e:
    print("Uhvaćena je iznimka tipa ZeroDivisionError.")
    print("Detalji iznimke:", e)