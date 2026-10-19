# Napišite program koji će od korisnika tražiti dvije vrijednosti. Prva
# vrijednost neka bude neki proizvoljan cijeli broj, a druga vrijednost
# neka bude znamenka od 0 do 9. Kreirajte rekurzivnu funkciju koja će
# odrediti broj pojavljivanja zadane znamenke u zadanom broju.
# Prototip funkcije:
# prebroji(broj , znamenka

def prebroji(broj, znamenka):
    broj = abs(broj)  # da radi i za negativne brojeve

    if broj < 10:
        return 1 if broj == znamenka else 0

    zadnja = broj % 10
    return (1 if zadnja == znamenka else 0) + prebroji(broj // 10, znamenka)


broj = int(input("Unesite cijeli broj: "))
znamenka = int(input("Unesite znamenku (0-9): "))

if 0 <= znamenka <= 9:
    rezultat = prebroji(broj, znamenka)
    print(f"Znamenka {znamenka} se pojavljuje {rezultat} puta.")
else:
    print("Greška: druga vrijednost mora biti znamenka od 0 do 9.")