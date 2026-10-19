
# Napišite bezimenu funkciju koja prima 3 vrijednosti (pretpostavimo da
# su sve tri vrijednosti pozitivne i strogo veće od 0). Ta bezimena
# funkcija izračunava i vraća rezultat matematičke formule: (a*b +
# c) / c . U glavnom programu ispišite rezultat matematičke formule
# za sljedeće vrijednosti: a = 5, b = 10, c = 2

formula = lambda a, b, c: (a * b + c) / c

a, b, c = 5, 10, 2
print(formula(a, b, c))


# Nadogradite prethodni zadatak tako da prethodno implementirana
# bezimena funkcija može primiti 3 vrijednosti u rasponu od < <--∞, ∞>.
# Ako izračun nije moguće provesti, ispišite poruku: "Greška u
# predanim podacima!", u suprotnom ispišite rezultat matematičke
# formule. Napomena: obradite slučaj dijeljenja s 0.

formula = lambda a, b, c: (a * b + c) / c if c != 0 else "Greška u predanim podacima!"