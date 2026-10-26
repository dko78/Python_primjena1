# Napišite program koji će kreirati praznu tekstualnu datoteku naziva
# datoteka.txt . U kreiranu datoteku spremite sve brojeve od 1 do 10.
# Svaki broj neka bude u zasebnoj liniji. Nakon što je datoteka kreirana,
# pročitajte iz nje sve brojeve te napravite sumu pročitanih brojeva, a taj
# rezultat ispišite na zaslon.

# 1) Kreiranje/pregazivanje datoteke i upis brojeva 1-10 (svaki u svom retku)
# ZADATAK 2:
# datoteka.txt -> upis brojeva 1-10 (svaki u novi red),
# zatim čitanje i suma

with open("datoteka.txt", "w+", encoding="utf-8") as f:
    # Upis brojeva 1-10, svaki u novi red
    broj = 1
    while broj <= 10:
        f.write(str(broj) + "\n")
        broj += 1

    # Vraćanje pokazivača na početak datoteke za čitanje
    f.seek(0)

    # Čitanje i suma
    suma = 0
    for line in f:
        suma += int(line.strip())
    f.write(f"<{suma}>")  # Upis sume na kraj datoteke u formatu "<suma>"    
    


print("Suma pročitanih brojeva je:", suma)

# 3. Izmijenite prethodno napisani program tako da se ukupna suma brojeva
# iz datoteke datoteka.txt zapiše na kraj datoteke u formatu: "<55>".