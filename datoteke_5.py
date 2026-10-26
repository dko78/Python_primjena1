# 8.10.5 medijski_pokazatelji.csv
# CSV datoteka je sljedećeg formata:
# [
# datum mi1 ],[mi2],[mi3],[mi4],[mi5],[mi6],[
# Potrebno je za svaki mjesec izračunati prosjek neizvjesnosti za svih 7
# medija (prosjek zaokružiti na dvije decimale).
# Rezultat spremiti u datoteku imena
# prosjekNeizvjesnosti.txt u
# sljedećem formatu (svaki redak sadrži prosjek za jedan mjesec):
# [datum
# prosjekMedijskeNeizvjesnosti
# Primjer jednog izlaznog retka (rezultat dobiven na temelju zadnje linije
# ulazne datoteke):
# 2020
# 12, 1770.71

ulaz = open("8.10.5-medijski_pokazatelji.csv", "r", encoding="utf-8")
izlaz = open("prosjekNeizvjesnosti.txt", "w", encoding="utf-8")

#čitam ulaznu datoteku 
for linija in ulaz:
    elementi = linija.strip().split(",")
    print(elementi)
    suma = 0
    for i in range(1, len(elementi)):
        suma += float(elementi[i])

    prosjek = round(suma / (len(elementi) - 1), 2)

    izlaz.write(f"{elementi[0]}, {prosjek}\n")


ulaz.close()
izlaz.close()