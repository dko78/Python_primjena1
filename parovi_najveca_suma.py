# Napišite program koji s tipkovnice učitava cijeli broj n iz intervala [3, 20].
# U slučaju da je unesena vrijednost neispravna, ispisati prikladnu poruku
# na ekran te zatražiti ponovni unos cijelog broja. Nakon učitane
# vrijednosti n, učitajte n parova cijelih brojeva. Nakon što je n parova
# brojeva učitano, ispišite parove brojeva koji imaju najveću sumu.

def ucitaj_n():
    while True:
        unos = input("Unesite cijeli broj n iz intervala [3, 20]: ")
        try:
            n = int(unos)
        except ValueError:
            print("Neispravan unos. Potrebno je unijeti cijeli broj.")
            continue

        if 3 <= n <= 20:
            return n

        print("Neispravan unos. Broj n mora biti u intervalu [3, 20].")


def ucitaj_cijeli_broj(poruka):
    while True:
        unos = input(poruka)
        try:
            return int(unos)
        except ValueError:
            print("Neispravan unos. Potrebno je unijeti cijeli broj.")


def main():
    n = ucitaj_n()

    parovi = []
    for i in range(1, n + 1):
        a = ucitaj_cijeli_broj(f"Unesite prvi broj {i}. para: ")
        b = ucitaj_cijeli_broj(f"Unesite drugi broj {i}. para: ")
        parovi.append((a, b))

    najveca_suma = max(a + b for a, b in parovi)
    najbolji_parovi = [(a, b) for a, b in parovi if a + b == najveca_suma]

    print(f"Parovi s najvećom sumom ({najveca_suma}):")
    for a, b in najbolji_parovi:
        print(a, b)


if __name__ == "__main__":
    main()
