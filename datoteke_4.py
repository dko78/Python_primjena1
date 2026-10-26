# Pomoću programa Notepad kreirajte datoteku i u 10 redaka te datoteke
# napišite po jedan proizvoljan broj. Napišite program koji će pročitati tu
# datoteku te sve parne brojeve iz nje upisati u novu datoteku. Također,
# izračunajte sumu svih neparnih brojeva te ih zapišite u treću datoteku.

# ulazna datoteka koju ste kreirali u Notepadu (10 redaka, po jedan broj)
ulazna_datoteka = "brojevi.txt"

# izlazne datoteke
parni_datoteka = "parni.txt"
neparni_suma_datoteka = "suma_neparnih.txt"

parni = []
suma_neparnih = 0

with open(ulazna_datoteka, "r", encoding="utf-8") as f:
 for linija in f:
    linija = linija.strip()
    if linija == "":
        continue  # preskoči prazne retke

    broj = int(linija)

    if broj % 2 == 0:
        parni.append(broj)
    else:
        suma_neparnih += broj

# 2) Upis svih parnih brojeva u novu datoteku (svaki u svoj red)
with open(parni_datoteka, "w", encoding="utf-8") as f:
    for broj in parni:
        f.write(str(broj) + "\n")

# 3) Upis sume neparnih brojeva u treću datoteku
with open(neparni_suma_datoteka, "w", encoding="utf-8") as f:
    f.write(str(suma_neparnih))

print("Parni brojevi:", parni)
print("Suma neparnih brojeva:", suma_neparnih)        