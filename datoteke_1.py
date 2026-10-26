# 1.
# Napišite program koji će kreirati praznu tekstualnu datoteku naziva
# datoteka.txt (ako datoteka identičnog imena već postoji od prije,
# tada ju je potrebno pregaziti s praznom datotekom ). U kreiranu datoteku
# potrebno je upisati sve parne brojeve do 20. Parni brojevi neka
# međusobno budu odvojeni razmakom.

with open("datoteka.txt", "w", encoding="utf-8") as f:
    broj = 2
    while broj <= 20:
        f.write(str(broj))
        if broj < 20:
            f.write(" ")
        broj += 2

#moze i ovako
# with open("datoteka.txt", "w", encoding="utf-8") as f:
#     parni = [str(broj) for broj in range(2, 21, 2)]
#     f.write(" ".join(parni))


# Zato što range(start, stop, step) radi ovako:
# - 2 je početak (prvi paran broj)
# - 21 je granica koja se ne uključuje, pa zadnji bude 20
# - 2 je korak, pa ide samo kroz parne: 2, 4, 6, ..., 20