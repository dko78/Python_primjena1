parni = ["2", "4", "6"]
print(type(parni))  # <class 'list'>
rez = ",".join(parni)#" ".join(parni) znači: spoji sve elemente liste parni u jedan string, i između svakog elementa stavi razmak " ".
print(type(rez))  # <class 'str'>
print(rez)   # 2 4 6