# Implementirajte generatorsku funkciju imena danUTjednu ()(),
# funkcija mora vratiti generator s danima u tjednu. Nakon što svi dani
# u tjednu budu otpušteni, ne kreće se ponovo s otpuštanjem
# vrijednosti od ponedjeljka. U glavnom programu pozivom
# implementirane generatorske funkcije ispišite sve dane u tjednu.

def danUTjednu():
    dani = [
        "Ponedjeljak",
        "Utorak",
        "Srijeda",
        "Četvrtak",
        "Petak",
        "Subota",
        "Nedjelja",
    ]
    for dan in dani:
        yield dan


# Glavni program
generator_dana = danUTjednu()

print(next(generator_dana))  # Ispisuje prvi dan (Ponedjeljak)
print(next(generator_dana))  # Ispisuje prvi dan (Ponedjeljak)

# for dan in generator_dana:
#     print(dan)

print("Idući dan u tjednu:", next(generator_dana))  # Ispisuje idući dan (Utorak)


