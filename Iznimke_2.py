# Napišite funkciju imena ucitajPaZbroji ()(), koja učitava 3 broja s
# tipkovnice i ispisuje njihov zbroj. U toj funkciji uhvatite potencijalne
# iznimke te tako uhvaćene iznimke proslijedite u glavni dio programa (dio
# programa unutar kojeg je funkcija pozvana) te tamo ispišite da se
# dogodila iznimka.
# def ucitajPaZbroji():
#     try:
#         a = float(input("Unesite prvi broj: "))
#         b = float(input("Unesite drugi broj: "))
#         c = float(input("Unesite treći broj: "))
#         print("Zbroj je:", a + b + c)
#     except Exception as e:
#         # Uhvaćenu iznimku prosljeđujemo dalje u glavni dio programa
#         raise e


# # Glavni dio programa
# try:
#     ucitajPaZbroji()
# except Exception as e:
#     print("Dogodila se iznimka.")
#     print("Detalji:", e)





# 2.
# Prethodni zadatak nadogradite tako da rezultat zbroja ispisujete unutar
# else bloka funkcije imena ucitajPaZbroji ()(). Također, napišite i
# blok finally koji će ispisivati generičku poruku poput: " Finally blok!".

def ucitajPaZbroji():
    try:
        a = float(input("Unesite prvi broj: "))
        b = float(input("Unesite drugi broj: "))
        c = float(input("Unesite treći broj: "))
    except Exception:
        raise
    else:
        print("Zbroj je:", a + b + c)
    finally:
        print("Finally blok!")


# Glavni dio programa
try:
    ucitajPaZbroji()
except Exception as e:
    print("Dogodila se iznimka.")
    print("Detalji:", e)


# 3.
# Definirajte vlastitu iznimku NegativanBrojError . Napišite funkciju
# korijen(broj) koja za negativan broj podiže tu iznimku, a inače
# vraća drugi korijen broja. U glavnom programu učitajte broj s tipkovnice
# i pozovite funkciju, a iznimke ValueError (neispravan unos) i
# NegativanBrojError obradite zasebnim blokovima except
class NegativanBrojError(Exception):
    pass


def korijen(broj):
    if broj < 0:
        raise NegativanBrojError("Korijen negativnog broja nije definiran u skupu realnih brojeva.")
    return broj ** 0.5


try:
    unos = input("Unesite broj: ")
    broj = float(unos)
    rezultat = korijen(broj)
    print("Drugi korijen je:", rezultat)

except ValueError:
    print("Greška: neispravan unos (morate unijeti broj).")

except NegativanBrojError as e:
    print("Greška:", e)