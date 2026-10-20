# Funkcija sorted
# •
#     Ugrađena funkcija
#     •
#     Radi za bilo koji iterable (na primjer: niz znakova, lista, n torka, rječnik (dobivaju se
#     ključevi), generator, itd.)
#     •
#     Vraća novu sortiranu listu
#     •
#     Originalna lista ostaje netaknuta
# •
# Metoda sort
# •
#     Metoda liste
#     •
#     Radi samo za listu
#     •
#     Vraća None vrijednost
#     •
#     Sortira listu nad kojom je pozvana tj. na mjestu (engl. in place
#     •
#     Nakon poziva ove metode, gubi se originalni poredak elemenata objekta nad kojim je
#     ova metoda pozvana
# •
# Metoda sort je brža od funkcije sorted zato što metoda sort
# ne kreira novu listu
# •
# Koristi se algoritam Timsort (mješavina algoritama: sortiranje
# sjedinjavanjem i sortiranje umetanjem, složenost je O(n log n) )

# dortiranje biranjem (selection sort) uz istovremeno preslagivanje dvije liste
sudionici = ["Iva", "Marica", "Perica", "Nika", "Nikica", "Tihana", "Stjepan", "Petra"]
rezultati = [10.11, 11.58, 10.08, 10.06, 10.77, 11.22, 11.55, 10.05]

# Selection sort uz istovremeno preslagivanje obje liste
n = len(rezultati)

for i in range(n - 1):
    min_idx = i
    for j in range(i + 1, n):
        if rezultati[j] < rezultati[min_idx]:
            min_idx = j

    # zamjena rezultata
    rezultati[i], rezultati[min_idx] = rezultati[min_idx], rezultati[i]
    # zamjena pripadnih sudionika
    sudionici[i], sudionici[min_idx] = sudionici[min_idx], sudionici[i]

print("Poredak (od najbržeg do najsporijeg):")
for ime, vrijeme in zip(sudionici, rezultati):
    print(f"{ime}: {vrijeme:.2f} s")

# bubble sort uz istovremeno preslagivanje obje liste
sudionici = ["Iva", "Marica", "Perica", "Nika", "Nikica", "Tihana", "Stjepan", "Petra"]
rezultati = [10.11, 11.58, 10.08, 10.06, 10.77, 11.22, 11.55, 10.05]

# Bubble sort uz istovremeno preslagivanje obje liste
print("\nBubble sort:")
n = len(rezultati)

for i in range(n - 1):
    zamjena = False
    for j in range(n - 1 - i):
        if rezultati[j] > rezultati[j + 1]:
            # zamijeni rezultate
            rezultati[j], rezultati[j + 1] = rezultati[j + 1], rezultati[j]
            # zamijeni pripadne sudionike
            sudionici[j], sudionici[j + 1] = sudionici[j + 1], sudionici[j]
            zamjena = True
    if not zamjena:
        break

print("Poredak (od najbržeg do najsporijeg):")
for ime, vrijeme in zip(sudionici, rezultati):
    print(f"{ime}: {vrijeme:.2f} s")
      