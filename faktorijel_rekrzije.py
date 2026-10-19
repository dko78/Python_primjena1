# 1) Napišite funkciju proizvoljnog imena koja prima proizvoljnu pozitivnu
# cjelobrojnu vrijednost. Rezultat je zbroj svih brojeva od 1 do primljene
# vrijednosti. Na primjer, ako funkcija primi vrijednost 5, u pozivajući dio
# programa mora se vratiti vrijednost 1+2+3+4+5 = 15 . Ovo je potrebno
# implementirati pomoću rekurzivne funkcije.

def rekurzivni_zbroj(n):
    if n == 1:#bazni slučaj
        return 1
    return n + rekurzivni_zbroj(n - 1)


broj = int(input("Unesite pozitivan cijeli broj: "))

if broj <= 0:
    print("Greška: broj mora biti pozitivan cijeli broj.")
else:
    rezultat = rekurzivni_zbroj(broj)
    print("Rezultat:", rezultat)
