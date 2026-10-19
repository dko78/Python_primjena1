def zbrajanje(a, b):
    return a + b


def oduzimanje(a, b):
    return a - b


def mnozenje(a, b):
    return a * b


def dijeljenje(a, b):
    if b == 0:
        return "Greška: dijeljenje s nulom nije dozvoljeno."
    return a / b


def ucitaj_broj(poruka):
    while True:
        unos = input(poruka)
        try:
            return float(unos)
        except ValueError:
            print("Neispravan unos. Unesite broj.")


def main():
    while True:
        print("Odaberite računsku operaciju:")
        print("1 zbrajanje")
        print("2 oduzimanje")
        print("3 množenje")
        print("4 dijeljenje")
        print("0 izlaz iz programa")

        odabir = input("Unesite broj željene operacije: ")

        if odabir == "0":
            print("Izlaz iz programa.")
            break

        if odabir not in {"1", "2", "3", "4"}:
            print("Nepostojeća operacija. Pokušajte ponovno.\n")
            continue

        prvi_broj = ucitaj_broj("Unesite prvu vrijednost: ")
        drugi_broj = ucitaj_broj("Unesite drugu vrijednost: ")

        if odabir == "1":
            rezultat = zbrajanje(prvi_broj, drugi_broj)
        elif odabir == "2":
            rezultat = oduzimanje(prvi_broj, drugi_broj)
        elif odabir == "3":
            rezultat = mnozenje(prvi_broj, drugi_broj)
        else:
            rezultat = dijeljenje(prvi_broj, drugi_broj)

        print(f"Rezultat: {rezultat}\n")


if __name__ == "__main__":
    main()
