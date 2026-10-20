import time

sudionici = ["Iva", "Marica", "Perica", "Nika", "Nikica", "Tihana", "Stjepan", "Petra"]
rezultati = [10.11, 11.58, 10.08, 10.06, 10.77, 11.22, 11.55, 10.05]

# Spojimo ime i rezultat (manje vrijeme = bolji rezultat)
podaci = list(zip(sudionici, rezultati))


def bubble_sort(lista):
    arr = lista.copy()
    n = len(arr)

    for i in range(n - 1):
        zamjena = False
        for j in range(n - 1 - i):
            if arr[j][1] > arr[j + 1][1]:  # uzlazno po vremenu
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                zamjena = True
        if not zamjena:
            break
    return arr


def selection_sort(lista):
    arr = lista.copy()
    n = len(arr)

    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j][1] < arr[min_idx][1]:  # tražimo najmanje vrijeme
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


# Mjerenje bubble sort
start = time.perf_counter()
bubble_rez = bubble_sort(podaci)
bubble_elapsed = time.perf_counter() - start

# Mjerenje selection sort
start = time.perf_counter()
selection_rez = selection_sort(podaci)
selection_elapsed = time.perf_counter() - start

print("Bubble sort poredak:")
for ime, vrijeme in bubble_rez:
    print(f"{ime}: {vrijeme:.2f} s")
print(f"Bubble elapsed: {bubble_elapsed:.10f} s\n")

print("Selection sort poredak:")
for ime, vrijeme in selection_rez:
    print(f"{ime}: {vrijeme:.2f} s")
print(f"Selection elapsed: {selection_elapsed:.10f} s\n")

brzi = "Bubble sort" if bubble_elapsed < selection_elapsed else "Selection sort"
print(f"Brži u ovom pokretanju: {brzi}")