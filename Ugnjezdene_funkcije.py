
# Isprobajte korištenje ugniježđenih funkcija. Vanjska funkcija imena
# izracun neka prima dva parametra. Unutar vanjske funkcije
# kreirajte dvije unutarnje funkcije imena parniZbroj i
# neparniZbroj ()(). Funkcija parniZbroj neka vraća rezultat
# matematičke formule 2*a+5*b , a funkcija neparniZbroj neka
# vraća rezultat matematičke formule a*b - 10 . Koja će se od dviju
# unutarnjih funkcija pozvati, neka se odredi na temelju parnosti zbroja
# primljenih parametara a+b . U glavnom programu na zaslon ispisati
# rezultat.


def izracun(a, b):
    def parniZbroj():
        return 2 * a + 5 * b

    def neparniZbroj():
        return a * b - 10  # ako treba drugačiji operator, lako promijenimo

    return parniZbroj() if (a + b) % 2 == 0 else neparniZbroj()


# Glavni program
a = int(input("Unesite a: "))
b = int(input("Unesite b: "))

rezultat = izracun(a, b)
print("Rezultat:", rezultat)