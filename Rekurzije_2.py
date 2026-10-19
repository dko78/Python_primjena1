# Napišite program koji će s tipkovnice učitati jednu proizvoljnu
# cjelobrojnu vrijednost. Za tako učitani cijeli broj prebrojite i ispišite
# koliko se parnih znamenki nalazi u njemu. Prebrojavanje parnih
# znamenki napravite pomoću rekurzivne funkcije. Na primjer, za broj
# 12345, potrebno je na zaslon ispisati vrijednost 2

def broj_parnih_znamenki(n):
    n = abs(n)  # da radi i za negativne brojeve

    if n < 10:
        return 1 if n % 2 == 0 else 0

    zadnja = n % 10
    return (1 if zadnja % 2 == 0 else 0) + broj_parnih_znamenki(n // 10)


broj = int(input("Unesite cijeli broj: "))
print("Broj parnih znamenki je:", broj_parnih_znamenki(broj))